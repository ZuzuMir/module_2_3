my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
zero = 0
while zero < len(my_list):
    if my_list[zero] > 0:
        print(my_list[zero])
    if my_list[zero] < 0:
        break
    zero += 1




