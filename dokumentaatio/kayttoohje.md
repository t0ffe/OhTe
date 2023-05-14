# Käyttöohje

Lataa projektin viimeisimmän [releasen](https://github.com/t0ffe/OhTe/releases) lähdekoodi valitsemalla _Assets_-osion alta _Source code_.

## Ohjelman käynnistäminen

Ennen ohjelman käynnistämistä, asenna riippuvuudet komennolla:

```bash
poetry install
```

Jonka jälkeen suorita alustustoimenpiteet komennolla:

```bash
poetry run invoke build
```

Nyt ohjelman voi käynnistää komennolla:

```
poetry run invoke start
```

## Pelaaminen / Kontrollit

Peliä voi pelata joka WASD- tai nuolinäppäimillä.

    - Sivulle liikutta palikkaa
    - Ylös kääntää palikkaa
    - Alas nopeuttaa palikan alas
