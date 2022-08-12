from flask import Flask, render_template, send_from_directory   
from main import Ets
from flask_socketio import SocketIO, send, emit
import os


def main():
    app = Flask(__name__)
    socketio = SocketIO(app, cors_allowed_origins='*')
    ets = Ets()
    @app.route('/')
    def index():
        return render_template('index.html')
        try:
            last_line = ets.tail()
        except:
            return 'No log file found'
        
        try:
            return ets.translateMessage()
        except:
            return 'Could not translate message'

        return 'Unexpected error'

    @app.route('/favicon.ico')
    def favicon(): 
        return send_from_directory(os.path.join(app.root_path, 'images'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

    @socketio.on('message')
    def handle_message(message):
        send(message)

    # app.run(host='0.0.0.0', port=81)
    socketio.run(app, debug = True)

if __name__ == "__main__":
    main()
    