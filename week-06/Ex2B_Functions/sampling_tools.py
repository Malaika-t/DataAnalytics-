# Lab 1:

import random

products = ['Laptop', 'Monitor', 'Keyboard', 'Mouse', 'Webcam', 'Headset', 'Docking Station', 
'USB Hub', 'Desk Lamp', 'Surge Protector']

# 4a. Product of the Day - random.choice()
product_of_the_day = random.choice(products)
print(f"Product of the Day: {product_of_the_day}")

# 4b. Usability Survey - random.sample()
survey_products = random.sample(products, 3)
print(f"Usability Survey Products: {survey_products}")

# 4c. Randomized Order - random.shuffle()
random.shuffle(products)
print(f"Randomized Product Order: {products}")

# 4d. Transaction Count - random.randint()
transaction_count = random.randint(50, 300)
print(f"Transaction Count: {transaction_count}")