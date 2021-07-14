from project.player.player import Player


class PlayerRepository:
    def __init__(self):
        self.count: int = 0
        self.players: list = []

    def add(self, player: Player):
        for p in self.players:
            if p.username == player.username:
                raise ValueError(f"Player {player.username} already exists!")
        self.players.append(player)
        self.count += 1

    def remove(self, player: str):
        if player == '':
            raise ValueError("Player cannot be an empty string!")

        p_to_remove = self.find(player)
        self.players.remove(p_to_remove)
        self.count -= 1

    def find(self, username: str):
        for p in self.players:
            if p.username == username:
                return p
