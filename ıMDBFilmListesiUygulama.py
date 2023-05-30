import requests
import re
import time
import json
import textwrap

class Film:
    def __init__(self):
        self.dongu=True

    def program(self):
        secim=self.menu()
        if secim=="1":
            self.eniyi250()
        
        if secim=="2":
            self.enpopuler()
        if secim=="3":
            self.sinemalarda()
        if secim=="4":
            self.yakında()
        if secim=="5":
            self.filmAra()
        if secim=="6":
            self.cıkıs()

    def menu(self):
        def kontrol(secim):
            if re.search("[^1-6]",secim):
                raise Exception("Lütfen 1 ve 6  arasında geçerli bir seçim yapınız...")
        while True:
            try:
                secim=input("Merhabalar,Şevket Uğurel IMDb programına hoşgeldiniz\n\nLütfen yamak istediğiniz işlemi seçiniz...\n\n[1]-En iyi 250 Film \n[2]-En Popüler Filmler\n[3]-Sinemalarda\n[4]-Yakında\n[5]-Film Ara\n[6]-Çıkış\n")
                kontrol(secim)
            except Exception as hata:
                print(hata)
                time.sleep(2)
            else:
                break
        return secim

    def eniyi250(self):
        print("En iyi 250 Film listesine ulaşılıyor...\n\n")
        time.sleep(2)
        url=requests.get("https://imdb-api.com/en/API/Top250Movies/k_jgd1dufe")
        sonuc=url.json()
        for i in sonuc["items"]:
            print(i["fullTitle"])
        self.menuDon()

    def enpopuler(self):
        print("En popüler film listesine ulaşılıyor...\n\n")
        time.sleep(2)
        url=requests.get("https://imdb-api.com/en/API/MostPopularMovies/k_jgd1dufe")
        sonuc=url.json()
        for i in sonuc["items"]:
            print(i["fullTitle"])
        self.menuDon()

    def sinemalarda(self):
        print("sinemlarda olan film listesine ulaşılıyor...\n\n")
        time.sleep(2)
        url=requests.get("https://imdb-api.com/en/API/InTheaters/k_jgd1dufe")
        sonuc=url.json()
        for i in sonuc["items"]:
            print(i["fullTitle"])
        self.menuDon()

    def yakında(self):
        print("yakında olacak film listesine ulaşılıyor...\n\n")
        time.sleep(2)
        url=requests.get("https://imdb-api.com/en/API/ComingSoon/k_jgd1dufe")
        sonuc=url.json()
        for i in sonuc["items"]:
            print(i["fullTitle"])
        self.menuDon()

    def filmAra(self):
        print("Film Arama Menüsüne ulaşılıyor...\n")
        time.sleep(2)
        film=input("Lütfen Film adını giriniz\n")

        url=requests.get("https://imdb-api.com/en/API/Top250Movies/k_jgd1dufe")
        sonuc=url.json()

        ID=list()
        for i in sonuc["items"]:
            ID.append(i["id"])

        AD=list()
        for i in sonuc["items"]:
            AD.append(i["title"])

        cevir=zip(AD,ID)
        veri=dict(cevir)
        key=veri.get(film)

        url2=requests.get("https://imdb-api.com/tr/API/Wikipedia/k_jgd1dufe/{}".format(key))
        
        sonuc2=url2.json()

        print(textwrap.fill(sonuc2["plotShort"]["plainText"]),130)
        self.menuDon()

    def cıkıs(self):
        print("Çıkılıyor...")
        time.sleep(2)
        self.dongu=False
        exit()

    def menuDon(self):
        while True:
            x=input("Ana menüye dönmek için 7'ye ,Çıkmak için 6'ya basınız...:")
            if x=="7":
                print("Ana Menüye dönülüyor...")
                time.sleep(2)
                self.program()
                break   
            elif x=="6":
                self.cıkıs()
            else:
                print("Lütfen geçerli bir değer giriniz!!!")


Sistem=Film()
while Sistem.dongu:
    Sistem.program()