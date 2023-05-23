from typing import Dict, List, Union

# Gramatica este reprezentată ca un dicționar unde cheile sunt neterminale și
# valorile sunt liste de producții pentru acel neterminal.
# Producțiile sunt reprezentate ca liste de simboluri (terminale și neterminale).

Gramatica = Dict[str, List[List[Union[str, None]]]]
Productii = List[Union[str, None]]

def genereaza_cuvinte(gramatica: Gramatica, start: str, lungime: int) -> List[str]:
    # Începe cu simbolul de start
    in_asteptare = [(list(start), [])]

    cuvinte = []

    while in_asteptare:
        # Scoate o derivare și cuvântul său curent din fața listei
        derivare, cuvant = in_asteptare.pop(0)

        # Dacă derivarea este goală și cuvântul are lungimea dorită,
        # atunci am găsit un cuvânt
        if not derivare and len(cuvant) == lungime:
            cuvinte.append(''.join(cuvant))
            continue

        # Dacă derivarea este goală sau cuvântul este prea lung,
        # atunci această derivare poate fi eliminată
        if not derivare or len(cuvant) > lungime:
            continue

        # Ia primul simbol din derivare
        simbol = derivare[0]
        rest = derivare[1:]

        # Dacă simbolul este un neterminal, adaugă noi derivate
        # pentru fiecare producție a acestui neterminal
        if simbol in gramatica:
            for productie in gramatica[simbol]:
                in_asteptare.append((productie + rest, cuvant))

        # Dacă simbolul este un terminal, adaugă-l la cuvânt
        else:
            in_asteptare.append((rest, cuvant + [simbol]))

    return cuvinte


# Exemplu de utilizare:
gramatica = {
    'S': [['A', 'B'], ['B', 'A']],
    'A': [['a'], ['a', 'A']],
    'B': [['b'], ['b', 'B']],
}

print(genereaza_cuvinte(gramatica, 'S', 4))
