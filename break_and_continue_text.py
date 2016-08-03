#_*_coding:utf-8_*_
#author:tiantian

#break and continue statements

for n in range(2,10):
    for x in range(2,n):
        if n % x == 0 :
            print(n,"equals",x,"*",n//x)
            break
        else :
            # loop fell through without finding a factor
            print(n,"is a prime number")
            break
for num in range(2,10):
    if num % 2 == 0 :
        print("Found an enve number",num)
        continue
    print("found a number",num)
