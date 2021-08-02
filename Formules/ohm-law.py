# loi d'ohm 'U = RI' 

print('Calcul de la loi d\'ohm. Entrez une valeur, si vous ne connaissez pas la valeur indiquez simplement 0')


U = float(input('Entrez une valeur de tension U : ') or 0)
I = float(input('Entrez une valeur d intensité I : ') or 0)
R = float(input('Entrez une valeur de résistance R : ') or 0)

if not U:
    U = R * I
elif not I:
    I = U / R
elif not R:
    R = U / I
else:
    print('Il manque ue valeur pour calculer la loi d\'ohm')

print('U =', U, '[V]')
print('I =', I, '[A]')
print('R =', R, '[Ω]')

--------------------------------------------------------------------
#Autre solution

while (1):
    print("1. Calculer Voltage")
    print("2. Calculer Resistance")
    print("3. Calculer Intensite")
    print("4. Sortir du programme")
    ask = input("> ")
    if (ask == "1"):
        print("-- Calcul du voltage --")
        i = float(input("Intensite: "))
        r = float(input("Resistance: "))
        v = i * r
        print("Voltage = ", format(v, ".2f"))

    elif(ask == "2"):
        print("-- Calcul de la  resistance --")
        v = float(input("Voltage: "))
        i = float(input("Intensite: "))
        r = v / i
        print("Resistance = ", format(r, ".2f"))

    elif(ask == "3"):
        print("-- Calcul de l'intensite --")
        v = float(input("Voltage: "))
        r = float(input("Resistence: "))
        i = v / r
        print("Intensite= ", format(i, ".2f"))

    elif(ask == "4"):
        break
    else:
        print("FIN")
