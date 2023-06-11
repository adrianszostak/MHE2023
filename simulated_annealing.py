import networkx as nx  # Biblioteka do tworzenia grafów
import matplotlib.pyplot as plt  # Biblioteka do tworzenia wizualizacji
import random  # Moduł do generowania liczb losowych
import math # Moduł do działań matematycznych

# Ta funkcja oblicza cel naszego algorytmu, którym jest minimalizacja liczby użytych kolorów.
def objective_function(colors):
    # Zwracamy liczbę unikalnych kolorów użytych do pokolorowania grafu
    return len(set(colors.values()))

# Główna funkcja realizująca algorytm symulowanego wyżarzania
def simulated_annealing(graph, pos, iterations=200, T=1.0, T_min=0.0001, alpha=0.9):
    # Przydzielamy każdemu wierzchołkowi grafu unikalny kolor (numer od 0 do liczby wierzchołków)
    colors = {node: i for i, node in enumerate(graph.nodes)}
    
    # Obliczamy liczbę użytych kolorów na początku (tutaj na początku każdy wierzchołek ma inny kolor)
    previous_colors_count = objective_function(colors)
    
    # Rysujemy początkowy stan grafu, gdzie każdy wierzchołek ma inny kolor
    node_colors = [colors[node] for node in graph.nodes]
    nx.draw(graph, pos, with_labels=True, node_color=node_colors, cmap=plt.cm.jet)
    plt.show()
    
    # Wyświetlamy na ekranie początkowy układ kolorów i liczbę użytych kolorów
    print("Początkowy układ kolorów:", colors)
    print("Ilość użytych kolorów:", previous_colors_count)
    
    # Inicjalizujemy licznik iteracji
    iteration = 0

    # Główna pętla algorytmu, która trwa tak długo, jak temperatura jest większa od minimalnej temperatury
    while T > T_min:
        # Wykonujemy określoną liczbę iteracji przy stałej temperaturze
        for _ in range(iterations):
            # Losowo wybieramy jeden z wierzchołków grafu
            node = random.choice(list(graph.nodes))
            
            # Sprawdzamy, jakie kolory są już używane przez sąsiadów wybranego wierzchołka
            neighbor_colors = {colors[neighbor] for neighbor in graph.neighbors(node)}
            # Z listy wszystkich kolorów wykluczamy te, które są już używane przez sąsiadów
            available_colors = set(colors.values()) - neighbor_colors
            
            # Jeśli są dostępne kolory, które nie są używane przez sąsiadów to losowo wybieramy jeden z nich
            if available_colors:
                new_color = random.choice(list(available_colors))
                # Zpamiętujemy stary kolor wierzchołka
                old_color = colors[node]

                # Obliczamy różnicę między starym a nowym kolorem. 
                # Ta różnica to 0 jeśli kolor się nie zmienił i 1 jeśli kolor się zmienił
                delta = (old_color != new_color)

                # Akceptujemy nowe rozwiązanie z pewnym prawdopodobieństwem, które zależy od różnicy między starym a nowym kolorem oraz od temperatury.
                # Im większa różnica i niższa temperatura, tym mniejsze prawdopodobieństwo akceptacji nowego rozwiązania.
                if delta < 0 or random.random() < math.exp(-delta / T):
                    colors[node] = new_color

            # Zwiększamy licznik iteracji
            iteration += 1

            # Obliczamy liczbę kolorów w aktualnym rozwiązaniu
            current_colors_count = objective_function(colors)

            # Jeżeli liczba kolorów się zmniejszyła, to rysujemy graf i wyświetlamy na ekranie układ kolorów
            if current_colors_count < previous_colors_count:
                previous_colors_count = current_colors_count
                node_colors = [colors[node] for node in graph.nodes]
                nx.draw(graph, pos, with_labels=True, node_color=node_colors, cmap=plt.cm.jet)
                plt.show()
                
                print("Iteracja:", iteration)
                print("Aktualny układ kolorów:", colors)
                print("Ilość użytych kolorów:", current_colors_count)
        
        # Po wykonaniu określonej liczby iteracji obniżamy temperaturę, co zmniejsza prawdopodobieństwo akceptacji nowego rozwiązania, które jest gorsze od starego
        T = T * alpha

    # Na koniec zwracamy słownik kolorów, który udało się znaleźć
    return colors

# Tworzymy graf
G = nx.Graph()
G.add_edges_from([
    ('A', 'B'), ('A', 'C'), ('B', 'C'), 
    ('B', 'D'), ('D', 'E'), ('D', 'F'), 
    ('E', 'F'), ('C', 'F'), ('C', 'G'), 
    ('G', 'H'), ('H', 'I'), ('I', 'J'), 
    ('J', 'K'), ('K', 'L'), ('L', 'A'),
    ('G', 'H'), ('A', 'I'), ('C', 'J')
])
pos = nx.spring_layout(G) #zwraca słownik, gdzie kluczem jest wierzchołek, a wartością jest pozycje wierzchołka w dwuwymiarowej przestrzeni.

# Uruchamiamy algorytm na stworzonym grafie
colors = simulated_annealing(G, pos)

# Rysujemy końcowy stan grafu
node_colors = [colors[node] for node in G.nodes]
nx.draw(G, pos, with_labels=True, node_color=node_colors, cmap=plt.cm.jet)
plt.show()

# Wyświetlamy na ekranie końcowy układ kolorów
print("Końcowy układ kolorów:", colors)
