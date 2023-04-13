# Kontrolni-sistem-za-ulaz-u-banku

Simulira se sistem za ulazak u banku pomocu troje vrata. Kroz prva vrata se ulazi u sobu za cekanje ocitavanjem RFID kartice. Ako kartica postoji u bazi korisnik se pusta, u suprotnom se pali alam i id kartice se ispisuje u datoteku _provalnik.txt_. Kroz druga vrata se izlazi iz sobe za cekanje i ulazi u banku pomocu kapacitivnog senzora dodira. Pritiskom na njega aktivira se prekid i proverava se da li su prva vrata zatvorena sto se simulira uz pomoc ultrazvucnog senzora koji meri razdaljinu. Kroz treca vrata se izlazi iz banke i to se realizuje unosenjem sifre za izlaz. Python i Arduino sve vreme razmenjuju podatke uz pomoc serijske komunikacije. :bank: :safety_vest:

Alati i programski jezici korisceni: :toolbox:

- Python
- Arduino IDE with Serial communication
