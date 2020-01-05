class Young:
    def __init__(self, name):
        self.name = name
        self.age = None
        self.No_Of_Elders = 0
        self.reviewsYoung = dict()
        self.ratings_Young = []

    def get_Name(self):
        return self.name

    def set_Age(self, age):
        self.age = age
        pass

    def Add_Elders(self, elder):
        if len(self.No_Of_Elders) < 4:
            self.No_Of_Elders.append(elder)
        else:
            print("He is full so you had to chose the another elder ")
            return "Full"
        pass

    def set_Reviews(self, Elder_name, review):
        if self.reviewsYoung.get(Elder_name) is None:
            self.reviewsYoung[Elder_name] = [review]
        else:
            self.reviewsYoung[Elder_name].append(review)
        pass

    def get_Reviews(self):
        print("Reviews are the ")
        for i, j in self.reviewsYoung.items():
            print(i.get_Name())
            print(j)

    def set_Rating(self, ratings):
        self.ratings_Young.append(ratings)
        pass

    def get_Ratings(self):
        if len(self.ratings_Young) == 0:
            return "This Person is not yet Rated"
        return sum(self.ratings_Young) // len(self.ratings_Young)
