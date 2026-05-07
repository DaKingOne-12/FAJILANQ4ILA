from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello PSHS! This is my first Flask app (stored on GitHub)."

@app.route("/about")
def about():
    return "About: This simple app demonstrates Flask + Git + VS Code."

if __name__ == "__main__":
    app.run(debug=True)