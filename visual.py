import matplotlib.pyplot as plt

def dict_to_graph(D):
    plt.bar(range(len(D)), list(D.values()), align='center', color = 'red', edgecolor = 'black')
    plt.xticks(range(len(D)), list(D.keys()))
    plt.show()


def mult_graph(D, F, G):
    fig = plt.figure()
    ax1 = fig.add_subplot()
    ax2 = fig.add_subplot()
    ax3 = fig.add_subplot()
    ax1.bar(range(len(D)), list(D.values()), align='center', color = 'red', edgecolor = 'black')
    ax2.bar(range(len(F)), list(F.values()), align='center', color = 'red', edgecolor = 'black')
    ax3.bar(range(len(G)), list(G.values()), align='center', color = 'red', edgecolor = 'black')
    ax1.xticks(range(len(D)), list(D.keys()))
    ax2.xticks(range(len(F)), list(F.keys()))
    ax3.xticks(range(len(G)), list(G.keys()))
    plt.show()