
from exam_prep.python_oop_exam_16_aug_2020.project import Player


class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if player in self.players:
            return f"Player {player.name} is already in the guild."
        if not player.guild == "Unaffiliated":
            return f"Player {player.name} is in another guild."

        self.players.append(player)
        player.guild = self.name
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str):
        if player_name not in [player.name for player in self.players]:
            return f"Player {player_name} is not in the guild."

        player = [player for player in self.players if player.name == player_name][0]
        self.players.remove(player)
        return f"Player {player.name} has been removed from the guild."

    def guild_info(self):
        players_details = "".join([player.player_info() for player in self.players])
        return f"Guild: {self.name}\n" \
               f"{players_details}"

