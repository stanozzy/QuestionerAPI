''' This file initializes the app '''


import os

from app import create_app

config_name = os.getenv('APP_SETTINGS')

app = create_app(config_name)

@app.route('/')
def index():
    return 'Questioner Home'


if __name__ == '__main__':

    app.run(debug=True)