"""
Rich UI Utilities for CLI Chatbot
Premium terminal experience with stunning visuals and animations.
"""
from rich.console import Console
from rich.theme import Theme
from rich.panel import Panel
from rich.text import Text
from rich.markdown import Markdown
from rich.align import Align
from rich.table import Table
from rich.columns import Columns
from rich.style import Style
from rich.live import Live
from rich import box
import time
import random

# ═══════════════════════════════════════════════════════════════════════════════
#  🎨 PREMIUM COLOR PALETTE - Cyberpunk Neon Theme
# ═══════════════════════════════════════════════════════════════════════════════

# Neon accent colors
NEON_CYAN = "#00FFFF"
NEON_PINK = "#FF00FF"
NEON_GREEN = "#00FF88"
NEON_YELLOW = "#FFFF00"
NEON_ORANGE = "#FF6B35"
NEON_PURPLE = "#B388FF"
NEON_BLUE = "#00BFFF"
NEON_RED = "#FF3366"

# Gradient colors
GRADIENT_START = "#667eea"
GRADIENT_END = "#764ba2"

# Background accents
DARK_BG = "#0D1117"
CARD_BG = "#161B22"
BORDER_GLOW = "#58A6FF"

# Define a premium custom theme
THEME = Theme({
    "info": f"{NEON_CYAN}",
    "warning": f"bold {NEON_YELLOW}",
    "error": f"bold {NEON_RED}",
    "success": f"bold {NEON_GREEN}",
    "user_panel": f"{NEON_BLUE}",
    "bot_panel": f"{NEON_GREEN}",
    "header": f"bold white",
    "menu_border": f"{NEON_CYAN}",
    "highlight": f"bold {NEON_PINK}",
    "accent": f"{NEON_PURPLE}",
    "muted": "dim white",
    "glow": f"bold {BORDER_GLOW}",
})

# Global console instance
console = Console(theme=THEME)

# ═══════════════════════════════════════════════════════════════════════════════
#  🔤 ASCII ART TITLE GENERATOR
# ═══════════════════════════════════════════════════════════════════════════════

MAIN_TITLE_ART = """
    ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
    ┃  ╦ ╦┌─┐┌┐┌┌┬┐┬ ┬ ╦ ╦┌─┐┬─┐┌─┐   ░█▀█░▀█▀░  ╋╋╋╋╋╋╋╋░░░░░  ┃
    ┃  ╠═╣├─┤│││ ││└┬┘ ║║║├─┤├┬┘├┤    ░█▀█░░█░░  ╋╋╋╋╋╋╋╋░░░░░  ┃
    ┃  ╩ ╩┴ ┴┘└┘─┴┘ ┴  ╚╩╝┴ ┴┴└─└─┘   ░▀░▀░▀▀▀░  ╋╋╋╋╋╋╋╋░░░░░  ┃
    ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
"""

AI_HUB_ART = """
     █████╗ ██╗    ██╗  ██╗██╗   ██╗██████╗ 
    ██╔══██╗██║    ██║  ██║██║   ██║██╔══██╗
    ███████║██║    ███████║██║   ██║██████╔╝
    ██╔══██║██║    ██╔══██║██║   ██║██╔══██╗
    ██║  ██║██║    ██║  ██║╚██████╔╝██████╔╝
    ╚═╝  ╚═╝╚═╝    ╚═╝  ╚═╝ ╚═════╝ ╚═════╝ 
"""

