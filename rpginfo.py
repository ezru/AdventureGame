class RPGinfo():
    author = "Anonymous"

    def __init__(self, game_name):
        self.game_name = game_name

    def welcome(self):
        print("Welcome to", self.game_name)

    @staticmethod
    def info():
        print("Made using the OOP RPG game creator \N{COPYRIGHT SIGN} me")

    @classmethod
    def credits(cls):
        print("Thank you for playing.")
        print("This game was created by", cls.author)
