from flask import request, jsonify
from config import app, db
from models import Career,Joker
import zlib, json

@app.route("/", methods=["POST"])
def readFile():
    if(request.files.get("profile").filename != "profile.jkr"):
        return jsonify({"message": "Please upload a profile.jkr file"}), 400
    
    file_data = request.files.get("profile").read()
    file_data = zlib.decompress(file_data, wbits= -zlib.MAX_WBITS).decode("utf-8")

    if "career_stats" not in file_data or "joker_usage" not in file_data or "voucher_usage" not in file_data or "challenge_progress" not in file_data or "consumeable_usage" not in file_data:
        return jsonify({"message": "profile.jkr file missing required information"}), 400
    
    #removes unecessary characters to enable json conversion
    file_data = file_data.replace("[", "")
    file_data = file_data.replace("]", "")
    file_data = file_data.replace("=", ":")
    file_data = file_data.replace(",}", "}")
    file_data = file_data.replace("return ", "")

    # replaces difficulty naming convention in save file to a readable format to enable json conversion
    file_data = file_data.replace("1:", '"white_stake":')
    file_data = file_data.replace("2:", '"red_stake":')
    file_data = file_data.replace("3:", '"green_stake":')
    file_data = file_data.replace("4:", '"black_stake":')
    file_data = file_data.replace("5:", '"blue_stake":')
    file_data = file_data.replace("6:", '"purple_stake":')
    file_data = file_data.replace("7:", '"orange_stake":')
    file_data = file_data.replace("8:", '"gold_stake":')

    file_data = json.loads(file_data)
    for joker in file_data["joker_usage"]:
        wins = 0
        losses = 0
        for stake in file_data["joker_usage"][joker]["wins"]:
            wins += file_data["joker_usage"][joker]["wins"][stake]
        
        for stake in file_data["joker_usage"][joker]["losses"]:
            losses += file_data["joker_usage"][joker]["losses"][stake]
        file_data["joker_usage"][joker]["wins"] = wins
        file_data["joker_usage"][joker]["losses"] = losses

    print(file_data)
    return jsonify({"message": "File Uploaded Successfully"}), 200

if __name__ == "__main__":
    app.run(debug=True)