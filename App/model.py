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
from DISClib.Algorithms.Sorting import mergesort as mer
from DISClib.Algorithms.Sorting import quicksort as qck
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
    catalog = {'videos': None,
               'categories': None} 
    catalog['videos'] = lt.newList(dtEstructure)
    catalog["categories"] = lt.newList(dtEstructure)          
    return catalog
# Funciones para agregar informacion al catalogo
def addVideo(catalog, video, dtEstructure):
    if not video["country"] in  catalog.keys():
        tc= video["country"]
        catalog[tc]= None
        catalog[tc]= lt.newList(dtEstructure)
        lt.addLast(catalog[tc], video)
    else:
        tc= video["country"]
        lt.addLast(catalog[tc], video)

    lt.addLast(catalog['videos'], video)

def addCategory(catalog, category):
    lt.addLast(catalog["categories"], category)

# Funciones para creacion de dato

def topVideos(catalog, topAmount, countryname, category,sorting):
    for i in catalog["categories"]["elements"]:
        if i["name"] == category:
            idnumber= i["id"]
    top= lt.newList()
    for i in catalog[countryname]["elements"]:
        if i["category_id"] == idnumber:
            lt.addLast(top, i)

    sortVideos(top, sorting)
    if topAmount > lt.size(top):
        print("No se puede mostrar el top "+str(topAmount)+", ya que solo existen "+str(lt.size(top))+" videos que cumplen con los filtros seleccioados")
        print("Se mostrara en cambio el top "+str(lt.size(top)))
        topAmount= lt.size(top)
    sub= lt.subList(top, 1,topAmount)
    for i in range(1, lt.size(sub)+1):
        a=lt.getElement(sub, i)
        print("Posicion: "+str(i)+"|"+"Titulo: "+a["title"]+"|Vistas: "+a["views"])
    
    

    

# Funciones de consulta



# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
def cmpCountries(country1, country):
    if (country1.lower() in country['name'].lower()):
        return 0
    return -1


def cmpVideosByViews(video1, video2):
    
    return int(video1['views']) > int(video2['views'])

def sortVideos(lt, sorting):
    if sorting == 0:
        sa.sort(lt, cmpVideosByViews)
    elif sorting == 1:
        ins.sort(lt, cmpVideosByViews)
    elif sorting == 2:
        sel.sort(lt, cmpVideosByViews)
    elif sorting == 3:
        mer.sort(lt, cmpVideosByViews)
    else:
        qck.sort(lt, cmpVideosByViews)
    
        





    
   
