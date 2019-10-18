#Un treballador vols saber el seu salari mensual, el qual s’obté de la següent manera:
#Si el treballador treballa menys de 40 hores setmanals, se li paga 10€/hora
#Si el treballador treballa 40 o més hores setmanals, se li paga 10€/hora les 40 primeres i 15€/h les següents.
#El treballador, a més vol saber quina quantitat d’IRPF ha de pagar al mes, suposant que cada mes cobra el mateix i tenint en compte que:	
#si el treballador té més de 30 anys i el seu salari brut anual és superior a 20000 (14 pagues) se li aplica un 18%. 
#si el treballador té més de 50 anys, s’aplica un IRPF de 15%.
#Per la resta, apliqueu un IRPF els 20%
 
#El programa demana el nom del treballador, l'edat, i les hores que fa setmanals i el programa mostra una frase del tipus:
#“Joan té un salari mensual de …  euros al mes i paga un irpf de … euros”

dades= input ("Nom, edat i hores en aquest ordre separat per comes")
entrada=dades.split(',')
nom=entrada[0]
edat=float(entrada[1])
hores=float(entrada[2])

if 40 > hores:
    sueldo = hores*10
    print ("tu sueldo es", "%d" % (sueldo))
else:
    hores = hores - 40 #para saber las horas de mas que se hacen se les resta las 40 estandard que se cobran a 10. 49-40= 9 -> 9*15
    sueldo = (hores * 15) + 400 # siempre van a haber 40 que son a 10 € por hora -> 400€ mas las las 9 horas de mas, que se pagan a 15 (hores*15)
    print ("tu sueldo es", "%d" % (sueldo))

sueldo_mes = sueldo * 4
sueldo_anio = sueldo_mes * 14

if edat > 30 and sueldo_anio > 20000:
    irpf= sueldo_anio*0.18
elif edat > 50 :
    irpf= sueldo_anio*0.15
else:
    irpf= sueldo_anio*0.20

print (nom, "te un salari mensual de ", sueldo_mes, "mensuals i paga un irpf de" ,irpf )