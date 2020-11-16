from functools import reduce


def prod(x,y):
    return x * y


if __name__ == '__main__':
    L1 = [1,2,3,4,5,6,9]
    L2 = reduce(prod, L1)
    print(L2)