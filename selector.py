import random

T = int(input("how many times?: "))


def get_lucky_nums():
    result = random.sample(range(1,45+1), k=6)
    print(result)

if __name__ == '__main__':
    for _ in range(T):
        get_lucky_nums()
