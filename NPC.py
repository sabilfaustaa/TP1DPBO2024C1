from Character import Character

class NPC(Character):
    def __init__(self, name, gender, weapon, role, hp, damage):
        super().__init__(name, gender, weapon, role, hp, damage)

    def interact(self):
        print(f"{self._name} berinteraksi.")