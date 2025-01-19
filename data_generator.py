import csv
import random
from person import Customer  

def generate_customers_csv(filename="Customers.csv", num_customers=100):
    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["id", "name", "email", "age", "balance", "income"])
        for i in range(num_customers):
            age = random.randint(19, 70)
            balance = random.randint(-500, 500)
            income = random.randint(-500, 500)
            email = f"customer{i+2}@email.cm"
            name = f"customer{i+2}"
            writer.writerow([i + 4, name, email, age, balance, income])

if __name__ == "__main__": # this ensures the generate_customers_csv function is only called if this script is run directly
    generate_customers_csv()
    print("Customers.csv file generated.")