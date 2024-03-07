from NPC import NPC

class EnemyNPC(NPC):
    def __init__(self, name, gender, weapon, role, hp, damage, aggression_level, required_damage):
        super().__init__(name, gender, weapon, role, hp, damage)
        self._aggression_level = aggression_level
        self.required_damage = required_damage

    def attack(self, player):
        damage = self._damage * (1 + self._aggression_level / 10)  # Agresi menambah kerusakan
        print(f"{self._name} menyerang {player.get_name()} dengan {damage} kerusakan.")
        player.set_hp(player.get_hp() - damage)
        if player.get_hp() <= 0:
            print(f"{player.get_name()} telah dikalahkan oleh {self._name}.")
