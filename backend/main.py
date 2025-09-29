from flask import request, jsonify
from config import app, db
from models import Career,Joker,Consumable,Voucher,Hands,Deck
import zlib, json

@app.route("/upload_file/<int:file_number>", methods=["POST"])

#Reads file from given form data and stores it under given file number
#Reads all notable information including: Career, Joker, Hand, Consumable, and Deck Statistics
#Checks the total file to see if information is stored and if it is it will total the stats otherwise it will create a new entry
def readFile(file_number):

    #Combined data stored as a 4th file under file number 4
    TOTAL_FILE = 4

    #List of planet cards to check for to distinguish consumables
    planet_list = ["ceres", "earth", "eris", "jupiter", "mars", "mercury", "neptune", "planet_x", "pluto", "saturn", "uranus", "venus"]

    #List of spectral cards to check for to distinguish consumables
    spectral_list = ["ankh", "aura", "black_hole", "cryptid", "deja_vu", "ectoplasm", "familiar", "grim", "hex", "immolate", "incantation", "medium", "ouija", "sigil", "talisman", "trance", "soul", "wraith"]

    #List of Jokers whose names are followed by Joker ie. Abstract Joker but aren't listed as such in the save file
    name_joker = ["abstract", "ancient", "burnt", "clever", "crafty", "crazy", "devious", "droll", "faceless", "glass", "golden", "half", "invisible", "jolly", "mad", "marble", "sly", "smeared", "space", 
                  "square", "stone", "wee", "wily", "zany"]
    
    #List of Jokers whose names start with The ie. The Duo but aren't listed as such in the save file
    the_joker = ["duo", "family", "idol", "order", "tribe", "trio"]

    #List of Jokers whose names are followed by Card ie. Baseball Card but aren't listed as such in the save file
    card_joker = ["baseball", "business", "flash", "gift", "trading"]

    #List of Tarots whose names dont start with The (most do but none have it listed within the save file)
    not_the_tarot = ["death", "judgement", "justice", "strength", "temperance"]

    if(request.files.get("profile").filename != "profile.jkr"):
        return jsonify({"message": "Please upload a Balatro save file"}), 400
    
    file_data = request.files.get("profile").read()
    file_data = zlib.decompress(file_data, wbits= -zlib.MAX_WBITS).decode("utf-8")

    if "career_stats" not in file_data or "joker_usage" not in file_data or "voucher_usage" not in file_data or "challenge_progress" not in file_data or "consumeable_usage" not in file_data or "deck_usage" not in file_data:
        return jsonify({"message": "Save file missing required information"}), 400
    
    # removes unecessary characters to enable json conversion
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

    #Reads Joker data from file and tallies wins and losses
    for joker in file_data["joker_usage"]:
        wins = 0
        losses = 0
        for stake in file_data["joker_usage"][joker]["wins"]:
            wins += file_data["joker_usage"][joker]["wins"][stake]
        
        for stake in file_data["joker_usage"][joker]["losses"]:
            losses += file_data["joker_usage"][joker]["losses"][stake]
        file_data["joker_usage"][joker]["wins"] = wins
        file_data["joker_usage"][joker]["losses"] = losses

    #Reads Deck data from file and tallies wins and losses
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
    
    #Creates new entries for respective file numbers
    #Also checks total file to either combine data or create a new entry if not present
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

    q = db.session.query(Career).filter(Career.file_num == TOTAL_FILE)
    if(db.session.query(q.exists()).scalar()):
        for x in q:
            x.cards_discarded += career["cards_discarded"]
            x.hands_played += career["hands_played"]
            x.dollars_earned += career["dollars_earned"]
            x.cards_played += career["cards_played"]
            x.planetarium_used += career["planetarium_used"]
            x.wins += career["wins"]
            x.shop_rerolls += career["shop_rerolls"]
            x.losses += career["losses"]
            x.tarots_bought += career["tarots_bought"]
            x.shop_dollars_spent += career["shop_dollars_spent"]
            x.planets_bought += career["planets_bought"]
            x.vouchers_bought += career["vouchers_bought"]
            x.tarot_reading_used += career["tarot_reading_used"]
            x.rounds += career["rounds"]
            x.jokers_sold += career["jokers_sold"]
            x.face_cards_played += career["face_cards_played"]
            x.playing_cards_bought += career["playing_cards_bought"]
        
    else:
        new_career = Career(
            file_num = TOTAL_FILE,
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
        
        elif name == "gluttenous_joker":
            name = "gluttonous_joker"

        elif name == "drivers_license":
            name = "driver's_license"

        elif name == "stencil":
            name = "joker_stencil"

        elif name == "todo_list":
            name = "to_do_list"
        
        elif name == "caino":
            name = "canio"

        new_joker = Joker(
            file_num = file_number,
            joker_name = name,
            joker_count = file_data["joker_usage"][joker]["count"],
            joker_wins =  file_data["joker_usage"][joker]["wins"],
            joker_losses = file_data["joker_usage"][joker]["losses"])
        
        db.session.add(new_joker)

        q = db.session.query(Joker).filter(Joker.file_num == TOTAL_FILE).filter(Joker.joker_name == name)
        if(db.session.query(q.exists()).scalar()):
            for x in q:
                x.joker_count += file_data["joker_usage"][joker]["count"]
                x.joker_wins +=  file_data["joker_usage"][joker]["wins"]
                x.joker_losses += file_data["joker_usage"][joker]["losses"]
        
        else:
            new_joker = Joker(
                file_num = TOTAL_FILE,
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
            if name == "the_heirophant":
                name = "the_hierophant"
            c_type = "tarot"

        new_consumable = Consumable(
            file_num = file_number,
            consumable_name = name,
            consumable_count = file_data["consumeable_usage"][consumable]["count"],
            consumable_type = c_type
        )
        db.session.add(new_consumable)

        q = db.session.query(Consumable).filter(Consumable.file_num == TOTAL_FILE).filter(Consumable.consumable_name == name)
        if(db.session.query(q.exists()).scalar()):
            for x in q:
                x.consumable_count += file_data["consumeable_usage"][consumable]["count"]
        
        else:
            new_consumable = Consumable(
                file_num = TOTAL_FILE,
                consumable_name = name,
                consumable_count = file_data["consumeable_usage"][consumable]["count"],
                consumable_type = c_type
            )
            db.session.add(new_consumable)

    for voucher in file_data["voucher_usage"]:
        name = voucher
        if name == "magitrick":
            name = "magic_trick"

        elif name == "overstock_norm":
            name = "overstock"
        
        elif name == "directors_cut":
            name = "director's_cut"

        new_voucher = Voucher(
            file_num = file_number,
            voucher_name = name,
            voucher_count = file_data["voucher_usage"][voucher]["count"]
        )
        db.session.add(new_voucher)

        q = db.session.query(Voucher).filter(Voucher.file_num == TOTAL_FILE).filter(Voucher.voucher_name == name)
        if(db.session.query(q.exists()).scalar()):
            for x in q:
                x.voucher_count += file_data["voucher_usage"][voucher]["count"]
        
        else:
            new_voucher = Voucher(
                file_num = TOTAL_FILE,
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

        q = db.session.query(Hands).filter(Hands.file_num == TOTAL_FILE).filter(Hands.hand_name == hands)
        if(db.session.query(q.exists()).scalar()):
            for x in q:
                x.hand_count += file_data["hand_usage"][hands]["count"]
        
        else:
            new_hands = Hands(
                file_num = TOTAL_FILE,
                hand_name = hands,
                hand_count = file_data["hand_usage"][hands]["count"]
            )
            db.session.add(new_hands)

    for deck in file_data["deck_usage"]:
        new_deck = Deck(
            file_num = file_number,
            deck_name = deck,
            deck_wins = file_data["deck_usage"][deck]["wins"],
            deck_losses = file_data["deck_usage"][deck]["losses"])
        db.session.add(new_deck)

        q = db.session.query(Deck).filter(Deck.file_num == TOTAL_FILE).filter(Deck.deck_name == deck)
        if(db.session.query(q.exists()).scalar()):
            for x in q:
                x.deck_wins += file_data["deck_usage"][deck]["wins"]
                x.deck_losses += file_data["deck_usage"][deck]["losses"]
        
        else:
            new_deck = Deck(
                file_num = TOTAL_FILE,
                deck_name = deck,
                deck_wins = file_data["deck_usage"][deck]["wins"],
                deck_losses = file_data["deck_usage"][deck]["losses"])
            db.session.add(new_deck)
        
    db.session.commit()
    return jsonify({"message": "File uploaded successfully"}), 200

@app.route("/get_<string:item_type>/<int:file_number>", methods=["GET"])
#Retrieves all stats from a given item type and file number
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

#Removes the data of the given file number from the total before deleting the entries related to that number
def remove_file(file_number):
    TOTAL_FILE = 4
    for x in db.session.query(Career).filter(Career.file_num == file_number):
        q = db.session.query(Career).filter(Career.file_num == TOTAL_FILE)
        if(db.session.query(q.exists()).scalar()):
            for y in q:
                y.cards_discarded -= x.cards_discarded
                y.hands_played -= x.hands_played
                y.dollars_earned -= x.dollars_earned
                y.cards_played -= x.cards_played
                y.planetarium_used -= x.planetarium_used
                y.wins -= x.wins
                y.shop_rerolls -= x.shop_rerolls
                y.losses -= x.losses
                y.tarots_bought -= x.tarots_bought
                y.shop_dollars_spent -= x.shop_dollars_spent
                y.planets_bought -= x.planets_bought
                y.vouchers_bought -= x.vouchers_bought
                y.tarot_reading_used -= x.tarot_reading_used
                y.rounds -= x.rounds
                y.jokers_sold -= x.jokers_sold
                y.face_cards_played -= x.face_cards_played
                y.playing_cards_bought -= x.playing_cards_bought
        db.session.delete(x)
    
    for x in db.session.query(Joker).filter(Joker.file_num == file_number):
        q = db.session.query(Joker).filter(Joker.file_num == TOTAL_FILE).filter(Joker.joker_name == x.joker_name)
        if(db.session.query(q.exists()).scalar()):
            for y in q:
                y.joker_count -= x.joker_count
                y.joker_wins -=  x.joker_wins
                y.joker_losses -= x.joker_losses
        db.session.delete(x)

    for x in db.session.query(Consumable).filter(Consumable.file_num == file_number):
        q = db.session.query(Consumable).filter(Consumable.file_num == TOTAL_FILE).filter(Consumable.consumable_name == x.consumable_name)
        if(db.session.query(q.exists()).scalar()):
            for y in q:
                y.consumable_count -= x.consumable_count
        db.session.delete(x)

    for x in db.session.query(Voucher).filter(Voucher.file_num == file_number):
        q = db.session.query(Voucher).filter(Voucher.file_num == TOTAL_FILE).filter(Voucher.voucher_name == x.voucher_name)
        if(db.session.query(q.exists()).scalar()):
            for y in q:
                y.voucher_count -= x.voucher_count
        db.session.delete(x)

    for x in db.session.query(Hands).filter(Hands.file_num == file_number):
        q = db.session.query(Hands).filter(Hands.file_num == TOTAL_FILE).filter(Hands.hand_name == x.hand_name)
        if(db.session.query(q.exists()).scalar()):
            for y in q:
                y.hand_count -= x.hand_count
        db.session.delete(x)

    for x in db.session.query(Deck).filter(Deck.file_num == file_number):
        q = db.session.query(Deck).filter(Deck.file_num == TOTAL_FILE).filter(Deck.deck_name == x.deck_name)
        if(db.session.query(q.exists()).scalar()):
            for y in q:
                y.deck_wins -= x.deck_wins
                y.deck_losses -= x.deck_losses
        db.session.delete(x)
    
    db.session.commit()
    return jsonify({"message": "File removed successfully"}), 200

@app.route("/toggle_file/<int:status>/<int:file_number>", methods=["PATCH"])
#adds or removes indicated save file from total to "toggle" its visibility
def toggleFile(status, file_number):
    TOTAL_FILE = 4
    for x in db.session.query(Career).filter(Career.file_num == file_number):
        q = db.session.query(Career).filter(Career.file_num == TOTAL_FILE)
        if(db.session.query(q.exists()).scalar()):
            for y in q:
                if(status):
                    y.cards_discarded += x.cards_discarded
                    y.hands_played += x.hands_played
                    y.dollars_earned += x.dollars_earned
                    y.cards_played += x.cards_played
                    y.planetarium_used += x.planetarium_used
                    y.wins += x.wins
                    y.shop_rerolls += x.shop_rerolls
                    y.losses += x.losses
                    y.tarots_bought += x.tarots_bought
                    y.shop_dollars_spent += x.shop_dollars_spent
                    y.planets_bought += x.planets_bought
                    y.vouchers_bought += x.vouchers_bought
                    y.tarot_reading_used += x.tarot_reading_used
                    y.rounds += x.rounds
                    y.jokers_sold += x.jokers_sold
                    y.face_cards_played += x.face_cards_played
                    y.playing_cards_bought += x.playing_cards_bought
                else:
                    y.cards_discarded -= x.cards_discarded
                    y.hands_played -= x.hands_played
                    y.dollars_earned -= x.dollars_earned
                    y.cards_played -= x.cards_played
                    y.planetarium_used -= x.planetarium_used
                    y.wins -= x.wins
                    y.shop_rerolls -= x.shop_rerolls
                    y.losses -= x.losses
                    y.tarots_bought -= x.tarots_bought
                    y.shop_dollars_spent -= x.shop_dollars_spent
                    y.planets_bought -= x.planets_bought
                    y.vouchers_bought -= x.vouchers_bought
                    y.tarot_reading_used -= x.tarot_reading_used
                    y.rounds -= x.rounds
                    y.jokers_sold -= x.jokers_sold
                    y.face_cards_played -= x.face_cards_played
                    y.playing_cards_bought -= x.playing_cards_bought
    
    for x in db.session.query(Joker).filter(Joker.file_num == file_number):
        q = db.session.query(Joker).filter(Joker.file_num == TOTAL_FILE).filter(Joker.joker_name == x.joker_name)
        if(db.session.query(q.exists()).scalar()):
            for y in q:
                if(status):
                    y.joker_count += x.joker_count
                    y.joker_wins +=  x.joker_wins
                    y.joker_losses += x.joker_losses
                else:
                    y.joker_count -= x.joker_count
                    y.joker_wins -=  x.joker_wins
                    y.joker_losses -= x.joker_losses
                
        

    for x in db.session.query(Consumable).filter(Consumable.file_num == file_number):
        q = db.session.query(Consumable).filter(Consumable.file_num == TOTAL_FILE).filter(Consumable.consumable_name == x.consumable_name)
        if(db.session.query(q.exists()).scalar()):
            for y in q:
                if(status):
                    y.consumable_count += x.consumable_count
                else:
                    y.consumable_count -= x.consumable_count

    for x in db.session.query(Voucher).filter(Voucher.file_num == file_number):
        q = db.session.query(Voucher).filter(Voucher.file_num == TOTAL_FILE).filter(Voucher.voucher_name == x.voucher_name)
        if(db.session.query(q.exists()).scalar()):
            for y in q:
                if(status):
                    y.voucher_count += x.voucher_count
                else:
                    y.voucher_count -= x.voucher_count

    for x in db.session.query(Hands).filter(Hands.file_num == file_number):
        q = db.session.query(Hands).filter(Hands.file_num == TOTAL_FILE).filter(Hands.hand_name == x.hand_name)
        if(db.session.query(q.exists()).scalar()):
            for y in q:
                if(status):
                    y.hand_count += x.hand_count
                else:
                    y.hand_count -= x.hand_count

    for x in db.session.query(Deck).filter(Deck.file_num == file_number):
        q = db.session.query(Deck).filter(Deck.file_num == TOTAL_FILE).filter(Deck.deck_name == x.deck_name)
        if(db.session.query(q.exists()).scalar()):
            for y in q:
                if(status):
                    y.deck_wins += x.deck_wins
                    y.deck_losses += x.deck_losses
                else:
                    y.deck_wins -= x.deck_wins
                    y.deck_losses -= x.deck_losses
    
    db.session.commit()

    return jsonify({"message": "File toggled successfully"}), 200

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run()