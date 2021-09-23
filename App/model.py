"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


from os import replace
from DISClib.DataStructures.arraylist import iterator
import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def initCatalog():
  """
  Carga la informacion proveniente del archivo csv.
  """
  catalog = {
    'artists': None,
    'artworks': None,
  }
  
  return catalog


# Funciones para agregar informacion al catalogo

def loadArtists(catalog, filename):
    catalog['artists'] = lt.newList('ARRAY_LIST', filename=filename)
    return catalog

def loadArtworks(catalog, filename):
    catalog['artworks'] = lt.newList('ARRAY_LIST', filename=filename)
    return catalog
    
# Funciones para creacion de datos
def addArtist(catalog, artist):
    lt.addLast(catalog["artists"], artist)

def addArtwork(catalog, artwork):
    lt.addLast(catalog["artworks"], artwork)

def addArtworkToNatio(nacion, artwork):
  lt.addLast(nacion, artwork)

# Funciones de consulta
def listArtist(catalog,ainicio,afinal):
    rank_artist = lt.newList(datastructure="ARRAY_LIST")

    for artist in lt.iterator(catalog["artists"]):
      if int(artist["BeginDate"]) >= ainicio and int(artist["BeginDate"]) <= afinal:
        lt.addLast(rank_artist, artist)
      
    sa.sort(rank_artist,compare_dates)
    return rank_artist

def listArtworks(catalog,finicial,ffinal):
    finicial_new = finicial.split("-")
    ffinal_new = ffinal.split("-")

    rank_artworks = lt.newList(datastructure="ARRAY_LIST")
    for artwork in lt.iterator(catalog["artworks"]):
      if len(artwork["DateAcquired"]) != 0:
         year = int(artwork["DateAcquired"].split("-")[0])
         month = int(artwork["DateAcquired"].split("-")[1])
         day = int(artwork["DateAcquired"].split("-")[2])
         if year > int(finicial_new[0]) and year < int(ffinal_new[0]):
           lt.addLast(rank_artworks,artwork)
         elif year == int(finicial_new[0]) or year == int(ffinal_new[0]):
           if month > int(finicial_new[1]) and month < int(ffinal_new[1]):
               lt.addLast(rank_artworks,artwork)
           elif month == int(finicial_new[1]) or month == int(ffinal_new[1]):
             if day >= int(finicial_new[2]) and day <= int(ffinal_new[2]):
               lt.addLast(rank_artworks,artwork)


    sa.sort(rank_artworks, compare_dates)
    return rank_artworks

#Requerimiento 4

def listarNacionalidadObras(catalog):
  naciones_dict = {}
  naciones_list = lt.newList(datastructure='ARRAY_LIST')

  for artwork in lt.iterator(catalog['artworks']):
    creators = nacionalidadListaArtistas(catalog, artwork['ConstituentID'])

    for info in lt.iterator(creators):
      nacionalidad_dict = info['nacionalidad']

      if nacionalidad_dict == '' or nacionalidad_dict == 'Nationality unknown':
        nacionalidad_obtener = 'Unknown'
      else:
        nacionalidad_obtener = nacionalidad_dict

      if naciones_dict.get(nacionalidad_obtener, None) == None:
        naciones_dict[nacionalidad_obtener] = lt.newList(datastructure='SINGLE_LINKED')
        lt.addLast(naciones_dict[nacionalidad_obtener], info['infoArtista'])
      else:
        lt.addLast(naciones_dict[nacionalidad_obtener], info['infoArtista'])

  for nacionalidad in naciones_dict:
    lt.addLast(naciones_list, {'nacionalidad': nacionalidad, 'tamano': lt.size(naciones_dict[nacionalidad])})

  sorted_list = sa.sort(naciones_list, ordernar_naciones_cantidad)
  primer_elemento = lt.removeFirst(sorted_list)
  primer_elemento = {'nacionalidad': primer_elemento['nacionalidad'], 'obras': naciones_dict[primer_elemento['nacionalidad']], 'tamano': primer_elemento['tamano']}
  lt.addFirst(sorted_list, primer_elemento)
  return sorted_list['elements'][:10]


def nacionalidadListaArtistas(catalog, idArtistas):
  naciones = lt.newList(datastructure='ARRAY_LIST')

  for artista in lt.iterator(catalog['artists']):
    for creador in crearListaDesdeStr(idArtistas):
      if artista['ConstituentID'] == creador:
        lt.addLast(naciones, {'infoArtista': artista, 'nacionalidad': artista['Nationality']})

  return naciones


