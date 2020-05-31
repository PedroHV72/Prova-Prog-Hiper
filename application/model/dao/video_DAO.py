class VideoDAO:
    def __init__(self):
        pass

    def max_curtido(self):
        mais_curtida1 = self._todos_videos[0]
        mais_curtida2 = self._todos_videos[0]
        for video in self._todos_videos:
            if self.mais_curtida.get_curtida > video.get_curtida():
                mais_curtida1 = video

            if self.max_curtida.get_qntCurtida > video.get_curtida() and =! mais_curtida1:
                mais_curtida2 = video

    def somar_visualizacao(self, video):
        visualizacao(0) += 1
        video.set_visualizacoes(visualizacoes)

    def somar_curtida(self, video):
        curtida(0) += 1
        video.set_curtida(curtida)