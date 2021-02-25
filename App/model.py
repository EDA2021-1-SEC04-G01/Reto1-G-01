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
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as sel
assert cf
import time

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog(dtEstructure):
    """
    Inicializa el catálogo de libros. Crea una lista vacia para guardar
    todos los libros, adicionalmente, crea una lista vacia para los autores,
    una lista vacia para los generos y una lista vacia para la asociación
    generos y libros. Retorna el catalogo inicializado.
    """
    catalog = {'videos': None, "countries": None,
               'categories': None}
    if dtEstructure == 0:       
        catalog['videos'] = lt.newList('ARRAY_LIST' )
        catalog["countries"] = lt.newList('ARRAY_LIST')
        catalog['categories'] = lt.newList('ARRAY_LIST')
        
    else:
        catalog['videos'] = lt.newList("SINGLE_LINKED")
        catalog['categories'] = lt.newList("SINGLE_LINKED")
        catalog["countries"] = lt.newList("SINGLE_LINKED")
        
        
    return catalog
# Funciones para agregar informacion al catalogo
def addVideo(catalog, video):
    countries= []
    lt.addLast(catalog['videos'], video)
    countries.append(video["country"])
    
    for country in countries:
        addVideoCountry(catalog, country, video)

def addVideoCountry(catalog, countryname, video):

    countries = catalog["countries"]
    poscountry = lt.isPresent(countries, countryname)
    if poscountry > 0:
        country = lt.getElement(countries, poscountry)
    else:
        country = newCountry(countryname)
        lt.addLast(countries, country)
    lt.addLast(country["videos"], video)

def addCategory(catalog, category):
    lt.addLast(catalog['categories'], category)

    


# Funciones para creacion de datos
def newCountry(name):

    country = {"name": "", "videos": None, "average_rating": 0}
    country["name"] = name
    country["videos"] = lt.newList("ARRAY_LIST")
    return country
def topVideos(catalog, topAmount, countryname):
    poscountry = lt.isPresent(catalog["countries"], countryname)
   if poscountry > 0:
        country = lt.getElement(catalog["countries"], poscountry)
        lt.subList(country,1,topAmount)
    

# Funciones de consulta



# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
def cmpVideosByViews(video1, video2):
    
    return (float(video1['views']) > float(video2['views']))

def sortVideos(catalog, sorting):
    if sorting == 0:
        sa.sort(catalog["videos"], cmpVideosByViews)
    elif sorting == 1:
        ins.sort(catalog["videos"], cmpVideosByViews)
    else:
        sel.sort(catalog["videos"], cmpVideosByViews)




    
   
