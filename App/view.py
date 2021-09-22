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
    return controller.loadData(catalog, 'Artists-utf8-small.csv', 'Artworks-utf8-small.csv') 

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

def clasificarPorNacionalidad(catalog):
    print(controller.nacionalidadObras(catalog))

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
    elif int(inputs[0]) == 4:
        if catalog == None:
            print("Debe cargar los datos primero")
            input("Presione enter para continuar...")
        else:
            clasificarPorNacionalidad(catalog)
            input("Presione enter para continuar...")
    else:
        sys.exit(0)
sys.exit(0)