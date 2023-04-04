
# OhTe-tris

Klooni tetris pelistä. Ohjelmistotekniikka 2023-kurssin harjoitustyö.


## Dokumentaatio

- [Vaatimusmaarittely](dokumentaatio/vaatimusmaarittely.md)
- [Tuntikirjanpito](dokumentaatio/tuntikirjanpito.md)
- [Changelog](dokumentaatio/changelog.md)

## Komentorivitoiminnot
### Pelin käynnistäminen
Pelin pystyy käynnistämään komennolla:

```bash
poetry run invoke start
```
### Testaus
Testit suoritetaan komennolla:
```bash
poetry run invoke test
```
### Testikattavuus
Testikattavuusraportin voi generoida komennolla:
```bash
poetry run invoke coverage-report
```
Testikattavuusraportin löytää _htmlcov_-hakemistosta.
