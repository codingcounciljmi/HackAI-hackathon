"""
Code Made Easy - Main Agent Controller
"""
import google.generativeai as genai
from enum import Enum, auto
from typing import Optional
import time
from datetime import datetime
from core.rich_ui import (console, print_header, print_user_msg, print_bot_msg, 
                          print_error, print_success, clear_screen, print_menu,
                          print_agent_banner, NEON_CYAN, NEON_PINK, NEON_GREEN)
from core.logger import ChatLogger
from core.soundbox import soundbox

from .storage import BugStorage, CodeStorage, SavedCode
from .debugger import CodeDebugger
from .generator import CodeGenerator
from .rater import CodeRater

class CodeFeature(Enum):
    """Features available in Code Made Easy."""
    DEBUGGER = auto()
    GENERATOR = auto()
    RATE_CODE = auto()

class CodeMadeEasy:
    """
    Code Made Easy - The Master Coding Assistant
    """
    
    MENU_OPTIONS = {
        '1': {'name': 'AI Code Debugger', 'description': 'Find and fix bugs instantly', 'icon': '🐛'},
        '2': {'name': 'AI Code Generator', 'description': 'Turn ideas into code', 'icon': '⚡'},
        '3': {'name': 'Rate My Programme', 'description': 'Get quality scores and feedback', 'icon': '⭐'},
        '4': {'name': 'View Bug History', 'description': 'Review past mistakes', 'icon': '📜'},
        '5': {'name': 'View Saved Codes', 'description': 'Access your generated snippets', 'icon': '💾'},
        '0': {'name': 'Back to Main Menu', 'description': 'Return to agent selection', 'icon': '🔙'},
    }

    def __init__(self, model: genai.GenerativeModel):
        self.model = model
        self.storage = BugStorage()
        self.code_storage = CodeStorage()
        self.debugger = CodeDebugger(model, self.storage)
        self.generator = CodeGenerator(model)
        self.rater = CodeRater(model)
        self.session_messages = []
    
    def _log_interaction(self, user_text: str, bot_text: str, context: str = ""):
        """Log Interaction to session history."""
        self.session_messages.append({"role": "user", "text": f"[{context}] {user_text}"})
        self.session_messages.append({"role": "model", "text": bot_text})

    def _get_multiline_input(self, prompt: str = "") -> str:
        """Helper to get multiline input from user."""
        console.print(f"[bold cyan]{prompt}[/bold cyan]")
        console.print("[dim](Type 'END' on a new line to finish)[/dim]")
        
        lines = []
        while True:
            try:
                line = console.input("[dim]> [/dim]")
                if line.strip() == 'END':
                    break
                lines.append(line)
            except KeyboardInterrupt:
                return ""
        return "\n".join(lines)

    def run(self):
        """Main execution loop for Code Made Easy."""
        while True:
            # Premium agent banner
            print_agent_banner("Code Made Easy", "Debug • Generate • Optimize • Like a Pro 💪")
            print_menu(self.MENU_OPTIONS, "CODE TOOLS")
            
            choice = console.input(f"\n[bold {NEON_CYAN}]   ▶ Choice:[/bold {NEON_CYAN}] ").strip()
            
            if choice == '1':
                self._run_debugger()
            elif choice == '2':
                self._run_generator()
            elif choice == '3':
                self._run_rater()
            elif choice == '4':
                self._view_bug_history()
            elif choice == '5':
                self._view_saved_codes()
            elif choice == '0':
                if self.session_messages:
                    console.print("\n")
                    save = console.input("[yellow]💾 Save coding session? (y/n): [/yellow]").strip().lower()
                    if save in ['yes', 'y']:
                        title = console.input("[yellow]   Title: [/yellow]").strip()
                        ChatLogger.save_chat("Code Made Easy", self.session_messages, title if title else "Coding Session")
                        print_success("Saved!")
                break
            else:
                print_error("Invalid choice. Please try again.")
                time.sleep(1)

    def _run_debugger(self):
        """Run the debugger workflow."""
        clear_screen()
        print_header("AI Code Debugger", "Find bugs fast")
        
        console.print("[bold]1. Select Language[/bold]")
        language = console.input("   [cyan]Language (or 'exit'):[/cyan] ").strip()
        if not language or language.lower() in ['exit', 'back']: return
            
        console.print("\n[bold]2. Enter Code[/bold]")
        code = self._get_multiline_input("Paste your broken code below:")
        if not code.strip():
            print_error("No code provided.")
            time.sleep(1)
            return

        print_user_msg(f"Debug this {language} code:\n...\n{code[:50]}...")

        with console.status("[bold green]🔍 Analyzing code for bugs...", spinner="dots"):
            analysis = self.debugger.debug_code(code, language)
        
        print_bot_msg(analysis, title="Debugger AI")
        self._log_interaction(code, analysis, context="Debugger")
        
        console.input("\n[dim]Press Enter to return...[/dim]")

    def _run_generator(self):
        """Run the generator workflow."""
        clear_screen()
        print_header("AI Code Generator", "Text to Code")
        
        console.print("[bold]Describe what you want to build:[/bold]")
        console.print("[dim]Example: 'Create a Python script that scrapes headlines from news.com'[/dim]")
        
        console.print("[dim](Type 'exit' to go back)[/dim]")
        prompt = soundbox.get_input("\n[cyan]📝 Request:[/cyan]", input_style="cyan")
        if not prompt or prompt.lower() in ['exit', 'back']: return
            
        language = soundbox.get_input("[cyan]💻 Target Language (default: Python):[/cyan]", input_style="cyan") or "Python"
        
        print_user_msg(f"Generate {language} code: {prompt}")
        
        with console.status(f"[bold green]⚡ Generating {language} code...", spinner="moon"):
            result = self.generator.generate_code(prompt, language)
        
        print_bot_msg(result, title="Generator AI")
        if soundbox.last_input_was_voice:
             soundbox.speak(result) # Might read code, which is verbose. But requested.
        self._log_interaction(prompt, result, context=f"Generator ({language})")
        
        # Generator Interact Loop
        while True:
            console.rule("[bold cyan]Options[/bold cyan]")
            console.print("[1] Refine  [2] Explain  [3] New Request  [4] 💾 Save Code  [0] Done")
            action = soundbox.get_input("\n[bold cyan]👉 Next:[/bold cyan]", input_style="bold cyan").lower()
            
            if action == '0' or action == 'done':
                break
            elif action == '3' or action == 'new':
                self._run_generator()
                return
            elif action == '4' or action == 'save':
                desc = console.input("[cyan]   Enter Description for Code: [/cyan]").strip()
                if desc:
                    # We save the *result* (generated output) as the code.
                    # Ideally we extract code, but saving the full output is safer for now.
                    saved_item = SavedCode(
                        date=datetime.now().strftime("%Y-%m-%d"),
                        language=language,
                        code=result,
                        description=desc
                    )
                    self.code_storage.add_code(saved_item)
                    print_success("Code saved successfully!")
                    
            elif action == '1' or action.startswith('refine'):
                feedback = soundbox.get_input("[cyan]   What should I change? [/cyan]", input_style="cyan")
                if feedback:
                    print_user_msg(f"Refine: {feedback}")
                    with console.status("[bold green]⚡ Refining code...", spinner="dots"):
                        result = self.generator.refine_code(feedback)
                    print_bot_msg(result, title="Generator AI")
                    if soundbox.last_input_was_voice:
                        soundbox.speak(result)
                    self._log_interaction(feedback, result, context="Refinement")
            elif action == '2' or action.startswith('explain'):
                question = soundbox.get_input("[cyan]   What's confusing? [/cyan]", input_style="cyan")
                if question:
                    print_user_msg(f"Explain: {question}")
                    with console.status("[bold green]🤖 Explaining...", spinner="dots"):
                        result = self.generator.explain_further(question)
                    print_bot_msg(result, title="Generator AI")
                    if soundbox.last_input_was_voice:
                        soundbox.speak(result)
                    self._log_interaction(question, result, context="Explanation")
    
    def _run_rater(self):
        """Run the rater workflow."""
        clear_screen()
        print_header("Rate My Programme", "Code Quality Review")
        
        language = console.input("[cyan]💻 Programming Language (or 'exit'):[/cyan] ").strip()
        if not language or language.lower() in ['exit', 'back']: return
            
        code = self._get_multiline_input("Paste your code:")
        if not code.strip(): return

        print_user_msg(f"Rate this {language} code...")

        with console.status("[bold green]⭐ Reviewing code quality...", spinner="star"):
            review = self.rater.rate_code(code, language)
        
        print_bot_msg(review, title="Code Reviewer")
        self._log_interaction(code, review, context=f"Rating ({language})")
        
        # Rater Interact Loop
        while True:
            console.rule("[bold cyan]Options[/bold cyan]")
            console.print("[1] Ask Question  [2] New Review  [0] Done")
            action = console.input("\n[bold cyan]👉 Next:[/bold cyan] ").strip().lower()
            
            if action == '0' or action == 'done':
                break
            elif action == '2' or action == 'new':
                return
            elif action == '1' or action == 'ask':
                question = console.input("[cyan]   Ask about the rating: [/cyan]").strip()
                if question:
                    print_user_msg(question)
                    with console.status("[bold green]🤖 Answering...", spinner="dots"):
                        response = self.rater.ask_question(question)
                    print_bot_msg(response, title="Code Reviewer")
                    self._log_interaction(question, response, context="Rating Q&A")

    def _view_bug_history(self):
        """View stored bug reports."""
        clear_screen()
        print_header("Bug History", "Your personal bug tracker")
        
        bugs = self.storage.get_all_bugs()
        if not bugs:
            console.print("\n[italic yellow]📭 No bugs recorded yet. Start debugging to build your history![/italic yellow]")
        else:
            console.print(f"[bold]📜 Found {len(bugs)} bug reports:[/bold]")
            for i, bug in enumerate(reversed(bugs), 1):
                console.print(f"\n[bold cyan]--- Bug #{i} ---[/bold cyan]")
                console.print(bug.display()) 
        
        console.input("\n[dim]Press Enter to return...[/dim]")

    def _view_saved_codes(self):
        """View saved code snippets."""
        clear_screen()
        print_header("Saved Codes", "Your Code Library")
        
        codes = self.code_storage.get_all_codes()
        if not codes:
            console.print("\n[italic yellow]📭 No saved codes yet. Generate some code to save it![/italic yellow]")
        else:
            console.print(f"[bold]💾 Found {len(codes)} saved snippets:[/bold]")
            for i, snippet in enumerate(reversed(codes), 1):
                console.print(f"\n[bold green]--- Snippet #{i} ---[/bold green]")
                console.print(f"[bold]Date:[/bold] {snippet.date}")
                console.print(f"[bold]Language:[/bold] {snippet.language}")
                console.print(f"[bold]Description:[/bold] {snippet.description}")
                console.print("[bold]Code:[/bold]")
                print_bot_msg(snippet.code, title=f"Snippet {i}")
        
        console.input("\n[dim]Press Enter to return...[/dim]")

def run_code_made_easy(model: genai.GenerativeModel) -> None:
    """Main entry for Code Made Easy."""
    app = CodeMadeEasy(model)
    app.run()
