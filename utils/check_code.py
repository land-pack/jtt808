def check(a_tuple):
    flag = True
    check_code = 1
    temp = a_tuple[:-1]
    for each in temp:
        if flag:
            check_code = each
            flag = False
        else:
            check_code = check_code ^ each
    return check_code


if __name__ == '__main__':
    sample = (1, 0, 0, 2, 78, 56, 45, 34, 25, 78, 0, 1, 51, 52, 43)
    print check(sample)
