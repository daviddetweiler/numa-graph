import sys
import matplotlib.pyplot as plt


if __name__ == '__main__':
    data = eval(''.join(open(sys.argv[1]).readlines()))
    data = [[k] + v for k, v in data.items()]
    for l in data:
        print(', '.join(str(f) for f in l))
