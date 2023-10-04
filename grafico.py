import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib 
import numpy as np
import random
from sgarebuild import Rebuild
print("====================================== SGA RELATORIOS ==========================")
valor = random.randint(1000, 5000)
#valores  = int(input("Informe o valor : "))

meses = ['SAIDA', 'VENDITENS', 'GRAVA', 'QUITADO ', 'CCFISCAL', 'VENDDUP', 'CICF', 'COMISSAO', 'RECIBO', 'ENTRADA', 'BALANCO', 'MOVBCO' ]
valores = [valor * 2, valor * 3, valor * 2, valor * 2, valor * 3, valor * 2, valor * 3, valor * 2, valor / 2, valor * 3, valor * 6, valor * 3]  


matplotlib.pyplot.title('Escala Rebuild')
matplotlib.pyplot.xlabel('Rebuild')
matplotlib.pyplot.ylabel('Quantidade Rebuild')

matplotlib.pyplot.plot(meses, valores)


matplotlib.pyplot.show()

x = np.linspace(0, 2, 100)  # Sample data.

plt.figure(figsize=(5, 2.7), layout='constrained')
plt.plot(x, x, label='SAIDA')  # Plot some data on the (implicit) axes.
plt.plot(x, x**5, label='VENDDUP')  # etc.
plt.plot(x, x*9, label='RECIBO')
plt.xlabel('x label')
plt.ylabel('y label')
plt.title("Simple Plot")
plt.legend()

plt.show()

fig, ax = plt.subplots(figsize=(5, 2.2), layout='constrained')
categories = ['SAIDA', 'VENDITENS', 'GRAVA', 'QUITADO ', 'CCFISCAL', 'VENDDUP', 'CICF', 'COMISSAO', 'RECIBO', 'ENTRADA', 'BALANCO', 'MOVBCO' ]
ax.bar(categories, np.random.rand(len(categories)))


plt.show()

X, Y = np.meshgrid(np.linspace(-3, 3, 128), np.linspace(-3, 3, 128))
Z = (1 - X/2 + X**5 + Y**3) * np.exp(-X**2 - Y**2)

fig, axs = plt.subplots(2, 2, layout='constrained')
pc = axs[0, 0].pcolormesh(X, Y, Z, vmin=-1, vmax=1, cmap='RdBu_r')
fig.colorbar(pc, ax=axs[0, 0])
axs[0, 0].set_title('pcolormesh()')

co = axs[0, 1].contourf(X, Y, Z, levels=np.linspace(-1.25, 1.25, 11))
fig.colorbar(co, ax=axs[0, 1])
axs[0, 1].set_title('contourf()')

pc = axs[1, 0].imshow(Z**2 * 100, cmap='plasma',
                          norm=mpl.colors.LogNorm(vmin=0.01, vmax=100))
fig.colorbar(pc, ax=axs[1, 0], extend='both')
axs[1, 0].set_title('imshow() with LogNorm()')

data1 = random.randint(100, 200)
data2 = random.randint(201, 400)
data3 = random.randint(100,500)

pc = axs[1, 1].scatter(data1, data2, c=data3, cmap='RdBu_r')
fig.colorbar(pc, ax=axs[1, 1], extend='both')
axs[1, 1].set_title('scatter()')

plt.show()

np.random.seed(19680801)  # seed the random number generator.
data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
ax.scatter('a', 'b', c='c', s='d', data=data)
ax.set_xlabel('Rebuild')
ax.set_ylabel('Quantidade')

plt.show()
print("Fim")
a = input("")
