from math import gcd
def A():
    answer = ""
    for i in range(int(input())):
        a,b = map(int,input().split(' '))
        if gcd(a,b) == 1:
            answer += "Finite \n"
        else:
            answer += "Infinite \n"
    print(answer)
A()
