from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here' # Needed for session security

# Initialize SocketIO
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('index.html')

# Listen for a connection event
@socketio.on('connect')
def handle_connect():
    print("A user connected!")
    send("Welcome to the chat server!") # Sends a message back to the client

if __name__ == '__main__':
    # Run the app with SocketIO
    socketio.run(app, debug=True)