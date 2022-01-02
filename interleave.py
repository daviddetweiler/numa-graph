import sys
import os


def main():
    if len(sys.argv) != 2:
        return

    dump = open(f'{sys.argv[1]}.dat', 'w')
    for name in os.listdir(f'./{sys.argv[1]}/'):
        for line in open(f'./{sys.argv[1]}/{name}', 'r').readlines():
            print(line, end='', file=dump)


if __name__ == '__main__':
    main()
