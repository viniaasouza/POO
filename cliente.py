class Cliente:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def get_nome(self):
        return self.__nome.title()

    def nome(self, nome):
        self.__nome = nome
