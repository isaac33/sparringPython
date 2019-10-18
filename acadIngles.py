fecha=input("Introduce una fecha con el dia escrito/ numero de dia del mes /mes del actual año\n")
entrada=fecha.split('/')
diaSemana=str(entrada[0])
diaMes=int(entrada[1])
mes=int(entrada[2])
print(fecha)
numApr=0
numAlu=20
diaSemana=diaSemana.lower()

if diaMes > 31 or mes > 12:
    print ("Fecha incorrecta")
else:
    
    if diaSemana == "lunes" or diaSemana == "martes" or diaSemana == "miercoles" :
        print ("Dia de examen")
        numApr=int(input("¿Cuantos alumnos han aprobado?"))
        if numApr <= 20:
            print ("Han aprovado", numApr, "chavalxs")
        else:
            print ("Revisa el numero de notas por alumno, es incorrecto")

    elif diaSemana == "jueves":
        asClase=int(input("¿Cuanta gente ha venido a clase?"))
        if numAlu > asClase:
            print ("Han venido",asClase,"chavalxs")
        else:
            print ("Han venido mas chavales de los matriculados, algo ha pasado")
    elif diaSemana == "viernes" and ( diaMes ==1 and mes==7):
        print ("Empieza nuevo ciclo,cada matriculacion vale 100 chelines")
        nuevoAlumn=int(input("Cuantos alumnos se han matriculado"))
        ingresoTotal= nuevoAlumn*100
        print("El centro se ha ingresado",ingresoTotal,"chelines")
    else:
        print ("Revisa los datos, hay algun error")





    