def crearListaDesdeStr(cadena: str):
  sin_corchete = cadena[1:-1]
  sin_espacio = sin_corchete.replace(' ', '')
  return sin_espacio.split(',')

#Requerimiento 5

def transportarObras(obras):
  info = {}
  info['cantidad'] = lt.size(obras)

  valorTotal = 0
  pesoTotal = 0

  for obra in lt.iterator(obras):
    valorTotal += obra['costoTransporte']
    if obra['Weight (kg)'].replace(' ', '') != '':
      pesoTotal += float(obra['Weight (kg)'].replace(' ', ''))

  info['costoServicio'] = valorTotal
  info['pesoObras'] = pesoTotal
  info['masAntiguas'] = sa.sort(obras, mas_antigua)['elements'][:5]
  info['masCostosas'] = sa.sort(obras, ordenar_costo)['elements'][:5]

  return info


def obtenerObrasDepartamento(catalog, departamento):
  obras_depto = lt.newList(datastructure='ARRAY_LIST')

  for obra in lt.iterator(catalog['artworks']):
    if obra['Department'] == departamento:
      obraNueva = obra.copy()
      obraNueva['costoTransporte'] = calcularCostosObra(obra)
      lt.addLast(obras_depto, obraNueva)

  return obras_depto


def calcularCostosObra(obra):  
  peso = obra['Weight (kg)'].replace(' ', '')
  alto = obra['Height (cm)'].replace(' ', '')
  ancho = obra['Width (cm)'].replace(' ', '')
  fondo = obra['Length (cm)'].replace(' ', '')

  valorKgM2M3 = 0

  if (peso != ''):
    peso = float(peso)
    if peso * 72 > valorKgM2M3:
      valorKgM2M3 = peso * 72

  if alto != '' and ancho != '' and fondo != '':
    m3 = (float(alto) * float(ancho) * float(fondo))/10000
    if m3 * 72 > valorKgM2M3:
      valorKgM2M3 = m3 * 72
  
  elif alto != '' and ancho != '':
    m2 = (float(alto) * float(ancho)) / 10000
    if m2 * 72 > valorKgM2M3:
      valorKgM2M3 = m2 * 72
  
  elif alto != '' and fondo != '':
    m2 = (float(alto) * float(fondo)) / 10000
    if m2 * 72 > valorKgM2M3:
      valorKgM2M3 = m2 * 72
  
  elif ancho != '' and fondo != '':
    m2 = (float(ancho) * float(fondo)) / 10000
    if m2 * 72 > valorKgM2M3:
      valorKgM2M3 = m2 * 72
  
  if valorKgM2M3 == 0:
    valorKgM2M3 = 48

  return valorKgM2M3


def proponerObras(catalog, dateInicial, dateFinal, areaDisponible):
  disponible = float(areaDisponible)
  obras_en_fecha = lt.newList(datastructure='LINKED_LIST')
  for obra in lt.iterator(catalog['artworks']):
    if obra['Date'] != '':
      if int(obra['Date']) <= dateFinal and int(obra['Date']) >= dateInicial:
        lt.addLast(obras_en_fecha, obra)

  seleccionadas = lt.newList(datastructure='ARRAY_LIST')
  atotal = 0

  for obra in lt.iterator(obras_en_fecha):
    alto = obra['Height (cm)'].replace(' ', '')
    ancho = obra['Width (cm)'].replace(' ', '')
    fondo = obra['Length (cm)'].replace(' ', '')

    m2 = 0

    if alto != '' and ancho != '':
      m2 = (float(alto) * float(ancho)) / 10000
  
    elif alto != '' and fondo != '':
      m2 = (float(alto) * float(fondo)) / 10000
    
    elif ancho != '' and fondo != '':
      m2 = (float(ancho) * float(fondo)) / 10000

    if m2 != 0 and m2 <= disponible:
      lt.addLast(seleccionadas, obra)
      atotal += m2
      disponible -= m2

  return {'obras': seleccionadas, 'atotal': atotal, 'cantidad': lt.size(seleccionadas)}

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
def compare_dates(date1, date2):
  return (int(date1["BeginDate"]) < int(date2["BeginDate"]))

def ordernar_naciones_cantidad(nacion1, nacion2):
  return nacion1['tamano'] >= nacion2['tamano']

def ordenar_costo(obra1, obra2):
  return obra1['costoTransporte'] >= obra2['costoTransporte']

def mas_antigua(date1, date2):
  if date1['Date'] == '':
    return False
  if date2['Date'] == '':
    return False
  return int(date1['Date']) < int(date2['Date'])