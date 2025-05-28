
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

# 1. Gráfico de Linha
# Mostra a variação de uma variável contínua. Ideal para séries temporais ou funções matemáticas.
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'b-', linewidth=2, label='sen(x)')
plt.title('Função Seno')
plt.xlabel('x')
plt.ylabel('sen(x)')
plt.grid(True)
plt.legend()
plt.show()

# 2. Gráfico de Dispersão
# Mostra a relação entre duas variáveis numéricas. Útil para encontrar correlações ou padrões.
x = np.random.rand(50)
y = x + 0.3 * np.random.randn(50)
cores = np.random.rand(50)
tamanhos = 1000 * np.random.rand(50)
plt.figure(figsize=(10, 6))
scatter = plt.scatter(x, y, c=cores, s=tamanhos, alpha=0.6, cmap='viridis')
plt.colorbar(scatter, label='Valor de Cor')
plt.title('Gráfico de Dispersão com Cores e Tamanhos Variáveis')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.grid(True)
plt.show()

# 3. Histograma
# Exibe a distribuição de frequência de uma variável. Mostra como os dados estão distribuídos.
dados = np.random.normal(0, 1, 1000)
plt.figure(figsize=(10, 6))
plt.hist(dados, bins=30, alpha=0.7, color='skyblue', edgecolor='black')
plt.title('Histograma de uma Distribuição Normal')
plt.xlabel('Valor')
plt.ylabel('Frequência')
plt.grid(True)
plt.show()

# 4. Boxplot
# Mostra mediana, quartis e outliers de dados. Ótimo para comparar distribuições entre grupos.
dados1 = np.random.normal(0, 1, 100)
dados2 = np.random.normal(2, 1.5, 100)
dados3 = np.random.normal(-1, 2, 100)
plt.figure(figsize=(10, 6))
plt.boxplot([dados1, dados2, dados3], labels=['Grupo A', 'Grupo B', 'Grupo C'], patch_artist=True)
plt.title('Boxplot Comparativo entre Grupos')
plt.xlabel('Grupos')
plt.ylabel('Valores')
plt.grid(True)
plt.show()

# 5. Gráfico de Barras
# Compara valores entre categorias distintas. Muito usado em análises categóricas.
categorias = ['A', 'B', 'C', 'D', 'E']
valores = [25, 40, 30, 55, 15]
plt.figure(figsize=(10, 6))
plt.bar(categorias, valores, color='skyblue', edgecolor='navy')
plt.title('Gráfico de Barras por Categoria')
plt.xlabel('Categorias')
plt.ylabel('Valores')
plt.grid(True, axis='y')
plt.show()

# 6. Gráfico de Pizza
# Mostra proporções relativas entre categorias. Funciona bem com poucos grupos.
categorias = ['Categoria A', 'Categoria B', 'Categoria C', 'Categoria D', 'Outros']
valores = [35, 25, 20, 15, 5]
plt.figure(figsize=(8, 8))
plt.pie(valores, labels=categorias, autopct='%1.1f%%', startangle=90, shadow=True)
plt.title('Distribuição por Categorias')
plt.axis('equal')
plt.show()

# 7. Gráfico de Superfície 3D
# Representa relações entre três variáveis contínuas. Muito usado em matemática e ciência de dados.
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm)
fig.colorbar(surf)
ax.set_title('Superfície 3D')
plt.show()
