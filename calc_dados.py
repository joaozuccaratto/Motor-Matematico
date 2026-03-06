def euclidiana(v1, v2):
    validar_vetores(v1, v2)
    soma_quadrados = sum((a - b) ** 2 for a, b in zip(v1, v2))
    return soma_quadrados ** 0.5

def produto_escalar(v1, v2):
    validar_vetores(v1, v2)
    return sum(a * b for a, b in zip(v1, v2))
  
def mae(v1, v2):
    validar_vetores(v1, v2)
    return sum (abs(a  - b) for a, b in zip(v1, v2)) / len(v1)

def mse(v1, v2):
    validar_vetores(v1, v2)
    return sum((a - b) ** 2 for a, b in zip(v1, v2)) / len(v1)
