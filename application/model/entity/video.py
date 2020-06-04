class Video:
    def __init__(self, id, titulo, descricao, video, imagem_video, categoria_video):
        self._id = id
        self._titulo = titulo
        self._descricao = descricao
        self._video = video
        self._imagem_video = imagem_video
        self._coments = []
        self._todas_visualizacoes = 0
        self._todas_curtidas = 0
        self._categoria_video = categoria_video

    def get_titulo(self):
        return self._titulo

    def get_descricao(self):
        return self._descricao

    def set_curtida(self, curtida):
        self._todas_curtidas = curtida
        
    def get_todas_curtidas(self):
        return self._todas_curtidas

    def set_visualizacoes(self, visualizacao):
        self._todas_visualizacoes = visualizacao

    def get_todas_visualizacoes(self):
        return self._todas_visualizacoes

    def get_imagem_video(self):
        return self._imagem_video

    def get_video(self):
        return self._video

    def get_id(self):
        return self._id

    def set_comentario(self, comentario):
        self._coments.append(comentario)

    def get_comentario(self):
        return self._coments
        
    def get_categoria_video(self):
        return self._categoria_video