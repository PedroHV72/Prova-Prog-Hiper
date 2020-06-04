from application import todos_os_videos
from application.model.entity.video import Video

class VideoDAO:
    def __init__(self):
        self._todos_os_videos = todos_os_videos

    def contar_curtida(self, video):
        like = video.get_todas_curtidas()
        like += 1
        video.set_curtida(like)

    def armazenar_visualizacao(self, video):
        visu = video.get_todas_visualizacoes()
        visu += 1
        video.set_visualizacoes(visu)

    def retornar_todos_videos(self):
        return self._todos_os_videos

    def procurar_video(self, id):
        for i in range(0, len(self._todos_os_videos)):
            if self._todos_os_videos[i].get_id() == int(id):
                return self._todos_os_videos[i]
        return None