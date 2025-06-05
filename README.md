# Bezpieczne przechowywanie haseł w aplikacjach

To repozytorium jest częśćią projektu na przedmiot Bezpieczeństwo systemów informatycznych "Bezpieczne przechowywanie haseł w aplikacjach.". Zawiera implementacje popularnych algorytmów haszujących, takich jak MD5, SHA-1, SHA-256, bcrypt oraz argon2 (argon2-cffi).

## Pliki

- `main.py` – główny plik uruchamiający proces haszowania haseł z pliku `passwords.txt` i zapisujący wyniki do folderu `hashed_passwords`.
- `hashers.py` – zawiera funkcje do haszowania haseł różnymi algorytmami.
- `utils.py` – funkcje pomocnicze do odczytu i zapisu plików.
- `passwords.txt` – przykładowa lista haseł do przetworzenia.
- `hashed_passwords/` – folder z wynikami haszowania dla każdego algorytmu.

## Wymagania

- Python 3.x
- Biblioteki: `bcrypt`, `argon2-cffi`

Instalacja zależności:

```
pip install bcrypt argon2-cffi
```

## Jak uruchomić

1. Umieść hasła do przetworzenia w pliku `passwords.txt` (każde hasło w osobnej linii).
2. Uruchom skrypt:

```
python main.py
```

3. Wyniki zostaną zapisane w folderze `hashed_passwords` w osobnych plikach dla każdego algorytmu.

## Algorytmy

- MD5
- SHA-1
- SHA-256
- bcrypt
- argon2

## Licencja

MIT
