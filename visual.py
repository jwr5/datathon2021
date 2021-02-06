import matplotlib.pyplot as plt

def dict_to_graph(D):
    plt.bar(range(len(D)), list(D.values()), align='center', color = 'red', edgecolor = 'black')
    plt.xticks(range(len(D)), list(D.keys()))
    plt.show()
