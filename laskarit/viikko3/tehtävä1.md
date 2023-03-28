
```mermaid
classDiagram
    Peli "1" -- "2...8" Pelaaja
    Peli "1" -- "1" Pelilauta
    Peli "1" -- "2" Noppa
    
    Pelilauta "1" -- "40" Ruutu

    Pelaaja "1" -- "1" Pelinappula
    Pelinappula "0...8" -- "1" Ruutu
    Ruutu "1" -- "1" Ruutu
```
