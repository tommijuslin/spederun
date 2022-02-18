# spederun

https://tsoha-spederun.herokuapp.com/

Rekisteröidy/kirjaudu normaalisti tai testaa ohjelmaa ylläpitäjänä:

- käyttäjänimi: admin
- salasana: admin

## Mikä ihmeen spederun?

Spederun on sovellus, joka pitää kirjaa videopelien [speedrun](https://en.wikipedia.org/wiki/Speedrun)-ennätyksistä. Speedruneissa on tarkoitus pelata peli tai sen osa läpi mahdollisimman nopeasti.

## Spederunin käyttäminen

Sivustoa voi selailla vapaasti kirjautumatta.

### Kirjautumattoman käyttäjän mahdolliset toiminnot:
- katso yksittäisen pelin speedruneja klikkaamalla pelin nimeä
- katso eri kategorioiden speedruneja klikkaamalla haluamaasi kategoriaa pelisivulta
- katso tietyn käyttäjän speedruneja klikkaamalla käyttäjänimeä
- etsi pelejä syöttämällä yläreunassa olevaan hakukenttään pelin nimi (tai osa nimestä)

### Kirjautuneen käyttäjän toiminnot:
- lisää peli etusivun Add Game -nappia painamalla
- lisää pelille speedruni siirtymällä pelisivulle ja klikkaa Submit Run -nappia. (kts. seuraava kohta)
- jos pelillä ei ole vielä yhtään kategoriaa, on sellainen lisättävä ennen speedrunin lisäämistä. Lisää kategoria klikkaamalla Add Category -nappia.
- oman speedrunin poistaminen. Siirry omalle käyttäjäsivullesi painamalla yläreunasta löytyvää käyttäjänimeäsi. Paina haluamasi ajan vieressä olevaa ruksia ja paina OK-nappia.

### Ylläpitäjän toiminnot:
- pelien, speedrunien ja kategorioiden poistaminen

## Kehityskohteet
- speedrunien filtteröinti pelialustan mukaan (näyttää epätodennäköiseltä tällä hetkellä)
- spagettikoodin siivoaminen
