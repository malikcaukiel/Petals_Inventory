import pandas as pd

# Loading the data into a DataFrame called inventory from .csv file
inventory = pd.read_csv('inventory.csv')

# Inspecting the data.
print(inventory.head(10))
#print(inventory.info())

# The first 10 rows represent data from your Staten Island location.
# So assigning these rows to staten_island.
staten_island = inventory.iloc[0:10]
#print(staten_island)

# A customer wants to know what products are sold at your Staten Island location.
# Selecting the column product_description from staten_island.
product_request = staten_island['product_description']
#print(product_request)

# Another customer emails to ask what types of seeds are sold at the Brooklyn location.
# Selecting all rows where location is equal to Brooklyn and product_type is equal to seeds.
seed_request = inventory[(inventory.location == 'Brooklyn') & (inventory.product_type == 'seeds')]
#print(seed_request)

# We want to know if certain product is in stock or not.
# Adding a column to inventory called in_stock which is True if quantity is greater than 0 and False if quantity equals 0.
#inventory['in_stock'] = inventory.apply(lambda row: True if row.quantity>0 else False, axis=1) # lambda is the 1st parameter, and axis=1 is the 2nd parameter
inventory['in_stock'] = inventory.quantity.apply(lambda x: True if x>0 else False) # also good here
#print(inventory)

# The company wants to know how valuable their current inventory is.
# Creating a column called total_value that gives value, which is equal to price multiplied by quantity.
inventory['total_value'] = inventory.price * inventory.quantity
#or#inventory['total_value'] = inventory['price'] * inventory['quantity']
#print(inventory)

# The Marketing department wants a complete description of each product for their catalog.
# The following lambda function combines product_type and product_description into a single string:
combine_lambda = lambda row: \
    '{} - {}'.format(row.product_type,
                     row.product_description)
#print(inventory.head(10))

# Using combine_lambda, creating a new column in inventory called full_description that has the complete description of each product.
inventory['full_description'] = inventory.apply(combine_lambda, axis=1) # just using the above function
print(inventory)
#####################################################################################################



