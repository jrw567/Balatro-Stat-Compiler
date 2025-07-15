from flask import Flask
from flask_cors import CORS

#create the app
app = Flask(__name__)
CORS(app)

@app.route("/")
def temp():
    return True

if __name__ == "__main__":
    app.run(debug=True)