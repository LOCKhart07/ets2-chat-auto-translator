from flask import Flask
from main import Ets


def main():
    app = Flask(__name__)
    ets = Ets()
    @app.route('/')
    def index():
        try:
            last_line = ets.tail()
        except:
            return 'No log file found'
        
        try:
            return ets.translateMessage()
        except:
            return 'Could not translate message'
            
        return 'Unexpected error'
    app.run(host='0.0.0.0', port=81)

if __name__ == "__main__":
    main()