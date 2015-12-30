def check(a_tuple):
    flag = True
    check_code = 0
    temp = a_tuple[:-1]
    for each in temp:
        if flag:
            check_code = each
            flag = False
        else:
            check_code = check_code ^ each
    return check_code
