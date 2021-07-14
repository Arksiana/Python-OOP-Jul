from project.player.player import Player


class Beginner(Player):
    def __init__(self, username):
        super(Beginner, self).__init__(username, 50)
