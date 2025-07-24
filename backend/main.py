from flask import request, jsonify
from config import app, db
from models import Career,Joker,Consumeable,Voucher,Deck
import zlib, json

@app.route("/upload_file/<int:file_number>", methods=["POST"])
def readFile(file_number):
    if(request.files.get("profile").filename != "profile.jkr"):
        return jsonify({"message": "Please upload a profile.jkr file"}), 400
    
    file_data = request.files.get("profile").read()
    file_data = zlib.decompress(file_data, wbits= -zlib.MAX_WBITS).decode("utf-8")

    if "career_stats" not in file_data or "joker_usage" not in file_data or "voucher_usage" not in file_data or "challenge_progress" not in file_data or "consumeable_usage" not in file_data or "deck_usage" not in file_data:
        return jsonify({"message": "profile.jkr file missing required information"}), 400
    
    #removes unecessary characters to enable json conversion
    file_data = file_data.replace("[", "")
    file_data = file_data.replace("]", "")
    file_data = file_data.replace("=", ":")
    file_data = file_data.replace(",}", "}")
    file_data = file_data.replace("return ", "")

    # replaces difficulty naming convention for wins and losses in save file to a key/value pair format to enable json conversion
    file_data = file_data.replace("1:", '"1":')
    file_data = file_data.replace("2:", '"2":')
    file_data = file_data.replace("3:", '"3":')
    file_data = file_data.replace("4:", '"4":')
    file_data = file_data.replace("5:", '"5":')
    file_data = file_data.replace("6:", '"6":')
    file_data = file_data.replace("7:", '"7":')
    file_data = file_data.replace("8:", '"8":')

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

    for deck in file_data["deck_usage"]:
        wins = 0
        losses = 0
        for stake in file_data["deck_usage"][deck]["wins"]:
            wins += file_data["deck_usage"][deck]["wins"][stake]
        
        for stake in file_data["deck_usage"][deck]["losses"]:
            losses += file_data["deck_usage"][deck]["losses"][stake]
        file_data["deck_usage"][deck]["wins"] = wins
        file_data["deck_usage"][deck]["losses"] = losses

    career = file_data["career_stats"]
    
    career_stats = Career(
        file_num = file_number,
        file_name = file_data["name"],
        cards_discarded = career["c_cards_discarded"],
        hands_played = career["c_hands_played"],
        dollars_earned = career["c_dollars_earned"],
        cards_played = career["c_cards_played"],
        planetarium_used = career["c_planetarium_used"],
        wins = career["c_wins"],
        shop_rerolls = career["c_shop_rerolls"],
        losses = career["c_losses"],
        tarots_bought = career["c_tarots_bought"],
        shop_dollars_spent = career["c_shop_dollars_spent"],
        planets_bought = career["c_planets_bought"],
        vouchers_bought = career["c_vouchers_bought"],
        tarot_reading_used = career["c_tarot_reading_used"],
        rounds = career["c_rounds"],
        jokers_sold = career["c_jokers_sold"],
        face_cards_played = career["c_face_cards_played"],
        playing_cards_bought = career["c_playing_cards_bought"]
    )

    # db.session.add(career_stats)
    # db.session.commit()

    for joker in file_data["joker_usage"]:
        new_joker = Joker(
            file_num = file_number,
            joker_name = joker,
            joker_wins =  file_data["joker_usage"][joker]["wins"],
            joker_losses = file_data["joker_usage"][joker]["losses"])
        # db.session.add(new_joker)
        # db.session.commit()

    for consumeable in file_data["consumeable_usage"]:
        new_consumeable = Consumeable(
            file_num = file_number,
            consumeable_name = consumeable,
            consumeable_count = file_data["consumeable_usage"][consumeable]["count"]
        )
        # db.session.add(new_consumeable)
        # db.session.commit()

    for voucher in file_data["voucher_usage"]:
        new_voucher = Voucher(
            file_num = file_number,
            voucher_name = voucher,
            voucher_count = file_data["voucher_usage"][voucher]["count"]
        )
        # db.session.add(new_voucher)
        # db.session.commit()

    for deck in file_data["deck_usage"]:
        new_deck = Deck(
            file_num = file_number,
            deck_name = deck,
            deck_wins =  file_data["deck_usage"][deck]["wins"],
            deck_losses = file_data["deck_usage"][deck]["losses"])
        # db.session.add(new_deck)
        # db.session.commit()


    return jsonify({"message": "File Uploaded Successfully"}), 200

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)