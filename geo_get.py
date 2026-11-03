from flask import Flask, request, send_from_directory

app = Flask(__name__)

@app.route("/")
def index():
    return send_from_directory(".", "index.html")

@app.route("/logme/<coords>")
def logme(coords):
    with open("geo.log", "a", encoding="utf-8") as f:
        f.write(coords + "\n")
    return "ok"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000)
