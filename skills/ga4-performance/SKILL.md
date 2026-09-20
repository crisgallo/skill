---
name: "ga4-performance"
description: "Regole operative verificate per configurare, igienizzare e interrogare Google Analytics 4: eventi chiave, filtri dati, esplorazioni, report personalizzati, raccolte e menu, attribuzione, collegamenti a Google Ads e Search Console. Usare ogni volta che si lavora sul pannello GA4, si costruisce un report, si rifa il menu, o si giudica un numero prima di portarlo su un pannello che spende. Serve anche per fare l'igiene di una proprieta ereditata."
---

# GA4: regole operative

**Ultima verifica delle fonti: 12 agosto 2026.**

---

## 0. Manutenzione di questa skill (leggere per primo)

Vale la stessa regola delle skill Meta e Google Ads: se la data qui sopra ha più di due o tre mesi, si ricontrolla sulle fonti ufficiali prima di applicare un numero. Quando una fonte smentisce una regola scritta qui, la skill si aggiorna nello stesso turno, si riscrive la data e si annota cosa è cambiato.

Questa skill ha due metà, e vanno tenute distinte.

- **Conoscenza di dominio**: come si comporta GA4. Si verifica sulle fonti ufficiali Google.
- **Meccanica del pannello** (sezioni 4 e 5): come si comporta l'interfaccia quando ci lavori dentro. Non sta in nessuna documentazione, si impara sbagliando, e va scritta qui la prima volta che succede.

⚠️ Ogni volta che si aggiorna la skill si riallinea la copia in `Blog/skills/` e la riga nel README, nello stesso turno.

🔴 **Le soglie marcate `[DA VERIFICARE]` non sono state confermate su fonte ufficiale al 12/08/2026.** Non si citano a un cliente e non si usano per una decisione di spesa finché non hanno una fonte accanto.

✅ Quello che è marcato **VERIFICATO** è stato osservato di persona sul pannello, con la data accanto.

---

## 1. Eventi chiave: la regola che decide tutto il resto

**Contrassegnare o togliere un evento chiave NON è retroattivo. I dati già raccolti restano contati come erano al momento della raccolta.**

È la cosa che cambia più decisioni di qualunque altra in questa skill, ed è il contrario di quello che quasi tutti danno per scontato.

✅ **VERIFICATO il 12/08/2026 sulla proprietà 494970795.** L'11/08 gli eventi chiave sono passati da 13 a 5, togliendo fra gli altri `page_view_articolo_blog`. Poi, in una esplorazione con righe *Campagna sessione* per *Nome evento* e valore *Eventi chiave*:

| periodo | riga | eventi chiave |
|---|---|---|
| 11 ago - 12 ago | `campaign_191706` / `page_view_articolo_blog` | **17** |
| 12 ago - 12 ago | `campaign_191706` / `page_view_articolo_blog` | **0** |

Stessa proprietà, stesso evento, stessa campagna. L'evento non è più chiave dall'11 agosto, ma le righe dell'11 agosto continuano a dichiarare 17 conversioni. Idem `lettura_articolo_blog`: 1 il giorno 11, 0 il giorno 12.

### Le tre conseguenze operative

1. **La data di pulizia è una frattura nella serie storica, non una correzione.** Un confronto che scavalca quella data mette insieme due definizioni diverse di conversione e produce un crollo che sembra performance ed è contabilità. Stesso identico problema delle finestre di attribuzione di Meta a gennaio 2026.
2. **Il periodo di default di ogni report sulle conversioni parte dal giorno DOPO la pulizia**, non dal giorno stesso: la pulizia avviene a metà giornata e quel giorno è misto.
3. **Non si aspetta.** Poiché non è retroattivo, ogni ora in cui un evento spazzatura resta contrassegnato è storico sporco che non si recupera. La pulizia degli eventi chiave si fa il giorno in cui si apre la proprietà, prima di qualunque altra cosa.

### Cosa può essere un evento chiave

Un evento merita la stella solo se ha **un tag suo nel container** e rappresenta **un'intenzione**, non un comportamento. La verifica si fa su due fonti esterne alla lista, mai sulla lista stessa:

1. **Cosa arriva davvero**: Amministrazione, Visualizzazione dei dati, Eventi, scheda *Eventi recenti*. Sono gli eventi ricevuti negli ultimi 28 giorni. Se un evento chiave non compare qui, o è rotto o non esiste più.
2. **Cosa è configurato**: i tag del container GTM con il rispettivo attivatore. Dicono quale push del dataLayer produce quale nome evento, e quindi dove cercare il guasto quando un nome non arriva.

