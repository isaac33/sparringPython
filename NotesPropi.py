#Crea un programa que l’usuari introdueixi la nota del primer parcial, la nota del segon parcial 
#i la nota de les pràctiques i el programa calculi la seva nota final i li respongui entre “Suspès”, “Aprovat”, “Notable” i “Excel·lent”. 
#La nota final es calcula tenint en compte que el 30% correspon al primer parcial, el 50% al segon i el 20% és de les pràctiques de classe.  
#S’ha de tenir en compte també que si l’alumne no arriba al 4 en la nota del segon parcial, directament és un “suspès”.
#La entrada de dades s’ha de fer en una sola línia separat per “,”.
# Si tenen mes de un 8 de mitjana se'ls hi activa el prompt per matricularse a la universitat

notes = input("Introdueix la nota del primer parcial, la del segon parlcial i la nota de practiques, en aquest ordre i separat per comes")
entrada=notes.split(',')
n1p=float(entrada[0])
n2p=float(entrada[1])
npr=float(entrada[2])

nmitj = n1p*0.3 + n2p*0.5 + npr*0.2

if ( n2p < 4):
    print ("Suspes")
elif ( nmitj == 5):
    print ("Aprovat")
elif ( nmitj >= 6.5 and nmitj <= 8.5):
    print ("Notable")
elif ( nmitj > 8.5):
    print ("Excelent")

while (nmitj >= 8):
    decisio = input (" Vols matricularte a la uni")
    if ( decisio == 'Si' or 'si'):
        print ('Benvingut a Hogwarts')
    else:
        print ('Tampoc et serviria de res')
        



    





