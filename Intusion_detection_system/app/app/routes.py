from flask import render_template
from flask_socketio import emit
from app import app, socketio

@app.route("/")
def index():
    return render_template('index.html')

@socketio.on('connect')

def handle_connect():
    emit('message', 'Connected')

if __name__ == '__main__':
    socketio.run(app, debug = True)
