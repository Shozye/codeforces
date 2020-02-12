def main():
    answer = ""
    for query in range(int(input())):
        n = int(input())
        s1,s2 = input(),input()

        different = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                different.append(i)
        if len(different) == 0:
            answer += "Yes \n"
        elif len(different) == 2:
            pair1 = (s1[different[0]], s2[different[0]])
            pair2 = (s1[different[1]], s2[different[1]])
            if pair1[0] == pair2[0] and pair1[1] == pair2[1]:
                answer += "Yes \n"
            else:
                answer += "No \n"
        else:
            answer += "No \n"

            
        
    print(answer)
main()
