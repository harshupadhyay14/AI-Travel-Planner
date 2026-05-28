# ✈️ AI Travel Planner — Multi-Agent CrewAI System

> A multi-agent AI travel planning system where specialized agents collaborate to create complete, verified 7-day travel itineraries — powered by CrewAI + Groq LLaMA 3.1.

![Python](https://img.shields.io/badge/Python-3.10-blue?style=flat-square&logo=python)
![CrewAI](https://img.shields.io/badge/CrewAI-Multi--Agent-green?style=flat-square)
![Groq](https://img.shields.io/badge/Groq-LLaMA_3.1_8B-orange?style=flat-square)
![LangChain](https://img.shields.io/badge/LangChain-Integrated-purple?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)

🌐 **Live Demo:** [ai-travel-planner-ply0.onrender.com](https://ai-travel-planner-ply0.onrender.com)
💻 **GitHub:** [AI-Travel-Planner](https://github.com/harshupadhyay14/AI-Travel-Planner)

<img width="946" height="413" alt="Screenshot 2026-05-28 084025" src="https://github.com/user-attachments/assets/10f3cb99-179f-4a4f-83af-a02fc03a6c75" />
<img width="948" height="413" alt="Screenshot 2026-05-28 084037" src="https://github.com/user-attachments/assets/067f8e9e-74be-44c1-a7b3-d727fe74a539" />
<img width="947" height="411" alt="Screenshot 2026-05-28 084634" src="https://github.com/user-attachments/assets/0834644f-b663-405c-9d01-acd60edc3f41" />
<img width="943" height="367" alt="Screenshot 2026-05-28 084652" src="https://github.com/user-attachments/assets/d3dba437-5848-49e0-8b18-ac9358ae893c" />
<img width="948" height="412" alt="Screenshot 2026-05-28 084709" src="https://github.com/user-attachments/assets/67ac8ec1-704f-42ac-b1a0-db11bd895ae7" />
---

## 📌 Overview

The AI Travel Planner uses a **crew of 3 specialized AI agents** that work together to plan your perfect trip. Each agent has a distinct role, goal, and set of tools — mimicking how a real travel agency operates.

Unlike single-prompt AI tools, this system uses **agent collaboration and real-time search verification** to ensure itineraries contain real, accurate places — not hallucinated hotels or fake restaurants.

---

## 🤖 The Agent Crew

| Agent | Role | Responsibility |
|---|---|---|
| ✈️ **Expert Travel Agent** | Captain | Creates verified 7-day itinerary with real-world places using search |
| 🌆 **City Selection Expert** | Analyst | Picks best city based on weather, season, prices & interests |
| 🗺️ **Local Tour Guide** | Expert | Provides attractions, customs, weather & cost overview |

---

## ✨ Features

- 🤖 **Multi-Agent Collaboration** — 3 specialized agents work in a crew via CrewAI
- 🔍 **Real-Time Search Verification** — places verified via internet search before inclusion
- 📅 **Complete 7-Day Itinerary** — Morning / Afternoon / Evening breakdown per day
- 🏨 **Hotel & Restaurant Recommendations** — with location and price
- 💰 **Budget Breakdown** — Accommodation, Food, Transport, Total
- 🎒 **Packing List** — customized to destination and interests
- 🛡️ **Safety Tips** — local safety advice per destination
- 🌆 **City Guide** — overview, top attractions, local customs, best time to visit
- 🖊️ **Interest-Based Planning** — personalized based on your hobbies and preferences

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Agent Framework | CrewAI |
| LLM | Groq API — LLaMA 3.1 8B Instant |
| LLM Integration | LangChain (custom GroqLLM wrapper) |
| Search Tool | SearchTools (internet search) |
| Calculator | CalculatorTools (budget estimation) |
| Language | Python 3.10 |
| Deployment | Render |

---

## 📂 Project Structure

```
AI-Travel-Planner/
├── main.py                  # TripCrew — crew orchestration & CLI interface
├── agents.py                # TravelAgents — 3 specialized agent definitions
├── tasks.py                 # TravelTasks — 3 task definitions with structured output
├── tools/
│   ├── search_tools.py      # Internet search tool for agents
│   └── calculator_tools.py  # Budget calculator tool
├── .env                     # API keys (not committed)
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- Groq API Key → [Get one free at console.groq.com](https://console.groq.com)

### 1. Clone the Repository

```bash
git clone https://github.com/harshupadhyay14/AI-Travel-Planner.git
cd AI-Travel-Planner
```

### 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Mac/Linux
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Add Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key_here
```

### 5. Run the Planner

```bash
python main.py
```

You'll be prompted to enter:
- Origin city
- Destination cities
- Date range
- Your interests & hobbies

---

## 💡 How It Works

```
User inputs: origin, cities, dates, interests
              ↓
City Selection Expert
→ Analyzes weather, season, prices
→ Recommends best city to visit
              ↓
Local Tour Guide
→ Researches attractions, customs, weather
→ Builds city guide with cost overview
              ↓
Expert Travel Agent (Captain)
→ Verifies all places via real-time search
→ Assembles complete 7-day itinerary
→ Adds hotels, restaurants, budget, packing list
              ↓
Final Output: Complete personalized travel plan
```

---

## 📋 Sample Output Format

```
DAY 1:
- Morning: Visit Colosseum (arrive early)
- Afternoon: Lunch at Trattoria da Enzo
- Evening: Walk through Trastevere

HOTELS:
- Hotel Artemide | Via Nazionale | ~$120/night

BUDGET:
- Accommodation: $840
- Food: $300
- Transport: $150
- Total: $1,290

PACKING LIST:
- Comfortable walking shoes
- Sunscreen, light jacket

SAFETY TIPS:
- Watch for pickpockets near tourist areas
```

---

## 🔧 Environment Variables

| Variable | Description |
|---|---|
| `GROQ_API_KEY` | Groq API key for LLaMA inference |

---

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add your feature'`)
4. Push and open a Pull Request

---

## 👨‍💻 Author

**Harsh Upadhyay**
- 🎓 B.Tech CSE, Hindustan College of Science and Technology
- 💼 [LinkedIn](https://www.linkedin.com/in/harshu-53119124b)
- 💻 [GitHub](https://github.com/harshupadhyay14)
- 📧 harshupadhyay1414@gmail.com

---

## 📄 License

MIT License — free to use for learning or portfolio.

---

> ⭐ If you found this useful, give it a star on GitHub!
