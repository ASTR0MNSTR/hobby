import re


def take_ip(path_input):
    with open(path_input, 'r') as f:
        lines = f.readlines()
        print(lines)


if __name__ == '__main__':
    take_ip('C:/hobby/hobby/take_ip/input.txt')