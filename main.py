p=[]#an array to store the list of items
print("Goodies and Prices:\nFitbit Plus: 7980\nIPods: 22349\nMI Band: 999\nCult Pass: 2799\nMacbook Pro: 229900")#displaying the list of items part1
print("Digital Camera: 11101\nAlexa: 9999\nSandwich Toaster: 2195\nMicrowave Oven: 9800\nScale: 4999 ")#displaying the list of items part2
si=int(input("\n-------------------------\nEnter the number of employee: "))#taking the input of number of employee

print("-------------------------\nEnter only the price of goodies distributed")
for i in range(0,si):#taking the input of goodies that are distributed
  ele=int(input())
  p.append(ele)#adding the entered data to the list
a=max(p)#finding the largest number in the list entered
b=min(p)#finding the smallest number in the list entered
c=(a-b)#finding the diffrence of two number
print("-------------------------\nAnd the difference between the chosen goodie with highest price and the lowest price is ",c)#displaying the final value