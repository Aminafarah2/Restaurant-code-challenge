# TITLE: RESTRAUNT
Certainly! Below is a simple README.md template for the project:

markdown
Copy code
# Yelp-style Restaurant Review System

## Description

This project implements a Yelp-style domain for managing restaurants, customers, and reviews. It involves three models: `Restaurant`, `Customer`, and `Review`. The relationships include a many-to-many relationship between `Restaurant` and `Customer`. The goal is to build a system that allows customers to review restaurants, and provides functionality to retrieve information about customers, restaurants, and reviews.

## Setup Instructions

To set up and run the project, follow these instructions:

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/restaurant-review-system.git
Navigate to the Project Directory:

bash
Copy code
cd restaurant-review-system
Install Dependencies:

Ensure you have Python installed. Use the following command to install dependencies:

bash
Copy code
pip install -r requirements.txt
Note: The requirements.txt file may include dependencies like ipdb as mentioned in the provided Pipfile.

Run the Project:

Execute the main script or use a Python interactive environment to test the implemented classes and methods:

bash
Copy code
python main.py
Project Structure
The project is organized into three main files:

customer.py: Contains the Customer class definition.
restaurant.py: Contains the Restaurant class definition.
review.py: Contains the Review class definition.
Feel free to explore and modify these files as needed.

## Deliverables
The project includes the following deliverables:

`Customer __init__()`
  - Customer should be initialized with a given name and family name, both strings (i.e., first and last name, like George Washington)"
- `Customer given_name()`
  - returns the customer's given name
  - should be able to change after the customer is created
- `Customer family_name()`
  - returns the customer's family name
  - should be able to change after the customer is created
- `Customer full_name()`
  - returns the full name of the customer, with the given name and the family name concatenated, Western style.
- `Customer all()`
  - returns **all** of the customer instances
Restaurant
- `Restaurant __init__()`
  - Restaurants should be initialized with a name, as a string
- `Restaurant name()`
  - returns the restaurant's name
  - should not be able to change after the restaurant is created
 

Review
- `Review __init__()`
  - Reviews should be initialized with a customer, restaurant, and a rating (a number)
- `Review rating()`
  - returns the rating for a restaurant.
- `Review all()`
  - returns all of the reviews
Object Relationship Methods
Review
- `Review customer()`
  - returns the customer object for that review
  - Once a review is created, should not be able to change the customer
- `Review restaurant()`
  - returns the restaurant object for that given review
  - Once a review is created, should not be able to change the restaurant
Restaurant
- `Restaurant reviews()`
  - returns a list of all reviews for that restaurant
- `Restaurant customers()`
  - Returns a **unique** list of all customers who have reviewed a particular restaurant.
Customer
- `Customer restaurants()`
  - Returns a **unique** list of all restaurants a customer has reviewed
- `Customer add_review(restaurant, rating)`
  - given a **restaurant object** and a star rating (as an integer), creates a new review and associates it with that customer and restaurant.