Si costruisce la corrispondenza **tag → attivatore → nome evento** e la si confronta con le stelle. Le tre liste devono raccontare la stessa storia.

⚠️ **Gli eventi della misurazione avanzata non vanno quasi mai contrassegnati.** `form_submit`, `form_start`, `scroll`, `click`, `view_search_results` non hanno un tag nel container, scattano su qualunque elemento della pagina e si sovrappongono agli eventi veri. Marcarli significa contare doppio e non distinguere niente. Se un evento non ha un tag suo, chiedersi perché prima di trattarlo come conversione.

⚠️ **`purchase` compare nell'elenco anche su un sito senza e-commerce.** GA4 lo mostra di default. Senza stella non è un problema: è arredamento.

⚠️ **Un evento chiave senza dati non è per forza da buttare.** Può essere rotto, oppure semplicemente non ancora cliccato da nessuno perché la pagina ha tre utenti in ventotto giorni. Le due cose si distinguono in Modalità Anteprima di GTM, non guardando il report.

### Il numero massimo

`[DA VERIFICARE]` limite di eventi chiave per proprietà standard: il valore che gira è 30. Da confermare su fonte ufficiale prima di citarlo.

---

## 2. Filtri dati e traffico interno

### L'ordine è vincolante e sbagliarlo produce un filtro che non filtra

1. **Prima la regola di traffico interno**: Amministrazione, Raccolta e modifica dei dati, Stream di dati, il tuo stream, Impostazioni tag, Definisci traffico interno. La regola scrive il parametro `traffic_type = internal` sugli hit che arrivano dagli IP indicati.
2. **Poi il filtro dati** che esclude quel parametro: Amministrazione, Filtri dati.

Invertirli significa attivare un filtro che non ha niente da filtrare. GA4 non avvisa.

### Stati del filtro

| stato | cosa fa |
|---|---|
| **Test** | marca il traffico ma **lo tiene dentro**. È lo stato in cui Google crea il filtro di default, ed è quello in cui resta per sempre se nessuno lo attiva. |
| **Attivo** | esclude davvero. |
| **Inattivo** | non fa nulla. |

⚠️ **Il filtro non è retroattivo e Google lo dice esplicitamente al momento dell'attivazione: non si torna indietro.** I dati sporchi dei giorni precedenti restano dove sono. Da quel momento si smette di sporcare, il pregresso non si ripulisce.

✅ **VERIFICATO l'11/08/2026 sulla proprietà 494970795**: il filtro "Internal Traffic" esisteva ma era in stato Test, e non esisteva **nessuna** regola di traffico interno. Risultato: 6,8K eventi in 28 giorni di cui 5,9K negli ultimi 7, cioè l'87% del mese prodotto dalle nostre verifiche sul sito. Il rapporto che smaschera il problema è **visualizzazioni per utente**: una pagina con 415 visualizzazioni e 3 utenti non è traffico, siamo noi.

### La trappola dell'IP residenziale

Una regola su IP funziona finché l'IP non cambia. Su una linea residenziale ruota. La regola va ricontrollata periodicamente, e ne serve **una per ogni postazione** che tocca il sito. Un secondo strato più robusto è lavorare con la Modalità Anteprima di GTM attiva, quando il container instrada gli hit di debug su una proprietà separata.

⚠️ **Se l'ID misurazione dei tag GA4 è statico (e deve esserlo, vedi sezione 7), in Anteprima gli hit vanno in produzione.** In quel caso il filtro IP è l'unica difesa e va tenuto vivo.

### Esclusione dei referral indesiderati

**Non pulisce un referral: lo cancella come sorgente.** Il traffico escluso finisce in *diretto* e si perde l'informazione su chi lo ha portato.

Quindi si esclude **solo l'auto-referral**, cioè il dominio del sito stesso. Un canale che porta traffico vero (una newsletter, un sito amico) non si nasconde: si tagga con gli UTM, così arriva come canale dichiarato invece che come referral da cancellare.

---

## 3. Esplorazioni: cosa sono e cosa non sono

### Cosa sono

Tabelle pivot su misura sui dati grezzi della proprietà: si scelgono righe, colonne, valori e filtri, e si compone la domanda che i report standard non fanno. Sono lo strumento giusto quando la domanda incrocia due dimensioni ("quale campagna su quale pagina", "quale campagna su quale evento").

### Cosa non sono

