smallest_multiple_bool = False
smallest_multiple = 0
numbers = [x for x in range(1, 21)]
while True:
    smallest_multiple += 1
    rems = [smallest_multiple%x for x in numbers]
    if len(set(rems)) <= 1:
        print(smallest_multiple)
        smallest_multiple_bool = True
        break
    else:
        continue
     

    
