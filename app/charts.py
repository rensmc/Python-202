import matplotlib.pyplot as plt

def generate_bar_chart(): # Static values
    labels = ['a', 'b', 'c']
    values = [100, 200, 80]

    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.show() 

def generate_bar_chart2(labels, values): # Dynamic values
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.show() 

def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal')
    plt.show

if __name__ == '__main__':
    labels = ['a', 'b', 'c']
    values = [100, 200, 400]
    generate_bar_chart2(labels, values)
    #generate_pie_chart(labels, values)