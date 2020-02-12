from collections import Counter 
def B():
    answer = ""
    for i in range(int(input())):
        n = int(input())
        r,p,s = map(int, input().split(' '))
        moves = list(input())
        mset = Counter(moves)
        r_, p_, s_ = mset["R"], mset["P"], mset["S"]
        use_r, use_p, use_s = min(r,r_), min(p,p_), min(s,s_)
        winning = dict()
        winning["R"] = ["P",use_p]
        winning["P"] = ["S",use_s]
        winning["S"] = ["R",use_r]
        wins = min(r_,r) + min(p,p_) + min(s,s_)
        if wins < (n+1)//2:
            answer += "NO \n"
        else:
            answer +="YES \n"
            my_moves = ['']*n
            for i in range(len(moves)):
                move = moves[i]
                if winning[move][1] > 0:
                    my_moves[i] = winning[move][0]
                    winning[move][1] -= 1
            left_r = r-use_r
            left_p = p-use_p
            left_s = s-use_s
            for i in range(len(my_moves)):
                if my_moves[i] == '':
                    if left_r > 0:
                        my_moves[i] = "R"
                        left_r-=1
                    elif left_p > 0:
                        my_moves[i] = "P"
                        left_p-=1
                    else:
                        my_moves[i] = "S"
                        left_s -= 1
            answer += "".join(my_moves) + "\n"
    print(answer)
                   
B()
