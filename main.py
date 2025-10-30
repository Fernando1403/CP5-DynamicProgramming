from typing import List

# ---------------------------
# 1️-  Função iterativa (estratégia gulosa)
# ---------------------------
def qtdeMoedas(M: int, moedas: List[int]) -> int:
    """
    Usa a maior moeda possível até formar M.
    Args: M (int), moedas (List[int]).
    Return: int (mínimo de moedas) ou -1 se impossível.
    Complexidade: O(n log n) tempo (ordenar), espaço O(1) extra.
    """
    moedas.sort(reverse=True)
    total = 0
    for moeda in moedas:
        if M == 0:
            break
        qtd = M // moeda
        total += qtd
        M -= qtd * moeda
    return total if M == 0 else -1


# ---------------------------
# 2️- Função recursiva pura (sem memoização)
# ---------------------------
def qtdeMoedasRec(M: int, moedas: List[int]) -> int:
    """
    Tenta todas as combinações possíveis recursivamente.
    Args: M (int), moedas (List[int]).
    Return: int (mínimo de moedas) ou -1 se impossível.
    Complexidade: Exponencial no tempo no pior caso; espaço O(M) pilha.
    """
    if M == 0:
        return 0
    if M < 0:
        return float('inf')

    menor = float('inf')
    for moeda in moedas:
        res = qtdeMoedasRec(M - moeda, moedas)
        menor = min(menor, 1 + res)

    return menor if menor != float('inf') else -1


# ---------------------------
# 3️- Função recursiva (com memoização) (Top down)
# ---------------------------
def qtdeMoedasRecMemo(M: int, moedas: List[int], memo=None) -> int:
    """
    Recursiva com cache para evitar recalcular subproblemas.
    Args: M (int), moedas (List[int]), memo (dict) opcional.
    Return: int (mínimo de moedas) ou -1 se impossível.
    Complexidade: O(M * n) tempo, O(M) espaço para memo e recursão.
    """
    if memo is None:
        memo = {}
    if M in memo:
        return memo[M]
    if M == 0:
        return 0
    if M < 0:
        return float('inf')

    menor = float('inf')
    for moeda in moedas:
        res = qtdeMoedasRecMemo(M - moeda, moedas, memo)
        menor = min(menor, 1 + res)

    memo[M] = menor
    return menor if menor != float('inf') else -1


# ---------------------------
# 4️- Função usando Programação Dinâmica (Bottom up)
# ---------------------------
def qtdeMoedasPD(M: int, moedas: List[int]) -> int:
    """
    Constrói tabela dp onde dp[i] = mínimo de moedas para i.
    Args: M (int), moedas (List[int]).
    Return: int (mínimo de moedas) ou -1 se impossível.
    Complexidade: O(M * n) tempo, O(M) espaço.
    """
    dp = [float('inf')] * (M + 1)
    dp[0] = 0

    for i in range(1, M + 1):
        for moeda in moedas:
            if moeda <= i:
                dp[i] = min(dp[i], 1 + dp[i - moeda])

    return dp[M] if dp[M] != float('inf') else -1


# ---------------------------
# TESTES
# ---------------------------
print("Teste com M=6 e moedas=[1,3,4]\n")

print("Gulosa:", qtdeMoedas(6, [1, 3, 4]))
print("Recursiva:", qtdeMoedasRec(6, [1, 3, 4]))
print("Recursiva com Memoização:", qtdeMoedasRecMemo(6, [1, 3, 4]))
print("Programação Dinâmica (Bottom-Up):", qtdeMoedasPD(6, [1, 3, 4]))