from application import app
from flask import render_template, request, current_app, jsonify
from application.model.dao.categoria_DAO import CategoriaDAO
from application.model.dao.video_DAO import VideoDAO
from application.model.entity.category import Category
from application.model.entity.video import Video
from application.model.entity.coment import Coment


@app.route("/categorias/<category_id>/<video_id>")
def exibir(category_id, video_id):
    exibir = CategoriaDAO().procurar(category_id)
    video = VideoDAO().procurar_video(video_id)
    category = CategoriaDAO().procurar(category_id)
    categoria_dao = CategoriaDAO()
    video_dao = VideoDAO()
    exibir_video_list = video_dao.retornar_todos_videos()
    video_dao.armazenar_visualizacao(video)
    return render_template("exibicao.html", exibir = exibir, video = video, category = category, exibir_video_list = exibir_video_list)


@app.route("/<video_id>/comentario", methods=['POST'])
def comentar(video_id):
    video_dao = VideoDAO()
    video = video_dao.procurar_video(int(video_id))
    autor = request.values.get('nome')
    comentario = request.values.get('comentario')
    coment = Coment(comentario, autor)
    video.set_comentario(coment)
    lista_comentario = video.get_comentario()
    return render_template("comentario.html", video = video, lista_comentario = lista_comentario)


@app.route("/<video_id>/curtir", methods=['POST'])
def curtir(video_id):
    video_dao = VideoDAO()
    video = video_dao.procurar_video(int(video_id))
    video_dao.contar_curtida(video)
    return render_template("curtida.html", video = video)