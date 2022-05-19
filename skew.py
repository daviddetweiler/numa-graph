from collections import defaultdict


size = 10000000
harmonic = {}

def h(s, N):
	global harmonic
	if s not in harmonic:
		harmonic[s] = sum(pow(n, -s) for n in range(1, N + 1))

	return harmonic[s]

def p(s):
	global harmonic
	return sum(pow(n, -s) for n in range(1, size // 10 + 1)) / h(s, size)

target = 0.9
guess = 0.0
speed = 0.01
last = p(guess)
guess += speed
while True:
	probe = p(guess)
	print(guess, probe, last, speed)
	if probe > target:
		break

	last = probe
	guess += speed