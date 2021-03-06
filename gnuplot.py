import enum
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Need file')
        exit()

    with open(sys.argv[1]) as file:
        results = eval(''.join(file.readlines()))
        skews = [s for s in results]
        sl = [results[s][0] for s in skews]
        at = [results[s][1] for s in skews]
        nl = [results[s][2] for s in skews]
        print('Skew, Spinlock, Fetch-and-add, Unsynchronized')
        for skew, lock, atomic, null in zip(skews, sl, at, nl):
            print(f'{skew}, {lock}, {atomic}, {null}')
