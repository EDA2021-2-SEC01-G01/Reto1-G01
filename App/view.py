"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""
def initCatalog():
    return controller.initCatalog()
    
def loadData(catalog):
    artistas = input('Ingresa el nombre del archivo de artistas: (Por defecto es el archivo de artistas pequeño)')
    obras = input('Ingresa el nombre del archivo de obras: (Por defecto es el archivo de obras pequeño)')

    if artistas == '':
        artistas = 'Artists-utf8-small.csv'

    if obras == '':
        obras = 'Artworks-utf8-small.csv'

    return controller.loadData(catalog, artistas, obras) 

def listArtist(catalog):
    ainicio = int(input("Ingrese el año inicial: "))
    afinal = int(input("Ingrese el año final: "))

    rank_artist = (controller.listArtist(catalog,ainicio,afinal))
    print("Hay "+ str(lt.size(rank_artist))+" artistas nacidos entre "+ str(ainicio)+" y "+str(afinal)+".")
    print("Los primeros 3 y los ultimos 3 son: ")
    for artist in rank_artist["elements"][:3]:
        print("Nombre: "+ artist["DisplayName"] +"\t"+ "Fecha de nacimiento: " +str(artist["BeginDate"])+"\t"+ "Fecha de fallecimiento: "
        + str(artist["EndDate"]) +"\t"+ "Nacionalidad: " +artist["Nationality"] +"\t"+ "Genero: " + artist["Gender"])
    for artist in rank_artist["elements"][-3:]:
        print("Nombre: "+ artist["DisplayName"] +"\t"+ "Fecha de nacimiento: " +str(artist["BeginDate"])+"\t"+ "Fecha de fallecimiento: "
        + str(artist["EndDate"]) +"\t"+ "Nacionalidad: " +artist["Nationality"] +"\t"+ "Genero: " + artist["Gender"])

# Requerimiento 2

#Requerimiento 3

#Requerimiento 4

def clasificarPorNacionalidad(catalog):
    naciones = controller.nacionalidadObras(catalog)
    print('El top 10 naciones en el MoMA es:\n')
    print('Nacionalidad\t|\tObras')
    print('-----------------------------------\n')
    for nacion in naciones:
        print(nacion['nacionalidad'], '\t', '|', '\t', nacion['tamano'], '\n')
        print('-----------------------------------\n')

#Requerimiento 5

def transportarObras(catalog):
    departamento = input('Ingrese el departamento a transportar: ')
    info = controller.transportarObras(catalog, departamento)
    print('La cantidad de obras transportadas fue:', info['cantidad'])
    print('El peso aproximado que fue transportado es:', info['pesoObras'], '(Kg)')
    print('El costo aproimado del servicio fue:', info['costoServicio'])
    print('Las 5 obras más costosas de transportar son: \n')

    print('ObjectID','\t|\t', 'Title','\t|\t', 'ConstituentID','\t|\t', 'Medium','\t|\t', 'Date','\t|\t', 'Dimensions','\t|\t', 'Classification','\t|\t', 'TransCost (USD)\n')
    print('---------------------------------------\n')
    for obra in info['masCostosas']:
        print(obra['ObjectID'],'\t|\t', obra['Title'],'\t|\t', obra['ConstituentID'],'\t|\t', obra['Medium'],'\t|\t', obra['Date'],'\t|\t', obra['Dimensions'],'\t|\t', obra['Classification'],'\t|\t', obra['costoTransporte'], '\n')
        print('---------------------------------------\n')
    print('Las 5 obras más antiguas que se transportaron son: \n')

    print('ObjectID','\t|\t', 'Title','\t|\t', 'ConstituentID','\t|\t', 'Medium','\t|\t', 'Date','\t|\t', 'Dimensions','\t|\t', 'Classification','\t|\t', 'TransCost (USD)\n')
    print('---------------------------------------\n')
    for obra in info['masAntiguas']:
        print(obra['ObjectID'],'\t|\t', obra['Title'],'\t|\t', obra['ConstituentID'],'\t|\t', obra['Medium'],'\t|\t', obra['Date'],'\t|\t', obra['Dimensions'],'\t|\t', obra['Classification'],'\t|\t', obra['costoTransporte'], '\n')
        print('---------------------------------------\n')


#Requerimiento 6

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Listar cronológicamente los artistas")
    print("3- Listar cronologicamente las adquisiciones")
    print("4- Clasificar las obras de un artista por tecnica")
    print("5- Clasificar las obras por la nacionalidad de sus creadores")
    print("6- Transportar obras de un departamento")

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        catalog = initCatalog()
        print("Cargando información de los archivos ....")
        catalog = loadData(catalog)

    elif int(inputs[0]) == 2:
        if catalog == None:
            print("Debe cargar los datos primero")
            input("Presione enter para continuar...")
        else:
            listArtist(catalog)
            input("Presione enter para continuar...")
    elif int(inputs[0]) == 5:
        if catalog == None:
            print("Debe cargar los datos primero")
            input("Presione enter para continuar...")
        else:
            clasificarPorNacionalidad(catalog)
            input("Presione enter para continuar...")
    elif int(inputs[0]) == 6:
        if catalog == None:
            print("Debe cargar los datos primero")
            input("Presione enter para continuar...")
        else:
            transportarObras(catalog)
            input("Presione enter para continuar...")
    else:
        sys.exit(0)
sys.exit(0)