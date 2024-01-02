import matplotlib.pyplot as plt

def create_boxplot(data, labels, title):
    plt.boxplot(data, labels=labels)
    plt.title(title)
    plt.xlabel('Groups')
    plt.ylabel('Values')
    plt.show()
group1 = [10, 20, 30, 40, 50]
group2 = [15, 25, 35, 45, 55]
group3 = [12, 22, 32, 42, 52]
data = [group1, group2, group3]
labels = ['Group 1', 'Group 2', 'Group 3']
title = 'Comparison of Data Distribution Across Groups'

create_boxplot(data, labels, title)
