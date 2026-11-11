# Exemple 25 — Piège n°2 : un test vide
# Erreur attendue : ZeroDivisionError: division by zero

def mse(vrais, predits):
    total = 0
    for v, p in zip(vrais, predits):
        total += (v - p) ** 2
    return total / len(vrais)

test_vrais = []
test_predits = []
print(mse(test_vrais, test_predits))
