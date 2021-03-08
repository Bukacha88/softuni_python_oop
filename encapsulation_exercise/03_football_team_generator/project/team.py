class Team:
    def __init__(self, name, rating):
        self.rating = rating
        self.name = name
        self.players = []

    @staticmethod
    def find_player(player_name, players):
        return [player for player in players if player.name == player_name]

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, value):
        self.__rating = value

    @property
    def players(self):
        return self.__players

    @players.setter
    def players(self, value):
        self.__players = value

    def add_player(self, player):
        if player in self.__players:
            return f"Player {player.name} has already joined"
        self.__players.append(player)
        return f"Player {player.name} joined team {self.__name}"

    def remove_player(self, player_name):
        if not self.find_player(player_name, self.__players):
            return f"Player {player_name} not found"
        player = self.find_player(player_name, self.__players)[0]
        self.__players.remove(player)
        return player


