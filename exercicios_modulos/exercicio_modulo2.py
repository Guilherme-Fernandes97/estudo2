import matplotlib.pyplot as plt

import numpy as np

vendas = np.random.randint(1000, 3000, 50)
meses = np.arange(1, 51)

plt.plot(meses, vendas, color='red')
plt.axis([0, 50, 0, max(vendas) + 300])
plt.xlabel('Meses')
plt.ylabel('Vendas')
plt.show()