- **Non sono report standard.** Non compaiono nel menu di sinistra, non si aprono da una raccolta, vivono nella sezione Esplora.
- **Non sono condivise di default.** Nascono private dell'autore e vanno condivise esplicitamente. Chi non le ha ricevute non sa che esistono.
- **Non si creano via API.** La Data API di GA4 legge i dati, non crea esplorazioni.
- **Non hanno un intervallo di date che si aggiorna da solo a partire da una data fissa.** ✅ **VERIFICATO il 12/08/2026**: i preset sono tutte finestre mobili (ultimi 7, 14, 28, 30, 90 giorni, questo mese, mese scorso, trimestre corrente, ultimi 12 mesi) e l'intervallo personalizzato è **fisso**. Non esiste un "dall'11 agosto a oggi".

🔴 **Conseguenza: se una domanda va guardata più volte nel tempo, da più persone, la risposta non è una esplorazione ma un report personalizzato** (sezione 5). L'esplorazione serve a scoprire, il report a monitorare.

### La conseguenza sul disegno di un report dopo una pulizia

Se i dati sono affidabili solo da una certa data in poi, e i preset mobili scavalcano quella data, ci sono due sole strade oneste:

1. **Intervallo personalizzato fisso**, da aggiornare a mano finché il preset mobile non diventa pulito da solo.
2. **Aspettare che la finestra mobile superi la data di frattura** e poi passare al preset. Con una pulizia fatta l'11 agosto, "ultimi 28 giorni" torna pulito **dall'8 settembre**.

La seconda è quella giusta come stato finale, la prima come ponte. Va scritto nel nome o nella descrizione del report, altrimenti fra tre settimane nessuno si ricorda perché il periodo è quello.

### Campionamento e soglie

Tre cose diverse che si confondono e che portano a dire "i dati sono sbagliati":

- **Campionamento**: sopra una certa quantità di eventi nel periodo, l'esplorazione risponde su un campione. `[DA VERIFICARE]` la soglia sulle proprietà standard, il valore che gira è 10 milioni di eventi per query. Si riconosce dall'icona in alto a destra della scheda. Si riduce accorciando il periodo o togliendo dimensioni.
- **Soglie applicate (thresholding)**: GA4 nasconde le righe con pochissimi utenti quando i dati potrebbero identificare qualcuno. Compare quando **Google Signals è attivo** nell'identità dei report. Si toglie passando l'identità dei report a *basata su dispositivi*.
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

I report standard vivono dentro **raccolte**, le raccolte si compongono di **argomenti**, gli argomenti contengono i **report**. Una raccolta esiste ma non si vede finché non è **pubblicata**.

### Meccanica dell'editor di raccolta, verificata a mano il 12/08/2026

🔴 **Gli argomenti non si rinominano.** Un clic non fa niente, il doppio clic seleziona il testo come farebbe il browser su qualunque parola. Non c'è voce di menu. Per cambiare il nome di un argomento si crea l'argomento nuovo, si rimettono dentro i report e si cancella il vecchio.

🔴 **Un report non si trascina da un argomento all'altro.** Il drop non viene accettato e il report resta dov'era. L'unica sorgente valida per il trascinamento è **il pannello di destra**, dove i report si cercano per nome.

⚠️ **Il pannello di sinistra scorre durante il trascinamento e il rilascio può finire nell'argomento sbagliato.** Successo il 12/08. Su liste lunghe si trascina **uno alla volta**, con una verifica a schermo dopo ogni rilascio, mai in sequenza dentro la stessa passata.

- Conseguenza pratica: rinominare tre argomenti di una raccolta standard costa una ventina di trascinamenti fragili. Va deciso se vale, non fatto per inerzia.
- **Rilascia il rapporto di panoramica** e **Rilascia rapporto dettagliato** sono due zone distinte: un report di panoramica non entra nella zona dei dettagliati, e nel pannello di destra stanno in due schede separate.
- **Salva** offre due voci: *Salva le modifiche alla raccolta corrente* e *Salva come nuova raccolta*. La prima pubblica subito sulla raccolta viva.

### Report personalizzati contro esplorazioni

Quando serve una domanda su misura che deve **restare nel menu**, essere **condivisa** e avere un **periodo mobile**, la risposta è un **report dettagliato personalizzato** (Libreria, Crea nuovo report, Crea report dettagliato, Vuoto), non una esplorazione. Massimo 12 metriche per report. La descrizione ha un limite di **255 caratteri**, verificato: il testo oltre quella soglia viene troncato in silenzio.

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
- 🔴 **se ci sono canali a pagamento accesi, il menu deve avere una sezione che parla di quelli**, e sta in cima. È la voce che si apre ogni mattina.

