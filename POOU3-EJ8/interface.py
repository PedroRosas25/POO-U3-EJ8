from zope.interface import Interface
class IPersonal(Interface):
    def insertarelemento(self,personal,indice):
        pass
    def agregarelemento(self,personal):
        pass
    def mostrarelemento(self,indice):
        pass