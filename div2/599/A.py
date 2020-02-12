def main():
    answer = ""
    for query in range(int(input())):
        ans = ""
        n = int(input())
        planks = list(map(int,input().split(' ')))
        planks.sort(reverse=True)
        for i in range(len(planks)):
            plank = planks[i]
            if plank == i+1:
                ans = i+1
                break
            elif plank < i+1:
                ans = i
                break
        if ans == "":
            ans = len(planks)
        answer += str(ans) + "\n"
    print(answer)
main()
