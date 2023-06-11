# MHE2023

Opis problemu
Problem kolorowania grafu, znany również jako problem malowania wierzchołków, jest jednym z fundamentalnych problemów w teorii grafów. Polega on na przypisaniu kolorów do wierzchołków grafu w taki sposób, aby żadne dwa sąsiadujące wierzchołki nie miały tego samego koloru. Celem jest znalezienie najmniejszej liczby kolorów, która jest wystarczająca do pokolorowania wszystkich wierzchołków zgodnie z tym warunkiem.

Rozwiązanie problemu kolorowania grafu można znaleźć za pomocą różnych algorytmów. Należy jednak zauważyć, że problem kolorowania grafu jest NP-trudny, co oznacza, że nie istnieje znany skuteczny algorytm rozwiązujący ten problem w czasie wielomianowym dla dowolnego grafu. Dlatego w praktyce często stosuje się heurystyki lub aproksymacyjne algorytmy, które znajdują rozwiązania zbliżone do optymalnych, ale niekoniecznie optymalne

Zastosowanie rozwiązań
Problem kolorowania grafu ma praktyczne zastosowanie w wielu obszarach, gdzie konieczne jest przypisanie ograniczeń lub zasobów do elementów grafu w sposób zgodny z pewnymi regułami. Oto kilka przykładów:

Harmonogramowanie zadań: Graf może reprezentować zadania, a krawędzie między nimi oznaczają zależności lub ograniczenia czasowe. Kolorowanie grafu pozwala przypisać zadaniom różne sloty czasowe lub zasoby, takie jak pracownicy lub maszyny, tak aby żadne dwa zadania zależne od siebie nie były przypisane do tego samego slotu.

Projektowanie układów drukowanych: W przypadku projektowania układów drukowanych, graf może reprezentować komponenty elektroniczne, a krawędzie odzwierciedlają połączenia między nimi. Kolorowanie grafu jest stosowane do przypisywania ścieżek połączeń do różnych warstw ścieżek, tak aby nie doszło do konfliktów między połączeniami.

Alokcja zasobów sieciowych: W przypadku zarządzania sieciami komputerowymi lub telekomunikacyjnymi, graf może reprezentować węzły lub urządzenia, a krawędzie reprezentują połączenia między nimi. Kolorowanie grafu może być wykorzystane do przypisywania różnych zasobów, takich jak pasma szerokiego lub kanały transmisyjne, do poszczególnych węzłów, aby uniknąć konfliktów i zapewnić optymalne wykorzystanie zasobów sieciowych.

Harmonizacja harmonogramów egzaminów: W przypadku planowania egzaminów, graf może reprezentować różne egzaminy, a krawędzie oznaczają ograniczenia czasowe między nimi, takie jak konflikty harmonogramowe dla tych samych studentów. Kolorowanie grafu pozwala na przypisanie różnych slotów czasowych dla egzaminów, aby uniknąć konfliktów harmonogramowych dla studentów, którzy muszą zdawać kilka egzaminów.

Implementacja
Zarówno algorytm wspinaczkowy (hill climbing) jak i algorytm symulowanego wyżarzania (simulated annealing) mogą być zastosowane do rozwiązywania problemu kolorowania grafu.

Algorytm wspinaczkowy w problemie kolorowania grafu działa na zasadzie iteracyjnej optymalizacji. Na początku każdemu wierzchołkowi przypisywany jest unikalny kolor. Następnie, w serii iteracji, losowo wybierany jest wierzchołek, dla którego następuje próba zmiany koloru na jeden z kolorów nie używanych przez jego sąsiadów. Jeśli taki kolor istnieje, kolor wierzchołka jest zmieniany. W każdej iteracji obliczana jest liczba używanych kolorów. Algorytm kontynuuje ten proces przez określoną liczbę iteracji, starając się zmniejszyć ogólną liczbę używanych kolorów. W efekcie, algorytm wspinaczkowy dąży do znalezienia rozwiązania, w którym liczba używanych kolorów jest jak najmniejsza, a żadne dwa sąsiadujące wierzchołki nie mają tego samego koloru.

Algorytm symulowanego wyżarzania jest bardziej zaawansowanym algorytmem metaheurystycznym, który symuluje proces wyżarzania metalu. Polega na losowych zmianach rozwiązania w czasie, akceptując czasem gorsze rozwiązania, aby uniknąć utknięcia w lokalnym minimum. Algorytm symulowanego wyżarzania ma większe szanse na znalezienie optymalnego rozwiązania w porównaniu do algorytmu wspinaczkowego, ponieważ ma mechanizm, który pozwala na czasowe odrzucenie gorszych rozwiązań i eksplorację przestrzeni poszukiwań.

Algorytm wspinaczkowy (hill climbing) jest algorytmem heurystycznym, który polega na podejmowaniu kroków, które prowadzą do coraz lepszych rozwiązań. Jednak jest on podatny na wpadanie w lokalne minima, tzn. sytuacje, w których każdy pojedynczy ruch prowadzi do gorszego rozwiązania, choć istnieje lepsze rozwiązanie dostępne przez szersze poszukiwanie.

Algorytm ten nie jest zbyt efektywny dla problemów, które mają wiele lokalnych minimów, takich jak problem kolorowania grafu. Algorytm ten jest "krótkowzroczny" i nie jest w stanie "przekroczyć" lokalnych minimów w poszukiwaniu globalnego minimum.

W przypadku problemu kolorowania grafu, algorytm wspinaczkowy może "utknąć" w sytuacji, w której każde pojedyncze przemalowanie wierzchołka na inny kolor prowadzi do konfliktu z sąsiednim wierzchołkiem. W takim przypadku, algorytm nie jest w stanie zobaczyć, że przemalowanie dwóch (lub więcej) wierzchołków naraz mogłoby prowadzić do lepszego rozwiązania.
