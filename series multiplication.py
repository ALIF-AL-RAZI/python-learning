#1*2*3*4*... n

'''n=int(input("enter last number: "))
product=1

for x in range(1,n+1, 1):
    product=product*x
print(product)'''

#1*3*5*7*... n

'''n=int(input("enter last number: "))
product=1

for x in range(1,n+1, 2):
    product=product*x
print(product)'''

#(1**2) * (2**2) * (3**2) * (4**2) * ... (n**2)

n=int(input("enter last number: "))
product=1

for x in range(1,n+1, 1):
    product=product*(x**2)
print(product)




