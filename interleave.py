import sys
import os
from collections import defaultdict


def main():
    if len(sys.argv) != 2:
        return

    path = sys.argv[1]
    datasets = defaultdict(lambda : [])
    for name in os.listdir(path):
        prefix = name.split('.')[0].split('_')[0]
        datasets[prefix].append(name)

    print(datasets)

    for prefix, sources in datasets.items():
        file = open(f'{prefix}.dat', 'w')
        for source in sources:
            latencies = open(f'{path}{source}', 'r')
            for line in latencies.readlines():
                print(line, end='', file=file)


if __name__ == '__main__':
    main()
