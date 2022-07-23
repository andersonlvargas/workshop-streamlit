import math # Ativa o módulo de funções matemáticas
""" Gera a sequência de Fibonacci até ultrapassar um limite
    que deve ser menor do que 1000, para alinhar os resultados
    e razão entre cada dois elementos """
# O limite deve ser maior ou igual a 2
Limite=int(input('Entre com o limite (>= 2): '))
N=2 # Número de ordem de cada elemento da sequência
FibA = 1
FibB = 1
# Imprime os títulos da tabela
print(' N      Fib(N)          Razão')
# Imprime os dois primeiros
print ('001     001')
print ('002     001     1.0')
while FibB < Limite:
  Aux = FibA + FibB # Cada novo elemento será a soma dos dois anteriores
  FibA=FibB # O segundo elemento torna-se o primeiro
  FibB=Aux  # O segundo elemento recebe a soma dos dois anteriores
  N=N+1     # Número de ordem do próximo elemento
  # Concatena 00 à esquerda se Fib(N) for menor do que 10
  #   e um 0 se for maior do que 9 e menor do que 100
  print('00'+str(N) if N<10 else '0'+str(N) if N<100 else N,
      '   ', '00'+str(FibB) if FibB<10 else
      '0'+str(FibB) if FibB<100 else FibB,'   ', FibB/FibA)
  print('Compare com a razão áurea:\n','            ',(1+math.sqrt(5))/2)

Dando-se 200 como entrada para N, o resultado que apareceu foi (o espaçamento foi ajustado para o tipo de caractere sendo usado aqui):

Entre com o limite (>= 2): 200
 N     Fib(N)         Razão
001     001
002     001     1.0
003     002     2.0
004     003     1.5
005     005     1.6666666666666667
006     008     1.6
007     013     1.625
008     021     1.6153846153846154
009     034     1.619047619047619
010     055     1.6176470588235294
011     089     1.6181818181818182
012     144     1.6179775280898876
013     233     1.6180555555555556
Compare com a razão áurea:
                1.618033988749895

2. Exemplo de função recursiva
Este exemplo tem dupla finalidade: 1. Exemplificar como se declara uma função recursiva, isto é, uma função que, em seu corpo, ativa ela própria. 2. Mostrar como funções recursivas podem ser usadas para implementar diretamente uma definição matemática indutiva.

""" Esta funççao recursiva implementa diretamente
    a definição indutiva da soma dos inteiros de 1 até N:
    a) A soma dos inteiros positivos até 1 é 1;
    b) a soma dos inteiros positivos de 1 até N é
       a soma de N com a soma dos inteiros positivos até N-1"""

def Soma1aN(N):
if N==1: return(1)
else: return (N+Soma1aN(N-1)) # note-se a ativação recursiva

# Uso da função
N=int(input('Entre com o valor de N: '))
print('A soma de 1 a', N, 'é', Soma1aN(N))

Resultados da execução:

Entre com o valor de N: 5
A soma de 1 a 5 é 15

Entre com o valor de N: 10
A soma de 1 a 10 é 55