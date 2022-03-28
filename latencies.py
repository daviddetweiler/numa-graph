import sys
import matplotlib.pyplot as plt
import statistics as stats

def main():
    if len(sys.argv) != 2:
        return

    times = [int(line)
             for line in open(sys.argv[1], 'r').readlines() if line != '\n']

    print(f'maximum was {max(times)}')
    print(f'minimum was {min(times)}')
    print(f'mean was {stats.mean(times)}')
    print(f'median was {stats.median(times)}')
    plt.hist(times, bins=2**16, cumulative=True, histtype='step', density=True)
    plt.title(sys.argv[1])
    plt.show()


if __name__ == '__main__':
    main()