MINI_TITLES = {
    "Study Buddy": """
╔═╗╔╦╗╦ ╦╔╦╗╦ ╦  ╔╗ ╦ ╦╔╦╗╔╦╗╦ ╦
╚═╗ ║ ║ ║ ║║╚╦╝  ╠╩╗║ ║ ║║ ║║╚╦╝
╚═╝ ╩ ╚═╝═╩╝ ╩   ╚═╝╚═╝═╩╝═╩╝ ╩ """,

    "Lingua Link": """
╦  ╦╔╗╔╔═╗╦ ╦╔═╗  ╦  ╦╔╗╔╦╔═
║  ║║║║║ ╦║ ║╠═╣  ║  ║║║║╠╩╗
╩═╝╩╝╚╝╚═╝╚═╝╩ ╩  ╩═╝╩╝╚╝╩ ╩""",

    "Code Made Easy": """
╔═╗╔═╗╔╦╗╔═╗  ╔╦╗╔═╗╔╦╗╔═╗  ╔═╗╔═╗╔═╗╦ ╦
║  ║ ║ ║║║╣   ║║║╠═╣ ║║║╣   ║╣ ╠═╣╚═╗╚╦╝
╚═╝╚═╝═╩╝╚═╝  ╩ ╩╩ ╩═╩╝╚═╝  ╚═╝╩ ╩╚═╝ ╩ """,

    "Time Travel Chat": """
╔╦╗╦╔╦╗╔═╗  ╔╦╗╦═╗╔═╗╦  ╦╔═╗╦  
 ║ ║║║║║╣    ║ ╠╦╝╠═╣╚╗╔╝║╣ ║  
 ╩ ╩╩ ╩╚═╝   ╩ ╩╚═╩ ╩ ╚╝ ╚═╝╩═╝""",

    "Future Simulator": """
╔═╗╦ ╦╔╦╗╦ ╦╦═╗╔═╗  ╔═╗╦╔╦╗
╠╣ ║ ║ ║ ║ ║╠╦╝║╣   ╚═╗║║║║
╚  ╚═╝ ╩ ╚═╝╩╚═╚═╝  ╚═╝╩╩ ╩""",

    "Explain Like X": """
╔═╗═╗ ╦╔═╗╦  ╔═╗╦╔╗╔  ╦  ╦╦╔═╔═╗  ═╗ ╦
║╣ ╔╩╦╝╠═╝║  ╠═╣║║║║  ║  ║╠╩╗║╣   ╔╩╦╝
╚═╝╩ ╚═╩  ╩═╝╩ ╩╩╝╚╝  ╩═╝╩╩ ╩╚═╝  ╩ ╚═""",

    "Conversation Replay": """
╔═╗╔═╗╔╗╔╦  ╦╔═╗  ╦═╗╔═╗╔═╗╦  ╔═╗╦ ╦
║  ║ ║║║║╚╗╔╝║ ║  ╠╦╝║╣ ╠═╝║  ╠═╣╚╦╝
╚═╝╚═╝╝╚╝ ╚╝ ╚═╝  ╩╚═╚═╝╩  ╩═╝╩ ╩ ╩ """
}

# Gradient color sequences for animation
GRADIENT_COLORS = [
    "#FF6B6B", "#FF8E53", "#FFC107", "#4ECB71", 
    "#00D9FF", "#7B68EE", "#FF6B9D", "#C471ED"
]

NEON_COLORS = [NEON_CYAN, NEON_PINK, NEON_GREEN, NEON_PURPLE, NEON_BLUE, NEON_ORANGE]

def get_gradient_text(text: str, colors: list = None) -> Text:
    """Create a gradient-colored text effect."""
    if colors is None:
        colors = GRADIENT_COLORS
    
    rich_text = Text()
    color_count = len(colors)
    
    for i, char in enumerate(text):
        color = colors[i % color_count]
        rich_text.append(char, style=f"bold {color}")
    
    return rich_text

def get_neon_text(text: str, color: str = NEON_CYAN) -> Text:
    """Create a glowing neon text effect."""
    return Text(text, style=f"bold {color}")

def animate_title_gradient(title_art: str, cycles: int = 3, delay: float = 0.08):
    """Animate the title with shifting gradient colors."""
    lines = title_art.strip().split('\n')
    
    for cycle in range(cycles):
        shifted_colors = NEON_COLORS[cycle % len(NEON_COLORS):] + NEON_COLORS[:cycle % len(NEON_COLORS)]
        
        console.clear()
        for i, line in enumerate(lines):
            color = shifted_colors[i % len(shifted_colors)]
            console.print(line, style=f"bold {color}", justify="center")
        
        time.sleep(delay)
    
    # Final display with main color
    console.clear()

# ═══════════════════════════════════════════════════════════════════════════════
#  📦 PREMIUM UI COMPONENTS
# ═══════════════════════════════════════════════════════════════════════════════

# Custom box styles for premium look
NEON_BOX = box.Box(
    "╭──╮\n"
    "│  │\n"
    "├──┤\n"
    "│  │\n"
    "├──┤\n"
    "├──┤\n"
    "├──┤\n"
    "╰──╯\n"
)

GLOW_BOX = box.DOUBLE_EDGE

def print_header(title: str, subtitle: str = "", use_art: bool = True):
    """Print a stunning animated header with ASCII art."""
    
    # Check if we have mini art for this title
    if use_art and title in MINI_TITLES:
        art = MINI_TITLES[title]
        art_lines = art.strip().split('\n')
        
        # Print ASCII art with gradient
        for i, line in enumerate(art_lines):
            color = NEON_COLORS[i % len(NEON_COLORS)]
            console.print(line, style=f"bold {color}", justify="center")
        
        console.print()
        
        # Print subtitle in a sleek way
        if subtitle:
            subtitle_text = Text()
            subtitle_text.append("━━━ ", style=f"dim {NEON_CYAN}")
            subtitle_text.append(subtitle, style=f"italic {NEON_PURPLE}")
            subtitle_text.append(" ━━━", style=f"dim {NEON_CYAN}")
            console.print(Align.center(subtitle_text))
            console.print()
    else:
        # Fallback to panel style for main menu
        title_text = get_gradient_text(f"  {title}  ", NEON_COLORS)
        
        grid = Table.grid(expand=True)
        grid.add_column(justify="center", ratio=1)
        grid.add_row(title_text)
        
        if subtitle:
            sub_text = Text()
            sub_text.append(subtitle, style=f"italic dim {NEON_PURPLE}")
            grid.add_row(sub_text)
        
        panel = Panel(
            grid,
            style=f"{NEON_CYAN}",
            border_style=NEON_CYAN,
            padding=(1, 4),
            box=box.DOUBLE
        )
        console.print(panel)
    
    console.print()

