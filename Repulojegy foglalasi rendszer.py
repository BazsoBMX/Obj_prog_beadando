from abc import ABC, abstractmethod

class Jarat(ABC):
    def __init__(self, jaratszam, celallomas, jegyar):
        self.jaratszam = jaratszam
        self.celallomas = celallomas
        self.jegyar = jegyar

    @abstractmethod
    def jarat_tipus(self):
        pass

class BelfoldiJarat(Jarat):
    def jarat_tipus(self):
        return "Belföldi"

class NemzetkoziJarat(Jarat):
    def jarat_tipus(self):
        return "Nemzetközi"

class LegiTarsasag:
    def __init__(self, nev):
        self.nev = nev
        self.jaratok = []

    def hozzaad_jarat(self, jarat):
        self.jaratok.append(jarat)

    def keres_jarat(self, jaratszam):
        for jarat in self.jaratok:
            if jarat.jaratszam == jaratszam:
                return jarat
        return None

class JegyFoglalas:
    def __init__(self, foglalas_id, jarat):
        self.foglalas_id = foglalas_id
        self.jarat = jarat

class FoglalasKezelo:
    def __init__(self):
        self.foglalasok = {}

    def foglalas(self, foglalas_id, jarat):
        if foglalas_id in self.foglalasok:
            print("Hiba: Ez a foglalás már létezik.")
            return None
        self.foglalasok[foglalas_id] = JegyFoglalas(foglalas_id, jarat)
        return jarat.jegyar

    def lemondas(self, foglalas_id):
        if foglalas_id in self.foglalasok:
            del self.foglalasok[foglalas_id]
            print(f"{foglalas_id} foglalás törölve.")
        else:
            print("Hiba: Nincs ilyen foglalás.")

    def listazas(self):
        if not self.foglalasok:
            print("Nincs aktív foglalás.")
        else:
            for f in self.foglalasok.values():
                print(f"Foglalás ID: {f.foglalas_id}, Járat: {f.jarat.jaratszam}, Célállomás: {f.jarat.celallomas}")

legi = LegiTarsasag("BMX Air")
j1 = BelfoldiJarat("B101", "Budapest", 11000)
j2 = BelfoldiJarat("B102", "Debrecen", 13500)
j3 = NemzetkoziJarat("N201", "London", 56000)
legi.hozzaad_jarat(j1)
legi.hozzaad_jarat(j2)
legi.hozzaad_jarat(j3)

foglalas_kezelo = FoglalasKezelo()
foglalas_kezelo.foglalas("F001", j1)
foglalas_kezelo.foglalas("F002", j2)
foglalas_kezelo.foglalas("F003", j3)
foglalas_kezelo.foglalas("F004", j1)
foglalas_kezelo.foglalas("F005", j2)
foglalas_kezelo.foglalas("F006", j3)

def menu():
    while True:
        print("\n--- Légitársaság Foglalási Rendszer ---")
        print("1. Jegy foglalása")
        print("2. Foglalás lemondása")
        print("3. Foglalások listázása")
        print("4. Kilépés")
        valasztas = input("Választás (1-4): ")

        if valasztas == "1":
            jaratszam = input("Add meg a járatszámot: ")
            jarat = legi.keres_jarat(jaratszam)
            if not jarat:
                print("Hiba: Nincs ilyen járat.")
                continue
            foglalas_id = input("Adj meg egy egyedi foglalás ID-t: ")
            ar = foglalas_kezelo.foglalas(foglalas_id, jarat)
            if ar:
                print(f"Sikeres foglalás! Ár: {ar} Ft")
        elif valasztas == "2":
            foglalas_id = input("Add meg a lemondandó foglalás ID-ját: ")
            foglalas_kezelo.lemondas(foglalas_id)
        elif valasztas == "3":
            foglalas_kezelo.listazas()
        elif valasztas == "4":
            print("Kilépés...")
            break
        else:
            print("Érvénytelen választás.")

if __name__ == "__main__":
    menu()
