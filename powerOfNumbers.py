def power_of_num(base_num, power_num):
    result = 1
    if power_num == 0:
        return result
    if power_num == 1:
        return base_num
    for i in range(0, power_num):
        result = result * base_num
    return result


print(power_of_num(3, 4))
