class Player: 

    def __init__(self, name: str, player_id: int, player_password):
        self.name = name
        self.player_id = player_id
        self.password = player_password
        self.score = 0

        def add_score (self, punkte: int):
            self.score = punkte

        def get_score (self):
            return self.score