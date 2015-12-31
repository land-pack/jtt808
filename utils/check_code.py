def check(a_tuple):
    flag = True
    check_code = 1
    temp = a_tuple
    for each in temp:
        if flag:
            check_code = each
            flag = False
        else:
            check_code = check_code ^ each
    return check_code


if __name__ == '__main__':
    sample = (1,2,3,4,5,1)
    print check(sample)
