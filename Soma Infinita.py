cont=0
soma=0
while True:
    print("\nDigite 'exit' para dar o Resultado !")
    num=input('Digite um valor para Somar : ')
    if num.lower() == 'exit':
        break
    num=int(num)
    cont += 1
    soma += num
print(f'\n\nA soma dos {cont} valores foi : {soma}  \n\n')




