class Character:
    def __init__(self, name, gender, weapon, role, hp, damage):
        self._name = name
        self._gender = gender
        self._weapon = weapon
        self._role = role
        self._hp = hp
        self._damage = damage
        self.inventory = []

    def attack(self, target):
        if self._damage > target._hp: # jika damage yang diberikan lebih dari sisa hp sudah berhasil mengalahkan musuh
            print(f"{self._name} berhasil mengalahkan {target._name}!")
            target._hp = 0
        else: # jika belum print history attack nya
            print(f"{self._name} menyerang {target._name} dengan {self._damage} damage.")
            target._hp -= self._damage

    def use_item(self, item):
        # ceritanya bisa pakai item untuk menambah status damage
        if item in self.inventory:
            self._damage += item.get_value()
            self.inventory.remove(item)
            print(f"{self._name} menggunakan {item.get_name()} untuk meningkatkan damage.")
        else:
            print(f"{item.get_name()} tidak ditemukan di inventaris.")

    def add_item_to_inventory(self, item):
        # tambah item ke tas
        self.inventory.append(item)
        print(f"{item.get_name()} ditambahkan ke tas.")

    def show_inventory(self):
        # Menampilkan isi inventaris
        if self.inventory:
            print(f"Isi Tas {self._name}:")
            for item in self.inventory:
                print(f"- {item.get_name()}")
        else:
            print("Tas kosong.")

    def show_status(self):
        print(f"Nama: {self._name}\nPeran: {self._role}\nHP: {self._hp}\ndamage: {self._damage}")

    def get_name(self):
        return self._name

    def get_role(self):
        return self._role

    def set_name(self, name):
        self._name = name

    def set_role(self, role):
        self._role = role

    def get_hp(self):
        return self._hp

    def set_hp(self, hp):
        self._hp = hp

    def get_damage(self):
        return self._damage

    def set_damage(self, damage):
        self._damage = damage
