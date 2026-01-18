# 🌌 NextAdventure AI Game

> **A recursive, AI-powered "Choose Your Own Adventure" generator built with FastAPI, React, and Google Gemini 2.5.**

![Project Status](https://img.shields.io/badge/Status-Active-success)
![License](https://img.shields.io/badge/License-MIT-blue)
![Stack](https://img.shields.io/badge/Stack-FastAPI%20|%20React%20|%20PostgreSQL-purple)

## 📖 About The Project

**FableForge AI** is not just a chatbot—it's a **game engine**. 

Unlike standard AI text games that generate one response at a time, this system uses **Recursive AI Prompting** to pre-generate an entire branching narrative tree (3-4 levels deep) before the player even starts. This ensures consistent storytelling, multiple endings, and instant response times during gameplay.

### **Key Features**
* **🧠 Recursive Story Generation:** Generates a complex JSON tree with 15+ unique nodes, choices, and outcomes in a single batch process.
* **⚡ Streaming & Cancellation:** Real-time UI feedback with the ability to abort long-running AI generation tasks.
* **💾 Persistent Worlds:** Every generated story is saved to a PostgreSQL database, allowing users to replay or share scenarios.
* **🎨 Immersive UI:** A modern, dark-mode interface built with React and Vite, featuring loading animations and responsive design.
* **🛡️ Robust Backend:** Built on FastAPI with SQLAlchemy for high-performance async database handling.

---

## 🛠️ Tech Stack

### **Frontend**
* **React.js (Vite):** For a blazing fast UI.
* **Axios:** For API communication with cancellation signals.
* **CSS3:** Custom dark-mode styling with animations.

### **Backend**
* **Python 3.10+:** Core logic.
* **FastAPI:** High-performance async web framework.
* **Google GenAI SDK:** Interfacing with the Gemini 2.5 Flash model.
* **SQLAlchemy:** ORM for database management.
* **PostgreSQL:** Relational database for storing story trees.

---

## 🚀 Getting Started

Follow these steps to set up the project locally.

### **Prerequisites**
* Python 3.10 or higher
* Node.js & npm
* A Google AI Studio API Key (Free)
* A PostgreSQL Database URL (Local or Neon/Supabase)

### **1. Clone the Repository**
```bash
git clone https://github.com/YOUR_USERNAME/fableforge-ai.git
cd fableforge-ai
```

### **2. Backend Setup**
Navigate to the backend folder to set up the Python environment.

```bash
cd backend

# Create Virtual Environment
python -m venv venv

# Activate Environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install Dependencies
pip install -r requirements.txt
```

#### **Configuration (.env)**
Create a file named `.env` in the `backend/` folder:

```env
# Get a free DB from neon.tech if you don't have one locally
DATABASE_URL="postgresql://user:password@host/dbname?sslmode=require"

# Get a key from aistudio.google.com
GOOGLE_API_KEY="AIzaSy_YOUR_API_KEY_HERE"
```

#### **Run the Server**
```bash
uvicorn main:app --reload
```
Server runs at: `http://127.0.0.1:8000`

### **3. Frontend Setup**
Open a new terminal and navigate to the frontend folder.

```bash
cd frontend

# Install Libraries
npm install

# Start Dev Server
npm run dev
```
Client runs at: `http://localhost:5173`

---

## 🎮 How to Play
1. **Open** `http://localhost:5173`
2. **Input a Theme:** Type anything (e.g., "A janitor on the Death Star" or "A detective in 2050 Mumbai").
3. **Wait for Generation:** The AI will construct the world (approx 10-15 seconds). You can click "Stop Generation" if it takes too long.
4. **Play:** Make choices to navigate the story tree.
5. **Win/Loss:** Reach a valid ending node to finish the game.

---

## 📂 Project Structure

```
fableforge-ai/
├── backend/
│   ├── core/           # Config & Settings
│   ├── db/             # Database connection & models
│   ├── models/         # SQLAlchemy Tables (Stories, Nodes)
│   ├── services/       # AI Logic (Gemini integration)
│   ├── main.py         # API Entry point
│   └── .env            # Secrets (Ignored by Git)
│
├── frontend/
│   ├── src/
│   │   ├── api.js      # Axios API calls
│   │   ├── App.jsx     # Main Game Logic
│   │   └── App.css     # Dark Mode Styles
│   └── package.json
│
└── README.md
```

---

## 🔮 Future Roadmap
- [ ] **User Auth:** Allow users to save their favorite stories.
- [ ] **Image Generation:** Use Gemini Pro Vision to generate illustrations for each scene.
- [ ] **Voice Narration:** Add Text-to-Speech API for audio storytelling.
- [ ] **Multiplayer:** Allow two players to vote on choices.

---

## 🤝 Contributing
Contributions are welcome! Please fork the repository and create a pull request with your improvements.

---

## 📄 License
Distributed under the MIT License. See LICENSE for more information.

---

## 💬 Support
For issues, questions, or feature requests, please open an issue on GitHub or reach out to the maintainers.

**Happy storytelling! 🎭✨**
