import numpy as np
import matplotlib.pyplot as plt

# Gerando 6 números aleatórios entre 0 e 1
a = np.random.rand(60)
print(a)

# Criando o histograma
plt.hist(a, bins=10, edgecolor='black')  # ravel() não é necessário aqui
plt.xlabel("Valor")
plt.ylabel("Frequência")
plt.title("Histograma")
plt.show()

print(a.ravel().shape)