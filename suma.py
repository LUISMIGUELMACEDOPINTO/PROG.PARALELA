n=10
A = []
for i in range(n):
    print("Se van ingresando", i, "valores de", n, "valores")
    print("Ingrese valores que desee..")
    valor = int(input("Valores: "))
    A.append(valor)

suma = sum(A)
print(suma)
