import sys
import matplotlib.pyplot as plt


def main():
    if len(sys.argv) != 2:
        return

    times = [int(line)
             for line in open(sys.argv[1], 'r').readlines() if line != '\n']

    plt.hist(times, bins=1000)
    plt.show()


if __name__ == '__main__':
    main()
