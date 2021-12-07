# Commandline-Yatzy-App
 
 Sovelluksella on tarkoitus pelata Yatzya ~~toistaiseksi~~ pysyvästi komentorivillä. Sovelluksen alkuvaiheessa tuli suunniteltua rakenne hieman huonosti, ja kun aloin lisäämään UI:ta, huomasin että Pythonin kanssa projektia olisi kannattanut jo heti alusta alkaen rakentaa UI mielessä. Luulen että tämä virhearvio johtui aiemmasta kokemuksesta JavaScriptin web appien kanssa, joissa myöhemmin UI:n rakentaminen toimii hieman paremmin. Ainakin tuli kantapään kautta opittua suunnittelun tärkeys.
 


## Säännöt

Säännöt pohjautuvat vahvasti pohjoismaisen Yatzyn [sääntöihin](https://fi.wikipedia.org/wiki/Yatzy), sillä muunnelmalla että tässä tapauksessa ei tarvitse päättää etukäteen mitä yhdistelmää hakee takaa.

## Python

Sovellus on kehitetty sekä testattu Python 3.8:lla.

## Asennus

1. Suorita "poetry install" komento juurihakemistossa

2. Käynnistä sovellus komennolla "poetry run invoke start"

Vaihtoehtoisesti varsinkin Windowsilla suosittelen käyttämään sovellusta Pythonilla
avaamalla sen komennolla "main.py" src-hakemistossa.


## Dokumentaatio 
[Määrittelydokumentti](https://github.com/JVS23/ot-harjoitustyo/blob/master/Yatzy-app/dokumentaatio/vaatimusmaarittely.MD)

[Työaikakirjanpito](https://github.com/JVS23/ot-harjoitustyo/blob/master/Yatzy-app/dokumentaatio/tyoaikakirjanpito.MD)

## Testaus 

Komennoilla "poetry run invoke test" ja "poetry run invoke coverage-report"
voidaan testata sovellusta sekä generoida testausraportti
