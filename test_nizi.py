import os

def preberi_vrstice(file):
    return [line[:-1] for line in open(file, encoding="utf-8").readlines()]

def oblikuj(podatki):
    oblikovano = []
    for kraj in podatki:
        oblikovano.append(f"Kraj: {kraj[0]}, Vreme: {kraj[1]}, Temperatura: {kraj[2]}°C")
    return oblikovano

def preberi_csv(ime_datoteke):
    csv = []
    file = [line[:-1] for line in open(ime_datoteke, encoding="utf-8").readlines()]
    for city in file:
        terka = city.split(";")
        csv.append((terka[0], terka[1], float(terka[2])))
    return csv

def oblikuj_tabelo(podatki):
    oblikovano = ['Kraj            Vreme           Temperatura (°C)', '------------------------------------------------']
    for kraj in podatki:
        oblikovano.append(f"{kraj[0]:<16}{kraj[1]:<16}{kraj[2]:>16}")
    return oblikovano

def oblikuj_tabelo_f(podatki):
    oblikovano = ['Kraj            Vreme           Temperatura (°F)', '------------------------------------------------']
    for kraj in podatki:
        fahr = (float(kraj[2]) *1.8) + 32
        oblikovano.append(f"{kraj[0]:<16}{kraj[1]:<16}{fahr:>16.1f}")
    return oblikovano

def oblikuj_pike(podatki):
    oblikovano = ['Kraj            Vreme           Temperatura (°F)', '------------------------------------------------']
    for kraj in podatki:
        fahr = (float(kraj[2]) *1.8) + 32
        oblikovano.append(f"{kraj[0]:.<16}{kraj[1]:.<16}{fahr:.>16.1f}")
    return oblikovano

def oblikuj_fc(podatki):
    oblikovano = ['Kraj            Vreme        Temperatura °F (°C)', '------------------------------------------------']
    for kraj in podatki:
        fahr = f"{(float(kraj[2]) *1.8) + 32:.1f} ({kraj[2]})"
        oblikovano.append(f"{kraj[0]:.<16}{kraj[1]:.<16}{fahr:.>16}")
    return oblikovano

def shrani(vrstice, ime_datoteke):
    f = open(ime_datoteke, "w")
    f.write("\n".join(vrstice))
    f.close()

def najdaljse_besede(s):
    najdalse = f""
    max = 0
    for beseda in s.split():
        if len(beseda)>max:
            max = len(beseda)
    for beseda in s.split():
        if len(beseda) == max:
            najdalse += f"{beseda}, "
    return najdalse[:-2]

def py():
    return os.getcwd()




### ^^^ Naloge rešujte nad tem komentarjem. ^^^ ###

import unittest

class Testi(unittest.TestCase):

    def setUp(self):
        f = open("podatki.txt","w",encoding='utf-8')
        f.write("Ljubljana;oblačno;12.1\n")
        f.write("Maribor;sončno;9\n")
        f.write("Koper;sončno;14.7\n")
        f.close()

        self.podatki = [('Ljubljana', 'oblačno', 12.1), ('Maribor', 'sončno', 9.0), ('Koper', 'sončno', 14.7)]

    def test_preberi_vrstice(self):
        self.assertEqual(preberi_vrstice("podatki.txt"), ["Ljubljana;oblačno;12.1", "Maribor;sončno;9", "Koper;sončno;14.7"])

    def test_preberi_csv(self):
        self.assertEqual(preberi_csv("podatki.txt"), [('Ljubljana', 'oblačno', 12.1), ('Maribor', 'sončno', 9.0), ('Koper', 'sončno', 14.7)])

    def test_oblikuj(self):
        self.assertEqual(oblikuj(self.podatki),
                         ['Kraj: Ljubljana, Vreme: oblačno, Temperatura: 12.1°C',
                          'Kraj: Maribor, Vreme: sončno, Temperatura: 9.0°C',
                          'Kraj: Koper, Vreme: sončno, Temperatura: 14.7°C'])

    def test_oblikuj_tabelo(self):
        self.assertEqual(oblikuj_tabelo(self.podatki),
                         ['Kraj            Vreme           Temperatura (°C)',
                          '------------------------------------------------',
                          'Ljubljana       oblačno                     12.1',
                          'Maribor         sončno                       9.0',
                          'Koper           sončno                      14.7'])

    def test_oblikuj_tabelo_f(self):
        self.assertEqual(oblikuj_tabelo_f(self.podatki),
                         ['Kraj            Vreme           Temperatura (°F)',
                          '------------------------------------------------',
                          'Ljubljana       oblačno                     53.8',
                          'Maribor         sončno                      48.2',
                          'Koper           sončno                      58.5'])

    def test_oblikuj_pike(self):
        self.assertEqual(oblikuj_pike(self.podatki),
                         ['Kraj            Vreme           Temperatura (°F)',
                          '------------------------------------------------',
                          'Ljubljana.......oblačno.....................53.8',
                          'Maribor.........sončno......................48.2',
                          'Koper...........sončno......................58.5'])

    def test_oblikuj_fc(self):
        self.assertEqual(oblikuj_fc(self.podatki),
                         ['Kraj            Vreme        Temperatura °F (°C)',
                          '------------------------------------------------',
                          'Ljubljana.......oblačno..............53.8 (12.1)',
                          'Maribor.........sončno................48.2 (9.0)',
                          'Koper...........sončno...............58.5 (14.7)'])

    def test_shrani(self):
        lines = ['prva vrstica', 'druga vrstica', 'tretja vrstica']
        shrani(lines, 'datoteka.txt')
        f = open("datoteka.txt", "r")
        lines_f = f.read().splitlines()
        f.close()
        self.assertEqual(lines_f, lines)

    def test_najdaljse_besede(self):
        self.assertEqual(najdaljse_besede('ob znaku bo ura deset in pet minut'), 'znaku, deset, minut')

if __name__ == '__main__':
    unittest.main(verbosity=2)
