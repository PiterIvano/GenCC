from faker import Faker
import os
os.system("clear")


faker = Faker()


print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
print("▒▒▒▒▒▒▒▒▄▄▄▄▄▄▄▄▒▒▒▒▒▒")
print("▒▒█▒▒▒▄██████████▄▒▒▒▒")
print("▒█▐▒▒▒████████████▒▒▒▒")
print("▒▌▐▒▒██▄▀██████▀▄██▒▒▒")
print("▐┼▐▒▒██▄▄▄▄██▄▄▄▄██▒▒▒")
print("▐┼▐▒▒██████████████▒▒▒")
print("▐▄▐████─▀▐▐▀█─█─▌▐██▄▒")
print("▒▒█████───PITER──▐███▌")
print("▒▒█▀▀██▄█─▄───▐─▄███▀▒")
print("▒▒█▒▒███████▄██████▒▒▒")
print("▒▒▒▒▒██████████████▒▒▒")
print("▒▒▒▒▒██████████████▒▒▒")
print("▒▒▒▒▒█████████▐▌██▌▒▒▒")
print("▒▒▒▒▒▐▀▐▒▌▀█▀▒▐▒█▒▒▒▒▒")
print("▒▒▒▒▒▒▒▒▒▒▒▐▒▒▒▒▌▒▒▒▒▒")
print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")


#colores 
r = "\033[0;31m"#red
v = "\033[0;32m"#verde
a = "\033[0;34m"#azul
y = "\033[0;33m"#yelow
x = "\033[0;0m"#cerrar color
while True:
    print(f"{y}[{r}*{y}]{a}1-> Generar CC")
    print(f"{y}[{r}*{y}]{a}2-> Generar direccion y nombre")
    print(f"{y}[{r}*{y}]{a}3-> Empresa")
    option = int(input(f"{a}Elija su opcion-> "))


    if option == 1:
        
        print(f"{v}[*] Ingrese la cantidad de tarjetas que desea{x}")
        sea = int(input(f"{a}Numero de tarjetas-> {x}"))
        i = 1
        while i <= sea:
            i += 1
            print(f'{y}[*] Tarjeta Numero {i}{x}:\n{v}{faker.credit_card_full (card_type = None)}')
        input("Presione una letra para salir")
    elif option == 2:
        faker = faker.name()
        print(f"{y}[*] Nombre :{v} {faker} ")
        #faker1 = faker.address()
        #print(f'{y}[*]{v} Direccion : {faker1} \n')
    print("____________________________________________")
