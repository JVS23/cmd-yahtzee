# Cmd-Yatzy
 
 Cmd-Yatzy on tehty HY:n ohjelmistotekniikan kurssilla harjoitustyönä. Nimensä mukaisesti sillä on tarkoitus pelata Yatzya komentorivillä. Sovellusta on mahdollista pelata 1-4 pelaajalla vuoroittain.


## Säännöt

Säännöt pohjautuvat pitkälti [pohjoismaisen Yatzyn sääntöihin](https://fi.wikipedia.org/wiki/Yatzy), sillä muunnelmalla että tässä tapauksessa ei tarvitse päättää etukäteen mitä yhdistelmää hakee takaa.


## Python

Sovellus on kehitetty sekä testattu Python 3.8:lla. 


## Asennus

Lataa uusin release [täältä](https://github.com/JVS23/ot-harjoitustyo/releases) valitsemassasi muodossa Assets-osiosta.

Sovellusta voi käyttää Pythonilla runnaamalla tiedoston main.py. Muistathan asentaa tabulaten esim. pip:in avulla komennolla "pip install tabulate" tässä tapauksessa.

Sovellusta voi myös käyttää Poetryn kautta suorittamalla seuraavan komennon juurihakemistossa (Varmistathan, että sinulla on poetry asennettuna):
```bash
poetry install
```

3. Käynnistä sovellus komennolla:
```bash
poetry run invoke start
```


***Poetryllä runnattuna ohjelman toiminta on lievästi sanottuna kyseenalaista, joten vahva suositukseni on käyttää sovellusta suoraan commandlinelta Pythonilla.***


## Dokumentaatio 

[Käyttöohje](https://github.com/JVS23/ot-harjoitustyo/blob/master/Yatzy-app/dokumentaatio/kayttoohje.md)

[Vaatimusmäärittely](https://github.com/JVS23/ot-harjoitustyo/blob/master/Yatzy-app/dokumentaatio/vaatimusmaarittely.MD)

[Testausdokumentti](https://github.com/JVS23/ot-harjoitustyo/blob/master/Yatzy-app/dokumentaatio/testaus.MD)

[Arkkitehtuurikuvaus](https://github.com/JVS23/ot-harjoitustyo/blob/master/Yatzy-app/dokumentaatio/arkkitehtuuri.MD)


## Testaus 

Komennoilla "poetry run invoke test" ja "poetry run invoke coverage-report"
voidaan testata sovellusta sekä generoida testausraportti. Näistä lisää testausdokumentissa.

Sovelluksessa on käytössä myös pylint, jota voi testata poetry shellissä ("python3 -m poetry shell") komennolla pylint src. 
