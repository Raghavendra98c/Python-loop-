#1.Python for loop to find the sum of all numbers in a list
li=[20,10,50]
sum=0
for i in range(len(li)):
    sum+=li[i]
print(sum)

#2.Python for loop to find the multiples of 5 in a list
li=[1,2,3,45,5,10,20]
for i in li:
    if i%5 ==0:
        print(i)
        
4. Python for loop to copy elements from one list to another
l1=[1,2,3,4,5]
l2=[]
for i in l1:
    l2.append(i)
print(l2)

# 5.sort
li=[23,1,4,2,0,3]
for i in range(0,len(li)):
    for j in range(i+1,len(li)):
        if(li[i]>li[j]):
            x=li[i]
            li[i]=li[j]
            li[j]=x
print(li)   

# Python for loop to print the multiples of 3 using range() function

for i in range(3,20,2):
    print(i)
    
#Python for loop to print the numbers in reverse order using range() function
for i in range(20,0,-1):
    print(i)
