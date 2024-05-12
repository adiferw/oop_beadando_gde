#Hozz létre az Szoba osztályból EgyagyasSzoba és KetagyasSzoba származtatott
#osztályokat, amelyek különböző attributumai vannak, és az áruk is különböző!

from szoba import Szoba

class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(szobaszam, 17000)

    def foglalhato(self, datum):
        return True