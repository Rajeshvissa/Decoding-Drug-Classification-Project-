#taking  the selling price of icecreams and taking yearly wise

n=int(input("enter the no.of years: "))
list1=[]
for i in range(1,n+1):
    m=int(input("enter the selling price of icecream yearly order: "))
    list1.append(m)
    
list2=[]
count=0
sum=0

for i in range(len(list1)-2):
    y=list1[i+1]-list1[i]
    list2.append(y)
    
for j in range(1,len(list2)+1): #checking whether every selling price varying with a constant value or not
    if list2[0]==list2[i]:
        count=count+1
presentday =len(list1)-1
if count==len(list2):  
    b=list2[0]
    nextdayprice=list1[presentday]+b
else:
    for k in list2:
        sum=sum+k
    avg=sum/len(list2)
    nextdayprice=list1[presentday]+avg
print("price of icecream on the nextday will be",nextdayprice)    
    


    
   
    
    


