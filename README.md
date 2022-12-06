# D2NGJO_Mesint

# Féléves feladat. A D2NGJO.py tartalmazza a feladat megoldását.
## Feladat leírás:

## Probléma
> - **VRP:** *A Vehicle Routing Problem (VRP), a Traveling Salesman Problem (TSP) általánosítása. Az ügynök helyett több „futár” megy egy bázisból a városokba.*
> - **Algoritmus: Szimulált hűtés:** *Ez az algoritmus az egyszerű szomszédsági keresésre épül, azzal a különbséggel, hogy a keresés során valamilyen valószínűségtől függ, hogy elfogadunk-e rosszabb eredményt.*

## Feladat részletes leírása
> - *A városok mindegyikében egy, és csakis egy futárnak kell járnia.*
> - *A bázis az egyetlen pont, amelyet több futár érinthet.*
> - *A legenerált feladatok legyenek perzisztensen tárolva (vagy seedhez kötéssel procedurálisan generálva).*

# Programszerkezet leírása
## main
> - *Program elindítása, seed, car, city, iteration beállítása*
> - *Manhattan távolságot megadjuk*

## create_car_routes
> - *autók kezdő koordinátáját beállítjuk*
> - *autók útvonalait is eltároljuk*
> - *városokat kiosztjuk az autókra*

## neighbor_search
> - *szomszédsági keresést alkalmazzuk (véletlenszerűen kiválasztunk 2-t és megcseréljük)*
> - *végig megyünk a távolságokon*
> - *összeadjuk az összes távolságot és megnézzük a legjobb távolsághoz eltárolt távolságértékhez képest*
> - *ha nem találunk jobbat akkor, megnézzük hogy 0-e a hőmérséklet vagy nem nulla*

## calculatecarlength
> - *végig megy az autók összes útvonalán és a végén hozzáadjuk az előző város és a mostani város távolságát.*
