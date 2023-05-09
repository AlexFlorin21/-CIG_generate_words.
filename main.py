def expand_and_filter(grammar, symbol, length, current_word, words):
    if len(current_word) > length:
        return

    if symbol not in grammar:
        if len(current_word) == length:
            words.add(current_word)
        return

    for production in grammar[symbol]:
        new_word = current_word
        for prod_symbol in production:
            expand_and_filter(grammar, prod_symbol, length, new_word, words)
            if prod_symbol not in grammar:
                new_word += prod_symbol
        # Daca productia contine lambda (ε), reprezentat de un string vid
        if not production:
            expand_and_filter(grammar, "", length, new_word, words)

def genereaza_cuvinte(grammar, start_symbol, n):
    words = set()
    expand_and_filter(grammar, start_symbol, n, "", words)
    return words

# Exemplu de gramatica independenta de context cu lambda (ε):
# S -> aA | bB | ε
# A -> a | aS | bAA
# B -> b | bS | aBB
grammar = {
    "S": ["aA", "bB", ""],
    "A": ["a", "aS", "bAA"],
    "B": ["b", "bS", "aBB"]
}

n = 4  # Lungimea data

result = genereaza_cuvinte(grammar, "S", n)
print(result)
