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
      year = (artwork["DateAcquired"].split("/"))[3]
      month = (artwork["DateAcquired"].split("/"))[1]
      day = (artwork["DateAcquired"].split("/"))[2]
      if year >= finicial_new[1] and year <= ffinal_new[1]:
        if month >=finicial_new[2] and month <= ffinal_new[2]:
          if day >= finicial_new[3] and day <= ffinal_new[3]:
            lt.addLast(rank_artworks,artwork)

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
# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
def compare_dates(date1, date2):
  return (int(date1["BeginDate"]) < int(date2["BeginDate"]))

def ordernar_naciones_cantidad(nacion1, nacion2):
  return nacion1['tamano'] >= nacion2['tamano']