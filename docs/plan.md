"# 05-projekts" 
A. Programmas apraksts (2–3 teikumi) 
Programma ļauj lietotājam reģistrēt ikdienas izdevumus, grupēt tos pa kategorijām, skatīt mēneša kopsummas un eksportēt datus CSV failā.

B. Datu struktūra 

    "date": "2025-05-24", 
    "amount": 20.50, 
    "category": "Apģerbs", 
    "description": "Bikses" 

    Tieši šāda struktūra ietver sevī visus nepieciešamus parmatrus, kas raksturo izdevumus.

C. Moduļu plāns 

Failā būs faili:
1) app.py -Galvenā programma (izvēlne, lietotāja mijiedarbība)
2) export.py - CSV eksports
3) logic.py - Biznesa loģika (filtrēšana, grupēšana, summas)
   failā būs fuknkcijas: 
filter_by_month(expenses, year, month) - Atgriež tikai norādītā mēneša izdevumus 
sum_total(expenses) - Aprēķina kopējo summu 
sum_by_category(expenses) - Atgriež summārās vērtības pēc kategorijām
get_available_months(expenses) - Atgriež unikālo mēnešu sarakstu 

4) storage.py - JSON failu operācijas
 būs fukcijas: load_expenses() - funkicja Nolasa failu expenses.json; ja fails neeksistē — atgriež [] 
 save_expenses(expenses) - funkicja saglabā sarakstu JSON failā

D. Lietotāja scenāriji 

Apraksti 2–3 scenārijus: ko lietotājs dara un ko programma atbild. 
1)  Lietotājs pievieno izdevumu bez summas — programma parāda kļūdas paziņojumu un ļauj mēģināt vēlreiz.
2) Saraksts ir tukšs, lietotājs izvēlas "Parādīt". Programma atgriež paziņojumu: "Saraksts ir tukšs." Un piedavās izvēlēties funkciju "Pievienot izdevumu"
3) Lietotājs izvēlas komandu "Kopsavilkums pa kategorijām". Programma izvada sekojošo informāciju:

  Apģerbs:          50.00 EUR 
  Transports:       30.00 EUR 
  KOPĀ:          80.00 EUR 

E. Robežgadījumi 
Kas notiek, ja expenses.json neeksistē? ja fails neeksistē — atgriež [] 
Kas notiek, ja lietotājs ievada negatīvu summu? Tukšu aprakstu? Nepareizu datumu? 
Programma izved kļūdas paziņojumu un prasa ievadīt vērtības vēlrei, pieminot, kādas vērtības ir atļaujamas.
Kas notiek, ja saraksts ir tukšs un lietotājs izvēlas "Parādīt"? Programma atgriež paziņojumu: "Saraksts ir tukšs, vai ievadīsim vērtības?"