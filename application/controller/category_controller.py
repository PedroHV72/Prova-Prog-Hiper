from application import app
from flask import render_template, request
from application.model.dao.categoria_DAO import CategoriaDAO
from application.model.entity.category import Category


@app.route("/categorias/<category_id>")
def category(category_id):
    category = CategoriaDAO().procurar(category_id)
    categoria_dao = CategoriaDAO()
    video_list = categoria_dao.retornar_lista_videos()
    return render_template("categoria-escolhida.html", category = category, video_list = video_list)