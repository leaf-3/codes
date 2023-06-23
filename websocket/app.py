from flask import Flask
from flask_socketio import SocketIO
from applications import create_app
from extensions.websocket import websocket
app = create_app()

socketio = websocket(app)
if __name__ == "__main__":
    socketio.run(app=app,host="127.0.0.1",port=5000)