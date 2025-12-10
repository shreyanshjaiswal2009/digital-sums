import matplotlib.pyplot as plt
import math

def s10(m: int) -> int:
    """Return the sum of decimal digits of m."""
    return sum(int(d) for d in str(m))

# Range of n
ns = list(range(1, 101))

# Compute s10(lcm)
lcm = 1
fact = 1
lcms = [1]
facts = [1]
for i in range(2, 101):
    lcm = math.lcm(lcm, i)
    fact *= i
    lcms.append(s10(lcm))
    facts.append(s10(fact))

# Conjectured linear approximation
def approx_s10_fact(n):
    # return 9 / (2 * math.log(10)) * (math.log(2*math.pi)/2 + (n+.5)*math.log(n) - n - (n/4)*math.log(5)) 
    return 4.5 * (math.log10(math.factorial(n)) - n/4)

def approx_s10_lcm(n):
    return 9 / (2 * math.log(10)) * n

line = [approx_s10_lcm(n) for n in ns]
curve = [approx_s10_fact(n) for n in ns]


plt.figure(figsize=(8, 5))

# Scatter of s10(2^n)
plt.scatter(ns, lcms, label=r"$s_{10}(\Lambda_n)$", s=20)
plt.scatter(ns, facts, label=r"$s_{10}(n!)$", s=20)

# Line plot of the conjectured approximation
plt.plot(ns, line, label=r"$4.5n/\log(10)$")
plt.plot(ns, curve, 'r', label=r"$4.5 (\log_{10} n! - n/4)$")
plt.plot()
# plt.plot(ns, L0, label=r"$4.5n \,\log_{10} 2$")

plt.xlabel("n")
# plt.ylabel(r"$s_{10}(2^n)$")
# plt.title(r"Scatterplot of $s_{10}(2^n)$ with Conjectured Approximation")
plt.legend()
plt.tight_layout()
plt.savefig('lcm_fact_scatter.png')
plt.show()
