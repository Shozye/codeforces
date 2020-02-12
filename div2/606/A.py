import math
def main():
    answer = ""
    for test in range(int(input())):
        n = int(input())
        am_integer = math.floor(math.log(n,10))+1
        ans = (am_integer-1)*9
        add = 0
        for i in range(1,10):
            if int(str(i)*am_integer) <= n:
                add+=1
        answer += str(ans + add) + "\n"
    print(answer)
main()
