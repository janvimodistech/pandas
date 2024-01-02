import matplotlib.pyplot as plt

def generate_pie_chart(categories, values):
    plt.figure(figsize=(8, 8))
    plt.pie(values, labels=categories, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')    
    plt.show()
categories = ['Category A', 'Category B', 'Category C', 'Category D']
values = [25, 35, 20, 20]

generate_pie_chart(categories, values)
