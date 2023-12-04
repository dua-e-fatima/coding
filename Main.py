num = int(input("enter a number:"))
i = 1
while i <= num:
    print(i*"*")
    i = i + 1
    
num = int(input("enter a number:"))

for i in range(num): 
    print(" " * (num-i-1) + "*"*(2*i+1))   
    
num = int(input("enter a number:"))
i = 1
j = num
while i <= num:
    print(j* "*"+" "*i)
    i +=1
    j -=1
    
num = int(input("enter the number of rows:"))
for i in range(num):
    print(" " * i + "* " * (num-1)) 
for i in range(num-2,-1,-1):
    print(" " * i + "* " * (num-1))  
    

    
    