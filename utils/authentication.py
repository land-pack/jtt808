import random
from conf.settings import NUM_OF_CODE


def simple_auth():
    result_list = []
    for i in range(NUM_OF_CODE):
        temp = random.randint(1, 100)
        result_list.append(temp)
    return tuple(result_list)


if __name__ == '__main__':
    result = simple_auth()
    print result
