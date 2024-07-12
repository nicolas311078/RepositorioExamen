#prueba
import csv
import math
import random


trabajadores = [
    {"nombre": "Juan Pérez"},
    {"nombre": "María García"},
    {"nombre": "Carlos López"},
    {"nombre": "Ana Martínez"},
    {"nombre": "Pedro Rodríguez"},
    {"nombre": "Laura Hernández"},
    {"nombre": "Miguel Sánchez"},
    {"nombre": "Isabel Gómez"},
    {"nombre": "Francisco Díaz"},
    {"nombre": "Elena Fernández"}
]
sueldos=[]


def asignar_sueldos_aleatorios():
    global sueldos
    sueldos=[random.randint(300000,2500000) for _ in range(10)]
    print("Sueldos asignados aleatoriamente")

def clasificar_sueldos():
    print(" Clasificación de sueldos:")
    for trabajador, sueldo in zip(trabajadores, sueldos):
        print("Sueldo menores a $300.000", len([s for s in sueldos if s <=800000]))
        if sueldo<300000:
            print(f"Nombre Empleado:{trabajador['nombre']}  Sueldo:${sueldo}")
        print("Sueldo entre $800.000 y $2.0000.000", len([s for s in sueldos if 800000<=s <=2000000]))
        if 800000<=sueldo<=2000000 :
            print(f"Nombre Empleado:{trabajador['nombre']} |Sueldo:${sueldo}")
        print("Sueldos superiores a $2.000.000", len([s for s in sueldos if s>2000000]))
        if sueldo >2000000 :
            print(f"Nombre Empleado:{trabajador['nombre']}| Sueldo:${sueldo}")
    print("Total de sueldos", sum(sueldos))


def reporte_de_sueldos():
    with open('Reporte_de_sueldos.csv','w', newline='')as archivo:
        escribir= csv.writer(archivo)
        escribir.writerow(["Nombre empleado|", "|Sueldo Base|", "|Descuento Salud|", "|Descuento AFP|", "|Sueldo Líquido|"])
        for trabajador, sueldo in zip(trabajadores, sueldos):
            desc_salud= sueldo*0.07
            desc_afp=sueldo*0.12
            sueldo_liquido=sueldo-desc_afp-desc_salud
            escribir.writerow([trabajador["nombre"],sueldo,desc_salud,desc_afp,sueldo_liquido])
            print(f"|Nombre empleado:{trabajador['nombre']} |Sueldo base:${sueldo} |Descuento salud:${desc_salud} |Descuento AFP:${desc_afp}|")
    print("Reporte generado correctamente!")   
    
def  ver_estadisticas():
    sueldo_max= max(sueldos)
    sueldo_min=min(sueldos)
    sueldo_promedio= sum(sueldos)/ len(sueldos)
    sueldo_geom=math.exp(sum(math.log (sueldo)for sueldo in sueldos) /len(sueldos))
    print(f"EL sueldo maximo es:${sueldo_max} ")
    print(f"El sueldo mas bajo es:${sueldo_min}")
    print(f"El sueldo promedio es:${sueldo_promedio:.2f}")
    print(f"La media geometrica de sueldos es:{sueldo_geom:.2f}")
    
def main_menu():
    while True:
        print("Bienvenido al menú")
        print("1.- Asignar sueldos aleatorios")
        print("2.- Clasificar Sueldos") 
        print("3.- Ver estadisticas")
        print("4.- Reporte de sueldos")
        print("5.- Salir del programa")
        opc=int(input("Ingrese su respuesta\n>>>"))
        match opc:
            case 1:
                asignar_sueldos_aleatorios()
            case 2:
                clasificar_sueldos()
            case 3:
                ver_estadisticas()
            case 4:
                reporte_de_sueldos()
            case 5:
                print("Finalizando programa.......")
                print("Desarrollado por Nicolás Maureira")
                print("Rut 21.732.650-8")
                break
            case default:
                print("Error!")
                
                
main_menu()