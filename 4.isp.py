from abc import ABC

class Janela(ABC):
    def fechar(self):
        raise NotImplementedError

class JanelaTamanhoFixo(ABC, Janela):
    def mostrar_menu(self):
        raise NotImplementedError


class JanelaSemMenu(ABC, Janela):
    def maximizar(self):
        raise NotImplementedError
    
    def minimizar(self):
        raise NotImplementedError