---

## 6. Attribuzione, identità dei report, soglie

### Modelli

In GA4 restano **basato sui dati** e **ultimo clic**. I modelli *primo clic*, *lineare*, *decadimento temporale* e *basato sulla posizione* sono stati **rimossi** e non si applicano più ai dati.

⚠️ **Prima di leggere qualunque report di conversione si guarda quale modello è in uso e quale finestra di lookback.** Un confronto fra periodi con impostazioni diverse produce differenze che sembrano performance e sono contabilità.

`[DA VERIFICARE]` finestre di lookback disponibili: 30, 60 e 90 giorni per gli eventi chiave, 7 e 30 giorni per l'acquisizione. Da confermare su fonte ufficiale.

### Ultimo clic contro percorsi di conversione

Con più canali accesi insieme, "un form ogni duecento clic" attribuito all'ultimo clic **misura l'ordine di arrivo, non il contributo**. Il criterio di successo di una campagna che vive dentro un mix va definito sui **percorsi di conversione** (Pubblicità, Percorsi di conversione), non sul rapporto standard.

### Identità dei report

Tre opzioni: **mista**, **basata su utenti**, **basata su dispositivi**. Cambia come GA4 unisce le sessioni della stessa persona e quindi il conteggio degli utenti.

⚠️ L'identità che include **Google Signals** attiva il **thresholding**: righe con pochi utenti sparite dal report. A volumi bassi è la causa numero uno di righe mancanti. Passando a *basata su dispositivi* le righe tornano, al prezzo di perdere la deduplicazione cross-device.

---

## 7. Collegamenti: Google Ads, Search Console, container

### Google Ads

Il collegamento sblocca tre cose: **esportazione dei pubblici** verso Ads, **importazione degli eventi chiave** come conversioni, e le **dimensioni Ads** dentro i report GA4. Senza, si legge solo l'ultimo clic e non si importa niente.

⚠️ **Auto-tagging attivo significa niente UTM manuali.** Il `gclid` porta dentro GA4 campagna, gruppo e parola chiave. Un UTM scritto a mano sopra un URL con auto-tagging **sovrascrive** quei valori e rompe l'importazione delle conversioni. Su Google basta nominare bene la campagna.

⚠️ **Quello che è evento chiave in GA4 deve essere la primaria su Google Ads e l'evento giusto su Meta.** Un nome solo, tre posti. Se le tre liste divergono, ogni piattaforma ottimizza su una cosa diversa.

### Search Console

Il collegamento sblocca i due report *Query* e *Traffico di ricerca organica Google*.

⚠️ **I due report compaiono in Libreria ma non in nessuna raccolta pubblicata: finché non li si mette in un argomento e non si pubblica, sono invisibili.** Verificato l'11/08/2026. Sono la base per costruire le keyword di una campagna Search sui dati veri invece che a intuito.

### Container GTM

🔴 **L'ID misurazione dei tag GA4 deve essere una stringa statica, non una variabile.** Con un ID a variabile, GTM non riconosce il tag Google, i tag evento **non ereditano le impostazioni di configurazione** e `server_container_url` non viene mai applicato: gli hit vanno dritti a Google e il container server-side resta a zero.

Il sintomo è scritto dentro GTM su ogni tag evento: *"Impossibile rilevare se il tag Google è nel tuo contenitore. Potresti aver utilizzato una variabile o input non valido"*. Verificato il 12/08/2026: mezza giornata bruciata.

⚠️ **Prezzo da pagare, consapevole**: una tabella di ricerca che instrada gli hit di debug su una proprietà di test è un'ottima idea e **non è compatibile** con l'ereditarietà server-side. Le due cose non convivono. Scelta l'ereditarietà, in Anteprima gli hit vanno in produzione e li deve escludere il filtro sul traffico interno.

⚠️ **Per i tag la fonte di verità è la Modalità Anteprima di GTM o la Gestione eventi della piattaforma, mai le richieste di rete.**

---

## 8. Cardinalità, campionamento, conservazione

### Cardinalità e la riga (other)

Una dimensione con troppi valori distinti nel periodo fa collassare la coda in una riga **(other)**. Succede tipicamente su URL con stringhe di query, ID di sessione, titoli generati. Si evita usando dimensioni più grosse (percorso pagina invece di pagina più stringa di query) o accorciando il periodo.

