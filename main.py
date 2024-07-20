

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
   
        

# Read data from file
f = open("data.csv")
data = f.read()

print(get_prices(data))