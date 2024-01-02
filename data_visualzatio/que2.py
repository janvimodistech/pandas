import seaborn as sns
import matplotlib.pyplot as plt
categories = ['Category A', 'Category B', 'Category C', 'Category D']
values = [23, 45, 56, 78]
sns.barplot(x=categories, y=values)
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Plot Example')
plt.show()
