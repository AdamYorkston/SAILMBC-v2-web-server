from app import create_app
import os

if __name__ == "__main__":
    create_app().run(host='0.0.0.0', port=os.environ.get("FLASK_SERVER_PORT"), debug=True)
