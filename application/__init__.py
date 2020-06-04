from flask import Flask
import os
from application.model.entity.video import Video
from application.model.entity.category import Category


template_folder = os.path.abspath("application/view/templates")
static_folder = os.path.abspath("application/view/static")

app = Flask(__name__, template_folder = template_folder, static_folder = static_folder)


video1 = Video(1, "Pre Fire ", "- PRE FIRE FEITO COM AUXÍLIO DO SOM DO OPONENTE NA ESCADA.", "/videos/prefire.mp4", "/img/img-pre.jpg", "Categoria Pre Fire")
video2 = Video(2, "Triple Kill ", "- RETAKE PARA RETOMAR ÁREA PERTO DO BOMB", "/videos/triple.mp4", "/img/img-triple.jpg", "Categoria Triple Kill")
video3 = Video(3, "Headshot ", "- KILL FEITA COM O GLAZ, HEADSHOT E ONE TAP.", "/videos/hs.mp4", "/img/img-hs.jpg", "Categoria Headshot")
todos_os_videos = [video1, video2, video3]

lista_das_categorias = []
lista_das_categorias.append(Category(1, "Pre Fire", [video1]))
lista_das_categorias.append(Category(2, "Triple Kill", [video2]))
lista_das_categorias.append(Category(3, "Headshot", [video3]))


from application.controller import hello_controller
from application.controller import category_controller
from application.controller import video_controller