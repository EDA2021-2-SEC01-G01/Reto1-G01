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

# Funciones de consulta
def listArtist(catalog,ainicio,afinal):
    rank_artist = lt.newList(datastructure="ARRAY_LIST")

    for artist in lt.iterator(catalog["artists"]):
      if int(artist["BeginDate"]) >= ainicio and int(artist["BeginDate"]) <= afinal:
        lt.addLast(rank_artist, artist)
      
    sa.sort(rank_artist,compare_dates)
    return rank_artist

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
def compare_dates(date1, date2):
  return (int(date1["BeginDate"]) < int(date2["BeginDate"]))