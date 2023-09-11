import datetime


class ProjectManagement:
    def __init__(self, name="",	start_date="", priority=int, cost=float, completion=int):
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = priority
        self.cost = cost
        self.completion = completion

    def __str__(self):
        """Return string"""
        return f"{self.name}, {self.start_date}, {self.priority}, {self.cost:,.2f}, {self.completion}"

    def __repr__(self):
        return f"{self.name}, {self.start_date}, {self.priority}, {self.cost:,.2f}, {self.completion}"

    def compare_date(self, input_date):
        """Compare the user_input date with project start date."""
        input_date = datetime.datetime.strptime(input_date, "%d/%m/%Y").date()
        return self.start_date >= input_date

    def update_percentage(self, value):
        """Update the project completion percentage."""
        self.completion = value

    def update_priority(self, value):
        """Update the project priority"""
        self.priority = value
