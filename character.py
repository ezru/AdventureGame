class Character():

    # Create a character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

    # Describe this character
    def describe(self):
        print(self.name + " is here!")
        print(self.description)

    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        self.conversation = conversation

    # Talk to this character
    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    # Fight with this character
    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you")
        return True


class Enemy(Character):

    enemies_count = 0

    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self._weakness = None
        self.sleep_spell = None
        Enemy.enemies_count += 1

    @property
    def weakness(self):
        return self._weakness

    @weakness.setter
    def weakness(self, enemy_weakness):
        self._weakness = enemy_weakness

    def set_sleep_spell(self, sleep_spell):
        self.sleep_spell = sleep_spell

    def get_sleep_spell(self):
        return self.sleep_spell

    def fight(self, combat_item):
        if combat_item == self.weakness:
            Enemy.enemies_count -= 1
            print("You fend off", self.name, "with", self.weakness)
            print("There are", Enemy.enemies_count, "enemies left.")
            return True
        else:
            print(self.name, 'Crushed your weak ass!')
            return False

    def send_to_sleep(self, spell):
        if spell == self.sleep_spell:
            print(self.name, "Has gone to sleep!")
            return True
        else:
            print("Your spell has no effect on", self.name)
            return False


class Friend(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.feeling = 20

    def hug(self):
        print(self.name, " hugs you back!")
        self.feeling = self.feeling + 2
        print(self.name, "has a feeling level of:", self.feeling)
