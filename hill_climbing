!sudo apt update
!sudo apt install libcairo2-dev ffmpeg texlive texlive-latex-extra texlive-fonts-extra texlive-latex-recommended texlive-science tipa libpango1.0-dev
!pip install manim
!pip install IPython --upgrade

import networkx as nx  # Biblioteka do tworzenia grafów
import matplotlib.pyplot as plt  # Biblioteka do tworzenia wizualizacji
import random  # Moduł do generowania liczb losowych

# Definiujemy funkcję celu - liczbę unikalnych kolorów
def funkcja_celu(colors):
    return len(set(colors.values()))  # Zwracamy liczbę unikalnych kolorów

# Definiujemy główną funkcję - algorytm wspinaczkowy
def hill_climbing(graph, pos, iterations=200):
    # Przydzielamy każdemu wierzchołkowi grafu unikalny kolor (numer od 0 do liczby wierzchołków)
    colors = {node: i for i, node in enumerate(graph.nodes)}

    # Obliczamy liczbę użytych kolorów na początku (tutaj na początku każdy wierzchołek ma inny kolor)
    previous_colors_count = funkcja_celu(colors) 

    # Wyświetlamy początkowy układ kolorów i liczbę kolorów
    print('Początkowy układ kolorów: ', colors)
    print('Początkowa liczba kolorów: ', previous_colors_count)

    # Powtarzamy proces dla zadanej liczby iteracji
    for iteration in range(iterations):
        # Wybieramy losowo wierzchołek
        node = random.choice(list(graph.nodes))

        # Sprawdzamy kolory sąsiadujących wierzchołków
        neighbor_colors = set(colors[neighbor] for neighbor in graph.neighbors(node))
        
        # Znajdujemy wszystkie dostępne kolory, których nie używają sąsiedzi
        available_colors = set(colors.values()) - neighbor_colors

        # Jeżeli są dostępne kolory, zmieniamy kolor wierzchołka
        if available_colors:
            colors[node] = random.choice(list(available_colors))

        # Obliczamy aktualną liczbę kolorów
        current_colors_count = funkcja_celu(colors)

        # Wyświetlaj wyniki dla pierwszych 10 iteracji, a potem co 10. iteracji
        if iteration < 10 or iteration % 10 == 0:
            print('Iteracja ', iteration, ', układ kolorów: ', colors)
            print('Liczba kolorów: ', current_colors_count)

        # Wyświetlaj wykres tylko gdy liczba kolorów się zmienia
        if current_colors_count != previous_colors_count:
            # Wizualizacja
            node_colors = [colors[node] for node in G.nodes]
            nx.draw(G, pos, with_labels=True, node_color=node_colors, cmap=plt.cm.jet)
            plt.show()

            # Zapisujemy aktualną liczbę kolorów jako poprzednią na potrzeby następnej iteracji
            previous_colors_count = current_colors_count
            
    # Zwracamy końcowy układ kolorów
    return colors

# Tworzymy graf
G = nx.Graph()
G.add_edges_from([
    ('A', 'B'), ('A', 'C'), ('B', 'C'), 
    ('B', 'D'), ('D', 'E'), ('D', 'F'), 
    ('E', 'F'), ('C', 'F'), ('C', 'G'), 
    ('G', 'H'), ('H', 'I'), ('I', 'J'), 
    ('J', 'K'), ('K', 'L'), ('L', 'A'),
    ('G', 'H'), ('A', 'I'), ('C', 'J')])

# Obliczanie pozycji wierzchołków dla wizualizacji
# Zwraca słownik, gdzie kluczem jest wierzchołek, a wartością jest pozycje wierzchołka w dwuwymiarowej przestrzeni.
pos = nx.spring_layout(G)

# Uruchamiamy algorytm na stworzonym grafie
final_colors = hill_climbing(G, pos)

# Rysujemy końcowy stan grafu
node_colors = [final_colors[node] for node in G.nodes]
nx.draw(G, pos, with_labels=True, node_color=node_colors, cmap=plt.cm.jet)
plt.show()
