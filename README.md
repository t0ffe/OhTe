
# OhTe-tris

Klooni tetris pelistä. Ohjelmistotekniikka 2023-kurssin harjoitustyö.


## Dokumentaatio

- [Vaatimusmaarittely](dokumentaatio/vaatimusmaarittely.md)
- [Tuntikirjanpito](dokumentaatio/tuntikirjanpito.md)
- [Changelog](dokumentaatio/changelog.md)
- [Arkkitehtuurikuvaus](dokumentaatio/arkkitehtuuri.md)

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

### Pylint

Tiedoston [.pylintrc](./.pylintrc) määrittelemät tarkistukset voi suorittaa komennolla:

```bash
poetry run invoke lint
```

# Release

[latest release](https://github.com/t0ffe/OhTe/releases/tag/viikko6)
