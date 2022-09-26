from collections import Counter
def factor(num, anwer = 2):
    delit = []
    while not num % anwer:
        delit.append(anwer)
        num //= anwer
    anwer = 3
    while anwer*anwer <= num:
        while not num % anwer:
            delit.append(anwer)
            num //= anwer
        anwer += 2
    if num - 1:
        delit.append(num)
    return delit

def main(m, n):
    dmax = 0
    for i in range(m, n+1):
        fact = Counter(factor(i)).values()
        k = 1
        for d in fact:
            k *= d + 1
        if k > dmax:
            dmax = k 
            res = i 
    return res 
print(main(2, 100000))