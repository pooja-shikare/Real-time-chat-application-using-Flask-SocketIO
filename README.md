# Real time chat application using Flask SocketIO

# 💬 Real-Time Chat Application

An advanced asynchronous web-based chat application built using **Flask**, **Flask-SocketIO**, and native **WebSockets** to enable seamless, real-time communication between multiple users.

---

### 🚀 Week 1 Milestones Achieved
* **Environment Isolation:** Initialized a local Python virtual environment to manage dependencies safely.
* **Framework Initialization:** Configured a boilerplate Flask web server integrated with WSGI/ASGI-like socket capabilities.
* **WebSocket Implementation:** Established open event listeners (`connect`) handling instant bi-directional messaging protocols.
* **Frontend Setup:** Linked external JavaScript socket clients to capture background network transmissions.

---

### 📁 Project Architecture
```text
├── static/
│   ├── chat.js          # Handles client-side WebSocket event loops
│   └── style.css        # Custom UI styling configurations
├── templates/
│   └── index.html       # Primary chat application view template
├── app.py               # Main Flask server application and SocketIO routing
├── requirements.txt     # Python production and development dependencies
└── README.md            # Project documentation and tracking