def print_main_header():
    """Print the spectacular main application header."""
    # Print main title art with animated gradient
    lines = MAIN_TITLE_ART.strip().split('\n')
    
    for i, line in enumerate(lines):
        color = NEON_COLORS[i % len(NEON_COLORS)]
        console.print(line, style=f"bold {color}", justify="center")
    
    # Compact tagline right below the art
    tagline = Text()
    tagline.append("⟨ ", style=f"dim {NEON_CYAN}")
    tagline.append("⚡ Powered by Gemini 2.5 Flash Lite ⚡", style=f"bold {NEON_PINK}")
    tagline.append(" ⟩", style=f"dim {NEON_CYAN}")
    console.print(Align.center(tagline))
    console.print()

def print_user_msg(text: str):
    """Print a premium styled user message (right-aligned)."""
    content = Text(text, style="white")
    
    panel = Panel(
        content,
        title=f"[bold {NEON_BLUE}]👤 You[/bold {NEON_BLUE}]",
        title_align="right",
        border_style=NEON_BLUE,
        subtitle=f"[dim]💬[/dim]",
        subtitle_align="right",
        box=box.ROUNDED,
        padding=(0, 2),
        expand=False
    )
    console.print(Align.right(panel))

def print_bot_msg(text: str, title: str = "Bot", style: str = "white", icon: str = "🤖"):
    """Print a premium styled bot message with custom title and icon."""
    try:
        content = Markdown(text)
    except:
        content = Text(text)
    
    # Dynamic icon based on bot type
    bot_icons = {
        "Senior Mentor": "👨‍🏫",
        "Study Buddy": "📚",
        "Lingua Link": "🗣️",
        "Code Made Easy": "💻",
        "Time Travel": "⏰",
        "Future Simulator": "🔮",
        "Explain Like X": "🎭",
        "Profile Status": "📊",
    }
    
    display_icon = bot_icons.get(title, icon)
    
    panel = Panel(
        content,
        title=f"[bold {NEON_GREEN}]{display_icon} {title}[/bold {NEON_GREEN}]",
        title_align="left",
        border_style=NEON_GREEN,
        box=box.ROUNDED,
        padding=(0, 2),
        expand=False,
        width=min(console.width - 10, 100)
    )
    console.print(Align.left(panel))
    console.print()

def print_menu(options: dict, title: str = "COMMAND CENTER"):
    """Print a sleek, compact menu with modern design."""
    
    # Sort keys - put exit (0) at the end
    sorted_keys = sorted([k for k in options.keys() if k != '0'], key=lambda x: int(x) if x.isdigit() else 99)
    sorted_keys.append('0')  # Add exit at end
    
    # Create two-column grid for compact display
    left_items = []
    right_items = []
    
    for idx, key in enumerate(sorted_keys):
        info = options[key]
        if not info.get('available', True):
            continue
            
        icon = info.get('icon', '◆')
        name = info.get('name', 'Unknown')
        
        # Style based on key
        if key == '0':
            item_text = Text()
            item_text.append(f" {key}", style=f"bold {NEON_RED}")
            item_text.append(f" ▸ ", style=f"dim {NEON_PURPLE}")
            item_text.append(f"{icon} ", style=f"bold {NEON_YELLOW}")
            item_text.append(f"{name}", style=f"bold {NEON_RED}")
        else:
            item_text = Text()
            item_text.append(f" {key}", style=f"bold {NEON_CYAN}")
            item_text.append(f" ▸ ", style=f"dim {NEON_PURPLE}")
            item_text.append(f"{icon} ", style=f"bold {NEON_YELLOW}")
            item_text.append(f"{name}", style=f"bold white")
        
        # Distribute to columns (first 4 left, rest right)
        if idx < 4:
            left_items.append(item_text)
        else:
            right_items.append(item_text)
    
    # Build the two-column table
    table = Table(
        box=None,
        show_header=False,
        expand=True,
        padding=(0, 1),
        pad_edge=True
    )
    table.add_column("Left", justify="left", ratio=1)
    table.add_column("Right", justify="left", ratio=1)
    
    # Pad the shorter column
    max_rows = max(len(left_items), len(right_items))
    while len(left_items) < max_rows:
        left_items.append(Text(""))
    while len(right_items) < max_rows:
        right_items.append(Text(""))
    
    for left, right in zip(left_items, right_items):
        table.add_row(left, right)
    
    # Wrap in a compact panel
    panel = Panel(
        table,
        title=f"[bold {NEON_PINK}]⚡ {title} ⚡[/bold {NEON_PINK}]",
        border_style=NEON_CYAN,
        padding=(0, 2),
        box=box.ROUNDED
    )
    console.print(panel)

