def power_of_num(base_num, power_num):
    result = 1
    for i in range(power_num):
        result = result * base_num
    return result


print(power_of_num(3, 0))
