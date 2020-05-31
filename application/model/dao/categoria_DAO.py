from application.model.entity.category import Category
from application.model.entity.video import Video

class CategoriaDAO:
    def __init__(self):
        video1 = Video(1, "Pre Fire 1 ", "- PRE FIRE FEITO COM AUXÍLIO DO SOM DO OPONENTE NA ESCADA.", "/videos/prefire1.mp4", "/img/img-pre-1.jpg")
        video2 = Video(2, "Pre Fire 2 ", "- PRE FIRE FEITO SEGUINDO O RASTRO DE BALA DO OPONENTE.", "/videos/prefire2.mp4", "/img/img-pre-2.jpg")
        video3 = Video(3, "Triple Kill 1 ", "- RETAKE PARA RETOMAR ÁREA PERTO DO BOMB", "/videos/triple1.mp4", "/img/img-triple-2.jpg")
        video4 = Video(4, "Triple Kill 2 ", "- RETAKE PELA COSTAS IMPEDINDO O PLANT.", "/videos/triple2.mp4", "/img/img-triple-1.jpg")
        video5 = Video(5, "Headshot 1 ", "- KILL DE PISTOLA COM CLICK RÁPIDO COM O ESCUDO NA FRENTE.", "/videos/hs1.mp4", "/img/img-hs-1.jpg")
        video6 = Video(6, "Headshot 2 ", "- KILL FEITA COM O GLAZ, HEADSHOT E ONE TAP.", "/videos/hs2.mp4", "/img/img-hs-2.jpg")
        self._todos_os_videos = [video1, video2, video3, video4, video5, video6]
        
        self._lista_dos_videos = []
        self._lista_dos_videos.append(Category(1, "Pre Fire", [video1, video2]))
        self._lista_dos_videos.append(Category(2, "Triple Kill", [video3, video4]))
        self._lista_dos_videos.append(Category(3, "Headshot", [video5, video6]))

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