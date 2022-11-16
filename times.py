import enum
import sys

def dump(name, data):
    with open(name, 'w') as file:
        for n, t in data:
            print(f'{n}: {t}', file=file)

def main():
    if len(sys.argv) != 3:
        return

    cutoff = int(sys.argv[2])
    data = (int(l) for l in open(sys.argv[1]).readlines())
    data = list((n, t) for n, t in enumerate(data) if t > cutoff)
    dump('dump.txt', data)

if __name__ == '__main__':
    main()
