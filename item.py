class Item():
    def __init__(self, itemName):
        self.name = itemName
        self.description = None
        self.skill_level = None

    def set_name(self, item_name):
        self.name = item_name

    def get_name(self):
        return self.name

    def set_description(self, description):
        self.description = description

    def get_description(self):
        return self.description

    def set_skill_level(self, skill):
        self.skill_level = skill

    def get_skill_level(self):
        return self.skill_level

    def item_details(self):
        print(self.name + ":", self.description)
