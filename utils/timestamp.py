from utils.tools import dec2hex4tuple
import time


def to_datetime(x):
    val = dec2hex4tuple(x)
    date = val[0:3]  # Example (16,1,5)
    the_time = val[3:6]  # Example (11,40,19)
    sub_date = '20'
    sub_time = ' '
    count = 0
    for item in date:
        sub_date += str(item)
        if count < 2:
            sub_date += '-'
        count += 1
    # sub_date = '2016-1-5'
    count = 0
    for item in the_time:
        sub_time += str(item)
        if count < 2:
            sub_time += ':'
        count += 1
    # sub_time = ' 11:40:19'
    datetime = sub_date + sub_time
    # datetime = 2016-1-5 11:40:19'
    return datetime


def to_sec(val):
    sec = time.mktime(time.strptime(val, '%Y-%m-%d %H:%M:%S'))
    temp = int(sec)  # take the point out,Example 111.11 --> 111
    return str(temp)


def to_timestamp_fun(val):
    temp = to_datetime(val)
    return to_sec(temp)


if __name__ == '__main__':
    print '---------Test to_timestamp----------'
    sample9 = (22, 1, 5, 17, 64, 25)
    sample9x = to_timestamp_fun(sample9)
    print 'old          :', sample9
    print 'new          :', sample9x
