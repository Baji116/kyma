from flask import Flask
import hdbcli
app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello World! Tested successfully!!!"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("8000"), debug=True)
