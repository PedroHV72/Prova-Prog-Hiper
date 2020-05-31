class Video:
    def __init__(self, id, titulo, descricao, video, imagem_video):
        self._id = id
        self._titulo = titulo
        self._descricao = descricao
        self._video = video
        self._imagem_video = imagem_video
        self.coments = []

    def get_titulo(self):
        return self._titulo

    def get_descricao(self):
        return self._descricao

    def set_curtida(self, curtida):
        self._curtida = curtida
        
    def get_todas_curtidas(self):
        return self.get_todas_curtidas

    def set_visualizacoes(self, visualizacao):
        self._visualizacao = visualizacao

    def get_todas_visualizacoes(self):
        return self.get_todas_visualizacoes

    def get_imagem_video(self):
        return self._imagem_video

    def get_video(self):
        return self._video

    def get_id(self):
        return self._id

    def get_data(self, get):
        return self._data

    def set_comentario(self, comentario):
        self._coments.append(comentario)