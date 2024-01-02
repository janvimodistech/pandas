import seaborn as sns
import matplotlib.pyplot as plt
iris = sns.load_dataset("iris")
sns.pairplot(iris, vars=['sepal_length', 'sepal_width', 'petal_length', 'petal_width'], hue='species')

plt.show()
