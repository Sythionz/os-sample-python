from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Gegrüßt seien die die sich auf diesem Planeten befinden der sich Erde nennt!"

if __name__ == "__main__":
    application.run()
