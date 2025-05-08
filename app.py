from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='eventlet')

@app.route('/')
def index():
    return "Server is running"

@socketio.on('connect')
def handle_connect():
    print("Client connected")

@socketio.on('disconnect')
def handle_disconnect():
    print("Client disconnected")

@socketio.on('screen-data')
def handle_screen(data):
    socketio.emit('screen-data', data, broadcast=True)

@socketio.on('audio-data')
def handle_audio(data):
    socketio.emit('audio-data', data, broadcast=True)

@socketio.on('video-data')
def handle_video(data):
    socketio.emit('video-data', data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0", port=10000)
