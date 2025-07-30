from config import db

class Career(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    file_num = db.Column(db.Integer, unique=False, nullable=False)
    file_name = db.Column(db.String(50), unique=False, nullable=False)
    
    cards_discarded = db.Column(db.Integer, unique=False, nullable=False)
    hands_played = db.Column(db.Integer, unique=False, nullable=False)
    dollars_earned = db.Column(db.Integer, unique=False, nullable=False)
    cards_played = db.Column(db.Integer, unique=False, nullable=False)
    planetarium_used = db.Column(db.Integer, unique=False, nullable=False)
    wins = db.Column(db.Integer, unique=False, nullable=False)
    shop_rerolls = db.Column(db.Integer, unique=False, nullable=False)
    losses = db.Column(db.Integer, unique=False, nullable=False)
    tarots_bought = db.Column(db.Integer, unique=False, nullable=False)
    shop_dollars_spent = db.Column(db.Integer, unique=False, nullable=False)
    planets_bought = db.Column(db.Integer, unique=False, nullable=False)
    vouchers_bought = db.Column(db.Integer, unique=False, nullable=False)
    tarot_reading_used = db.Column(db.Integer, unique=False, nullable=False)
    rounds = db.Column(db.Integer, unique=False, nullable=False)
    jokers_sold = db.Column(db.Integer, unique=False, nullable=False)
    face_cards_played = db.Column(db.Integer, unique=False, nullable=False)
    playing_cards_bought = db.Column(db.Integer, unique=False, nullable=False)

    
    def to_json(self):
        return {
            # "career_stats" : {
                "file_name": self.file_name,
                "cards_discarded": self.cards_discarded,
                "hands_played": self.hands_played,
                "dollars_earned": self.dollars_earned,
                "cards_played": self.cards_played,
                "planetarium_used": self.planetarium_used,
                "wins": self.wins,
                "shop_rerolls": self.shop_rerolls,
                "losses": self.losses,
                "tarots_bought": self.tarots_bought,
                "shop_dollars_spent": self.shop_dollars_spent,
                "planets_bought": self.planets_bought,
                "vouchers_bought": self.vouchers_bought,
                "tarot_reading_used": self.tarot_reading_used,
                "rounds": self.rounds,
                "jokers_sold": self.jokers_sold,
                "face_cards_played": self.face_cards_played,
                "playing_cards_bought": self.playing_cards_bought,
            # }
        }

class Joker(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    file_num = db.Column(db.Integer, unique=False, nullable=False)

    joker_name = db.Column(db.String(30), unique=False, nullable=False)
    joker_count = db.Column(db.Integer, unique=False, nullable=False)
    joker_wins = db.Column(db.Integer, unique=False, nullable=False)
    joker_losses = db.Column(db.Integer, unique=False, nullable=False)

    def to_json(self):
        return {
            self.joker_name : {"rounds": self.joker_count, "wins": self.joker_wins, "losses": self.joker_losses}
        }
    
class Consumable(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    file_num = db.Column(db.Integer, unique=False, nullable=False)

    consumable_name = db.Column(db.String(30), unique=False, nullable=False)
    consumable_count = db.Column(db.Integer, unique=False, nullable=False)
    consumable_type = db.Column(db.String(30), unique=False, nullable=False)

    def to_json(self):
        return {
            self.consumable_name: {"count": self.consumable_count}
        }
    
class Voucher(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    file_num = db.Column(db.Integer, unique=False, nullable=False)

    voucher_name = db.Column(db.String(30), unique=False, nullable=False)
    voucher_count = db.Column(db.Integer, unique=False, nullable=False)

    def to_json(self):
        return {
            self.voucher_name: {"count": self.voucher_count}
        }
    
class Hands(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    file_num = db.Column(db.Integer, unique=False, nullable=False)

    hand_name = db.Column(db.String(30), unique=False, nullable=False)
    hand_count = db.Column(db.Integer, unique=False, nullable=False)

    def to_json(self):
        return {
            self.hand_name: {"count": self.hand_count}
        }
    
class Deck(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    file_num = db.Column(db.Integer, unique=False, nullable=False)

    deck_name = db.Column(db.String(30), unique=False, nullable=False)
    deck_wins = db.Column(db.Integer, unique=False, nullable=False)
    deck_losses = db.Column(db.Integer, unique=False, nullable=False)

    def to_json(self):
        return {
            self.deck_name: {"wins": self.deck_wins, "losses": self.deck_losses}
        }

