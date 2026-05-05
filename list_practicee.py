#1) basic list opreation
num_list=[10,20,30,40,50]
print("list is :",num_list)

num_list.append(60)
print("The list after adding new element :",num_list)

num_list.remove(30)
print("The list after removing a element :",num_list)



#2)shopping bill
bill=[]
for i in range(5):
    price=int(input(f"enter the price of itrm {i+1} :"))
    bill.append(price)
print("all the price is :",bill)
print("the total bill is :",sum(bill))
print("the expensive item amount is :",max(bill))
print("the cheapest item amount is :",min(bill))

#3)find the largest of 3 number
number=[22,33,89,-55,11]
largest=number[0]

for num in number:
    if num>largest:
        largest=num
print("The largest among all the number is :",largest)
    
