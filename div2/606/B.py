def even_max(tab):
    _max = -1
    i = 0
    while i < len(tab):
        num = tab[i]
        if _max < num and num%2 == 0:
            _max = num
        i+=1
    if _max == -1:
        return False
    else:
        return _max
def divide(tab,num):
    i = 0
    while i < len(tab):
        if tab[i] == num:
            tab[i] //= 2
        i+=1
def main():
    answer = ""
    for test in range(int(input())):
        n = int(input())
        integers = list(map(int,input().split(" ")))
        _max = even_max(integers)
        counter = 0
        while _max != False:
            divide(integers,_max)
            counter += 1
            _max = even_max(integers)
        answer += str(counter) + "\n"
    print(answer)
            
main()
