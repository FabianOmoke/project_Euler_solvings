two_digit_pali = 9009
pali_list = []

for i in range(100, 999):
    for x in range(100, 999):
        possible_pali = i*x 
        check_pali = str(possible_pali)
        if check_pali == check_pali[::-1]:
            pali_list.append(int(check_pali))
        

print(max(pali_list))