from application import app
from flask import render_template, request
from application.model.dao.categoria_DAO import CategoriaDAO
from application.model.entity.category import Category


@app.route("/")
def hello():
    categoria_dao = CategoriaDAO()
    category_list = categoria_dao.retornar_lista_videos()
    return render_template("index.html", category_list = category_list)