#Hozz létre az Szoba osztályból EgyagyasSzoba és KetagyasSzoba származtatott
#osztályokat, amelyek különböző attributumai vannak, és az áruk is különböző!

from szoba import Szoba
from datetime import datetime, timedelta

class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(szobaszam, 26000)

    def foglalhato(self, datum):
        return datum >= datetime.now() + timedelta(days=1)