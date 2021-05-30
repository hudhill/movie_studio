class Movie:

    def __init__(self, title, rating, id = None):
        self.title = title
        self.rating = rating
        self.id = id

    def change_rating(self):
        self.rating = input(f"How would you rate {self.title}: 1-10? \n")