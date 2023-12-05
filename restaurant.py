class Restaurant:
    all_restaurants = []  # Class variable to keep track of all restaurants

    def __init__(self, name):
        self.name = name
        self.reviews = []  # List to store restaurant reviews
        Restaurant.all_restaurants.append(self)  # Add the restaurant to the list of all restaurants

    def name(self):
        return self.name

    def reviews(self):
        return self.reviews

    def customers(self):
        return list({review.customer for review in self.reviews})

    @classmethod
    def all(cls):
        return cls.all_restaurants

    def average_star_rating(self):
        total_ratings = sum(review.rating for review in self.reviews)
        num_reviews = len(self.reviews)
        if num_reviews > 0:
            return total_ratings / num_reviews
        else:
            return 0  # Return 0 if there are no reviews yet