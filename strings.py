import sympy as sp
from numpy import random
import matplotlib.pyplot as plt

n = 10
#print("array length:", n)
m = 128
#print("elements range: [0, "+str(m)+")")

primes = list(sp.primerange(max(m,n**2)*2, max(m,n**2)*40))
#print(primes)
theoretical_rates = []
tested_rates = []

for k in range(len(primes)):
    p = primes[k]
    #print("prime field: " + str(p))

    theoretical_rate = (1-(n-1)/p)*100
    theoretical_rates.append(theoretical_rate)
    #print("theoretical minimum acceptance rate: " + str(round(theoretical_rate, 5)) + "%")

    a = [random.randint(m) for _ in range(n)]
    #print("string A: " + str(a))

    b = a.copy()
    b = [random.randint(m) for _ in range(n)]
    #print("string B: " + str(b))

    def h(c, r):
        res = 0
        for i in range(len(c)):
            res += c[i]*r**i % p
        return res % p

    hit = 0
    miss = 0

    for i in range(p):
        r = random.randint(p)
        # print("random r: " + str(r))

        v_a = h(a, r)
        # print("poly eval by A: " + str(v_a))

        v_b = h(b, r)
        # print("poly eval by B: " + str(v_b))

        if v_a == v_b:
            hit += 1
        else:
            miss += 1

    if hit != 0:
        tested_rate = (1-hit/miss)*100
    else:
        tested_rate = 100
    tested_rates.append(tested_rate)
    #print("tested acceptance rate: " + str(round(tested_rate,5)) + "%")

plt.plot(primes, theoretical_rates, 'r', label='theoretical')
plt.plot(primes, tested_rates, 'b', label='tested')
plt.show()

