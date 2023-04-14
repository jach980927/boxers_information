import matplotlib.pyplot as plt 

def generate_bar_chart(labels, values, name_boxer):
    #labels = ['a', 'b', 'c']
    #values = [100,200,80]

    fig,ax = plt.subplots()
    ax.bar(labels, values)
    plt.savefig(f'./imgs/ {name_boxer} record bar.png')
    plt.close()
def generate_pie_chart(labels, values, name_boxer):
    fig,ax = plt.subplots()
    ax.pie(values, labels = labels)
    ax.axis('equal')
    plt.savefig(f'./imgs/ {name_boxer} record pie.png')
    plt.close()


if __name__ == '__main__':
    labels = ['c', 'd', 'f']
    values = [300,500,800]

    #generate_bar_chart(labels, values)
    generate_pie_chart(labels,values)