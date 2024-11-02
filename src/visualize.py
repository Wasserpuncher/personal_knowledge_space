import matplotlib.pyplot as plt
import networkx as nx
from database import Database

class Visualize:
    def __init__(self, db):
        self.db = db

    def display(self):
        G = nx.DiGraph()  # Ein gerichteter Graph für Eltern-Kind-Beziehungen
        notes = self.db.get_all_notes()
        
        for note in notes:
            G.add_node(note['id'], label=note['title'])
            if note['parent_id']:
                G.add_edge(note['parent_id'], note['id'])

        pos = nx.spring_layout(G)
        labels = nx.get_node_attributes(G, 'label')
        nx.draw(G, pos, labels=labels, with_labels=True, node_size=2000, node_color="skyblue", font_size=10)
        plt.show()