`[DA VERIFICARE]` soglia di cardinalità giornaliera sulle proprietà standard. Da confermare.

### Conservazione dei dati

- Amministrazione, Raccolta e modifica dei dati, Conservazione dei dati.
- Su proprietà standard il massimo è **14 mesi** su eventi e utenti. È il valore da impostare sempre: il default è più basso e nessuno se ne accorge finché non serve il confronto anno su anno.
- ⚠️ **La conservazione riguarda i dati a livello di evento**, cioè **esplorazioni, segmenti e confronti**. I report standard aggregati continuano a mostrare periodi più lunghi. Quindi un dato che si vede in un report standard può essere sparito da una esplorazione: non è un guasto.

### Limiti da non sbagliare

`[DA VERIFICARE]` dimensioni personalizzate a livello evento e a livello utente, numero massimo di parametri per evento, lunghezza dei nomi evento.

---

## 9. Igiene di una proprietà ereditata: ordine di controllo

Ordine che fa emergere i problemi nell'ordine in cui contano. **Il primo punto va fatto lo stesso giorno**, perché è l'unico non retroattivo.

1. **Eventi chiave.** Quanti sono, quali sono, quali sono visualizzazioni o scroll travestiti. Si incrocia con gli eventi ricevuti e con i tag del container. Si pulisce subito, non domani.
2. **Regola di traffico interno** e **filtro dati**, in quest'ordine. Verificare che il filtro non sia in Test.
3. **Il rapporto visualizzazioni su utenti** delle pagine su cui si è lavorato di recente. È il modo più veloce per capire quanta parte del traffico siamo noi.
4. **Conservazione dei dati** a 14 mesi.
5. **Misurazione avanzata**, voce per voce, non a blocco. Spegnere *Interazioni con modulo* se il sito ha form tracciati da GTM: è l'origine di `form_start` e `form_submit`.
6. **Referral indesiderati**: dentro solo l'auto-referral.
7. **Libreria**: quante raccolte esistono, quali sono pubblicate, quali report restano orfani.
8. **Collegamenti**: Google Ads, Search Console, e la coerenza fra eventi chiave GA4 e conversioni primarie su Ads.
9. **Identità dei report** e **modello di attribuzione**, prima di leggere qualunque numero.
10. **Definizioni personalizzate**: quante ne sono state bruciate e per cosa.

---

## 10. Cosa non fare mai

- **Giudicare la lista degli eventi chiave guardando la lista.** Non contiene l'informazione che serve a giudicarla. Servono gli eventi ricevuti e il container.
- **Attivare un filtro dati prima di aver creato la regola.** Filtra il nulla e sembra fatto.
- **Escludere dai referral un canale che funziona.** Non lo pulisce, lo cancella: quel traffico diventa diretto.
- **Confrontare periodi a cavallo di una pulizia degli eventi chiave** o di un cambio di modello di attribuzione, senza dirlo.
- **Dedurre uno slug dal titolo che compare in un report** e poi dichiarare rotta una pagina. Il percorso si legge dalla dimensione *Percorso pagina*, non dal titolo.
- **Dire "il report è nascosto" prima di aver aperto la Libreria.**
- **Dire "l'evento è rotto" perché ha zero dati.** Una pagina con tre utenti in ventotto giorni produce zero clic anche se il tag è perfetto. La prova si fa in Anteprima.
- **Usare una esplorazione come report ricorrente da distribuire.** È privata, non si crea via API e l'intervallo personalizzato è fisso.
- **Potare il menu di Google invece di costruirne uno nostro.** Togliere le voci vuote è metà del lavoro: l'altra metà è che il menu deve avere in cima la domanda che ci si fa ogni giorno.

---

## Fonti

⚠️ **Al 12/08/2026 questa skill è costruita su verifiche dirette sul pannello e su conoscenza di dominio non ancora riancorata alle pagine ufficiali.** È la differenza con `meta-ads-performance` e `google-ads-performance`, che hanno l'elenco delle fonti in fondo.

**Da fare al primo giro di manutenzione**: ricontrollare su `support.google.com/analytics` e `developers.google.com/analytics` tutti i punti marcati `[DA VERIFICARE]`, più la conferma documentale della non retroattività degli eventi chiave (che qui è provata da una misurazione diretta, il che vale operativamente, ma va anche citata) e l'elenco dei modelli di attribuzione rimossi con la data di rimozione. Fatto questo, si aggiunge qui l'elenco degli URL e si riscrive la data in testa.

