
class Band:

    def __init__(self, name=""):
        self.name = name
        self.band = []

    def __str__(self):
        """Return a string showing the instrument playing their first (or no) instrument."""
        return f"{self.name} ({self.play()}) "

    def add(self, band):
        self.band.append(band)

    def play(self):
        result = ""
        for band in self.band:
            result += band.play() + "\n"
        return result
