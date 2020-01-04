input = "387638-919123"
lower_bound, upper_bound = input.split("-")

fit = 0

for number in range(int(lower_bound), int(upper_bound)):
    last_digit = 0
    current_number = str(number)
    less_crit = True
    double_crit = False
    
    for i in range(len(current_number)):
        current_digit = int(current_number[i]) #11122 22111
        if current_digit == last_digit:
            double_crit = True

        if int(current_digit) < int(last_digit):
            less_crit = False

        last_digit = current_digit

    if double_crit & less_crit:
        fit += 1
    
print(fit)
