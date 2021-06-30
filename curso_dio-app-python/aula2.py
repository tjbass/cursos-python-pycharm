# a = 10
# b = 5
# soma = a+b
# print (soma)

a = int(input("digite o primeiro número: "))
b = int(input("digite o segundo número: "))

resto_a = a % 2
resto_b = b % 2

if resto_a == 0 or resto_b == 0:
    print("Foi digitado um número par.")
else:
    print("não foi digitado um número par.")
