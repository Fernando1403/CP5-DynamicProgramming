# Desafio: Troca de Moedas — Checkpoint 05

-  Fernando Gonzales Alexandre - RM: 555045 
-  Lucas Dias - RM: 555450 
-  Vitor Teixeira - RM: 555012 

---

## 1. Introdução e Contextualização

**Problema:** Dado um conjunto de moedas (valores inteiros positivos, quantidade ilimitada) e um montante `M`, determinar a **menor quantidade de moedas** cuja soma seja exatamente `M`.

**Objetivo:** Minimizar o número de moedas usadas.

**Premissas:** moedas ilimitadas; valores inteiros positivos; se não for possível formar `M`, a função retorna `-1`.

**Natureza:** Problema de otimização combinatória — buscar a melhor solução entre muitas combinações possíveis.

---

## 2. Programação Dinâmica (PD) — Conceito Rápido

**PD** é uma técnica que resolve problemas decompondo-os em subproblemas menores e reutilizando soluções de subproblemas sobrepostos.

- **Subestrutura ótima:** a solução ótima para `M` pode ser construída a partir das soluções ótimas para valores menores.
- **Subproblemas sobrepostos:** vários caminhos da recursão resolvem os mesmos subproblemas; memoização/DP evita recomputações.

---

## 3. Abordagens Implementadas

As quatro funções estão no arquivo `main.py`:

1. `qtdeMoedas(M, moedas)` — **Gulosa (iterativa)**
   - Conceito: escolhe sempre a maior moeda possível.
   - Limitação: **não garante** solução ótima para todas as moedas (ex.: `M=6, moedas=[1,3,4]` => gulosa dá 3, ótimo é 2).
   - Complexidade: `O(n log n)` pelo sort, depois `O(n)` passagem.

2. `qtdeMoedasRec(M, moedas)` — **Recursiva pura**
   - Conceito: tenta todas as combinações recursivamente.
   - Performance: árvore de recursão com muitos reprocessamentos; tempo exponencial.
   - Complexidade: Exponencial no pior caso.

3. `qtdeMoedasRecMemo(M, moedas)` — **Recursiva com memoização (Top-Down)**
   - Conceito: mesma recursão, mas armazena resultados em `memo` para evitar recalcular.
   - Ligação com PD: é PD Top-Down (memoização).
   - Complexidade: `O(M * n)` tempo, `O(M)` espaço.

4. `qtdeMoedasPD(M, moedas)` — **Programação Dinâmica (Bottom-Up)**
   - Conceito: constrói vetor `dp[0..M]` com `dp[i] =` mínimo de moedas para `i`.
   - Fluxo: para cada `i` calcula `dp[i]` a partir de `dp[i - moeda]`.
   - Vantagem: evita overhead de chamadas recursivas; também `O(M * n)` tempo.

---

## 4. Demonstração / Exemplos

Exemplo simples usado no código:
```py
qtdeMoedas(6, [1,3,4])         # Gulosa -> 3 (4+1+1) [não ótima]
qtdeMoedasRec(6, [1,3,4])      # -> 2 (3+3)
qtdeMoedasRecMemo(6, [1,3,4])  # -> 2
qtdeMoedasPD(6, [1,3,4])       # -> 2
