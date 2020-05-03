'''Peter wants to generate some prime numbers for his cryptosystem. Help him! Your task is to generate all prime numbers between two given numbers!'''


num=int(input("Enter No of test cases: "))
for i in range(num):
    case2 = input().split()
    m=int(case2[0])
    n=int(case2[1])
    case1=list(range(2,n+1))
    for k in case1:
        for l in range(k**2,n+1):
            if l%k==0:
                case1.remove(l)
            else:
                continue
    for k in case1:
        if k>=m and k<=n:

            print(k,end=" ")

    print()