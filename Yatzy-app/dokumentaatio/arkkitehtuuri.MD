# Arkkitehtuurikuvaus

## Tiivistelmä

Sovellus ei ole äärimmäisen monimutkainen, joten mielestäni olisi jopa haitallista kuvata sitä 
hienoilla buzzwordeilla ja kaavioilla yksinkertaisen tiivistelmän sijaan.

Sovelluksen käyttöliittymä, kovin yllättäen, on kokonaan commandlinellä. Lähes kaikki commandlinelle
tulostuva käyttöliittymä tulee luokalta UI.

Sovelluslogiikka vuorostaan tulee luokilta Dice, Player ja Categories. 

- Dice-luokka on vastuussa noppien olemassaolosta,
niiden heittämisestä sekä käsittelystä kuten printtaamisesta ja nollaamisesta. 
- Player-luokka vastaa enimmäkseen pelaajien pisteiden ylläpidosta ja pistetaulukon käsittelystä.
- Categories-luokka (scorelogic.py-tiedostossa, älä kysy) sisältää kaikki pisteytyskategoriat, 
joista valittuun nopat pisteytetään, ja pisteet lähetetään aktiiviselle Player-objektille.

