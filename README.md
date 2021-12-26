# Cmd-Yatzy
 
 Cmd-Yatzy on tehty HY:n ohjelmistotekniikan kurssilla harjoitustyönä. Nimensä mukaisesti sillä on tarkoitus pelata Yatzya komentorivillä. Sovellusta on mahdollista pelata 1-4 pelaajalla vuoroittain.


## Säännöt

Säännöt pohjautuvat pitkälti pohjoismaisen Yatzyn [sääntöihin](https://fi.wikipedia.org/wiki/Yatzy), sillä muunnelmalla että tässä tapauksessa ei tarvitse päättää etukäteen mitä yhdistelmää hakee takaa.


## Python

Sovellus on kehitetty sekä testattu Python 3.8:lla. 


## Asennus

1. Lataa uusin release [täältä](https://github.com/JVS23/ot-harjoitustyo/releases) valitsemassasi muodossa Assets-osiosta.

2. Suorita seuraava komento sovelluksen juurihakemistossa (Varmistathan, että sinulla on poetry asennettuna):
```bash
poetry install
```

3. Käynnistä sovellus komennolla:
```bash
poetry run invoke start
```

Muistathan myös käyttää tarpeellisia prefixejä komennoissa systeemistäsi riippuen, kuten "python -m" tai "python3 -m"

Vaihtoehtoisesti sovellusta voi käyttää Pythonilla avaamalla sen komennolla "main.py" src-hakemistossa. Muistathan asentaa tabulaten pip:in avulla komennolla "pip install tabulate" tässä tapauksessa. **Poetryn kautta runnattuna ohjelman toiminta on lievästi sanottuna kyseenalaista, joten vahva suositukseni on käyttää sovellusta tällä tavalla Pythonilla.**


## Dokumentaatio 

[Käyttöohje](https://github.com/JVS23/ot-harjoitustyo/blob/master/Yatzy-app/dokumentaatio/kayttoohje.MD)

[Määrittelydokumentti](https://github.com/JVS23/ot-harjoitustyo/blob/master/Yatzy-app/dokumentaatio/vaatimusmaarittely.MD)

[Työaikakirjanpito](https://github.com/JVS23/ot-harjoitustyo/blob/master/Yatzy-app/dokumentaatio/tyoaikakirjanpito.MD)


## Testaus 

Komennoilla "poetry run invoke test" ja "poetry run invoke coverage-report"
voidaan testata sovellusta sekä generoida testausraportti.
Sovelluksessa on käytössä myös pylint, jota voi testata poetry shellissä komennolla pylint src. 
Main on toistaiseksi poisluettu testauksesta sillä se on suurimmilta osin UI:ta, ensiviikon toteutuksessa eritytän UI:n omaan tiedostoonsa.
