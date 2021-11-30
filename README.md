# Yatzy-App
 
 Sovelluksella on tarkoitus pelata Yatzya, toistaiseksi komentorivillä ja seuraavalla viikolla pygamella rakennetun graafisen käyttöliittymän kautta. Sovellus toimii tällä hetkellä komentoriviltä käytännössä kokonaan, mutta jätin tarkoituksella lisäämättä liikaa toimintoja sillä pygameen siirtyessä tulee luultavasti suuri osa käyttöliittymästä kirjoitettua uudestaan kuitenkin.
 


## Säännöt

Säännöt pohjautuvat vahvasti pohjoismaisen Yatzyn [sääntöihin](https://fi.wikipedia.org/wiki/Yatzy), sillä muunnelmalla että tässä tapauksessa ei tarvitse päättää etukäteen mitä yhdistelmää hakee takaa.

## Python

Sovellus on kehitetty sekä testattu Python 3.8:lla.

## Asennus

1. Suorita "poetry install" komento juurihakemistossa

2. Käynnistä sovellus komennolla "poetry run invoke start"

Vaihtoehtoisesti varsinkin Windowsilla suosittelen käyttämään sovellusta pythonilla
avaamalla sen komennolla "main.py" src-hakemistossa.


## Dokumentaatio 
[Määrittelydokumentti](https://github.com/JVS23/ot-harjoitustyo/blob/master/Yatzy-app/dokumentaatio/vaatimusmaarittely.MD)

[Työaikakirjanpito](https://github.com/JVS23/ot-harjoitustyo/blob/master/Yatzy-app/dokumentaatio/tyoaikakirjanpito.MD)

## Testaus 

Komennoilla "poetry run invoke test" ja "poetry run invoke coverage-report"
voidaan testata sovellusta sekä generoida testausraportti