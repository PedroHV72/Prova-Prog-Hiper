class Category:
    def __init__(self, id, titulo, todos_videos):
        self._id = id
        self._titulo = titulo
        self._todos_videos = todos_videos

    def get_titulo(self):
        return self._titulo

    def get_todos_videos(self):
        return self._todos_videos

    def set_id(self, id):
        self._id = id

    def get_id(self):
        return self._id