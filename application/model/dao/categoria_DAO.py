from application.model.entity.category import Category
from application.model.entity.video import Video
from application import lista_das_categorias

class CategoriaDAO:
    def __init__(self):
        self.lista_das_categorias = lista_das_categorias

    def retornar_lista_videos(self):
        return lista_das_categorias

    def procurar(self, id):
        for i in range(0, len(lista_das_categorias)):
            if lista_das_categorias[i].get_id() == int(id):
                return lista_das_categorias[i] 
        return None