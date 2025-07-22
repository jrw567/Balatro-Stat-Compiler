from config import db

class SaveFile(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    file_num = db.Column(db.Integer, unique=False, nullable=False)
    file_name = db.Column(db.String(50), unique=False, nullable=False)
    
    # 18 stats
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
    cards_sold = db.Column(db.Integer, unique=False, nullable=False)

    joker_count = db.Column(db.Integer, unique=False, nullable=False)
    joker_wins = db.Column(db.Integer, unique=False, nullable=False)
    joker_losses = db.Column(db.Integer, unique=False, nullable=False)

    greedy_joker_count = db.Column(db.Integer, unique=False, nullable=False)
    greedy_joker_wins = db.Column(db.Integer, unique=False, nullable=False)
    greedy_joker_losses = db.Column(db.Integer, unique=False, nullable=False)

    lusty_joker_count = db.Column(db.Integer, unique=False, nullable=False)
    lusty_joker_wins = db.Column(db.Integer, unique=False, nullable=False)
    lusty_joker_losses = db.Column(db.Integer, unique=False, nullable=False)

    wrathful_joker_count = db.Column(db.Integer, unique=False, nullable=False)
    wrathful_joker_wins = db.Column(db.Integer, unique=False, nullable=False)
    wrathful_joker_losses = db.Column(db.Integer, unique=False, nullable=False)

    gluttenous_joker_count = db.Column(db.Integer, unique=False, nullable=False)
    gluttenous_joker_wins = db.Column(db.Integer, unique=False, nullable=False)
    gluttenous_joker_losses = db.Column(db.Integer, unique=False, nullable=False)

    jolly_joker_count = db.Column(db.Integer, unique=False, nullable=False)
    jolly_joker_wins = db.Column(db.Integer, unique=False, nullable=False)
    jolly_joker_losses = db.Column(db.Integer, unique=False, nullable=False)

    zany_joker_count = db.Column(db.Integer, unique=False, nullable=False)
    zany_joker_wins = db.Column(db.Integer, unique=False, nullable=False)
    zany_joker_losses = db.Column(db.Integer, unique=False, nullable=False)

    mad_joker_count = db.Column(db.Integer, unique=False, nullable=False)
    mad_joker_wins = db.Column(db.Integer, unique=False, nullable=False)
    mad_joker_losses = db.Column(db.Integer, unique=False, nullable=False)

    crazy_joker_count = db.Column(db.Integer, unique=False, nullable=False)
    crazy_joker_wins = db.Column(db.Integer, unique=False, nullable=False)
    crazy_joker_losses = db.Column(db.Integer, unique=False, nullable=False)

    droll_joker_count = db.Column(db.Integer, unique=False, nullable=False)
    droll_joker_wins = db.Column(db.Integer, unique=False, nullable=False)
    droll_joker_losses = db.Column(db.Integer, unique=False, nullable=False)

    sly_joker_count = db.Column(db.Integer, unique=False, nullable=False)
    sly_joker_wins = db.Column(db.Integer, unique=False, nullable=False)
    sly_joker_losses = db.Column(db.Integer, unique=False, nullable=False)

    wily_joker_count = db.Column(db.Integer, unique=False, nullable=False)
    wily_joker_wins = db.Column(db.Integer, unique=False, nullable=False)
    wily_joker_losses = db.Column(db.Integer, unique=False, nullable=False)

    clever_joker_count = db.Column(db.Integer, unique=False, nullable=False)
    clever_joker_wins = db.Column(db.Integer, unique=False, nullable=False)
    clever_joker_losses = db.Column(db.Integer, unique=False, nullable=False)

    devious_joker_count = db.Column(db.Integer, unique=False, nullable=False)
    devious_joker_wins = db.Column(db.Integer, unique=False, nullable=False)
    devious_joker_losses = db.Column(db.Integer, unique=False, nullable=False)

    crafty_joker_count = db.Column(db.Integer, unique=False, nullable=False)
    crafty_joker_wins = db.Column(db.Integer, unique=False, nullable=False)
    crafty_joker_losses = db.Column(db.Integer, unique=False, nullable=False)

    half_joker_count = db.Column(db.Integer, unique=False, nullable=False)
    half_joker_wins = db.Column(db.Integer, unique=False, nullable=False)
    half_joker_losses = db.Column(db.Integer, unique=False, nullable=False)

    stencil_joker_count = db.Column(db.Integer, unique=False, nullable=False)
    stencil_joker_wins = db.Column(db.Integer, unique=False, nullable=False)
    stencil_joker_losses = db.Column(db.Integer, unique=False, nullable=False)

    four_fingers_count = db.Column(db.Integer, unique=False, nullable=False)
    four_fingers_wins = db.Column(db.Integer, unique=False, nullable=False)
    four_fingers_losses = db.Column(db.Integer, unique=False, nullable=False)

    mime_count = db.Column(db.Integer, unique=False, nullable=False)
    mime_wins = db.Column(db.Integer, unique=False, nullable=False)
    mime_losses = db.Column(db.Integer, unique=False, nullable=False)

    credit_card_count = db.Column(db.Integer, unique=False, nullable=False)
    credit_card_wins = db.Column(db.Integer, unique=False, nullable=False)
    credit_card_losses = db.Column(db.Integer, unique=False, nullable=False)

    ceremonial_count = db.Column(db.Integer, unique=False, nullable=False)
    ceremonial_wins = db.Column(db.Integer, unique=False, nullable=False)
    ceremonial_losses = db.Column(db.Integer, unique=False, nullable=False)

    banner_count = db.Column(db.Integer, unique=False, nullable=False)
    banner_wins = db.Column(db.Integer, unique=False, nullable=False)
    banner_losses = db.Column(db.Integer, unique=False, nullable=False)

    mystic_summit_count = db.Column(db.Integer, unique=False, nullable=False)
    mystic_summit_wins = db.Column(db.Integer, unique=False, nullable=False)
    mystic_summit_losses = db.Column(db.Integer, unique=False, nullable=False)

    marble_count = db.Column(db.Integer, unique=False, nullable=False)
    marble_wins = db.Column(db.Integer, unique=False, nullable=False)
    marble_losses = db.Column(db.Integer, unique=False, nullable=False)

    loyalty_card_count = db.Column(db.Integer, unique=False, nullable=False)
    loyalty_card_wins = db.Column(db.Integer, unique=False, nullable=False)
    loyalty_card_losses = db.Column(db.Integer, unique=False, nullable=False)

    eight_ball_count = db.Column(db.Integer, unique=False, nullable=False)
    eight_ball_wins = db.Column(db.Integer, unique=False, nullable=False)
    eight_ball_losses = db.Column(db.Integer, unique=False, nullable=False)

    misprint_count = db.Column(db.Integer, unique=False, nullable=False)
    misprint_wins = db.Column(db.Integer, unique=False, nullable=False)
    misprint_losses = db.Column(db.Integer, unique=False, nullable=False)

    dusk_count = db.Column(db.Integer, unique=False, nullable=False)
    dusk_wins = db.Column(db.Integer, unique=False, nullable=False)
    dusk_losses = db.Column(db.Integer, unique=False, nullable=False)

    raised_fist_count = db.Column(db.Integer, unique=False, nullable=False)
    raised_fist_wins = db.Column(db.Integer, unique=False, nullable=False)
    raised_fist_losses = db.Column(db.Integer, unique=False, nullable=False)

    chaos_count = db.Column(db.Integer, unique=False, nullable=False)
    chaos_wins = db.Column(db.Integer, unique=False, nullable=False)
    chaos_losses = db.Column(db.Integer, unique=False, nullable=False)

    fibonacci_count = db.Column(db.Integer, unique=False, nullable=False)
    fibonacci_wins = db.Column(db.Integer, unique=False, nullable=False)
    fibonacci_losses = db.Column(db.Integer, unique=False, nullable=False)

    steel_joker_count = db.Column(db.Integer, unique=False, nullable=False)
    steel_joker_wins = db.Column(db.Integer, unique=False, nullable=False)
    steel_joker_losses = db.Column(db.Integer, unique=False, nullable=False)

    scary_face_count = db.Column(db.Integer, unique=False, nullable=False)
    scary_face_wins = db.Column(db.Integer, unique=False, nullable=False)
    scary_face_losses = db.Column(db.Integer, unique=False, nullable=False)

    abstract_count = db.Column(db.Integer, unique=False, nullable=False)
    abstract_wins = db.Column(db.Integer, unique=False, nullable=False)
    abstract_losses = db.Column(db.Integer, unique=False, nullable=False)

    delayed_grat_count = db.Column(db.Integer, unique=False, nullable=False)
    delayed_grat_wins = db.Column(db.Integer, unique=False, nullable=False)
    delayed_grat_losses = db.Column(db.Integer, unique=False, nullable=False)

    hack_count = db.Column(db.Integer, unique=False, nullable=False)
    hack_wins = db.Column(db.Integer, unique=False, nullable=False)
    hack_losses = db.Column(db.Integer, unique=False, nullable=False)

    pareidolia_count = db.Column(db.Integer, unique=False, nullable=False)
    pareidolia_wins = db.Column(db.Integer, unique=False, nullable=False)
    pareidolia_losses = db.Column(db.Integer, unique=False, nullable=False)

    gros_michel_count = db.Column(db.Integer, unique=False, nullable=False)
    gros_michel_wins = db.Column(db.Integer, unique=False, nullable=False)
    gros_michel_losses = db.Column(db.Integer, unique=False, nullable=False)

    even_steven_count = db.Column(db.Integer, unique=False, nullable=False)
    even_steven_wins = db.Column(db.Integer, unique=False, nullable=False)
    even_steven_losses = db.Column(db.Integer, unique=False, nullable=False)

    odd_todd_count = db.Column(db.Integer, unique=False, nullable=False)
    odd_todd_wins = db.Column(db.Integer, unique=False, nullable=False)
    odd_todd_losses = db.Column(db.Integer, unique=False, nullable=False)

    scholar_count = db.Column(db.Integer, unique=False, nullable=False)
    scholar_wins = db.Column(db.Integer, unique=False, nullable=False)
    scholar_losses = db.Column(db.Integer, unique=False, nullable=False)

    business_count = db.Column(db.Integer, unique=False, nullable=False)
    business_wins = db.Column(db.Integer, unique=False, nullable=False)
    business_losses = db.Column(db.Integer, unique=False, nullable=False)

    supernova_count = db.Column(db.Integer, unique=False, nullable=False)
    supernova_wins = db.Column(db.Integer, unique=False, nullable=False)
    supernova_losses = db.Column(db.Integer, unique=False, nullable=False)

    ride_the_bus_count = db.Column(db.Integer, unique=False, nullable=False)
    ride_the_bus_wins = db.Column(db.Integer, unique=False, nullable=False)
    ride_the_bus_losses = db.Column(db.Integer, unique=False, nullable=False)

    space_count = db.Column(db.Integer, unique=False, nullable=False)
    space_wins = db.Column(db.Integer, unique=False, nullable=False)
    space_losses = db.Column(db.Integer, unique=False, nullable=False)

    egg_count = db.Column(db.Integer, unique=False, nullable=False)
    egg_wins = db.Column(db.Integer, unique=False, nullable=False)
    egg_losses = db.Column(db.Integer, unique=False, nullable=False)

    burglar_count = db.Column(db.Integer, unique=False, nullable=False)
    burglar_wins = db.Column(db.Integer, unique=False, nullable=False)
    burglar_losses = db.Column(db.Integer, unique=False, nullable=False)

    blackboard_count = db.Column(db.Integer, unique=False, nullable=False)
    blackboard_wins = db.Column(db.Integer, unique=False, nullable=False)
    blackboard_losses = db.Column(db.Integer, unique=False, nullable=False)

    runner_count = db.Column(db.Integer, unique=False, nullable=False)
    runner_wins = db.Column(db.Integer, unique=False, nullable=False)
    runner_losses = db.Column(db.Integer, unique=False, nullable=False)

    ice_cream_count = db.Column(db.Integer, unique=False, nullable=False)
    ice_cream_wins = db.Column(db.Integer, unique=False, nullable=False)
    ice_cream_losses = db.Column(db.Integer, unique=False, nullable=False) # 'ORDER':50,

    _count = db.Column(db.Integer, unique=False, nullable=False)
    _wins = db.Column(db.Integer, unique=False, nullable=False)
    _losses = db.Column(db.Integer, unique=False, nullable=False)

    def to_json(self):
        return {}