# 📝 Online Whiteboard (Miro-lite)

An online collaborative whiteboard built with Flask, SQLite3, HTML, CSS, and JavaScript. This project allows freehand drawing, adding sticky notes, and saving/reloading boards.

🔗 **Live Demo**: [https://online-whiteboard-x9jc.onrender.com](https://online-whiteboard-x9jc.onrender.com)

## 🚀 Purpose
Built as a portfolio project for internship applications (e.g., Adobe).

## ✨ Features
- ✏️ **Freehand Drawing** on canvas
- 🗒️ **Sticky Notes** (text boxes)
- 💾 **Save Boards** to SQLite3
- 📂 **Reload Saved Boards**
- 🎨 **Simple, Intuitive Interface**

## 📂 Project Structure
```
online_whiteboard/
│
├── app.py                # Flask backend
├── whiteboard.db         # SQLite database (auto-created)
│
├── static/
│   ├── style.css         # Styling
│   └── script.js         # Canvas + sticky notes logic
│
└── templates/
    └── index.html        # Frontend UI
```

## ⚡ Installation & Setup
1. Clone the repository (or copy project files):
   ```bash
   cd online_whiteboard
   ```
2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   ```
3. Activate the virtual environment:
   ```bash
   source venv/bin/activate
   ```
4. Install Flask:
   ```bash
   pip install flask
   ```
5. Run the application:
   ```bash
   python3 app.py
   ```
6. Open in browser: [http://127.0.0.1:5000](http://127.0.0.1:5000)

## 📌 Future Improvements
- 🖼️ **Export board as PNG**
- 🔵 **Add basic shapes** (lines, rectangles, circles)
- ↩️ **Undo/Redo support**
- 🌍 **Real-time collaboration** (WebSockets/Socket.IO)

## 🏆 Why This Project?
- Demonstrates creativity and collaboration features (relevant for Adobe tools).
- Full-stack project: Frontend (HTML/JS/CSS) + Backend (Flask) + Database (SQLite).
- Lightweight, runs locally in minutes.

--- 
