class Coment:
    def __init__(self, text, nome):
        self._text = text
        self._nome = nome

    def get_text(self):
        return self._text

    def get_nome(self):
        return self._nome