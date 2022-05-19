import matplotlib.pyplot as plt

data = eval(input())
skews = data.keys()
spin = [data[s][0] for s in skews]
cas = [data[s][1] for s in skews]
race = [data[s][2] for s in skews]
plt.plot(skews, spin, 'ro', skews, cas, 'go', skews, race, 'bo')
plt.show()
