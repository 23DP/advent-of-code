input = "387638-919123"
lower_bound, upper_bound = input.split("-")

fit = 0

def LessCrit(num: str) -> bool:
    for i in range(len(num)-1):
        if int(num[i+1])  < int(num[i]) :
            return False
    return True

def DoubleCrit(ch: chr, num: str) -> bool:
    cnt = 0
    for i in num:
        cnt += 1 if ch == i else 0

    return True if cnt == 2 else False

for number in range(int(lower_bound), int(upper_bound)):
    double_crit = False
    for i in str(number):
        if DoubleCrit(i, str(number)):
            double_crit = True

    if double_crit & LessCrit(str(number)):
        fit += 1
    
print(fit)
