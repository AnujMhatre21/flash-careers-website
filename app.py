from flask import Flask

app = Flask(__name__)


# @ decorator
@app.route("/")
def hello_world():
  return "hello Boss"


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
