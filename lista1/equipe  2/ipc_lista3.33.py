#professor jucimar junior
#Bruno de Oliveira freire - 1615310030
#Felipe Henrique Bastos Costa -1615310032
#Caio de OLiveira Martins-1615310031
#Samuel Silva de França- 1615310049
#Eduardo Maia Freire-1615310003
#lista de Repetição
cont = 1
soma = 0
cond = True
maior = 0
menor = 99999999999999999999999999999999999999999999999999999999999
while(cond):
    val = int(input("Digite 1 para continuar o programa e 0 para pará-lo:\n"))
    if( val == 1):
        temp = float(input("Informe a temperatura, em ºC:\n"))
        soma += temp
        if( temp > maior ):
            maior = temp
            cont += 1
        if( temp < menor ):
            menor = temp
            cont += 1
    else:
        cond = False
        
media = soma / cont
print("A media das temperaturas informadas e de %.2fºC\nA maior temperatura foi de %.2fºC\nA menor foi %.2fºC"%(media,maior,menor))    
