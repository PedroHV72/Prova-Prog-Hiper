from application import app
from application import todos_os_videos
from flask import render_template, request
from application.model.dao.categoria_DAO import CategoriaDAO
from application.model.entity.category import Category
from application.model.entity.video import Video


@app.route("/")
def hello():
    categoria_dao = CategoriaDAO()
    category_list = categoria_dao.retornar_lista_videos()
    
    
    lista_mais_curtidos_ordem = sorted(todos_os_videos, key=Video.get_todas_curtidas, reverse=True)
    lista_mais_curtidos = [lista_mais_curtidos_ordem[0], lista_mais_curtidos_ordem[1]]

    return render_template("index.html", category_list = category_list, lista_mais_curtidos = lista_mais_curtidos)