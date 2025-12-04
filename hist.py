import requests
import matplotlib.pyplot as plt

url = "https://oeis.org/A077196/b077196.txt"
text = requests.get(url).text

# parse lines: skip comments; split on whitespace; take second field
vals = []
for line in text.splitlines():
    if line.startswith('#'):  
        continue
    parts = line.split()
    if len(parts) >= 2:
        vals.append(int(parts[1]))

from collections import Counter
print(sorted(Counter(vals).items()))
plt.hist(vals, bins='auto')
plt.xlabel('a(n)')
plt.ylabel('Frequency')
plt.title('Histogram of A077196 values')
plt.show()
