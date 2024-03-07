from Player import Player
from FriendlyNPC import FriendlyNPC
from EnemyNPC import EnemyNPC
from Quest import Quest
from Item import Item

class Main:
    def __init__(self):
        self.setup_world()
        self.setup_characters()
        self.choose_character()

    def setup_characters(self):
        self.available_characters = {
            "Warrior": {"name": "Warrior", "gender": "M", "weapon": "Sword", "role": "Warrior", "hp": 120, "damage": 50},
            "Archer": {"name": "Archer", "gender": "F", "weapon": "Bow", "role": "Archer", "hp": 100, "damage": 150},
            "Mage": {"name": "Mage", "gender": "M", "weapon": "Staff", "role": "Mage", "hp": 80, "damage": 35}
        }

    def choose_character(self):
        print("Pilih karakter Anda:")
        for role, details in self.available_characters.items():
            print(f"{role}: HP {details['hp']}, ATK {details['damage']}")

        choice = input("Masukkan role karakter yang Anda pilih: ")
        if choice in self.available_characters:
            selected = self.available_characters[choice]
            self.player = Player(selected['name'], selected['gender'], selected['weapon'], selected['role'], selected['hp'], selected['damage'])
            print(f"Anda telah memilih {selected['role']} dengan ATK {selected['damage']} dan HP {selected['hp']}.")
        else:
            print("Pilihan tidak valid. Memilih karakter default.")
            default = self.available_characters["Warrior"]
            self.player = Player(default['name'], default['gender'], default['weapon'], default['role'], default['hp'], default['damage'])

    def setup_world(self):
        # instansiasi item
        item1 = Item("Obat Misterius", "Quest", 0)
        item2 = Item("Pesan Rahasia", "Quest", 0)
        item3 = Item("Pedang Kuno", "Weapon", 25)
        item4 = Item("Baju Besi", "Armor", 15)

        # instansiasi quest
        quest1 = Quest("Cari Obat", "Temukan dan bawakan obat.", {"xp": 50, "items": [item3]})
        quest2 = Quest("Pesan Rahasia", "Sampaikan pesan rahasia kepada Ally.", {"xp": 100})
        quest3 = Quest("Kalahkan Goblin", "Kalahkan Goblin yang mengganggu desa.", {"xp": 75, "items": [item4]})
        quest4 = Quest("Penyelamatan", "Selamdamagean penduduk desa yang ditawan.", {"xp": 150, "items": [item3, item4]})

        # instansiasi friendly npc
        self.npc_baik = {
            "John": FriendlyNPC("John", "M", None, "Trader", 100, 0, quests = [quest1], items_for_trade = [item1]),
            "Ally": FriendlyNPC("Ally", "F", None, "Messenger", 100, 0, quests = [quest2], items_for_trade = [item2]),
            "Marcus": FriendlyNPC("Marcus", "M", None, "Warrior", 100, 0, quests = [quest3], items_for_trade = [item3]),
            "Elaine": FriendlyNPC("Elaine", "F", None, "Healer", 100, 0, quests = [quest4], items_for_trade = [item4]),
        }

        # instansiasi
        self.npc_jahat = {
            "Goblin": EnemyNPC("Goblin", "M", "Club", "Enemy", 50, 10, aggression_level = 5, required_damage = 15),
            "Orc": EnemyNPC("Orc", "M", "Axe", "Enemy", 75, 15, aggression_level = 7, required_damage = 50),
            "Dragon": EnemyNPC("Dragon", "M", "Fire Breath", "Boss", 200, 50, aggression_level = 10, required_damage = 75),
            "Skeleton": EnemyNPC("Skeleton", "M", "Dagger", "Enemy", 40, 20, aggression_level = 4, required_damage = 10),
        }

    def eksplorasi(self):
        print("Anda menemukan sebuah kotak di tanah dan memutuskan untuk membukanya...")
        obat_misterius = Item("Obat Misterius", "Quest", 0)
        self.player.add_item_to_inventory(obat_misterius)

    def run_game(self):
        print("Selamat datang di Game!")
        while True:
            print("\nApa yang ingin Anda lakukan?")
            print("1. Bicara dengan NPC")
            print("2. Cari musuh")
            print("3. Lihat status")
            print("4. Lihat tas")
            print("5. Eksplorasi")
            print("6. Keluar")
            choice = input("Pilih aksi: ")

            if choice == "1":
                print("=============== Search NPC ==============")
                self.interact_with_npc()
                print("=========================================")
            elif choice == "2":
                print("================ Fighting ===============")
                self.fight_enemy()
                print("=========================================")
            elif choice == "3":
                print("============= Status Pemain =============")
                self.player.show_status()
                print("=========================================")
            elif choice == "4":
                print("=============== Lihat Tas ===============")
                self.player.show_inventory()
                print("=========================================")
            elif choice == "5":
                print("=============== Treasure ================")
                self.eksplorasi()
                print("=========================================")
            elif choice == "6":
                print("Terima kasih telah bermain!")
                break
            else:
                print("Pilihan tidak valid, coba lagi.")

    def interact_with_npc(self):
        print("NPC yang tersedia untuk ditemui:")
        for npc_name in self.npc_baik.keys():
            print(npc_name)
        chosen_npc = input("Pilih NPC yang ingin kamu temui: ")
        if chosen_npc in self.npc_baik:
            self.npc_baik[chosen_npc].give_quest(self.player)
        else:
            print(f"NPC dengan nama {chosen_npc} tidak ditemukan.")


    def fight_enemy(self):
        print("Musuh yang tersedia untuk dihadapi:")
        for npc_name in self.npc_jahat.keys():
            print(npc_name)
        enemy = input("Pilih musuh yang ingin kamu hadapi: ")
        if enemy in self.npc_jahat:
            enemy_npc = self.npc_jahat[enemy]
            if self.player.get_damage() < enemy_npc.required_damage:
                print(f"Kekuatanmu terlalu rendah untuk melawan {enemy}. Diperlukan damage minimal: {enemy_npc.required_damage}")
            else:
                print(f"Menemukan {enemy_npc._name}!")
                while enemy_npc._hp > 0 and self.player._hp > 0:
                    self.player.attack(enemy_npc)
                    if enemy_npc._hp <= 0:
                        print(f"{enemy_npc._name} telah dikalahkan!")
                        break
                    enemy_npc.attack(self.player)
                    if self.player._hp <= 0:
                        print("Anda telah dikalahkan. Game over.")
                        break
        else:
            print(f"Musuh dengan nama {enemy} tidak ditemukan.")


# Membuat instance game dan menjalankannya
if __name__ == "__main__":
    game = Main()
    game.run_game()
