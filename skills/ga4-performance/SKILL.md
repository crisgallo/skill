---
name: "ga4-performance"
description: "Regole operative verificate per configurare, igienizzare e interrogare Google Analytics 4: eventi chiave, filtri dati, esplorazioni, report personalizzati, raccolte e menu, attribuzione, collegamenti a Google Ads e Search Console. Usare ogni volta che si lavora sul pannello GA4, si costruisce un report, si rifa il menu, o si giudica un numero prima di portarlo su un pannello che spende. Serve anche per fare l'igiene di una proprieta ereditata."
---

# GA4: regole operative

**Ultima verifica delle fonti: 23 settembre 2026.**

---

## 0. Manutenzione di questa skill (leggere per primo)

Vale la stessa regola delle skill Meta e Google Ads: se la data qui sopra ha più di due o tre mesi, si ricontrolla sulle fonti ufficiali prima di applicare un numero. Quando una fonte smentisce una regola scritta qui, la skill si aggiorna nello stesso turno, si riscrive la data e si annota cosa è cambiato.

Questa skill ha due metà, e vanno tenute distinte.

- **Conoscenza di dominio**: come si comporta GA4. Si verifica sulle fonti ufficiali Google.
- **Meccanica del pannello** (sezioni 4 e 5): come si comporta l'interfaccia quando ci lavori dentro. Non sta in nessuna documentazione, si impara sbagliando, e va scritta qui la prima volta che succede.

⚠️ Ogni volta che si aggiorna la skill si riallinea la copia in `Blog/skills/` e la riga nel README, nello stesso turno.

🔴 **Le soglie marcate `[DA VERIFICARE]` non sono state confermate su fonte ufficiale al 20/09/2026.** Non si citano a un cliente e non si usano per una decisione di spesa finché non hanno una fonte accanto. Al 20/09/2026 ne resta una sola, la cardinalità (sezione 8): Google non pubblica il numero.

✅ Quello che è marcato **VERIFICATO** è stato osservato di persona sul pannello, con la data accanto.

### Cosa è cambiato il 20/09/2026

