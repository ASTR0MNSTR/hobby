import string
import re


def take_ip(path_input, path_output):
    with open(path_input, 'r') as input:
        lines = input.readlines()
        sites = [item for ind, item in enumerate(lines) if ind % 3 == 0]
        sites_out = ''
        for item in sites:
            sites_out += re.sub(r'\n', '', item) + ' '
        print(sites_out)
        with open(path_output, 'w') as output:
            output.write(sites_out)
            output.close()
    

if __name__ == '__main__':
    take_ip('C:/hobby/hobby/take_ip/input.txt', 'C:/hobby/hobby/take_ip/output.txt')