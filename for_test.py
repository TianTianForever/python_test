#_*_coding:utf-8_*_
#author:tiantian

#Measure some string:

words = ["cat","window","defenestrate"]
for w in words :
    print(w,len(w))

for i in words[:]:
    if len(i) > 6 :
        words.insert(0,i)
print(words) 

a = ["Mary","had","list","little","range"]
for i in range(len(a)):
    print(i,a[i])
