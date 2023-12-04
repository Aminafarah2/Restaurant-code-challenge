# Define a Customer class
class Customer:
    all_customers = []

    # Constructor method to initialize a customer with given_name and family_name
    def __init__(self, given_name, family_name):
        # Instance variables prefixed with underscore to indicate they are intended to be private
        self._given_name = given_name
        self._family_name = family_name
        # Add the new customer instance to the list of all customers
        Customer.all_customers.append(self)

    # Getter method to retrieve the given name of the customer
    def given_name(self):
        return self._given_name

    # Getter method to retrieve the family name of the customer
    def family_name(self):
        return self._family_name

    # Method to concatenate and return the full name of the customer
    def full_name(self):
        return f"{self._given_name} {self._family_name}"

    # Class method to retrieve the list of all customer instances
    @classmethod
    def all(cls):
        return cls.all_customers

# Example usage:

# Creating customer instances
customer1 = Customer("George", "Washington")
customer2 = Customer("John", "Adams")



# Changing given_name and family_name
customer1._given_name = "Thomas"
customer1._family_name = "Jefferson"
# Accessing all customer instances
all_customers = Customer.all()
print("All Customers:", all_customers)  
for customer in all_customers:
    print (vars(customer))
