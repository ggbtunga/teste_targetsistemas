n = int(input("Digite o número que desaja saber se pertence a sequencia de fibonacci: "))
n1=0
n2=1
n3=0
print(n)

while n3 < n:
    n3 = n1 + n2
    n1=n2
    n2=n3

if n3 == n:
    print("O número {} pertence a sequência de Fibonacci".format(n))
else:
    print("O número {} não pertence a sequência de Fibonacci".format(n))
    
