from flask import request, jsonify
from config import app, db
from models import Career,Joker,Consumable,Voucher,Hands,Deck
import zlib, json

@app.route("/upload_file/<int:file_number>", methods=["POST"])
def readFile(file_number):
    planet_list = ["ceres", "earth", "eris", "jupiter", "mars", "mercury", "neptune", "planet_x", "pluto", "saturn", "uranus", "venus"]

    spectral_list = ["ankh", "aura", "black_hole", "cryptid", "deja_vu", "ectoplasm", "familiar", "grim", "hex", "immolate", "incantation", "medium", "ouija", "sigil", "talisman", "trance", "soul", "wraith"]

    name_joker = ["abstract", "ancient", "burnt", "clever", "crafty", "crazy", "devious", "droll", "faceless", "glass", "golden", "half", "invisible", "jolly", "mad", "marble", "sly", "smeared", "space", 
                  "square", "stencil", "stone", "wee", "wily", "zany"]
    
    the_joker = ["duo", "family", "idol", "order", "tribe", "trio"]

    card_joker = ["baseball", "business", "flash", "gift", "trading"]

    not_the_tarot = ["death", "judgement", "justice", "strength", "temperance"]

    if(request.files.get("profile").filename != "profile.jkr"):
        return jsonify({"message": "Please upload a Balatro save file"}), 400
    
    file_data = request.files.get("profile").read()
    file_data = zlib.decompress(file_data, wbits= -zlib.MAX_WBITS).decode("utf-8")

    if "career_stats" not in file_data or "joker_usage" not in file_data or "voucher_usage" not in file_data or "challenge_progress" not in file_data or "consumeable_usage" not in file_data or "deck_usage" not in file_data:
        return jsonify({"message": "Save file missing required information"}), 400
    
    #removes unecessary characters to enable json conversion
    # should be able to replace this with regex re.sub(regex, regex_replacement, string input)
    file_data = file_data.replace("[", "")
    file_data = file_data.replace("]", "")
    file_data = file_data.replace("=", ":")
    file_data = file_data.replace(",}", "}")
    file_data = file_data.replace("c_", "")
    file_data = file_data.replace("j_", "")
    file_data = file_data.replace("b_", "")
    file_data = file_data.replace("v_", "")
    
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
    
    # when reading check to see if something exists in file num 4 (total) if not create it otherwise add the values to it

    new_career = Career(
        file_num = file_number,
        file_name = file_data["name"],
        cards_discarded = career["cards_discarded"],
        hands_played = career["hands_played"],
        dollars_earned = career["dollars_earned"],
        cards_played = career["cards_played"],
        planetarium_used = career["planetarium_used"],
        wins = career["wins"],
        shop_rerolls = career["shop_rerolls"],
        losses = career["losses"],
        tarots_bought = career["tarots_bought"],
        shop_dollars_spent = career["shop_dollars_spent"],
        planets_bought = career["planets_bought"],
        vouchers_bought = career["vouchers_bought"],
        tarot_reading_used = career["tarot_reading_used"],
        rounds = career["rounds"],
        jokers_sold = career["jokers_sold"],
        face_cards_played = career["face_cards_played"],
        playing_cards_bought = career["playing_cards_bought"]
    )

    db.session.add(new_career)
    # db.session.commit()

    for joker in file_data["joker_usage"]:
        name = joker

        # checks savefile naming and converts joker names to proper names as needed
        if name in name_joker:
            name += "_joker"

        elif name in the_joker:
            name = "the_" + name

        elif name in card_joker:
            name += "_card"

        elif name == "ceremonial":
            name += "_dagger"

        elif name == "delayed_grat":
            name += "ification"

        elif name == "trousers":
            name = "spare_" + name

        elif name == "mail":
            name += "_in_rebate"

        elif name == "chaos":
            name += "_the_clown"

        elif name == "mr_bones":
            name = "mr._bones"

        elif name == "mystisummit":
            name = "mystic_summit"

        elif name == "smiley":
            name += "_face"

        elif name == "selzer":
            name = "seltzer"

        elif name == "dna":
            name = "DNA"
        
        elif name == "ring_master":
            name = "showman"

        elif name == "ticket":
            name = "golden_" + name

        elif name == "oops":
            name += "!_all_6s"
        
        elif name == "riff_raff":
            name = "Riff-Raff"

        new_joker = Joker(
            file_num = file_number,
            joker_name = name,
            joker_count = file_data["joker_usage"][joker]["count"],
            joker_wins =  file_data["joker_usage"][joker]["wins"],
            joker_losses = file_data["joker_usage"][joker]["losses"])
        db.session.add(new_joker)

    for consumable in file_data["consumeable_usage"]:
        name = consumable
        c_type = ""
        if consumable in planet_list:
            c_type = "planet"
        elif consumable in spectral_list:
            if name == "soul":
                name = "the_" + name
            c_type = "spectral"
        else:
            if name not in not_the_tarot:
                name = "the_" + name
            c_type = "tarot"
        new_consumable = Consumable(
            file_num = file_number,
            consumable_name = name,
            consumable_count = file_data["consumeable_usage"][consumable]["count"],
            consumable_type = c_type
        )
        db.session.add(new_consumable)

    for voucher in file_data["voucher_usage"]:
        name = voucher
        if name == "magitrick":
            name = "magic_trick"
        print(name)
        new_voucher = Voucher(
            file_num = file_number,
            voucher_name = name,
            voucher_count = file_data["voucher_usage"][voucher]["count"]
        )
        db.session.add(new_voucher)

    for hands in file_data["hand_usage"]:
        new_hands = Hands(
            file_num = file_number,
            hand_name = hands,
            hand_count = file_data["hand_usage"][hands]["count"]
        )
        db.session.add(new_hands)

    for deck in file_data["deck_usage"]:
        new_deck = Deck(
            file_num = file_number,
            deck_name = deck,
            deck_wins =  file_data["deck_usage"][deck]["wins"],
            deck_losses = file_data["deck_usage"][deck]["losses"])
        db.session.add(new_deck)
        
    db.session.commit()
    return jsonify({"message": "File uploaded successfully"}), 200

