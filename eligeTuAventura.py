skills=input( "Introduce en este orden y separado por comas el valor de estos atributos: NOMBRE,VIDA, DEFENSA, ATAQUE")
entrada=skills.split(',')
nombre=entrada[0]
vida=int(entrada[1])
defensa=int(entrada[2])
ataque=int(entrada[3])

print ("Bienvenido",nombre,"el sino del guerrero te ha otorgado",vida,"golpes vitales,los dioses te han otorgado su favor por",defensa,"ocasiones, y tu españa daña",ataque,"veces.\n")

print ("Estas frente a un torreon con una puerta de obsidiana enorme, te separa de ella un puente de madera , sobre un rio del cual se desprende un olor y un color terrible. ¿Que haces?\n")
dec1=input ("A. Avanzas decidido a la puerta\nB.No te fias de la estabilidad del puente, confías en que cogiendo carrerilla y saltando puedas llegar al umbral de la puerta\nC.Rodeas el edificio")
if dec1 =='a':
    print("Fssshhhh! De pronto una flecha se te clava en el hombro\n")
    vida=vida-20
    print("Tienes",vida,"puntos de vida")
elif (vida > 0):
    print ("¡Has llegado por los pelos!No hay mucha seguridad, te apoyas y la puerta enseguida se abre\n")
    print ("Enseguida un hedor destroza tu olfato, un uruk-hay esta frente a ti, el combate es inevitable, desenvainas tu espada")
    dec2=input ("¿Qué haces? A. Golpeas a la cabeza B. Golpeas la mano con la que coje su arma C. Tomas una posicion de defensa")
    if dec2 == 'a':
        uruk=100
        uruk=100-(50*2)
        print("La vida del uruk es",uruk,"cae desplomado al suelo")
    elif dec2 == 'b':
        uruk=100
        uruk=100-25
        print("La vida del uruk es",uruk,"pero esta desarmado")
        dec21=input ("¿Qué haces? Tiene una gran potencia física, todavia tiene sus puños A. Golpeas a la cabeza B. Lo empujas y huyes hacia delante")
        if dec21== 'a':
            uruk=uruk-75
            print("La vida del uruk es",uruk,"cae desplomado al suelo")
        elif dec21== 'b':
            print("Consigues dejarlo atras. Llegas a otra puerta, oyes como uruk se levanta entre rugidos de rabia, busca su arma desesperado")
        else:
            print("Consigues dejarlo atras. Llegas a otra puerta, oyes como uruk se levanta entre rugidos de rabia, busca su arma desesperado")
    else:
        print ("Tomas una posicion de defensa\nUruk ataca y te golpea, al estar en posicion de defensa te roza con su arma")
        vida=vida-10
        print ("Tienes",vida,"puntos de vida")

        
elif dec1 =='b':
    print ("Efectivamente has llegado al umbral de la puerta, y el puente se ha desmoronado a tus espaldas, apenas tienes espacio para apoyar tus pies en un renglon de piedra")
else:
    print ("Oyes murmullos y movimiento del torreon y no ves nada, de pronto escuchas un ruido metálico y solo sientes dolor intenso de quemadura, han tirado sobre ti aceite hirviendo")
    vida=vida-60
    print("Tienes",vida,"puntos de vida")







