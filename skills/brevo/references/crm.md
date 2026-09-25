# Brevo, CRM e Sales Platform: deal, pipeline, task, punteggi

Approfondimento per la sezione 5b di SKILL.md. Fonti: articoli di help.brevo.com letti via API Zendesk il 25/09/2026 (data di aggiornamento tra parentesi). Prezzi in dollari come esposti nell'articolo add-on; quelli in euro si leggono nel pannello dell'account.

## 1. Cosa è incluso e cosa si paga

Fonte: [4409354969746](https://help.brevo.com/hc/en-us/articles/4409354969746) (24/09/2026).

- **Gratis in ogni piano**: **50 deal aperti** e **1 pipeline**, prenotazione meeting, live chat, report ricavi / ciclo di vendita / team, previsione, task e promemoria, **1 calendario e 1 casella collegati**, app mobile Conversations, agente AI per Conversations.
- **Sales Essentials, 31 $/mese** (add-on su Starter, Standard, Professional, Enterprise; **multiutente solo da Standard in su**): deal e pipeline illimitati, **automazioni di vendita** (trigger e azioni Deals/Meetings/Conversations/Phone, vedi references/automazioni.md), scenari chatbot e risposte salvate, **regole di fase**, arricchimento AI di contatti e aziende, calendari e caselle illimitati, Instagram DM e Messenger, niente logo Brevo sulla chat, visitatori live, analytics Conversations.
- **Sales Advanced, 64 $/mese** (solo Professional ed Enterprise): tutto Essentials più sequenze di outreach, chatbot AI, **telefono VoIP** con registrazione, segreteria, menu, trasferimento, trascrizioni e riassunti AI, statistiche chiamate, **più valute nei deal**, round-robin dei meeting, SMS e WhatsApp 1:1, email di follow-up AI.
- **Posti (seats)**: ogni piano include 1 seat vendita; gli aggiuntivi costano quanto il pacchetto (31 o 64 $/mese l'uno): Standard + Essentials **fino a 5**, Professional **fino a 50**, Enterprise illimitati. Posti marketing: Free, Starter e Standard 1 (Standard fino a 3 con add-on da **12 $/mese** l'uno), Professional 10, Enterprise illimitati.
- ⚠️ Gli add-on si pagano subito **pro rata** fino alla prossima fattura, poi mensili, e **non sono rimborsabili**.
- **Limite dei 50 deal aperti**: oltre, la creazione (anche da automazione e da import) richiede un pacchetto ([360018942140](https://help.brevo.com/hc/en-us/articles/360018942140), 12/08/2026; [8739207130514](https://help.brevo.com/hc/en-us/articles/8739207130514), 20/05/2026).

## 2. Gli oggetti: contatti, aziende, deal, task

Fonti: [360019084619](https://help.brevo.com/hc/en-us/articles/360019084619) (17/08/2026), [8694983060754](https://help.brevo.com/hc/en-us/articles/8694983060754) (31/08/2026), [4406754397970](https://help.brevo.com/hc/en-us/articles/4406754397970) (02/09/2026).

- **Le associazioni sono sempre bidirezionali** (azienda ↔ contatti ↔ deal ↔ task) e sincronizzano lo storico: una nota sull'azienda compare anche nel deal associato.
- **Aziende create da sole**: Settings > Companies > Automated company management, "Automatically create and associate companies with contacts" crea o collega l'azienda **dal dominio dell'email** del contatto nuovo, **solo domini aziendali** (non gmail, hotmail). L'**arricchimento automatico** (settore, dimensione, sito, da fonti terze fra cui LinkedIn, tramite Aura) richiede un pacchetto Sales.
- **Associazione in blocco** via export e reimport: nel file dell'azienda (o del deal) si aggiungono colonne chiamate **esattamente** `Associated Deal` e `Associated Contact` (ID del deal; email o ID del contatto); una riga per ogni coppia (stessa azienda su più righe per più contatti); all'import si spunta "Associate ... to the corresponding objects"; per correggere un errore si reimporta con "Dissociate". ⚠️ L'export dei contatti **non** si può usare per associare: si parte da aziende o deal.
- **Attributi** ([10617359589906](https://help.brevo.com/hc/en-us/articles/10617359589906), 24/09/2026; [4415093924370](https://help.brevo.com/hc/en-us/articles/4415093924370), 20/08/2026): sette tipi (testo fino a 10.000 caratteri, data 1900-2050 in DD-MM-YYYY / MM-DD-YYYY / YYYY-MM-DD, numero fino a 15 cifre, categoria, scelta multipla, booleano, utente); **200 attributi contatto** per account, nomi fino a 50 caratteri alfanumerici e underscore senza cifra iniziale; 🔴 **nome e tipo non si modificano**: si cancella e si ricrea **perdendo i dati**; gli attributi nuovi sono nascosti dalla scheda finché non li si aggiunge alla vista. Per deal e aziende stessi sette tipi, da Settings > Deals > Deals attributes e Settings > Companies.
- **Attributi di default del deal** ([9229566234002](https://help.brevo.com/hc/en-us/articles/9229566234002), 08/04/2026): obbligatori *Name*, *Deal owner* (default: proprietario dell'account se manca nell'import), *Deal stage* (default *New*), *Pipeline*; poi *Amount*, *Close date*, *Closed won/lost reason* (testo), *Lost reason* (categoria modificabile: ⚠️ **cancellare una categoria cancella il motivo su tutti i deal**), *Deal description*. Calcolati da Brevo e non modificabili: *Created at*, *Last activity date*, *Last updated date*, *Number of activities*, *Number of contacts*, *Owner assign date*, *Stage updated at*. "Number of activities" e "Last activity date" sono le colonne per trovare i deal fermi.
- **Task** ([360019727819](https://help.brevo.com/hc/en-us/articles/360019727819), 10/07/2026): tipi **To do, Email, Call, Meeting, Lunch, Deadline, LinkedIn**; scadenza con ora, promemoria email e/o browser, priorità alta, note, associazione a contatti/aziende/deal, assegnazione. Notifiche in Settings > Deals > My notifications: promemoria task, task assegnato, contatto assegnato, **report task settimanale e giornaliero** ([360001192499](https://help.brevo.com/hc/en-us/articles/360001192499), 09/04/2026).
- **Proprietario del contatto** ([360001192599](https://help.brevo.com/hc/en-us/articles/360001192599), 06/09/2026): a mano (anche in blocco da CRM > Contacts > More actions > Assign, "No owner" per togliere) o da automazione con utente fisso o **round-robin**; si filtra con la condizione *Their contact owner*. Il deal creato da automazione eredita il proprietario del contatto.
- **Viste salvate** ([25889576395922](https://help.brevo.com/hc/en-us/articles/25889576395922), 07/04/2026): filtri + colonne + ordinamento salvati come tab su Contacts, Deals, Companies; le viste di default (All, My) non si sovrascrivono, si salvano come nuove. **Filtri utili sui deal** ([360019091500](https://help.brevo.com/hc/en-us/articles/360019091500), 10/09/2026): per proprietario, per *Close date* nel periodo (i più urgenti), per fase Won/Lost (solo vista elenco), per *Activities > Has overdue task = True* (i deal fermi).

## 3. Pipeline e fasi

Fonti: [9388306270226](https://help.brevo.com/hc/en-us/articles/9388306270226) (03/02/2026), [360019003659](https://help.brevo.com/hc/en-us/articles/360019003659) (13/05/2026), [360019089760](https://help.brevo.com/hc/en-us/articles/360019089760) (07/04/2026).

- **Pipeline di default, 7 fasi**: New → Qualifying → Demo scheduled → Pending commitment → In negotiation → Won / Lost. **Won e Lost sono fisse** (si rinominano, non si spostano né cancellano). Da **3 a 20 fasi**, nomi unici. Più pipeline solo con un pacchetto Sales.
- ⛔ **Cancellare una pipeline cancella i suoi deal**: prima si spostano; la pipeline di default non si cancella finché non se ne nomina un'altra.
- **Fasi ben fatte**: una per ogni passo reale del processo, con etichette che non lasciano dubbi ("Preventivo inviato", "Contratto firmato"), non stati d'animo ("Interessato").
- **Regole di fase** (Sales Essentials): attributi "importanti" da compilare per passare a una fase; renderli **obbligatori** richiede Sales Advanced.
- **Pipeline pesata**: Settings > Deals > Pipelines settings > tab Estimated Revenue, "Show estimated revenue for each stage"; poi una **probabilità di vittoria 0-100% per fase** nella tab Pipelines. Esempio Brevo: fase Qualifying al 15% con 5 deal per 38.530 $ → ricavo atteso **5.779,50 $**. Il ricavo stimato per fase si legge nella vista Cards passando sull'icona informativa; con più valute anche per valuta (solo Sales Advanced su Professional).

## 4. Deal: creare, importare, chiudere

- **Creare** (360018942140): da CRM > Deals, dalla scheda contatto o dalla scheda azienda, anche con Aura; se il contatto ha un'azienda associata il campo azienda è precompilato; **il task di follow-up è spuntato per default** (tipo, nome, scadenza); i campi obbligatori si scelgono in "Manage deal creation attributes". Per **deal privati per utente** si toglie il permesso "Manage deals and tasks from other users".
- **Importare** (8739207130514): un CSV alla volta, con mappatura degli attributi (anche creati durante l'import, categorie comprese); per associare si mettono nel file **email o ID del contatto** e **nome o ID dell'azienda**; ⚠️ "Use company name to update existing companies" acceso, altrimenti **ogni riga crea un'azienda nuova** e si producono duplicati; "Import empty fields to erase existing attribute data" compare solo se il file ha l'ID del deal e cancella i valori esistenti; report di import con file degli errori.
- **Chiudere**: vinto o perso con motivo (categoria *Lost reason* personalizzabile, testo libero *Closed lost reason*); un deal chiuso si può riaprire; *Duplicate a deal* da automazione ricrea i persi per riprovarci.

## 5. Report di vendita

Fonte: [9664360658962](https://help.brevo.com/hc/en-us/articles/9664360658962) (12/08/2026), CRM > Deals > Reports, per tutte le pipeline o per una.

- **Revenue report**: ricavo dei deal **vinti** nel periodo, numero e valore medio, per mese; **Current pipeline value**: valore totale e stimato per fase dei deal aperti.
- **Sales cycle report**: tasso di vittoria, **motivi di perdita** (con 6 o più motivi il grafico mostra i 5 principali più "Other reasons", l'elenco completo sta accanto), tasso di conversione fra fase e fase sui deal chiusi, **tempo medio per vincere** (da creazione a chiusura, esclusi i deal con chiusura precedente alla creazione) e tempo medio per fase sui vinti (⚠️ **esclude le permanenze sotto l'ora**: i due numeri non tornano fra loro, ed è normale).
- **Team report**: per utente tempo medio per vincere, valore medio, deal vinti, tasso di vittoria, quota di ricavo, totale; **solo deal chiusi**; medaglia al primo.
- Cosa portare a un cliente: ricavo vinto e valore pipeline pesato (dal Revenue report), tasso di vittoria e primi tre motivi di perdita (Sales cycle), deal con task scaduti (filtro). Il "valore pipeline" non pesato è un numero da vetrina, non una previsione.

## 6. Punteggi automatici e predittivi

Fonte: [30822459476114](https://help.brevo.com/hc/en-us/articles/30822459476114) (10/09/2026). Richiedono **dati e-commerce** (ordini da plugin o API). Attributi con prefisso `SCORE_`, ricalcolati a intervalli, **nascosti per default** (si aggiungono alla scheda o alla vista). ⛔ Non si modificano né si cancellano a mano.

| Punteggio | Attributo | Cosa restituisce |
|---|---|---|
| Tempo fra ordini | `SCORE_TIME_BETWEEN_ORDERS` | giorni medi fra due ordini consecutivi, servono almeno 2 ordini |
| Periodi chiave | `SCORE_KEY_SHOPPING_PERIODS` | scelta multipla fra San Valentino (7-14/02), Pasqua (7 giorni prima), Halloween (24-31/10), Black Friday (4 giorni prima, 3 dopo), Natale (18-25/12) |
| Comportamento d'ordine | `SCORE_ORDERING_BEHAVIOUR` | categoria: Orders consistently → Ordered recently → About to order → Late order → Very late order → No recent order → Ordered once → Never ordered |
| RFM | `SCORE_RECENCY_FREQUENCY_MONETARY` | categoria da Champion a Lost più Prospect, calcolata a **sestili (NTILE 6) sull'intera base**: **relativa**, un contatto cambia segmento anche se non ha fatto nulla |
| CLV | `SCORE_CUSTOMER_LIFETIME_VALUE` | valore medio ordine del contatto × ordini medi per cliente (tutti) × durata media (tutti); **un solo ordine = CLV 0** |

- **Predittivi** (Professional, Enterprise nuovo, CDP legacy): `SCORE_PREDICTIVE_CHURN_RISK` (0-1: 0,85 alto rischio), `SCORE_PREDICTIVE_PURCHASES_EXPECTED` (acquisti attesi nei prossimi 12 mesi, decimale), `SCORE_PREDICTIVE_CLV` (valore atteso a 12 mesi; con un solo ordine usa il valore osservato).
- **Finestra di calcolo**: Settings > Contacts > Scores, per singolo punteggio, ultimi 3/6/12/24 mesi o tutto; il ricalcolo **può richiedere fino a 24 ore**.
- Uso: segmenti (Key shopping periods = Black Friday, un mese prima del Black Friday), trigger di automazione al cambio di attributo (Ordering behavior = Very late order → winback), personalizzazione (CLV alto → prodotti premium).
- **Formule COUNT e SUM** ([209558545](https://help.brevo.com/hc/en-us/articles/209558545), 19/09/2026) sui parametri transazionali: fino a **50 valori calcolati** per contatto (es. `SUM[ORDER_VALUE,ORDER_DATE,>,NOW(-30)]` = speso negli ultimi 30 giorni) e **30 valori calcolati globali** sulla dashboard. Sono lo strumento vecchio: con i plugin e-commerce i punteggi `SCORE_` fanno lo stesso lavoro senza formule.

## 7. Meetings e Conversations

Fonti: [7073284620306](https://help.brevo.com/hc/en-us/articles/7073284620306) (10/09/2026), [6214223669138](https://help.brevo.com/hc/en-us/articles/6214223669138) (16/09/2026).

- **Meetings**: pagina di prenotazione con tipi di meeting (di serie *Intro* 15 minuti e *30-minute meeting* in video, oppure personalizzati per nome, strumento e durata), calendario **Google o Outlook** collegato per evitare doppie prenotazioni, disponibilità di default **lunedì-venerdì 9-17** modificabile per tipo. I trigger *Meeting booked/started/canceled* nelle automazioni richiedono un pacchetto Sales; la condizione di segmento *Meeting booked* compare dopo la prima prenotazione.
- **Conversations**: widget chat installato con un clic se c'è già il tracker o un plugin (Settings > Inbox > Chat widget), altrimenti guide per WordPress, WooCommerce, Shopify, GTM, landing; canali collegabili Messenger, Instagram Direct, WhatsApp, email; scenari chatbot, form di contatto offline, risposte salvate, chat mirate, gruppi di agenti. Instagram e Messenger richiedono Sales Essentials (4409354969746).

## 8. Ordine di controllo di un CRM Brevo ereditato

Sintesi operativa, non una pagina Brevo.

1. Piano e pacchetti: quanti deal aperti sui 50 gratuiti, quante pipeline, quanti seat.
2. Pipeline: fasi con nomi chiari, probabilità impostate o no, regole di fase.
3. Deal senza contatto associato: le automazioni di vendita non li vedono.
4. Aziende duplicate da import senza "Use company name"; creazione automatica dal dominio accesa o spenta.
5. Attributi: quanti dei 200 usati, quali obbligatori alla creazione.
6. Task scaduti per proprietario (filtro *Has overdue task*), notifiche attive per chi vende.
7. Report: tasso di vittoria e motivi di perdita degli ultimi 12 mesi, tempo medio per fase.
8. Punteggi `SCORE_` presenti (serve il plugin e-commerce), finestra di calcolo, chi li ha modificati a mano.
