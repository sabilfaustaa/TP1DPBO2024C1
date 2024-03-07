from NPC import NPC

class FriendlyNPC(NPC):
    def __init__(self, name, gender, weapon, role, hp, damage, quests=[], items_for_trade=[]):
        super().__init__(name, gender, weapon, role, hp, damage)
        self.quests = quests
        self.items_for_trade = items_for_trade

    def give_quest(self, player):
        required_item = "Obat Misterius"
        if any(item.get_name() == required_item for item in player.inventory):
            if self.quests:
                quest = self.quests.pop(0)
                print(f"{self._name} memberikan quest: {quest.title}")
                player.accept_quest(quest)
            else:
                print(f"{self._name} tidak memiliki quest untuk diberikan saat ini.")
        else:
            print(f"{self._name} mengatakan bahwa kamu perlu membawa '{required_item}' untuk menerima quest.")

    def trade(self, player, item_name):
        # Mencari item dalam daftar item yang dapat diperdagangkan
        item = next((item for item in self.items_for_trade if item.get_name() == item_name), None)
        if item:
            # Misal, kita hanya print interaksi. Logika untuk transfer item bisa ditambahkan
            print(f"{self._name} berdagang {item.get_name()} dengan {player.get_name()}.")
            player.add_item_to_inventory(item)
            self.items_for_trade.remove(item)
        else:
            print(f"{self._name} tidak memiliki item '{item_name}' untuk diperdagangkan.")
