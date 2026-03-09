# Ofdo
"Ofdo" on EELK Tartu Pauluse koguduse tehnikatiimi otseülekannete slaidide generaator. Programm võtab sisendina laulude numbrid, kirjakohad ja kaasa teenijad, mille põhjal loob see kasutatava .odp slaidide faili, mida on võimalik käsitsi edasi kontrollida ja parandada.


## Kuidas see töötab?
1. Käivitades leiab programm leiab järgmise teenistuse kuupäeva, kellaaja ja liturgilise korra. Vajadusel kasutab selleks kasutaja antud lippe (-h flags).
2. Seejärel saab kasutaja sisestada vajalikud andmed. Iga uut numbrit või kirjakohta sisestades otsib programm selle üles, et kontrollida, kas see eksisteerib.
3. Lõpuks hakkab programm slaide ühekaupa genereerima, kasutades välja otsitud laule ja kirjakohti eelmisest punktist. Kui tekib olukord, kus programm ei oska kirjakohta järgmisele slaidile poolitada, siis küsib see kasutaja nõu.
4. Slaidid salvestatakse programmiga samasse asukohta.


## Ofdo ajaloost
Ofdo arendustöö algas 7. detsembril 2025. Jõululaupäevaks (24. detsember 2025) oli valmis esimene versioon (v100), sellest ülejärgmisel päeval versioonid v101 ja v102. Vanaaastaõhtuks (31. detsember 2025) oli valmis ka esimene macOS versioon. Peale seda läks suureks vigade parandamiseks ja Ofdo arendus edenes hoogsa tempoga (v103 valmis 3. jaanuaril 2026, v104 valmis 18. jaanuaril 2026 ja v105 valmis 24. jaanuaril 2026). Peale versiooni v105 aeglustus arendustöö, sest v105 oli esmakordselt päris stabiilne versioon, mida oli võimalik järjekindlalt kasutada. Versioon v106 koos erinevate parandustega ja automaatse uuendamisega valmis 8. märtsil 2026.
