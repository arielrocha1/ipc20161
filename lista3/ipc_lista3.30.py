#professor jucimar junior
#Bruno de Oliveira freire - 1615310030
#Felipe Henrique Bastos Costa -1615310032
#Caio de OLiveira Martins-1615310031
#Samuel Silva de França- 1615310049
#Eduardo Maia Freire-1615310003
#lista de Repetição
cond = 1
x1 = 0
soma = 0
preco = float(input("Informe o preco do pao:\n"))

print("Preco do pao por unidade: R$ %.2f\nPanificadora Pao de ontem - Tabela de preco:"%preco)

while( cond <= 50 ):
    x1 += 1
    soma += preco
    print("%d - R$ %.2f"%(x1,soma))
    cond += 1