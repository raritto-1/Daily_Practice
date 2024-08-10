import pandas  as pd 



count = 0 
da = True
while True:
    item= input('enter the item : - ')

    if item =="exit":
        break
    price = int(input('enter the price of item: - '))
    
    count += price
print("Total:- ", count)
    


df  = pd.DataFrame({"Item" : item,"price": price})

total = df['Price'].sum()\


print("\nList of Items and Prices:")
print(df)
print(f"\nTotal: {total}")