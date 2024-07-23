

# Define function to retrieve prices colum in to a list
def get_prices(data):
    """
    Retrieves prices column in to a list

    Args:
        data (str): CSV format data

    Returns:
        list: list of prices
    """
    prices = []
    for row in data.split('\n')[1:]:
        price = row.split(',')[2]
        prices.append(float(price[1:]))
    return prices

def get_products(data):
    """
    Retrieves products column in to a list

    Args:
        data (str): CSV format data

    Returns:
        list: list of products
    """
    data = data.split('\n')[1:]
    products = []
    for row in data:
        product = row.split(',')[0]
        products.append(product)
    return products
   
def get_expensive(prices):
    """
    Finds the most expensive product of index

    Args:
        prices (list): list of prices

    Returns:
        int: index of most expensive product
    """
    idx = 0 # Most expensive product's index
    expensive = prices[idx]
    for i in range(len(prices)):
        if prices[i] > expensive:
            expensive = prices[i]
            idx = i
    return idx
    

# Read data from file
f = open("data.csv")
data = f.read()
products = get_products(data)
# print(products)
prices = get_prices(data)
# Get most expensive product index
idx = get_expensive(prices)
print(prices[idx])
# Print most expensive product
print(f'Most expensive product: {products[idx]}')