

from abc import ABC,abstractmethod


class Editor(ABC):


    @abstractmethod
    def edit(self):
        pass


    @abstractmethod
    def debug(self):
        pass


    @abstractmethod
    def exicute(self):
        pass


class Vscode(Editor):

    def edit(self):
        print("edit")


    def debug(self):
        print("debug")

    def exicute(self):
        print("exicute")


ed=Vscode()


ed.debug()
ed.edit()
ed.exicute()