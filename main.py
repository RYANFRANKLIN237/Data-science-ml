from person import Person, Customer
from data_generator import generate_customers_csv
from data_analysis import analyze_customer_data

# Create two Person objects
person1 = Person(1, "person1", "person1@email.cm", 27)
person2 = Person(2, "person2", "person2@email.cm", 33)

print(person1)
print(person2)

# Create one Customer object
customer1 = Customer(3, "customer1", "customer1@email.cm", 40, 1000, 2000)
print(customer1)

# Generates the CSV data
generate_customers_csv()

# Performs the data analysis
analyze_customer_data()