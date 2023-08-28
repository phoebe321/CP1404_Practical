
class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        # return f"My guitar: {self.name}, first made in {self.year}"
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def get_age(self):
        current_year = 2022
        age = current_year - self.year
        return age

    def is_vintage(self):
        age = self.get_age()
        return age >= 50