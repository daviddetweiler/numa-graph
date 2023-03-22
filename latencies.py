import sys
import matplotlib.pyplot as plt
import statistics as stats

def main():
    if len(sys.argv) != 2:
        return

    times = [int(line)
             for line in open(sys.argv[1], 'r').readlines() if line != '\n']

    title = sys.argv[1].split('\\')[-1]
    m = max(times)
    print(title)
    print(f'maximum was {m}')
    print(f'minimum was {min(times)}')
    print(f'mean was {stats.mean(times)}')
    print(f'median was {stats.median(times)}')
    #plt.xscale('log')
    #plt.yscale('log')
    #plt.xlim(0, 300)
    plt.hist(times, bins=m, cumulative=True, histtype='step', density=True)
    plt.title(title)
    plt.show()


if __name__ == '__main__':
    main()
