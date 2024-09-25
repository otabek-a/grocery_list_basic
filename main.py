

# Define function to retrieve prices colum in to a list
def get_prices(data):
    son=data.split("\n")
    javob=''
    i=1
    natija=''
    while i<len(son):
        son1=son[i].split(",")
        javob+=f"{i} {son1[2]} \n"
        natija+=f"{son1[2]}"
        i+=1
    return javob




def get_products(data):
    son=data.split("\n")
    javob=''
    i=1
    while i<len(son):
        son1=son[i].split(",")
        javob+=f"{i} {son1[0]} \n"
        i+=1
    return javob

    

def get_expensive(prices):
    
    son=data.split("\n")
    javob=''
    i=1
    natija=''
    result=[]
    while i<len(son):
        son1=son[i].split(',')
        javob = son1[2]
        natija+= javob[1:]
        result.append(float(javob[1:]))
        i+=1
    n=0
    max=result[0]
    while n<len(result):
        if result[n]>max:
            max=result[n]
        n+=1
    return max

    
    

    

# Read data from file
f = open("data.csv","r")
data = f.read()
price=get_prices(data)
print(price)
print(get_products(data))
sum=get_expensive(data)
print(f"The most expensive cost is {sum}")
