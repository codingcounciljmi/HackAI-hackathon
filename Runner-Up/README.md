# 🤖 Handyware AI Hub

> **A unified AI platform offering 7 specialized chatbots for productivity, development, education, and creativity — all powered by Google Gemini 2.5 Flash Lite.**

[![Built with Gemini](https://img.shields.io/badge/Powered%20by-Gemini%202.5-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://ai.google.dev/)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![CLI](https://img.shields.io/badge/Interface-CLI-00ADD8?style=for-the-badge&logo=windowsterminal&logoColor=white)](https://en.wikipedia.org/wiki/Command-line_interface)
[![Hackathon](https://img.shields.io/badge/🏆-Hackathon%20Project-FF6B6B?style=for-the-badge)](https://github.com)

---

## 🌐 Platform Overview

### What is Handyware AI Hub?

**Handyware AI Hub** is a command-line AI platform that brings together **seven specialized AI chatbots** under one unified interface. Instead of using multiple disconnected AI tools, users can access a curated suite of purpose-built AI agents—each designed for a specific domain or task.

### 🎯 Why We Built It

This project was developed for a **hackathon** to demonstrate:

1. **Multi-Agent Architecture**: How multiple specialized AI agents can coexist in a single platform
2. **Domain-Specific AI**: Each chatbot is fine-tuned with custom prompts for its specific use case
3. **Premium CLI Experience**: Proving that command-line interfaces can be visually stunning and user-friendly

### 👥 Who Is This For?

| Audience | Use Cases |
|----------|-----------|
| **Students** | Academic guidance, exam prep, study planning, career advice |
| **Developers** | Code debugging, generation, review, and optimization |
| **Creators** | Creative explanations, content generation, brainstorming |
| **Indian Users** | Hinglish conversations, India-centric historical exploration |
| **Decision Makers** | Life decision analysis with scenario simulation |
| **Everyone** | Learning through fun personas, exploring history, planning futures |

---

## 🏠 Main Menu Overview

When you launch Handyware AI Hub, you're greeted with a **stunning cyberpunk-themed terminal interface** featuring:

- **Animated ASCII Art Title** displaying "Handyware AI"
- **Neon color scheme** with cyan, pink, green, and purple accents
- **Two-column agent menu** for easy navigation
- **Real-time status indicators** and loading animations

### 📋 Agent Selection Dashboard

The main menu provides access to **7 specialized AI chatbots**, each designed for a specific domain:

```
╭─────────────────────────────── ⚡ AGENT SELECTION ⚡ ────────────────────────────────╮
│                                                                                       │
│  1 ▸ 📚 Study Buddy                    5 ▸ 🔮 Future Simulator                       │
│  2 ▸ 🌐 Lingua Link                    6 ▸ 🎭 Explain Like X                         │
│  3 ▸ 💻 Code Made Easy                 7 ▸ 🔄 Conversation Replay                    │
│  4 ▸ ⏰ Time Travel Chat               0 ▸ ❌ Exit                                   │
│                                                                                       │
╰───────────────────────────────────────────────────────────────────────────────────────╯
```

### 🔀 Navigation Philosophy

- **Single Entry Point**: All agents are accessed from one unified menu
- **Quick Switching**: Type `exit` in any agent to return to the main menu instantly
- **Session Persistence**: Conversations can be saved and replayed later
- **Keyboard Navigation**: Type your input and navigate with simple commands

---

## 🤖 Available Chatbots — Detailed Breakdown

---

### 📚 1. Study Buddy

> *"Your AI Senior Mentor for academic and career guidance"*

#### 🎯 Purpose

Study Buddy acts as a **virtual senior college mentor** who provides structured, actionable guidance on academics, careers, internships, and interview preparation. It's designed to replace the scattered advice students typically get with focused, practical help.

#### 👤 Primary Users

- College students (all branches: CSE, IT, ECE, ME, etc.)
- Fresh graduates seeking career guidance
- Anyone preparing for interviews or internships

#### 🧩 Problems It Solves

- "What subjects should I focus on this semester?"
- "What career paths are available after my degree?"
- "Where can I find internships?"
- "How do I prepare for technical interviews?"

#### 🧠 AI Behavior

Study Buddy uses **keyword detection** to automatically identify the type of guidance needed and responds with a **strict structured format**:

```
🎯 Summary (1–2 lines)

📚 Key Points
- Bullet 1
- Bullet 2

🛠️ What You Should Do Next
1. Step one
2. Step two

⚠️ Common Mistakes (optional)
```

##### 🔹 Available Options & Tools

| Feature | What It Does | When to Use |
|---------|--------------|-------------|
| **Subject Guide** | Provides semester-wise subject recommendations with 1-line descriptions | "What subjects should I study in 4th semester CSE?" |
| **Career Path** | Shows 4 career roles with required skills | "What can I do after B.Tech in IT?" |
| **Internship Finder** | Lists platforms and eligibility hints | "Where can I apply for internships?" |
| **Interview Prep** | Gives categorized questions (HR + Technical) | "Help me prepare for TCS interview" |
| **General Chat** | Open-ended academic/career Q&A | Any other study-related question |

##### 📥 Inputs Required
- Your branch/department (e.g., "CSE", "Mechanical")
- Your semester or year
- Your target role (optional)

##### 📤 Expected Output
- Structured bullet-point guidance
- Actionable next steps
- Maximum 250–300 words per response

##### 💬 Commands
- `status` — View your current profile (branch, semester, target role)
- `reset` — Start a fresh session
- `clear` / `cls` — Clear the screen
- `exit` — Return to main menu (with option to save conversation)

---

### 🌐 2. Lingua Link

> *"Apna Desi AI Companion — Hinglish Edition 🇮🇳"*

#### 🎯 Purpose

Lingua Link is a **Hinglish-speaking AI companion** that converses naturally in a mix of Hindi and English, exactly like a modern Indian student would text. It's designed to feel like chatting with a friend, not a formal assistant.

#### 👤 Primary Users

- Indian users comfortable with Hinglish
- Anyone who prefers casual, relatable conversations
- Users who find English-only AI too formal

#### 🧩 Problems It Solves

- "I want an AI that talks like my friends"
- "Pure English AI feels robotic"
- "I want casual, supportive conversations"

#### 🧠 AI Behavior

Lingua Link is programmed to:
- **Never** speak in pure English or pure Hindi — always mix
- Use words like "Arre", "Yaar", "Bhai", "Scene", "Sorted", "Jugad"
- Keep technical terms in English (Computer, Internet, etc.)
- Sound emotional and expressive with punctuation (!, ?, ...)
- Understand Indian pop culture references

##### 🔹 Conversation Style Examples

**User**: "I am feeling very sad about my exam."
**Lingua Link**: "Arre yaar, tension mat le. Exam hi toh tha, life thodi khatam ho gayi hai? Agli baar phod denge!"

**User**: "Tell me a joke."
**Lingua Link**: "Ek baat batau? Politicians ke promises aur meri diet plan... dono literally kabhi pure nahi hote!"

##### 📥 Inputs Required
- Just chat naturally! No special format needed.

##### 📤 Expected Output
- Casual Hinglish responses
- Supportive, witty, sometimes dramatic (filmy) personality

##### 💬 Commands
- `exit` / `bye` / `khatam` / `bas` — Exit with a fun goodbye
- `clear` / `cls` — Clear the screen

---

### 💻 3. Code Made Easy

> *"Debug • Generate • Rate — Like a Pro 💪"*

#### 🎯 Purpose

Code Made Easy is a **complete developer toolkit** powered by AI. It combines three major coding assistance modes: debugging broken code, generating new code from descriptions, and reviewing/rating code quality.

#### 👤 Primary Users

- Beginner to intermediate programmers
- Students learning to code
- Developers who want quick code reviews

#### 🧩 Problems It Solves

- "Why isn't my code working?" → Debugger
- "Write code that does X" → Generator
- "Is my code good?" → Rater

##### 🔹 Available Tools (Sub-Menu)

```
╭───────────────────── ⚡ CODE TOOLS ⚡ ─────────────────────╮
│  1 ▸ 🐛 AI Code Debugger    — Find and fix bugs instantly  │
│  2 ▸ ⚡ AI Code Generator   — Turn ideas into code         │
│  3 ▸ ⭐ Rate My Programme   — Get quality scores           │
│  4 ▸ 📜 View Bug History    — Review past mistakes         │
│  5 ▸ 💾 View Saved Codes    — Access your snippets         │
│  0 ▸ 🔙 Back to Main Menu                                  │
╰─────────────────────────────────────────────────────────────╯
```

---

#### 🐛 3.1 AI Code Debugger

**Purpose**: Paste broken code, get instant bug identification and fixes.

**How It Works**:
1. Select programming language
2. Paste your buggy code (type `END` on a new line to finish)
3. AI analyzes and returns formatted output

**Output Format**:
```
❌ Errors Found
1. Error Type – Short reason
2. Error Type – Short reason

🛠️ Fixes
- Fix 1
- Fix 2

✅ Corrected Code
```python
<fixed code here>
```


**Bug History**: All debugged bugs are automatically saved to your personal bug tracker for future reference.

---

#### ⚡ 3.2 AI Code Generator

**Purpose**: Describe what you want in plain English, get working code.

**How It Works**:
1. Describe your requirement (e.g., "Create a Python script that scrapes headlines from a news site")
2. Specify target language (default: Python)
3. AI generates complete, working code

**Post-Generation Options**:
| Option | Description |
|--------|-------------|
| `1` Refine | Request modifications to the generated code |
| `2` Explain | Ask questions about specific parts |
| `3` New Request | Start a completely new generation |
| `4` Save Code | Save the snippet to your personal library |
| `0` Done | Return to Code Made Easy menu |

---

#### ⭐ 3.3 Rate My Programme

**Purpose**: Submit code for quality review and receive a detailed rating.

**How It Works**:
1. Select programming language
2. Paste your code
3. Receive structured feedback

**Output Format**:
```
📊 Code Rating
Score: X / 10

🟢 Strengths
- Point 1
- Point 2

🔴 Improvements Needed
- Point 1
- Point 2

🚫 NOT Recommended For
- Use case 1
```

**Follow-Up**: After receiving the rating, you can ask questions about specific feedback.

---

#### 📜 3.4 View Bug History

A personal tracker that stores all bugs you've debugged, helping you:
- Learn from past mistakes
- Track common error patterns
- Review debugging sessions

---

#### 💾 3.5 View Saved Codes

Your personal code library containing all snippets you've saved from the Generator, organized by:
- Date
- Programming language
- Description

---

### ⏰ 4. Time Travel Chat

> *"India Through The Ages 🇮🇳 — Ancient → Modern → Future"*

#### 🎯 Purpose

Time Travel Chat is an **immersive historical conversation bot** that lets you chat with a person living in any year of Indian history. The AI fully adopts the perspective, language, and worldview of that era.

#### 👤 Primary Users

- History enthusiasts
- Students studying Indian history
- Anyone curious about life in different eras

#### 🧩 Problems It Solves

- "What was life like during the Mughal era?"
- "How did people feel during India's independence struggle?"
- "What would someone from 1857 think about today's world?"

#### 🧠 AI Behavior

The bot strictly stays in character:
- **Location**: Always India (Bharat/Hindustan/British India depending on era)
- **Language**: Hinglish with era-specific vocabulary
- **Knowledge**: Limited to what someone from that year would know
- **Perspective**: Cannot know the future from their timeline

**Era-Specific Adaptations**:

| Era | Time Period | Vocabulary & Themes |
|-----|-------------|---------------------|
| Ancient | Before 1200 AD | Sanskrit influence (Pranam, Arya, Dharma), Mauryas, Guptas, Philosophy |
| Medieval | 1200–1750 | Urdu/Persian (Salam, Huzoor, Saltanat), Mughal Courts, Bhakti/Sufi |
| British Raj | 1757–1947 | "Angrez", "Company Bahadur", "Swaraj", Freedom Struggle |
| Post-Independence | 1947–2024 | "Sarkar", "Desh", Nation Building, Cinema, Cricket |
| Future | 2025+ | India as Superpower, Space Missions, Technology |

##### 🔹 How to Use

1. **Enter a Year**: Type any year (e.g., `1857`, `1947`, `300 BC`, `2050`)
2. **Chat**: Ask questions as if talking to a local citizen
3. **Warp**: Type `warp` to travel to a different year mid-conversation

##### 📥 Example Interaction

**You enter**: `1947`
**Citizen of 1947**: "Pranam! Aaj toh bahut bada din hai mitra! Suna hai aaj raat ko Pandit Nehru jee bhashan denge... Azadi ka pehla din! Angrez finally ja rahe hain!"

##### 💬 Commands
- `warp` — Travel to a different year
- `clear` / `cls` — Clear the screen
- `exit` — Return to main menu (with save option)

---

### 🔮 5. Future Simulator

> *"See Tomorrow Today — Analyze Your Decisions 🔮"*

#### 🎯 Purpose

Future Simulator is a **decision analysis bot** that helps you think through major life choices by simulating three possible futures: best case, worst case, and realistic case.

#### 👤 Primary Users

- Anyone facing a major life decision
- Students choosing career paths
- Professionals considering job changes
- Anyone overthinking a choice

#### 🧩 Problems It Solves

- "Should I drop out to start a startup?"
- "Should I take this job offer or wait?"
- "Should I pursue higher studies abroad?"

#### 🧠 AI Behavior

For every decision, the AI generates a structured analysis:

```
🌟 BEST CASE SCENARIO
- Short-term (0-1 Year): [Immediate positive effects]
- Long-term (3-5+ Years): [Maximum potential success]

⚠️ WORST CASE SCENARIO
- Short-term (0-1 Year): [Immediate risks]
- Long-term (3-5+ Years): [Lasting negative consequences]

⚖️ REALISTIC / AVERAGE CASE
- Short-term (0-1 Year): [Most likely immediate outcome]
- Long-term (3-5+ Years): [Moderate, mixed results]

🔍 Risk vs Reward Analysis
[Comparison summary]

💡 Critical Questions
1. Question you should ask yourself
2. Another important consideration
3. Key factor to evaluate
```

##### 📥 Inputs Required
- A decision statement (e.g., "Should I quit my job to become a content creator?")

##### 📤 Expected Output
- Three detailed scenarios with timeframes
- Risk/reward summary
- Self-reflection questions (AI does NOT decide for you)

##### 💬 Commands
- `clear` / `cls` — Clear the screen
- `exit` — Return to main menu (with save option)

---

### 🎭 6. Explain Like X

> *"Any Topic • Any Persona — Unlimited Creativity 🎭"*

#### 🎯 Purpose

Explain Like X is a **creative explanation engine** that explains any topic through the lens of different styles, personas, and characters. It's perfect for making learning fun or understanding concepts in unconventional ways.

#### 👤 Primary Users

- Students trying to understand difficult concepts
- Teachers looking for creative analogies
- Anyone who learns better through stories/personas

#### 🧩 Problems It Solves

- "Explain quantum physics like I'm 5"
- "Explain machine learning like a pirate would"
- "Explain economics in Shakespeare's style"

#### 🧠 AI Behavior

The AI fully **transforms into the requested persona** without referencing the style explicitly. It adapts:
- Vocabulary and sentence structure
- Metaphors and analogies
- Tone and emotional expression

##### 🔹 Pre-Built Style Suggestions

The bot offers random suggestions from these styles:

| Style Category | Examples |
|----------------|----------|
| Age-Based | A 5-year-old child, A Grumpy Old Man |
| Character | A Pirate Captain, A Harry Potter Wizard |
| Era/Genre | Shakespeare, Noir Detective, Cyberpunk Hacker |
| Modern | Gen Z TikToker, Gordon Ramsay-style Chef |
| Sci-Fi | A Sci-Fi AI, A Caveman |

##### 📥 How to Use

1. **Enter Topic**: What do you want explained? (e.g., "Blockchain")
2. **Choose Style**: Select from suggestions OR type your own OR type `random`
3. **Receive Explanation**: AI responds fully in character

##### 📤 Example

**Topic**: "How does the stock market work?"
**Style**: "A Pirate Captain"

**Output**: "Arrr, listen here matey! The stock market be like the seven seas — everyone's tryin' to find treasure! When ye buy a 'stock', ye be claimin' a piece of a ship. If that ship finds gold (profits, they call it), yer share be worth more doubloons! But beware — storms (recessions) can sink yer ship faster than ye can say 'walk the plank'!"

##### 💬 Commands
- `random` — Get a randomly selected persona
- `clear` / `cls` — Clear the screen
- `exit` — Return to main menu (with save option)

---

### 🔄 7. Conversation Replay

> *"Relive Your Past Chats 🔄 — Learn From History"*

#### 🎯 Purpose

Conversation Replay is a **session management module** that lets you view, replay, and manage all your saved conversations from other agents.

#### 👤 Primary Users

- Anyone who wants to review past AI interactions
- Users learning from previous advice
- Users organizing their chat history

#### 🧩 Problems It Solves

- "What was that advice Study Buddy gave me last week?"
- "I want to reference that code the Generator created"
- "How do I clear old conversations?"

##### 🔹 Features

| Feature | Description |
|---------|-------------|
| **View History** | See a table of all saved conversations (newest first) |
| **Replay Chat** | Select a conversation by number to view the full exchange |
| **Clear All** | Delete entire chat history (with confirmation) |

##### 📋 History Table Display

```
┌────┬──────────────────┬────────────────────┬─────────────────────────────┐
│ #  │ Date             │ Agent              │ Title                       │
├────┼──────────────────┼────────────────────┼─────────────────────────────┤
│ 1  │ 2026-01-16 15:30 │ Study Buddy        │ Career Guidance Session     │
│ 2  │ 2026-01-16 14:00 │ Code Made Easy     │ Python Debugging            │
│ 3  │ 2026-01-15 20:00 │ Time Travel        │ Journey to 1947             │
└────┴──────────────────┴────────────────────┴─────────────────────────────┘
```

##### 💬 Commands
- `[number]` — View that conversation in detail
- `clear` — Delete all history (requires typing `yes` to confirm)
- `exit` — Return to main menu

---

## 🔁 User Flow Example

Here's how a typical user journey works in Handyware AI Hub:

```
┌─────────────────────────────────────────────────────────────────┐
│                         USER OPENS APP                          │
└───────────────────────────────┬─────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────┐
│              🎬 STARTUP ANIMATION + GEMINI CONNECT              │
│           (Auto-detects API key or prompts for input)           │
└───────────────────────────────┬─────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────┐
│                      🏠 MAIN MENU DISPLAYED                     │
│                    (7 agents + Exit option)                     │
└───────────────────────────────┬─────────────────────────────────┘
                                │
                    User types: "3"
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────┐
│                 💻 CODE MADE EASY LAUNCHES                      │
│                    (Sub-menu displayed)                         │
└───────────────────────────────┬─────────────────────────────────┘
                                │
                    User types: "1"
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────┐
│                    🐛 DEBUGGER ACTIVATES                        │
│         1. User enters language: "Python"                       │
│         2. User pastes buggy code                               │
│         3. AI returns analysis + fixed code                     │
│         4. User presses Enter to return                         │
└───────────────────────────────┬─────────────────────────────────┘
                                │
                    User types: "0"
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────┐
│                 📝 SAVE SESSION PROMPT                          │
│            "Save coding session? (y/n)"                         │
│                   → User types "y"                              │
│                   → Enters title                                │
│                   → Session saved to history                    │
└───────────────────────────────┬─────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────┐
│                   🏠 BACK TO MAIN MENU                          │
│            (User can select another agent or exit)              │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🚀 Key Features of the Platform

### 🎨 Premium CLI Experience

- **Cyberpunk Neon Theme**: Cyan, pink, purple, and green color palette
- **ASCII Art Headers**: Custom art for each agent
- **Animated Transitions**: Loading spinners, startup animation, goodbye screen
- **Responsive Panels**: Rich-formatted messages with icons and borders

### 💾 Session Management

- **Auto-Save Prompt**: Every agent asks if you want to save conversations when exiting
- **Conversation Replay**: Access all saved chats from the dedicated module
- **History Clearing**: Option to wipe all history with confirmation

### 🧩 Modular Agent Architecture

Each agent is a self-contained module with:
- Custom system prompts
- Feature-specific logic
- Session context management
- Error handling and recovery

### 🔄 Unified Design Patterns

All agents follow consistent patterns:
- `exit` always returns to menu
- `clear`/`cls` clears the screen
- Conversations can be saved
- Graceful handling of interrupts (Ctrl+C)

---

## 🛠️ Tech Stack

### Frontend (CLI)

| Technology | Purpose |
|------------|---------|
| **Rich** | Premium terminal formatting, colors, panels, tables, and spinners |
| **Python 3.8+** | Core programming language |

### Backend (Logic)

| Technology | Purpose |
|------------|---------|
| **Python Modules** | Modular agent architecture |
| **JSON** | Local storage for chat history and saved codes |
| **Dataclasses/Enums** | Structured data and type safety |

### AI / LLMs

| Technology | Purpose |
|------------|---------|
| **Google Gemini 2.5 Flash Lite** | Primary AI model for all agents |
| **google-generativeai** | Official Google SDK for Gemini API |
| **Custom Prompt Engineering** | Domain-specific prompts for each agent |

---

## ⚙️ Installation & Setup

### Prerequisites

- Python 3.8 or higher
- A Google Gemini API key ([Get one here](https://aistudio.google.com/apikey))

---

### 🚀 One-Click Launch (Recommended)

We provide launcher scripts that **automatically** create a virtual environment, install dependencies, and run the app!

#### Windows Users

```bash
# Just double-click or run:
run.bat
```

#### Linux/Mac Users

```bash
# Make executable (first time only)
chmod +x run.sh

# Run
./run.sh
```

**What the launcher does:**
1. ✅ Checks if Python is installed
2. ✅ Creates `.venv` virtual environment (if not exists)
3. ✅ Activates the virtual environment
4. ✅ Installs all dependencies from `requirements.txt`
5. ✅ Launches the Handyware AI Hub
6. ✅ Cleans up on exit

---

### 📋 Manual Installation (Alternative)

If you prefer manual setup, follow these steps:

#### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/hack-ai-hackathon.git
cd hack-ai-hackathon
```

### Step 2: Create Virtual Environment (Recommended)

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux/Mac
python3 -m venv .venv
source .venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Set Up API Key

**Option A**: Environment Variable (Recommended)

```bash
# Windows (PowerShell)
$env:GEMINI_API_KEY = "your-api-key-here"

# Windows (CMD)
set GEMINI_API_KEY=your-api-key-here

# Linux/Mac
export GEMINI_API_KEY="your-api-key-here"
```

**Option B**: Enter at Runtime

The app will prompt you to enter your API key if the environment variable is not set.

### Step 5: Run the Application

```bash
python chat-bot.py
```

You should see the animated startup sequence and the main menu!

---

## 📸 Screenshots / UI Walkthrough

> *Note: These are placeholder descriptions. Add actual screenshots by replacing the text below with image links.*

### 🏠 Main Menu

The main menu displays the Handyware AI ASCII art logo with gradient neon colors, followed by a two-column agent selection panel. Each agent is listed with its icon, name, and a "▸" arrow indicator.

```
Screenshot: Main menu with ASCII art and agent selection
Location: ./screenshots/main_menu.png
```

### 🤖 Agent Screen (Example: Study Buddy)

When entering an agent, you see:
1. Agent-specific ASCII art header
2. Tagline panel
3. Welcome message from the bot
4. Input prompt with keyboard navigation

```
Screenshot: Study Buddy agent interface
Location: ./screenshots/study_buddy.png
```

### 💬 Chat Interface

Messages are displayed in styled panels:
- **User messages**: Right-aligned, blue border, "👤 You" title
- **Bot messages**: Left-aligned, green border, agent name title
- **Markdown rendering**: Code blocks, bullets, and formatting preserved

```
Screenshot: Chat exchange with formatted messages
Location: ./screenshots/chat_interface.png
```

### 💻 Code Made Easy Sub-Menu

The Code Made Easy module has its own nested menu with 5 options displayed in a compact panel.

```
Screenshot: Code Made Easy tools menu
Location: ./screenshots/code_made_easy.png
```

---

## 🧪 Hackathon Challenges & Learnings

### 🎯 Challenge 1: Managing Multiple Agents

**Problem**: Keeping seven different AI agents consistent while maintaining unique personalities.

**Solution**: 
- Created a modular architecture where each agent is a self-contained package
- Defined common interfaces (run function signature, exit behavior, save prompts)
- Used a central UI module for consistent styling

### 🎯 Challenge 2: Prompt Engineering

**Problem**: Getting the AI to stay in character (especially for Time Travel and Lingua Link).

**Solution**: 
- Extensive system prompts with explicit rules and examples
- "What NOT to do" sections in prompts
- Era-specific vocabulary guidelines

### 🎯 Challenge 3: Terminal UI/UX

**Problem**: CLI apps typically look boring and uninviting.

**Solution**: 
- Rich library for colors, panels, and animations
- Custom cyberpunk neon color palette
- ASCII art headers for visual impact
- Gradient text effects and animated spinners

### 🎯 Challenge 4: Time Constraints

**Problem**: Building 7 unique agents in hackathon time limits.

**Solution**: 
- Prioritized core functionality over edge cases
- Reused common patterns across agents
- Focused on "wow factor" features (animations, unique personas)

---

## 🔮 Future Enhancements

### Planned Features

| Feature | Description | Status |
|---------|-------------|--------|
| **More Agents** | Add specialized agents for Writing, Translation, Research | 📋 Planned |
| **Memory/Context** | Persistent memory across sessions for personalized responses | 📋 Planned |
| **API Mode** | Expose agents via REST API for web/mobile clients | 📋 Planned |
| **Custom Agents** | Let users create their own agents with custom prompts | 📋 Planned |
| **Export Options** | Export conversations as PDF/Markdown | 📋 Planned |
| **Plugin System** | Third-party agent marketplace | 🔮 Future |
| **Web Interface** | Browser-based version alongside CLI | 🔮 Future |

### Known Limitations

- No image/file input support yet
- Single-user, local storage only

---

## 👥 Team / Author

| Role | Name | GitHub |
|------|------|--------|
| **Developer** | Arshad Ali | [@arshadali-coder](https://github.com/arshadali-coder) |
| **RnD** | Zaid | N/A |
| **RnD** | Sharmeen | N/A |
| **RnD** | Ansar | N/A |

### 🏆 Hackathon Participation

This project was built for a **hackathon** to demonstrate multi-agent AI architecture, premium CLI experiences, and creative prompt engineering with Google Gemini.

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2026 Handyware AI Hub

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---

## 🙏 Acknowledgments

- **Google Gemini Team** for the powerful AI model
- **Rich Library** (Will McGugan) for making CLI beautiful
- **Hackathon Organizers** for the opportunity to build this

---

<p align="center">
  <img src="https://img.shields.io/badge/Made%20with-❤️-red?style=for-the-badge" alt="Made with Love"/>
  <img src="https://img.shields.io/badge/Powered%20by-☕%20Coffee-brown?style=for-the-badge" alt="Powered by Coffee"/>
  <img src="https://img.shields.io/badge/Built%20for-Hackathon-purple?style=for-the-badge" alt="Built for Hackathon"/>
</p>

<p align="center">
  <strong>⭐ Star this repo if you found it useful! ⭐</strong>
</p>
