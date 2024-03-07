class Quest:

    def __init__(self, title, description, reward, status = "not started", prerequisites = None, quest_giver = None):
        self.title = title
        self.description = description
        self.reward = reward
        self.status = status
        self.prerequisites = prerequisites if prerequisites else []
        self.quest_giver = quest_giver

    def check_prerequisites(self, player):
        return all(prerequisite.is_completed for prerequisite in self.prerequisites)

    def complete_quest(self):
        self.status = "completed"
        print(f"Quest {self.title} selesai, Selamat!")

    def display_quest(self):
        print(f"Quest: {self.title}")
        print(f"Deskripsi: {self.description}")
        print(f"Hadiah: {self.reward}")
        print(f"Status: {self.status}")
