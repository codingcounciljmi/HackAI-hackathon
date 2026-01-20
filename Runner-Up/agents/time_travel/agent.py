"""
Time Travel Chat - Historical Conversation Module (India Edition)
"""
import google.generativeai as genai
from typing import Optional, List, Dict
import random
import time
from core.rich_ui import (console, print_header, print_user_msg, print_bot_msg, 
                          print_error, print_success, clear_screen, print_menu,
                          print_agent_banner, NEON_CYAN, NEON_YELLOW)
from core.logger import ChatLogger
from core.soundbox import soundbox

class TimeTravelChat:
    """Time Travel Chat - The Historical Immersion Bot (India Context)"""
    
    SYSTEM_PROMPT_TEMPLATE = """SYSTEM PROMPT: TIME TRAVEL BOT - INDIA CONTEXT
You are a person living in the INDIAN SUBCONTINENT (Bharat/Hindustan) in the year {YEAR}.
Your identity, knowledge, and worldview are strictly limited to what an Indian person would know in {YEAR}.

LOCATION:
- You are in INDIA.
- Refer to the land as "Bharatvarsh", "Hindustan", "British India", or "India" depending on the era.

LANGUAGE STYLE:
- Speak in a mix of English and Hindi (Roman Script/Hinglish).
- TONE: Maintain the FORMAL language and dignity of that particular time.
- VOCABULARY: Use era-specific terms.
  - Ancient: Sanskrit influence (Pranam, Arya, Dharma, Mitra).
  - Medieval/Mughal: Urdu/Persian influence (Salam, Huzoor, Saltanat).
  - British Raj: "Angrez", "Company Bahadur", "Swaraj", "Azadi".
  - Post-Independence: "Sarkar", "Desh", "Public".
- Do NOT use modern Gen-Z slang (no "bro", "chill", "vibes").

ERA BEHAVIOR MODIFIERS:
- Ancient (Before 1200 AD): Discuss Dharma, Philosophy, Kings (Mauryas, Guptas), and Scriptures.
- Medieval (1200-1750): Discuss the Courts, Art, Invaders, and Bhakti/Sufi movements.
- British Era (1757-1947): Discuss the struggle for freedom, exploitation, Railways, or Loyalty to the Crown (depending on persona).
- Post-1947: Discuss Nation Building, Politics, Cinema, Cricket.
- Future (2025+): Discuss India as a Superpower, Space Missions, Technocracy.

ABSOLUTE RULES:
1. You DO NOT know the future.
2. You believe {YEAR} is the present.
3. Your perspective is strictly INDIAN.
4. If asked about foreign events, interpret them through Indian news/rumors of that time.

active_year: {YEAR}
"""

    def __init__(self, model: genai.GenerativeModel):
        self.model = model
        self.active_year = None
        self.chat = None
    
    def set_year(self, year: str) -> bool:
        """Set the active year and initialize the chat."""
        try:
            self.active_year = year
            system_prompt = self.SYSTEM_PROMPT_TEMPLATE.replace("{YEAR}", str(year))
            
            # Initialize chat
            self.chat = self.model.start_chat(history=[
                {"role": "user", "parts": [system_prompt]},
                {"role": "model", "parts": [f"Pranam. I understand. I am living in India in the year {year}."]}
            ])
            return True
        except Exception:
            return False

    def get_response(self, user_input: str) -> str:
        """Get a response from the time traveler."""
        if not self.chat: return "⚠️ Please set a year first."
        try:
            response = self.chat.send_message(user_input)
            return response.text
        except Exception as e:
            return f"⚠️ Transformation error: {str(e)}"

def run_time_travel(model: genai.GenerativeModel) -> None:
    """Main entry point for Time Travel Chat."""
    bot = TimeTravelChat(model)
    session_messages = []
    
    # Premium agent banner
    print_agent_banner("Time Travel Chat", "India Through The Ages 🇮🇳 • Ancient → Modern → Future")
    
    # Year Setup
    while True:
        console.print("[dim italic](Type 'exit' to return to menu)[/dim italic]")
        year = soundbox.get_input("[bold yellow]📅 Enter a Year (e.g. 1857, 1947, 300 BC): [/bold yellow]", input_style="bold yellow")
        
        if year.lower() in ['exit', 'quit', 'back']:
             return

        if year:
            with console.status(f"[bold yellow]⚡ Traveling to {year} in India...[/bold yellow]", spinner="clock"):
                bot.set_year(year)
                time.sleep(1)
                
            print_success(f"Arrived in {year} (India)!")
            
            with console.status("[bold yellow]Awakening local citizen...", spinner="earth"):
                greeting = bot.get_response(f"Pranam! What is happening in India in {year}?")
            print_bot_msg(greeting, title=f"Citizen of {year}")
            session_messages.append({"role": "model", "text": greeting})
            if soundbox.last_input_was_voice:
                soundbox.speak(greeting)
            break
            
    # Conversation Loop
    while True:
        try:
            console.rule("[dim]Type 'warp' to change year, 'exit' to quit[/dim]")
            user_input = soundbox.get_input(input_style="bold yellow")
            
            if not user_input: continue
            
            if user_input.lower() in ['clear', 'cls']:
                clear_screen()
                print_header("Time Travel Chat", "India Through The Ages 🇮🇳")
                print_success(f"Timeline stabilized in {bot.active_year}!")
                continue

            if user_input.lower() in ['exit', 'quit', 'bye']:
                if session_messages:
                    save = console.input("[yellow]💾 Save conversation? (y/n): [/yellow]").strip().lower()
                    if save in ['yes', 'y']:
                        title = console.input("[yellow]   Title: [/yellow]").strip()
                        ChatLogger.save_chat("Time Travel", session_messages, title if title else f"Journey to {bot.active_year}")
                        print_success("Saved!")
                break
                
            if user_input.lower() == 'warp':
                console.print("[dim italic](Type 'exit' to return)[/dim italic]")
                year = soundbox.get_input("[bold yellow]📅 Warp to Year: [/bold yellow]", input_style="bold yellow")
                if year and year.lower() not in ['exit', 'quit']:
                    with console.status(f"[bold yellow]⚡ Warping to {year}...[/bold yellow]", spinner="clock"):
                        bot.set_year(year)
                        time.sleep(1)
                    
                    with console.status("[bold yellow]Stabilizing timeline...", spinner="earth"):
                        greeting = bot.get_response("Pranam! Where are we and what year is this?")
                    print_bot_msg(greeting, title=f"Citizen of {year}")
                    session_messages.append({"role": "model", "text": greeting})
                    if soundbox.last_input_was_voice:
                        soundbox.speak(greeting)
                continue

            # Record and Print User Message
            session_messages.append({"role": "user", "text": user_input})
            print_user_msg(user_input)
            
            with console.status(f"[italic yellow]Thinking in {bot.active_year}...[/italic yellow]", spinner="arc"):
                response = bot.get_response(user_input)
                
            print_bot_msg(response, title=f"Citizen of {bot.active_year}")
            session_messages.append({"role": "model", "text": response})
            
            if soundbox.last_input_was_voice:
                soundbox.speak(response)
            
        except KeyboardInterrupt:
            console.print("\n\n[yellow]⚠️ Interrupted! Returning to menu...[/yellow]")
            break
        except Exception as e:
            print_error(f"Error: {str(e)}")
