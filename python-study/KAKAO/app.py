from flask import Flask, render_template

app = Flask(__name__)

@app.route("/") #라우팅하는 방법
def main() : 
    return render_template('index.html')

app.run(host="localhost", port=8080)