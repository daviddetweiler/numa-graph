import matplotlib.pyplot as plt

def plot(zipped):
    x = [r for r, _, _, _ in zipped]
    a = [t for _, t, _, _ in zipped]
    b = [s for _, _, s, _ in zipped]
    c = [u for _, _, _, u in zipped]
    plt.plot(x, a, 'r', x, b, 'g', x, c, 'b')
    plt.xlabel('P(read)')
    plt.ylabel('Mops/s')
    plt.show()

if __name__ == '__main__':
    plot(eval(input()))
