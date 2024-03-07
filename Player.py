from Character import Character

class Player(Character):
    def __init__(self, name, gender, weapon, role, hp, damage, experience=0):
        super().__init__(name, gender, weapon, role, hp, damage)
        self.__experience = experience
        self.quests = []

    def do_quest(self, quest):
        print(f"{self._name} melakukan quest: {quest.get_title()}")
        self.__experience += quest.get_reward()
        print(f"Pengalaman bertambah, total sekarang: {self.__experience}")

    def accept_quest(self, quest):
        self.quests.append(quest)
        print(f"{self._name} menerima quest: {quest.title}")
  
    def show_quests(self):
        if not self.quests:
            print(f"{self._name} tidak memiliki quest.")
        else:
            print(f"{self._name} memiliki quest berikut:")
            for quest in self.quests:
                quest.display_quest()

    def upgrade(self, stat, amount):
        if stat == "hp":
            self._hp += amount
        elif stat == "damage":
            self._damage += amount
        else:
            print("Stat tidak dikenali")
        print(f"{stat} ditingkdamagean sebesar {amount}")

    def attack(self, target):
        if self._weapon == "Sword":
            damage = self._damage * 1.5
        elif self._weapon == "Bow":
            damage = self._damage * 1.2
        else:
            damage = self._damage
        print(f"{self._name} menyerang {target.get_name()} dengan {damage} kerusakan.")
        target.set_hp(target.get_hp() - damage)
  
    def get_experience(self):
        return self.__experience
  
    def set_experience(self, experience):
        self.__experience = experience
  
    def show_status(self):
        super().show_status()
        print(f"Pengalaman: {self.__experience}")
