# This is the elder class to get the information of the elder and its price to be
# Allocated  funds for taking care


class Elder:
    def __init__(self, name):
        self.name = name
        self.age = None
        self.fund = None
        self.reviews = dict()
        self.is_Available = True
        self.rating = []

    def set_Ratings(self, rating):
        self.rating.append(rating)
        pass

    def get_Ratings(self):
        if len(self.rating) == 0:
            return "Not Yet Rated "
        else:
            return sum(self.rating) // len(self.rating)

    def get_Name(self):
        return self.name

    def set_Age(self, age):
        self.age = age
        pass

    def get_Age(self):
        return self.age

    def set_Funds(self, fund):
        self.fund = fund
        pass

    def get_Funds(self):
        return self.fund

    def set_Reviews_Elder(self, review, Name):
        if self.reviews.get(Name) is None:
            self.reviews[Name] = [review]
        else:
            self.reviews[Name].append(review)
        pass

    def get_Reviews(self):
        print(f"Reviews of the {self.name}  are the")
        for i, j in self.reviews.items():
            print(i, "  :")
            print(j)
