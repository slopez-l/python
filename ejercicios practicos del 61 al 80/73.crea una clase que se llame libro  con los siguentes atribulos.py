"""73.crea una clase que se llame libro
 con los siguentes atribulos:
 titulo, autor, editorial, año de publicacion.
 Metodos:
 constructor para inicializar los atributos"""


class Libro:
    def __init__(self,
                 titulo,
                 autor,
                 editorial,
                 año_publicacion):

        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial
        self.año_publicacion = año_publicacion


mi_libro = Libro("cien años de soledad",
                 "Gabriel garcia marquez",
                 "no lo se",
                 "100")

print(mi_libro.__dict__)
# lo convertimos en un diccionario
# para que nos devuelva todo.
