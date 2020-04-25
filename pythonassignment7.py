#a<=b and
#a^2 + b^2 = A
#0 <= A
#A<=1000


num=int(input("enter the number"))
for i in range (0,num+1):
    for j in range(i,num+1):
        if i*i + j*j ==num:
            print("a={} \nb={}".format(i,j))