from application import app
from flask import render_template, request
from application.model.dao.categoria_DAO import CategoriaDAO
from application.model.entity.category import Category


@app.route("/categorias/<category_id>/<video_id>")
def exibir(category_id, video_id):
    exibir = CategoriaDAO().procurar(category_id)
    exibir2 = CategoriaDAO().procurar_video(video_id)
    category = CategoriaDAO().procurar(category_id)
    categoria_dao = CategoriaDAO()
    exibir_video_list = categoria_dao.retornar_todos_videos()
    return render_template("exibicao.html", exibir = exibir, exibir2 = exibir2, category = category, exibir_video_list = exibir_video_list)