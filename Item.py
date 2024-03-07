class Item:
    def __init__(self, name, item_type, value):
        self.__name = name
        self.__item_type = item_type
        self.__value = value

    def use(self):
        print(f"Item {self.__name} digunakan.")

    def get_name(self):
        return self.__name

    def get_item_type(self):
        return self.__item_type

    def get_value(self):
        return self.__value

    def set_name(self, name):
        self.__name = name

    def set_item_type(self, item_type):
        self.__item_type = item_type

    def set_value(self, value):
        self.__value = value

    def show_info(self):
        print(f"Nama Item: {self.__name}")
        print(f"Tipe Item: {self.__item_type}")
        print(f"Nilai Item: {self.__value}")
