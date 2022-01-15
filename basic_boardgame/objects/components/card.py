class Card:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name


class AdvancedCard(Card):
    def __init__(self, name: str, description: str):
        super().__init__(name)
        self.description = description

    def __str__(self):
        return f"{self.name}\n {self.description}"

    def show_description(self):
        return self.description
