import random


def simple_auth():
    result = []
    for i in range(8):
        temp = random.randint(1, 100)
        result.append(temp)
    return tuple(result)


if __name__ == '__main__':
    result = simple_auth()
    print result
