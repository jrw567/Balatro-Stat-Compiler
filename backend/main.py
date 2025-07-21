from flask import Flask, request, jsonify
from flask_cors import CORS
import zlib

#create the app
app = Flask(__name__)
CORS(app)

@app.route("/", methods=["POST"])
def temp():
    file_data = request.files.get("profile").read()
    print(zlib.decompress(file_data, wbits= -zlib.MAX_WBITS))
    return jsonify({"message": "File Uploaded Successfully"}), 200

if __name__ == "__main__":
    app.run(debug=True)