def print_divider(text: str = "", style: str = NEON_CYAN):
    """Print a stylish divider."""
    if text:
        rule_text = Text()
        rule_text.append(f" {text} ", style=f"bold {NEON_PINK}")
        console.rule(rule_text, style=style)
    else:
        console.rule(style=style)

def print_error(msg: str):
    """Print a premium error message."""
    error_panel = Panel(
        Text(f" {msg}", style="white"),
        title=f"[bold {NEON_RED}]❌ Error[/bold {NEON_RED}]",
        border_style=NEON_RED,
        box=box.ROUNDED,
        padding=(0, 1),
        expand=False
    )
    console.print(error_panel)

def print_success(msg: str):
    """Print a premium success message."""
    console.print(f"[bold {NEON_GREEN}]✨ {msg}[/bold {NEON_GREEN}]")

def print_warning(msg: str):
    """Print a premium warning message."""
    console.print(f"[bold {NEON_YELLOW}]⚠️  {msg}[/bold {NEON_YELLOW}]")

def print_info(msg: str):
    """Print a premium info message."""
    console.print(f"[{NEON_CYAN}]ℹ️  {msg}[/{NEON_CYAN}]")

def clear_screen():
    """Clear the terminal screen with style."""
    console.clear()

def print_loading(text: str = "Loading", duration: float = 1.0):
    """Display an animated loading indicator."""
    with console.status(f"[bold {NEON_CYAN}]{text}...", spinner="dots12"):
        time.sleep(duration)

def print_startup_animation():
    """Display a cool startup animation."""
    frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    colors = NEON_COLORS
    
    for i in range(15):
        frame = frames[i % len(frames)]
        color = colors[i % len(colors)]
        console.print(f"\r[bold {color}]{frame} Initializing Handyware AI...", end="")
        time.sleep(0.08)
    
    console.print(f"\r[bold {NEON_GREEN}]✓ System Ready!                    ")
    time.sleep(0.3)

def print_goodbye_animation():
    """Display a stylish goodbye screen."""
    console.clear()
    
    goodbye_art = """
    ╔══════════════════════════════════════════════╗
    ║                                              ║
    ║       🌟 Thanks for using Handyware AI! 🌟    ║
    ║                                              ║
    ║          See you next time, champ! 👋         ║
    ║                                              ║
    ╚══════════════════════════════════════════════╝
    """
    
    lines = goodbye_art.strip().split('\n')
    for i, line in enumerate(lines):
        color = NEON_COLORS[i % len(NEON_COLORS)]
        console.print(line, style=f"bold {color}", justify="center")
        time.sleep(0.05)
    
    console.print()

def print_agent_banner(agent_name: str, tagline: str = ""):
    """Print a stunning banner when entering an agent."""
    console.clear()
    
    # Print agent-specific ASCII art if available
    if agent_name in MINI_TITLES:
        art = MINI_TITLES[agent_name]
        art_lines = art.strip().split('\n')
        
        console.print()
        for i, line in enumerate(art_lines):
            color = NEON_COLORS[(i + 2) % len(NEON_COLORS)]
            console.print(line, style=f"bold {color}", justify="center")
        console.print()
    
    # Print tagline in a beautiful way
    if tagline:
        tag_panel = Panel(
            Text(tagline, style=f"italic {NEON_PURPLE}", justify="center"),
            border_style=f"dim {NEON_CYAN}",
            box=box.HORIZONTALS,
            padding=(0, 2)
        )
        console.print(tag_panel)
    
    console.print()

def get_input_prompt(style: str = "cyan") -> str:
    """Get a styled input prompt string."""
    return f"[bold {NEON_CYAN}]   ▶ [/bold {NEON_CYAN}]"

def print_feature_card(title: str, description: str, icon: str = "◆"):
    """Print a feature card with icon."""
    card = Panel(
        Text(description, style="white"),
        title=f"[bold {NEON_YELLOW}]{icon}[/bold {NEON_YELLOW}] [bold white]{title}[/bold white]",
        border_style=NEON_CYAN,
        box=box.ROUNDED,
        padding=(0, 1),
        expand=False
    )
    console.print(card)

# Legacy alias for backwards compatibility
def stream_thinking(text="Thinking..."):
    """Show a spinner (Use 'with console.status()' instead)."""
    pass