@app.route("/get_<string:item_type>/<int:file_number>", methods=["GET"])
def getStats(item_type,file_number):
    stats_json = []
    if item_type == "career":
        for x in db.session.query(Career).filter(Career.file_num == file_number):
            stats_json.append(x.to_json())
    elif item_type == "jokers":
        for x in db.session.query(Joker).filter(Joker.file_num == file_number):
            stats_json.append(x.to_json())
    elif item_type == "consumables":
        for x in db.session.query(Consumable).filter(Consumable.file_num == file_number):
            stats_json.append(x.to_json())
    elif item_type == "tarots":
        for x in db.session.query(Consumable).filter(Consumable.file_num == file_number).filter(Consumable.consumable_type == "tarot"):
            stats_json.append(x.to_json())
    elif item_type == "planets":
        for x in db.session.query(Consumable).filter(Consumable.file_num == file_number).filter(Consumable.consumable_type == "planet"):
            stats_json.append(x.to_json())
    elif item_type == "spectrals":
        for x in db.session.query(Consumable).filter(Consumable.file_num == file_number).filter(Consumable.consumable_type == "spectral"):
            stats_json.append(x.to_json())
    elif item_type == "vouchers":
        for x in db.session.query(Voucher).filter(Voucher.file_num == file_number):
            stats_json.append(x.to_json())
    elif item_type == "hands":
        for x in db.session.query(Hands).filter(Hands.file_num == file_number):
            stats_json.append(x.to_json())
    elif item_type == "decks":
        for x in db.session.query(Deck).filter(Deck.file_num == file_number):
            stats_json.append(x.to_json())
    else:
        return jsonify({"message": "Invalid stats request"}), 400

    return stats_json

@app.route("/remove_file/<int:file_number>", methods=["DELETE"])
def remove_file(file_number):
    for x in db.session.query(Career).filter(Career.file_num == file_number):
        db.session.delete(x)
    
    for x in db.session.query(Joker).filter(Joker.file_num == file_number):
        db.session.delete(x)

    for x in db.session.query(Consumable).filter(Consumable.file_num == file_number):
        db.session.delete(x)

    for x in db.session.query(Voucher).filter(Voucher.file_num == file_number):
        db.session.delete(x)

    for x in db.session.query(Hands).filter(Hands.file_num == file_number):
        db.session.delete(x)

    for x in db.session.query(Deck).filter(Deck.file_num == file_number):
        db.session.delete(x)
    
    db.session.commit()
    return jsonify({"message": "File removed successfully"}), 200

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)