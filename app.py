from flask import Flask

# Include the handler method(s)
from handlers.pollfish_handler import verify

app = Flask(__name__)


@app.route('/pollfish-webhook')
def verify_survey():
    return verify()


if __name__ == '__main__':
    app.run()