Primo giro di manutenzione sulle fonti ufficiali, con le note di rilascio GA4 (https://support.google.com/analytics/answer/9164320) lette da giugno a settembre 2026.

- **Sezione 7, UTM e auto-tagging**: la regola era capovolta. Con auto-tagging attivo vincono i valori auto-taggati, non esiste override, gli UTM manuali non rompono l'importazione delle conversioni (https://support.google.com/analytics/answer/11242870).
- **Sezione 6, modelli**: sono tre (basato sui dati, ultimo clic a pagamento e organico, ultimo clic canali a pagamento Google). Il cambio di modello è retroattivo; solo il cambio di finestra di lookback vale in avanti (https://support.google.com/analytics/answer/10597962).
- **Sezioni 3 e 6, soglie**: il thresholding non dipende più da "Google Signals nell'identità dei report"; dal 15/06/2026 Google Signals governa solo l'associazione con gli utenti loggati (https://support.google.com/analytics/answer/17016975).
- **Sezione 8, conservazione**: non tocca i confronti nei report standard, solo esplorazioni e canalizzazioni (https://support.google.com/analytics/answer/7667196).
- **Sezione 2, referral**: stesso dominio e sottodomini sono già esclusi da soli; il traffico escluso eredita la sorgente precedente, non va sempre in diretto (https://support.google.com/analytics/answer/10327750).
- **Chiusi i `[DA VERIFICARE]`** su eventi chiave (30/50), campionamento (10M), lookback (7/30 e 30/60/90) e definizioni personalizzate (50/50/25). Resta aperta la cardinalità.
- **Novità agosto-settembre 2026** dalle note di rilascio: finestre di conversione personalizzate 11/08/2026 (sezione 6); Dashboard dentro Report 09/09/2026 (sezioni 3 e 5, https://support.google.com/analytics/answer/17217303); filtro Hostname 11/06/2026 (sezione 2, https://support.google.com/analytics/answer/13296761); dimensione Source group 11/06/2026 (sezione 4); raccolta Google Business Profile 08/06/2026 (sezione 5); importazione costi con valuta obbligatoria 28/07/2026 e report di validazione 10/08/2026 (sezione 5).

---

## 1. Eventi chiave: la regola che decide tutto il resto

**Contrassegnare o togliere un evento chiave NON è retroattivo. I dati già raccolti restano contati come erano al momento della raccolta.** Lo dice anche Google: *"Marking an event as a key event affects reports from time of creation. It doesn't change historic data"* (https://support.google.com/analytics/answer/13128484). La stessa pagina avverte che un evento chiave nuovo impiega **fino a 24 ore** a comparire nei report standard.

È la cosa che cambia più decisioni di qualunque altra in questa skill, ed è il contrario di quello che quasi tutti danno per scontato.

✅ **VERIFICATO il 12/08/2026 sulla proprietà 494970795.** L'11/08 gli eventi chiave sono passati da 13 a 5, togliendo fra gli altri `page_view_articolo_blog`. Poi, in una esplorazione con righe *Campagna sessione* per *Nome evento* e valore *Eventi chiave*:

| periodo | riga | eventi chiave |
|---|---|---|
| 11 ago - 12 ago | `campaign_191706` / `page_view_articolo_blog` | **17** |
| 12 ago - 12 ago | `campaign_191706` / `page_view_articolo_blog` | **0** |

Stessa proprietà, stesso evento, stessa campagna. L'evento non è più chiave dall'11 agosto, ma le righe dell'11 agosto continuano a dichiarare 17 conversioni. Idem `lettura_articolo_blog`: 1 il giorno 11, 0 il giorno 12.

### Le tre conseguenze operative

1. **La data di pulizia è una frattura nella serie storica, non una correzione.** Un confronto che scavalca quella data mette insieme due definizioni diverse di conversione e produce un crollo che sembra performance ed è contabilità. Stesso identico problema delle finestre di attribuzione di Meta a gennaio 2026.
2. **Il periodo di default di ogni report sulle conversioni parte dal giorno DOPO la pulizia**, non dal giorno stesso: la pulizia avviene a metà giornata e quel giorno è misto, anche per la latenza fino a 24 ore di cui sopra.
3. **Non si aspetta.** Poiché non è retroattivo, ogni ora in cui un evento spazzatura resta contrassegnato è storico sporco che non si recupera. La pulizia degli eventi chiave si fa il giorno in cui si apre la proprietà, prima di qualunque altra cosa.

### Cosa può essere un evento chiave

Un evento merita la stella solo se ha **un tag suo nel container** e rappresenta **un'intenzione**, non un comportamento (criterio di metodo nostro, non regola GA4: su una fonte ufficiale non si trova). La verifica si fa su due fonti esterne alla lista, mai sulla lista stessa:

1. **Cosa arriva davvero**: Amministrazione, Visualizzazione dei dati, Eventi, scheda *Eventi recenti* (https://support.google.com/analytics/answer/12844695). Sono gli eventi ricevuti negli ultimi 28 giorni. Se un evento chiave non compare qui, o è rotto o non esiste più.
2. **Cosa è configurato**: i tag del container GTM con il rispettivo attivatore. Dicono quale push del dataLayer produce quale nome evento, e quindi dove cercare il guasto quando un nome non arriva.

Si costruisce la corrispondenza **tag → attivatore → nome evento** e la si confronta con le stelle. Le tre liste devono raccontare la stessa storia.

⚠️ **Gli eventi della misurazione avanzata non vanno quasi mai contrassegnati.** `form_submit`, `form_start`, `scroll`, `click`, `view_search_results` non hanno un tag nel container, scattano su qualunque elemento della pagina e si sovrappongono agli eventi veri. Marcarli significa contare doppio e non distinguere niente. Se un evento non ha un tag suo, chiedersi perché prima di trattarlo come conversione. Elenco degli eventi per opzione, e conferma che le opzioni si spengono una per una: https://support.google.com/analytics/answer/9216061.

⚠️ **`purchase` compare nell'elenco anche su un sito senza e-commerce.** GA4 lo mostra di default. Osservazione di pannello, non documentata.

🔴 **ATTENZIONE alla stella grigia di `purchase`: significa il CONTRARIO di quello che sembra.**

✅ **VERIFICATO il 19/09/2026 sulla proprietà Sceglinatura (a302851246p427921330).** Su una proprietà con e-commerce, `purchase` è **evento chiave d'ufficio e non si può togliere**. La sua stella appare **grigia e spenta** mentre quelle degli altri eventi chiave sono piene: passandoci sopra il tooltip dice *"Impossibile rimuovere il contrassegno dall'evento chiave"*. Grigio = **bloccato attivo**, non disattivato.

⛔ **È un errore già commesso due volte**: leggere quella stella come "purchase non è evento chiave" e annunciare un guasto grave che non esiste. La riga sopra ("senza stella è arredamento") vale **solo per un sito senza e-commerce**, dove `purchase` non scatta mai. Su un sito che vende non si applica.

📌 **Come si verifica in due secondi, invece di dedurlo dal colore**: si passa il mouse sulla stella. Se esce il tooltip di impossibilità, è bloccato attivo. Se esce la richiesta di conferma "Rimuovere il contrassegno da questo evento chiave?", allora era davvero attivo e modificabile.

⚠️ **Un evento chiave senza dati non è per forza da buttare.** Può essere rotto, oppure semplicemente non ancora cliccato da nessuno perché la pagina ha tre utenti in ventotto giorni. Le due cose si distinguono in Modalità Anteprima di GTM, non guardando il report.

### Il numero massimo

✅ **30 eventi chiave per proprietà standard, 50 per 360** (https://support.google.com/analytics/answer/13128484 e https://support.google.com/analytics/answer/12229528).

---

## 2. Filtri dati e traffico interno

### L'ordine è vincolante e sbagliarlo produce un filtro che non filtra

1. **Prima la regola di traffico interno**: Amministrazione, Raccolta e modifica dei dati, Stream di dati, il tuo stream, Impostazioni tag, Definisci traffico interno. La regola scrive il parametro `traffic_type = internal` sugli hit che arrivano dagli IP indicati. `traffic_type` è l'unico parametro a cui si può assegnare un valore, `internal` è il default.
2. **Poi il filtro dati** che esclude quel parametro: Amministrazione, Filtri dati. Massimo **10 filtri dati per proprietà**. ⚠️ Dall'11/06/2026 c'è un terzo tipo, il **filtro Hostname**, accanto a traffico interno e sviluppatore: esclude gli eventi per hostname, è la difesa contro le copie del sito su staging e i referral fantasma, conta nel limite dei 10 (https://support.google.com/analytics/answer/13296761, note di rilascio https://support.google.com/analytics/answer/9164320). 🔄 **Dal 21/09/2026 il filtro Hostname esiste anche in modalità Includi**: una lista di domini autorizzati a mandare eventi alla proprietà, tutto il resto fuori. Non si applica agli eventi del Measurement Protocol; gli hostname vuoti vengono bloccati in automatico (note di rilascio del 21/09/2026, https://support.google.com/analytics/answer/9164320). Su un sito con staging e sottodomini estranei è la forma più pulita del filtro.

Invertirli significa attivare un filtro che non ha niente da filtrare. GA4 non avvisa. Fonte, con i passi nello stesso ordine: https://support.google.com/analytics/answer/10104470.

### Stati del filtro

| stato | cosa fa |
|---|---|
| **Test** | marca il traffico ma **lo tiene dentro**. È lo stato in cui Google crea il filtro di default, ed è quello in cui resta per sempre se nessuno lo attiva. |
| **Attivo** | esclude davvero. |
| **Inattivo** | non fa nulla. |

⚠️ **Il filtro non è retroattivo e Google lo dice esplicitamente al momento dell'attivazione: non si torna indietro.** I dati sporchi dei giorni precedenti restano dove sono. Da quel momento si smette di sporcare, il pregresso non si ripulisce. *"Data filters do not affect historical data"*, e l'effetto è permanente anche su BigQuery (https://support.google.com/analytics/answer/13296761, https://support.google.com/analytics/answer/16608575). Stati: https://support.google.com/analytics/answer/13296662 (in Test GA4 marca i dati con la dimensione *Nome filtro dati di test*, in Attivo *"makes permanent changes"*, in Inattivo non valuta). Che il filtro nasca in Test non è scritto da nessuna parte: è osservazione di pannello, vedi sotto.

✅ **VERIFICATO l'11/08/2026 sulla proprietà 494970795**: il filtro "Internal Traffic" esisteva ma era in stato Test, e non esisteva **nessuna** regola di traffico interno. Risultato: 6,8K eventi in 28 giorni di cui 5,9K negli ultimi 7, cioè l'87% del mese prodotto dalle nostre verifiche sul sito. Il rapporto che smaschera il problema è **visualizzazioni per utente**: una pagina con 415 visualizzazioni e 3 utenti non è traffico, siamo noi.

### La trappola dell'IP residenziale

Una regola su IP funziona finché l'IP non cambia. Su una linea residenziale ruota. La regola va ricontrollata periodicamente, e ne serve **una per ogni postazione** che tocca il sito. Un secondo strato più robusto è lavorare con la Modalità Anteprima di GTM attiva, quando il container instrada gli hit di debug su una proprietà separata.

⚠️ **Se l'ID misurazione dei tag GA4 è statico (e deve esserlo, vedi sezione 7), in Anteprima gli hit vanno in produzione.** In quel caso il filtro IP è l'unica difesa e va tenuto vivo.

### Esclusione dei referral indesiderati

**Non pulisce un referral: gli toglie il ruolo di sorgente.** L'esclusione aggiunge `ignore_referrer=true` all'evento; per la regola dell'ultimo clic non diretto la sessione **eredita la sorgente precedente se c'è**, altrimenti finisce in *diretto*. In entrambi i casi si perde l'informazione su chi lo ha portato (https://support.google.com/analytics/answer/10327750).

Lo stesso dominio e i suoi sottodomini **sono già esclusi da soli**: GA4 non li tratta come referral. La lista serve per domini diversi dal nostro (gateway di pagamento, dominio secondario), massimo 50 voci per stream. Un canale che porta traffico vero (una newsletter, un sito amico) non si nasconde: si tagga con gli UTM, così arriva come canale dichiarato invece che come referral da cancellare.

---

## 3. Esplorazioni: cosa sono e cosa non sono

### Cosa sono

Tabelle pivot su misura sui dati grezzi della proprietà: si scelgono righe, colonne, valori e filtri, e si compone la domanda che i report standard non fanno. Sono lo strumento giusto quando la domanda incrocia due dimensioni ("quale campagna su quale pagina", "quale campagna su quale evento").

### Cosa non sono

- **Non sono report standard.** Non compaiono nel menu di sinistra, non si aprono da una raccolta, vivono nella sezione Esplora.
- **Non sono condivise di default.** Nascono private dell'autore e vanno condivise esplicitamente. Chi non le ha ricevute non sa che esistono. *"When you first create an exploration, only you can see it"*; chi la riceve la vede in sola lettura e deve duplicarla per modificarla (https://support.google.com/analytics/answer/7579450). Limiti: 200 esplorazioni per utente per proprietà, 500 condivise per proprietà, 10 segmenti per esplorazione, 10 filtri per scheda (https://support.google.com/analytics/answer/12229528).
- **Non si creano via API.** È vero per assenza, non c'è una frase ufficiale: la Data API legge i dati (https://developers.google.com/analytics/devguides/reporting/data/v1) e l'Admin API non ha una risorsa esplorazione (https://developers.google.com/analytics/devguides/config/admin/v1). Esiste però la copia di report ed esplorazioni fra proprietà (https://support.google.com/analytics/answer/15401228).
- **Non hanno un intervallo di date che si aggiorna da solo a partire da una data fissa.** ✅ **VERIFICATO il 12/08/2026**: i preset sono tutte finestre mobili (ultimi 7, 14, 28, 30, 90 giorni, questo mese, mese scorso, trimestre corrente, ultimi 12 mesi) e l'intervallo personalizzato è **fisso**. Non esiste un "dall'11 agosto a oggi". Confermato anche da 7579450: salvata il 1° maggio con "ultimi 28 giorni", il 1° giugno mostra il 4-31 maggio; con intervallo 1-31 maggio mostra sempre 1-31 maggio.

🔴 **Conseguenza: se una domanda va guardata più volte nel tempo, da più persone, la risposta non è una esplorazione ma un report personalizzato** (sezione 5). L'esplorazione serve a scoprire, il report a monitorare. 📌 **Terza via dal 09/09/2026: le Dashboard** dentro Report (*+ Crea > Dashboard*): fino a 15 per proprietà standard, 30 per 360; pubblicate sono condivise con tutta la proprietà; niente API, niente segmenti né confronti a livello di scheda. Per un cruscotto di KPI condiviso è la risposta; per una tabella su misura resta il report dettagliato (https://support.google.com/analytics/answer/17217303).

### La conseguenza sul disegno di un report dopo una pulizia

Se i dati sono affidabili solo da una certa data in poi, e i preset mobili scavalcano quella data, ci sono due sole strade oneste:

1. **Intervallo personalizzato fisso**, da aggiornare a mano finché il preset mobile non diventa pulito da solo.
2. **Aspettare che la finestra mobile superi la data di frattura** e poi passare al preset. Con una pulizia fatta l'11 agosto, "ultimi 28 giorni" torna pulito **dall'8 settembre**.

La seconda è quella giusta come stato finale, la prima come ponte. Va scritto nel nome o nella descrizione del report, altrimenti fra tre settimane nessuno si ricorda perché il periodo è quello.

### Campionamento e soglie

Tre cose diverse che si confondono e che portano a dire "i dati sono sbagliati":

- **Campionamento**: sopra una certa quantità di eventi nel periodo, l'esplorazione risponde su un campione. ✅ Soglia: **10 milioni di eventi per query** su proprietà standard, fino a 1 miliardo su 360 (default 100 milioni, opzione "risultati più dettagliati") (https://support.google.com/analytics/answer/13331292, https://support.google.com/analytics/answer/13888627). Si riconosce dall'icona di qualità dei dati in alto a destra della scheda, con la percentuale. Si riduce accorciando il periodo o togliendo dimensioni.
- **Soglie applicate (thresholding)**: GA4 trattiene le righe con pochissimi utenti quando i dati potrebbero identificare qualcuno, su dati demografici e query di ricerca. Causa, rimedi e il ruolo dell'identità dei report in sezione 6.
- **Cardinalità**: le dimensioni con troppi valori distinti collassano in una riga **(other)**. Vedi sezione 8.

Su un sito con poche decine di sessioni al giorno il campionamento non esiste, ma il thresholding sì, ed è la spiegazione più frequente di "manca una riga che so che c'è".

---

## 4. Meccanica del pannello Esplora, verificata a mano

Questa sezione esiste perché il 12/08/2026 si sono persi sei tentativi sul selettore di date e si è scritto due volte un nome storpiato. Non sta in nessuna documentazione. Va allungata ogni volta che il pannello si comporta in modo non ovvio.

### Le variabili vanno importate prima di comporre

La colonna di sinistra ha tre blocchi: **SEGMENTI**, **DIMENSIONI**, **METRICHE**, ognuno con un `+` che apre una finestra di ricerca a tutto schermo. Si cercano per nome, si spuntano, si chiude con **Conferma**.

⚠️ **I riquadri "Trascina o seleziona una dimensione" al centro non aprono il catalogo completo: aprono un menu con le sole variabili già importate a sinistra.** Quindi l'ordine è: prima si importa tutto quello che serve, poi si compone. Provare a comporre prima è il modo più veloce per convincersi che una dimensione non esista.

✅ Su una proprietà standard al 12/08/2026 il catalogo dichiara **364 dimensioni** e **168 metriche**.

Nomi italiani che si cercano male e vanno saputi:

| quello che serve | come si chiama |
|---|---|
| sorgente e mezzo della sessione | **Sorgente/mezzo sessione** (categoria *Sorgente di traffico*, non *Attribuzione*) |
| la campagna | **Campagna sessione** |
| la pagina di ingresso | **Pagina di destinazione** |
| il tempo medio | **Durata media del coinvolgimento per sessione** (categoria *Utente*) |
| il tasso di conversione | **Tasso di eventi chiave della sessione** |

⚠️ La ricerca "sorgente/mezzo" restituisce quindici risultati quasi identici divisi fra *Attribuzione* e *Sorgente di traffico*, più le varianti CM360, DV360, SA360, manuale e primo utente. Quella che serve per leggere le campagne è **Sorgente/mezzo sessione** sotto *Sorgente di traffico*.

📌 **Da ricontrollare a mano (nota del 20/09/2026)**: dall'11/06/2026 il catalogo ha la dimensione **Source group**, che raggruppa le sorgenti per piattaforma (Facebook/Instagram, TikTok, e retroattivamente ChatGPT, Perplexity): non è in tabella e serve per leggere il traffico AI; il conteggio 364/168 è probabilmente cambiato (note di rilascio https://support.google.com/analytics/answer/9164320). Limiti documentati il 23/09/2026 (https://support.google.com/analytics/answer/17217303): **15 schede per dashboard** su proprietà standard, 30 su 360; creano e pubblicano solo Editor e Amministratori; ogni dashboard pubblicata è visibile a tutta la proprietà; niente API, niente segmenti, niente confronti per scheda. Per quello restano le esplorazioni.

### Il selettore di date: la sequenza che funziona

Il comportamento non è quello di un normale range picker.

🔴 **Cliccare una data quando l'intervallo è già completo azzera l'inizio e svuota la fine.** Due clic consecutivi sul calendario non danno "dal primo al secondo": danno "inizio = secondo, fine = vuota".

🔴 **Scrivere nei campi non funziona.** Digitare la data e premere Invio, o digitarla e cliccare Applica, non la registra: Applica prende lo stato del calendario, non il testo.

✅ **La sequenza che funziona, verificata:**

1. clic sul giorno di **inizio** nel calendario
2. clic sul campo **Data di fine** per dargli il fuoco
3. clic sul giorno di **fine** nel calendario
4. **Applica**

Prima di procedere si rilegge la pillola sotto il nome dell'esplorazione: deve dire *Personalizzato* con le due date giuste.

### Il nome dell'esplorazione e delle schede

🔴 **Digitare nel campo del nome interlaccia il testo con il segnaposto e produce mostri.** Scrivendo "PAID: acquisizione, atterraggio, conversione" sopra "Esplorazione senza titolo" è uscito `PAID: acquisizione, atterEsplorazione senza titolo`, due volte, anche selezionando tutto prima.

✅ **Il modo affidabile**: dare il fuoco al campo, selezionare tutto il contenuto e inserire il testo in un colpo solo, in modo che il framework registri un evento di input vero. Poi **rileggere il valore del campo**, non fidarsi di quello che si vede a schermo perché è troncato con i puntini.

Il nome della **scheda** si modifica con un doppio clic sull'etichetta della scheda attiva. Le schede non attive collassano in una pastiglia numerata: si vede il nome solo di quella aperta.

### Righe, valori, chip

- Per **togliere** una dimensione dalle righe o una metrica dai valori: **un clic sul chip** fa comparire una **x** sul lato destro, un secondo clic sulla x lo rimuove. Non c'è menu contestuale.
- I nuovi elementi si **accodano in fondo**. L'ordine non si sceglie inserendo. Se serve un ordine preciso, si rimuove tutto e si reinserisce nella sequenza voluta: è più veloce del trascinamento.
- **MOSTRA RIGHE è 10 di default.** Va portato ad almeno 25, altrimenti la tabella mente per troncamento e nessuno se ne accorge. Le opzioni sono 10, 25, 50, 100, 250, 500.
- Finché non c'è **almeno una riga e almeno un valore**, la scheda dice *Nessun dato disponibile*. Non è un errore.

### Costruire un report a più schede: si duplica

1. Si costruisce la **scheda 1** completa: righe, valori, numero di righe, intervallo di date.
2. Freccia accanto al nome della scheda, **Duplica**. Copia tutto.
3. Sulla copia si sostituiscono i pezzi che cambiano e si rinomina.

Duplicare porta con sé anche l'intervallo di date e il numero di righe, che sono le due cose che si dimentica di allineare fra schede.

### Amministrazione: i link diretti non funzionano

⚠️ Navigare a mano su un URL del tipo `/admin/keyevents` **rimbalza alla home**. Ad Amministrazione si arriva dall'ingranaggio in basso a sinistra, e agli eventi chiave da lì: **Visualizzazione dei dati, Eventi**, scheda *Eventi chiave*.

---

## 5. Report standard, raccolte e menu

I report standard vivono dentro **raccolte**, le raccolte si compongono di **argomenti**, gli argomenti contengono i **report**. Una raccolta esiste ma non si vede finché non è **pubblicata** (https://support.google.com/analytics/answer/10460557). Limiti: **7 raccolte per proprietà, 5 argomenti per raccolta, 10 report per argomento**.

### Meccanica dell'editor di raccolta, verificata a mano il 12/08/2026

🔴 **Gli argomenti non si rinominano.** Un clic non fa niente, il doppio clic seleziona il testo come farebbe il browser su qualunque parola. Non c'è voce di menu. Per cambiare il nome di un argomento si crea l'argomento nuovo, si rimettono dentro i report e si cancella il vecchio.

🔴 **Un report non si trascina da un argomento all'altro.** Il drop non viene accettato e il report resta dov'era. L'unica sorgente valida per il trascinamento è **il pannello di destra**, dove i report si cercano per nome.

⚠️ **Il pannello di sinistra scorre durante il trascinamento e il rilascio può finire nell'argomento sbagliato.** Successo il 12/08. Su liste lunghe si trascina **uno alla volta**, con una verifica a schermo dopo ogni rilascio, mai in sequenza dentro la stessa passata.

- Conseguenza pratica: rinominare tre argomenti di una raccolta standard costa una ventina di trascinamenti fragili. Va deciso se vale, non fatto per inerzia.
- **Rilascia il rapporto di panoramica** e **Rilascia rapporto dettagliato** sono due zone distinte: un report di panoramica non entra nella zona dei dettagliati, e nel pannello di destra stanno in due schede separate.
- **Salva** offre due voci: *Salva le modifiche alla raccolta corrente* e *Salva come nuova raccolta*. La prima pubblica subito sulla raccolta viva.

📌 **Da ricontrollare a mano (nota del 20/09/2026)**: dal 09/09/2026 il menu Report ha un pulsante *+ Crea* con la voce *Dashboard* accanto alla Libreria (https://support.google.com/analytics/answer/17217303); l'editor di raccolta potrebbe essere stato ritoccato e quanto sopra va riverificato alla prima occasione.

### Report personalizzati contro esplorazioni

Quando serve una domanda su misura che deve **restare nel menu**, essere **condivisa** e avere un **periodo mobile**, la risposta è un **report dettagliato personalizzato** (Libreria, Crea nuovo report, Crea report dettagliato, Vuoto), non una esplorazione. Massimo 12 metriche per report e 150 report personalizzati per proprietà (https://support.google.com/analytics/answer/10445879). La descrizione ha un limite di **255 caratteri**, verificato: il testo oltre quella soglia viene troncato in silenzio (non documentato, resta osservazione di pannello). Per un cruscotto di KPI condiviso, dal 09/09/2026 c'è la Dashboard (sezione 3).

Un report dettagliato accetta **più dimensioni**: la prima è quella predefinita, le altre diventano selezionabili da un menu sopra la tabella. Due dimensioni in un report solo valgono due report.

### Cosa mettere nel menu, e cosa no

⚠️ **Un report che non sta in nessuna raccolta pubblicata è invisibile nel menu anche se esiste.** Ci si arriva solo dalla ricerca in alto. È la spiegazione tipica di "gli eventi non si trovano".

✅ **VERIFICATO l'11/08/2026**: su una proprietà dove i report standard sembravano nascosti, la raccolta *Ciclo di vita* **non esisteva più**. In Libreria c'era una sola raccolta. Prima di dire "il report è nascosto", si apre la **Libreria** e si guarda quante raccolte esistono.

**Annullare la pubblicazione non è eliminare.** Una raccolta spubblicata resta in Libreria e si ripubblica in un clic. È l'operazione giusta quando un menu è duplicato: si toglie di mezzo senza perdere niente.

**Un menu che mostra report vuoti insegna a non guardare il menu.** Le regole che ne derivano:

- un argomento con **un report solo** non è un argomento, è una voce persa;
- i report **Panoramica** sono cruscotti di schedine preconfezionate: uno per raccolta basta e avanza;
- i **dati demografici** sotto qualche centinaio di utenti al mese sono rumore, e un report che insegna cose false è peggio di un report assente;
- su un sito senza e-commerce si tolgono *Monetizzazione* e *Costo non Google*; a volumi bassi si toglie *Coorti di acquisizione utenti*;
- ⚠️ *Costo non Google* si tiene invece se si importano costi Meta o di altri canali: dal 28/07/2026 l'importazione dei dati campagne richiede il campo valuta e dal 10/08/2026 c'è un report di validazione che segnala le campagne senza costo, clic o impressioni (note di rilascio https://support.google.com/analytics/answer/9164320);
- ⚠️ dall'08/06/2026 l'integrazione **Google Business Profile** crea da sola una raccolta dedicata in Libreria (7 metriche, finestra mobile di 6 mesi): una raccolta in più non nostra, che conta nel limite di 7 (stesse note di rilascio);
- 🔴 **se ci sono canali a pagamento accesi, il menu deve avere una sezione che parla di quelli**, e sta in cima. È la voce che si apre ogni mattina.

---

## 6. Attribuzione, identità dei report, soglie

### Modelli

In GA4 i modelli sono **tre**: **basato sui dati**, **ultimo clic a pagamento e organico**, **ultimo clic canali a pagamento Google**. I due ultimo clic danno numeri diversi: si dice sempre quale si sta leggendo. I modelli *primo clic*, *lineare*, *decadimento temporale* e *basato sulla posizione* sono stati **rimossi a novembre 2023** e non si applicano più ai dati (https://support.google.com/analytics/answer/10596866).

⚠️ **Prima di leggere qualunque report di conversione si guarda quale modello è in uso, quale finestra di lookback e quale finestra di conversione.** Le tre cose non si comportano allo stesso modo: il **cambio di modello è retroattivo** e riscrive anche lo storico; il **cambio di finestra vale solo in avanti**. La frattura nella serie storica la produce la finestra, non il modello (https://support.google.com/analytics/answer/10597962, https://support.google.com/analytics/answer/16291704). Le conversioni possono essere riattribuite fino a 7 giorni dopo l'evento.

✅ **Finestre di lookback degli eventi chiave** (Amministrazione, Visualizzazione dei dati, Eventi, Impostazioni di attribuzione): per gli eventi chiave di acquisizione (`first_open`, `first_visit`) default **30 giorni**, opzione 7; per tutti gli altri default **90**, opzioni 30 e 60; engaged-view 3 giorni (https://support.google.com/analytics/answer/16291704).

⚠️ **Conversioni non è sinonimo di eventi chiave.** Le *conversioni* condivise con Google Ads si gestiscono in Pubblicità, Gestione conversioni (https://support.google.com/analytics/answer/13965727) e dall'**11/08/2026** hanno finestre a intero libero: 1-90 giorni click-through, 1-30 engaged-view (prima fissa a 3). Altra impostazione non retroattiva che sposta i numeri fra due periodi (note di rilascio https://support.google.com/analytics/answer/9164320, voce *Updated Conversion Window Configuration*).

### Ultimo clic contro percorsi di conversione

Con più canali accesi insieme, "un form ogni duecento clic" attribuito all'ultimo clic **misura l'ordine di arrivo, non il contributo**. Il criterio di successo di una campagna che vive dentro un mix va definito sui **percorsi di conversione** (Pubblicità, Percorsi di conversione, https://support.google.com/analytics/answer/10607798), non sul rapporto standard.

### Identità dei report

Tre opzioni: **mista** (User-ID, ID dispositivo, poi modellazione), **osservata** (User-ID, poi ID dispositivo), **basata su dispositivi**. Cambia come GA4 unisce le sessioni della stessa persona e quindi il conteggio degli utenti. Si cambia in qualunque momento senza effetti permanenti sui dati (https://support.google.com/analytics/answer/10976610).

⚠️ **Thresholding**: GA4 trattiene le righe con pochi utenti su **dati demografici** (e pubblici costruiti su di essi) e **query di ricerca**. Le identità *mista* e *osservata* sono soggette a soglie perché richiedono abbastanza utenti loggati; *basata su dispositivi* lo è meno (https://support.google.com/analytics/answer/9383630). A volumi bassi è la causa numero uno di righe mancanti. Rimedi: identità basata su dispositivi (al prezzo della deduplicazione cross-device), intervallo di date più largo, export BigQuery.

⚠️ **Google Signals non compare più fra i componenti dell'identità.** Dal **15/06/2026** l'interruttore governa solo l'associazione dei dati GA con gli utenti loggati per i report comportamentali; cookie e ID pubblicitari dipendono dal Consent Mode in Google Ads (https://support.google.com/analytics/answer/17016975). Nell'igiene di una proprietà ereditata si guarda lì, non solo l'interruttore in GA4.

---

## 7. Collegamenti: Google Ads, Search Console, container

### Google Ads

Il collegamento sblocca tre cose: **esportazione dei pubblici** verso Ads, **importazione degli eventi chiave** come conversioni, e le **dimensioni Ads** dentro i report GA4. Senza, si legge solo l'ultimo clic e non si importa niente (https://support.google.com/analytics/answer/9379420; scollegando, il traffico Ads resta `google / cpc` o con gli UTM disponibili).

⚠️ **Auto-tagging attivo significa niente UTM manuali, ma per la ragione giusta.** Il `gclid` porta dentro GA4 campagna, gruppo e parola chiave. Se sull'URL ci sono anche UTM scritti a mano, **vincono i valori auto-taggati**: gli UTM vengono ignorati nelle dimensioni di sorgente e mezzo, non sovrascrivono niente e non rompono l'importazione delle conversioni; in GA4 non esiste l'opzione di override che c'era in Universal Analytics (https://support.google.com/analytics/answer/11242870, https://support.google.com/analytics/answer/10723328). Non si mettono comunque: sono lavoro inutile che diverge dai nomi in Ads e confonde chi legge. Il rischio vero è l'opposto: **auto-tagging spento**, traffico che arriva con gli UTM ma senza `gclid`, conversioni che non si importano. Su Google basta nominare bene la campagna. Dal 30/07/2026 GA4 segnala da solo gli URL che perdono i parametri aggregati `gbraid` e `gad_` (note di rilascio https://support.google.com/analytics/answer/9164320).

⚠️ **Quello che è evento chiave in GA4 deve essere la primaria su Google Ads e l'evento giusto su Meta.** Un nome solo, tre posti. Se le tre liste divergono, ogni piattaforma ottimizza su una cosa diversa. Con Ads si condividono le *conversioni* create in Pubblicità, Gestione conversioni, non gli eventi chiave in quanto tali (https://support.google.com/analytics/answer/13965727).

### Search Console

Il collegamento sblocca i due report *Query* e *Traffico di ricerca organica Google* (https://support.google.com/analytics/answer/13682862, https://support.google.com/analytics/answer/13682863). Uno stream web si collega a una sola proprietà Search Console e viceversa; 16 mesi di storico; dati disponibili dopo 48 ore.

⚠️ **I due report compaiono in Libreria ma non in nessuna raccolta pubblicata: finché non li si mette in un argomento e non si pubblica, sono invisibili.** Verificato l'11/08/2026, e scritto da Google: *"The Search Console collection of reports is unpublished by default"* (https://support.google.com/analytics/answer/10737381). Sono la base per costruire le keyword di una campagna Search sui dati veri invece che a intuito.

### Container GTM

🔴 **L'ID misurazione dei tag GA4 deve essere una stringa statica, non una variabile.** Con un ID a variabile, GTM non riconosce il tag Google, i tag evento **non ereditano le impostazioni di configurazione** e `server_container_url` non viene mai applicato: gli hit vanno dritti a Google e il container server-side resta a zero.

Il sintomo è scritto dentro GTM su ogni tag evento: *"Impossibile rilevare se il tag Google è nel tuo contenitore. Potresti aver utilizzato una variabile o input non valido"*. Verificato il 12/08/2026: mezza giornata bruciata. Nessuna pagina ufficiale dice che l'ID deve essere una costante: resta osservazione di prima mano. La controprova più vicina è la diagnostica *Missing Google tags* di GTM (https://support.google.com/tagmanager/answer/13543899; ereditarietà: https://support.google.com/tagmanager/answer/12131703, https://support.google.com/tagmanager/answer/14681508).

⚠️ **Prezzo da pagare, consapevole**: una tabella di ricerca che instrada gli hit di debug su una proprietà di test è un'ottima idea e **non è compatibile** con l'ereditarietà server-side. Le due cose non convivono. Scelta l'ereditarietà, in Anteprima gli hit vanno in produzione e li deve escludere il filtro sul traffico interno.

⚠️ **Per i tag la fonte di verità è la Modalità Anteprima di GTM o la Gestione eventi della piattaforma, mai le richieste di rete.**

---

## 8. Cardinalità, campionamento, conservazione

### Cardinalità e la riga (other)

Una dimensione con troppi valori distinti nel periodo fa collassare la coda in una riga **(other)**. Succede tipicamente su URL con stringhe di query, ID di sessione, titoli generati. Si evita usando dimensioni più grosse (percorso pagina invece di pagina più stringa di query) o accorciando il periodo.

`[DA VERIFICARE]` limite di righe oltre il quale scatta (other) sulle proprietà standard: **Google non pubblica il numero**. L'unica indicazione ufficiale è che una dimensione con **più di 500 valori** va considerata ad alta cardinalità, e che le 360 hanno limiti più alti (https://support.google.com/analytics/answer/13208658). Il 500 è una soglia di attenzione, non un cut-off documentato.

### Conservazione dei dati

- Amministrazione, Raccolta e modifica dei dati, Conservazione dei dati.
- Su proprietà standard le opzioni sono **2 o 14 mesi** su eventi e utenti; 14 è il massimo ed è il valore da impostare sempre: all'apertura è a 2 e nessuno se ne accorge finché non serve il confronto anno su anno (https://support.google.com/analytics/answer/7667196). Il cambio scatta dopo 24 ore, e in quelle 24 ore è reversibile.
- ⚠️ **La conservazione riguarda solo esplorazioni e report canalizzazione**, con i segmenti e i confronti dentro le esplorazioni. I report standard aggregati non sono toccati, **nemmeno con i confronti attivi**. Quindi un dato che si vede in un report standard può essere sparito da una esplorazione: non è un guasto.
- Età, genere e interessi restano a 2 mesi qualunque sia l'impostazione. Se una standard diventa Large, la conservazione scende da sola a 2 mesi e il pregresso viene cancellato.

### Limiti da non sbagliare

✅ Per proprietà standard (https://support.google.com/analytics/answer/12229528, https://support.google.com/analytics/answer/9267744): **50 dimensioni personalizzate a livello evento**, **50 metriche personalizzate**, **25 dimensioni a livello utente** (cioè 25 proprietà utente); **25 parametri per evento**; nome evento e nome parametro **40 caratteri**, valore parametro 100 (`page_title` 300, `page_referrer` 420, `page_location` 1000); nome proprietà utente 24, valore 36. Altri: 100 pubblici, 50 confronti salvati, 50 segmenti salvati, esportazione 100.000 righe.

---

## 9. Igiene di una proprietà ereditata: ordine di controllo

Ordine che fa emergere i problemi nell'ordine in cui contano. **Il primo punto va fatto lo stesso giorno**, perché è l'unico non retroattivo.

1. **Eventi chiave.** Quanti sono, quali sono, quali sono visualizzazioni o scroll travestiti. Si incrocia con gli eventi ricevuti e con i tag del container. Si pulisce subito, non domani.
2. **Regola di traffico interno** e **filtro dati**, in quest'ordine. Verificare che il filtro non sia in Test. Se esistono domini di staging o hostname estranei, terzo filtro Hostname (sezione 2).
3. **Il rapporto visualizzazioni su utenti** delle pagine su cui si è lavorato di recente. È il modo più veloce per capire quanta parte del traffico siamo noi.
4. **Conservazione dei dati** a 14 mesi.
5. **Misurazione avanzata**, voce per voce, non a blocco. Spegnere *Interazioni con modulo* se il sito ha form tracciati da GTM: è l'origine di `form_start` e `form_submit`.
6. **Referral indesiderati**: dentro solo i domini estranei che non sono sorgenti vere (gateway di pagamento, dominio secondario); il proprio dominio è già gestito.
7. **Libreria**: quante raccolte esistono, quali sono pubblicate, quali report restano orfani. Una raccolta Google Business Profile non l'abbiamo creata noi (sezione 5).
8. **Collegamenti**: Google Ads, Search Console, e la coerenza fra eventi chiave GA4 e conversioni primarie su Ads.
9. **Identità dei report**, **modello di attribuzione**, **finestre di lookback e di conversione**, e il Consent Mode in Google Ads per i segnali, prima di leggere qualunque numero.
10. **Definizioni personalizzate**: quante ne sono state bruciate e per cosa, contro i limiti della sezione 8.

---

## 10. Cosa non fare mai

- **Giudicare la lista degli eventi chiave guardando la lista.** Non contiene l'informazione che serve a giudicarla. Servono gli eventi ricevuti e il container.
- **Attivare un filtro dati prima di aver creato la regola.** Filtra il nulla e sembra fatto.
- **Escludere dai referral un canale che funziona.** Non lo pulisce, lo cancella: quel traffico eredita la sorgente precedente o diventa diretto.
- **Confrontare periodi a cavallo di una pulizia degli eventi chiave** o di un cambio di finestra di lookback o di conversione, senza dirlo. Il cambio di modello invece riscrive anche il passato: non produce una frattura, cambia tutti i numeri insieme.
- **Mettere UTM manuali su un URL Google Ads con auto-tagging.** Non rompono niente, ma vengono ignorati: lavoro inutile che fa credere di controllare qualcosa.
- **Dedurre uno slug dal titolo che compare in un report** e poi dichiarare rotta una pagina. Il percorso si legge dalla dimensione *Percorso pagina*, non dal titolo.
- **Dire "il report è nascosto" prima di aver aperto la Libreria.**
- **Dire "l'evento è rotto" perché ha zero dati.** Una pagina con tre utenti in ventotto giorni produce zero clic anche se il tag è perfetto. La prova si fa in Anteprima.
- **Usare una esplorazione come report ricorrente da distribuire.** È privata, non si crea via API e l'intervallo personalizzato è fisso. Per un cruscotto condiviso c'è la Dashboard, per una tabella il report dettagliato.
- **Potare il menu di Google invece di costruirne uno nostro.** Togliere le voci vuote è metà del lavoro: l'altra metà è che il menu deve avere in cima la domanda che ci si fa ogni giorno.

---

## Fonti

Al 20/09/2026 le regole di dominio sono ancorate alle pagine ufficiali qui sotto. Le sezioni 4 e 5 restano meccanica di pannello, osservata a mano. Note di rilascio GA4, lette da giugno a settembre 2026: https://support.google.com/analytics/answer/9164320.

- **Sezione 1**: https://support.google.com/analytics/answer/13128484 (eventi chiave: non retroattività, 30/50, 24 ore), https://support.google.com/analytics/answer/12844695 (creare o modificare eventi chiave), https://support.google.com/analytics/answer/9216061 (misurazione avanzata), https://support.google.com/analytics/answer/12229528 (limiti di configurazione).
- **Sezione 2**: https://support.google.com/analytics/answer/10104470 (traffico interno, 10 filtri), https://support.google.com/analytics/answer/13296662 (stati del filtro), https://support.google.com/analytics/answer/13296761 (filtri dati, Hostname, non retroattività), https://support.google.com/analytics/answer/16608575 (traffico indesiderato), https://support.google.com/analytics/answer/10327750 (referral indesiderati).
- **Sezione 3**: https://support.google.com/analytics/answer/7579450 (esplorazioni), https://support.google.com/analytics/answer/13331292 e https://support.google.com/analytics/answer/13888627 (campionamento), https://support.google.com/analytics/answer/15401228 (copia fra proprietà), https://support.google.com/analytics/answer/17217303 (Dashboard), https://developers.google.com/analytics/devguides/reporting/data/v1 e https://developers.google.com/analytics/devguides/config/admin/v1 (API).
- **Sezione 5**: https://support.google.com/analytics/answer/10445879 (report dettagliati: 12 metriche, 150 report), https://support.google.com/analytics/answer/10460557 (raccolte: 7/5/10).
- **Sezione 6**: https://support.google.com/analytics/answer/10596866 e https://support.google.com/analytics/answer/10597962 (modelli), https://support.google.com/analytics/answer/16291704 (finestre di lookback), https://support.google.com/analytics/answer/13965727 (conversioni contro eventi chiave), https://support.google.com/analytics/answer/10976610 (identità dei report), https://support.google.com/analytics/answer/9383630 (soglie), https://support.google.com/analytics/answer/17016975 (Data Controls, 15/06/2026), https://support.google.com/analytics/answer/10607798 (percorsi di conversione).
- **Sezione 7**: https://support.google.com/analytics/answer/9379420 (collegamento Ads), https://support.google.com/analytics/answer/11242870 e https://support.google.com/analytics/answer/10723328 (auto-tagging e UTM), https://support.google.com/analytics/answer/10737381, https://support.google.com/analytics/answer/13682862, https://support.google.com/analytics/answer/13682863 (Search Console), https://support.google.com/tagmanager/answer/13543899, https://support.google.com/tagmanager/answer/12131703, https://support.google.com/tagmanager/answer/14681508 (Google tag in GTM).
- **Sezione 8**: https://support.google.com/analytics/answer/13208658 (riga other), https://support.google.com/analytics/answer/7667196 (conservazione), https://support.google.com/analytics/answer/12229528, https://support.google.com/analytics/answer/9267744 e https://support.google.com/analytics/answer/14240153 (limiti).

**Non trovato su fonte ufficiale, resta osservazione di prima mano**: ID misurazione statico in GTM (sezione 7), limite di 255 caratteri della descrizione di un report (sezione 5), filtro dati che nasce in stato Test (sezione 2), `purchase` nell'elenco eventi di un sito senza e-commerce (sezione 1), esplorazioni non creabili via API (sezione 3, vero per assenza).
