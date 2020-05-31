from application.model.entity.category import Category
from application.model.entity.video import Video

class CategoriaDAO:
    def __init__(self):
        video1 = Video(1, "Pre Fire ", "- PRE FIRE FEITO COM AUXÍLIO DO SOM DO OPONENTE NA ESCADA.", "/videos/prefire.mp4", "/img/img-pre.jpg")
        video2 = Video(2, "Triple Kill ", "- RETAKE PARA RETOMAR ÁREA PERTO DO BOMB", "/videos/triple.mp4", "/img/img-triple.jpg")
        video3 = Video(3, "Headshot ", "- KILL FEITA COM O GLAZ, HEADSHOT E ONE TAP.", "/videos/hs.mp4", "/img/img-hs.jpg")
        self._todos_os_videos = [video1, video2, video3]
        
        self._lista_dos_videos = []
        self._lista_dos_videos.append(Category(1, "Pre Fire", [video1]))
        self._lista_dos_videos.append(Category(2, "Triple Kill", [video2]))
        self._lista_dos_videos.append(Category(3, "Headshot", [video3]))

    def retornar_lista_videos(self):
        return self._lista_dos_videos

    def procurar(self, id):
        for i in range(0, len(self._lista_dos_videos)):
            if self._lista_dos_videos[i].get_id() == int(id):
                return self._lista_dos_videos[i] 
        return None

    def retornar_todos_videos(self):
        return self._todos_os_videos

    def procurar_video(self, id):
        for i in range(0, len(self._todos_os_videos)):
            if self._todos_os_videos[i].get_id() == int(id):
                return self._todos_os_videos[i]
        return None