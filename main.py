from customers import Customer
from review import Review
from restaurant import Restaurant

def main():
    # Instantiate some customers, restaurants, and reviews
    customer1 = Customer("Henry", "Styles")
    customer2 = Customer("Anne", "Smith")

    restaurant1 = Restaurant("Bevely Treats")
    restaurant2 = Restaurant("Pizza Palace")

    review1 = Review(customer1, restaurant1, 4)
    review2 = Review(customer2, restaurant2, 5)

    # Example usage of the methods
    print(customer1.full_name())  
    print(restaurant2.average_star_rating())  
    print(customer2.num_reviews())  
    print(vars(review1))
    print(vars(review2))

if __name__ == '__main__':
    main()