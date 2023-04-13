numero = int(input("Digite o número que desejar: "))

fibo_prev = 0
fibo_atual = 1

while fibo_atual < numero:
    fibo_prox = fibo_prev + fibo_atual
    fibo_prev = fibo_atual
    fibo_atual = fibo_prox

if fibo_atual == numero:
    print(f"O numero {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O numero {numero} não pertence à sequência de Fibonacci.")