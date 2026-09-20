---
name: looker-studio
description: "Regole operative verificate per costruire e mantenere report mensili per clienti su Looker Studio, che da aprile 2026 si chiama Data Studio: connettori GA4, Google Ads, Search Console, Fogli Google e BigQuery, credenziali del proprietario, quote GA4 ed errore quota superata, campionamento e riga (other), unione dati, campi calcolati, intervalli di date, filtri e parametri, cache e freschezza, condivisione, invio programmato, modelli e prestazioni. Usala ogni volta che si apre, si copia, si ripara o si consegna una dashboard, un report o un cruscotto a un cliente, anche se la piattaforma non viene nominata."
---

# Looker Studio (Data Studio): regole operative

**Ultima verifica delle fonti: 20 settembre 2026.**

## 0. Manutenzione di questa skill (leggere per primo)

1. **Finestra di freschezza: tre mesi.** Il prodotto rilascia ogni due-quattro settimane, ma i connettori Google e le quote GA4 cambiano poche volte l'anno. Se la data in cima ha più di tre mesi si rilegge la pagina delle release notes prima di applicare una soglia numerica.
2. Quando una fonte smentisce una regola scritta qui, si aggiorna la skill **nello stesso turno**, si riscrive la data in cima e si annota cosa è cambiato e da quando.
3. Due metà da tenere distinte: **conoscenza di dominio** (come si comporta il prodotto, verificata sulle fonti ufficiali) e **meccanica del pannello** (sez. 19: cosa sorprende quando ci si lavora dentro; si impara sbagliando e si scrive qui la prima volta).
4. Dove si guardano i cambiamenti: [release notes ufficiali](https://docs.cloud.google.com/data-studio/release-notes) (ultima voce letta: 13/08/2026). ⚠️ Gli URL `support.google.com/looker-studio/answer/...` **reindirizzano** su `docs.cloud.google.com/looker/docs/studio/...` e da lì su `docs.cloud.google.com/data-studio/...`: i vecchi link nei preferiti funzionano ancora, ma le pagine nuove stanno solo sotto `data-studio`.
5. 🔴 Nessuna soglia qui sotto è inventata. Quello che non si è potuto leggere è marcato **[DA VERIFICARE]** e non si cita al cliente.

---

## 1. Il nome è cambiato: Looker Studio è Data Studio (dal 16/04/2026)

- **Annuncio 10/04/2026, in produzione dal 16/04/2026**: "We've rebranded Looker Studio as Data Studio". Looker Studio Pro diventa **Data Studio Pro**; "Gemini in Looker" diventa "Gemini in Data Studio". Report, origini dati e permessi restano identici, gli URL `lookerstudio.google.com` continuano a funzionare ([release notes 16/04/2026](https://docs.cloud.google.com/data-studio/release-notes), [blog Google Cloud](https://cloud.google.com/blog/products/data-analytics/looker-studio-is-data-studio)).
- Conseguenza operativa: nelle offerte e nei report al cliente si scrive **"Data Studio (ex Looker Studio)"** almeno fino a fine 2026, perché il cliente conosce il nome vecchio. Looker (senza Studio) è un altro prodotto, a pagamento, con modello semantico LookML: non si confondono nei preventivi.

**Cosa è cambiato da giugno a settembre 2026** (release notes, verificate 20/09/2026):

- **01/06** Conversational Analytics su agenti BigQuery multi-region. **11/06** solo Pro: CMEK, storage gestito dal cliente, residenza dei dati. **18/06** ⚠️ **i visualizzatori possono aggiornare i dati a mano**, se l'editor lo abilita nelle impostazioni del report (sez. 12). **30/07** Conversational Analytics in disponibilità generale. **13/08** grafici a schermo intero, rotazione di testo/immagini/forme, etichette centrate nelle barre impilate, ricerca nelle impostazioni del pannello proprietà, **copia grafico come immagine PNG**, colore bordo bolle. Nessuna voce sui connettori GA4, Google Ads o Search Console nel periodo.

---

## 2. Origini dati, report e credenziali: quello che si rompe quando il proprietario se ne va

**Un report non contiene dati: contiene riferimenti a origini dati. L'origine dati contiene le credenziali di chi l'ha creata.** È il punto dove i report dei consulenti muoiono.

- **Origine incorporata vs riutilizzabile.** Un'origine creata dentro il report è *incorporata*: viaggia con il report quando lo si copia o condivide, e chiunque può modificare il report può modificarne anche la connessione. Un'origine *riutilizzabile* (creata dalla home) si condivide a parte e serve più report ([about-data-sources](https://docs.cloud.google.com/data-studio/about-data-sources)). Per il cliente mensile: **un'origine riutilizzabile per connettore per cliente**, così i report del cliente condividono la cache (sez. 3 e 12) e si cambiano le credenziali in un posto solo.
- **Credenziali del proprietario (Owner's credentials)**: i visualizzatori vedono i dati con l'accesso di chi possiede le credenziali, senza avere accesso a GA4/Ads/Search Console. **Credenziali del visualizzatore (Viewer's credentials)**: ogni visualizzatore deve avere il proprio accesso alla proprietà, altrimenti vede un errore ([data-credentials](https://docs.cloud.google.com/data-studio/data-credentials-article)).
- 🔴 **Quando il proprietario delle credenziali perde l'accesso o viene cancellato, i report basati sulle sue credenziali smettono di mostrare dati.** Google lo dice in due punti: le credenziali dell'utente uscito "vengono revocate, rompendo report e origini dati"; per la versione gratuita **gli asset di un account cancellato vengono eliminati definitivamente dopo 20 giorni** ([transfer-ownership](https://docs.cloud.google.com/data-studio/transfer-ownership)). Il caso tipico: il consulente costruisce con il proprio Google, il rapporto finisce, il cliente resta con un report vuoto.
- ✅ Regola: **le origini dati del cliente vanno create o trasferite a un account del cliente** (un utente amministrativo del suo dominio, non la persona che potrebbe licenziarsi). Trasferimento: Condividi → menu del ruolo → **Rendi proprietario** (Make owner); le credenziali restano intatte nel trasferimento, il nuovo proprietario può riconnettere con le sue. Un editor dell'origine può prendersi le credenziali con **"Rendimi proprietario"** (Make me the owner) nella sezione credenziali. Le origini da **caricamento file CSV non sono trasferibili**: si ricreano.
- **Account di servizio**: solo per **BigQuery** secondo la pagina credenziali; la pagina del connettore Search Console lo elenca fra le opzioni **[DA VERIFICARE sul pannello]**.
- Il proprietario **può revocare le proprie credenziali** in qualsiasi momento: è la via corretta per chiudere un rapporto senza lasciare accessi aperti, dopo il trasferimento.

---

## 3. Connettore GA4: quote, errore "quota superata", campionamento, (other), soglie

**Ogni grafico GA4 in Data Studio è una richiesta alla Google Analytics Data API e consuma i token della proprietà del cliente.** Non c'è una quota separata per Data Studio.

- **Numeri Google (proprietà standard):** **200.000 token al giorno**, **40.000 all'ora**, **14.000 all'ora per progetto**, **10 richieste simultanee**, **10 errori server all'ora** per proprietà. Proprietà **360**: 2.000.000 / 400.000 / 140.000 / 50 / 50 ([Data API quotas](https://developers.google.com/analytics/devguides/reporting/data/v1/quotas)). Il costo in token di una richiesta cresce con righe, numero di dimensioni e metriche, complessità dei filtri, lunghezza del periodo e cardinalità.
- **Messaggi d'errore riconosciuti** dalla guida ufficiale: "Exhausted concurrent requests quota", "This property has issued too many requests in the last day / hour", "Too many requests ... have encountered errors in the last hour", "This property is denied access to Google Analytics" ([troubleshooting](https://docs.cloud.google.com/data-studio/troubleshooting-guide)).
- **Rimedi, nell'ordine in cui Google li elenca:** (1) **credenziali del proprietario** sull'origine, così i visualizzatori condividono una sola cache; (2) **una sola origine GA4 riutilizzabile** invece di più copie della stessa proprietà; (3) ridurre il traffico sul report (meno condivisioni, niente embed pubblici); (4) **meno grafici per pagina**; (5) **Estrai dati** (Extract data) come istantanea statica, ma la quota si resetta in **24 ore** e l'estrazione stessa consuma token; (6) **esportare GA4 in BigQuery** e connettere BigQuery; (7) Analytics 360; (8) connettori partner.
- ⚠️ **Le 10 richieste simultanee** sono il limite che scatta per primo su un report con molti grafici aperto da più persone: una pagina con 20 scorecard GA4 lancia 20 richieste insieme. Si spezzano le pagine (sez. 17) e si accettano le scorecard solo dove il numero decide qualcosa.
- **Campionamento**: Data Studio **non segnala** se i dati GA4 sono campionati ("Data Studio doesn't indicate if data from Google Analytics is sampled"); includere **oggi** nel periodo "può avere implicazioni di campionamento" ([GA4 sampling](https://docs.cloud.google.com/looker/docs/studio/google-analytics-4-sampling)). La Data API può restituire dati campionati e lo dichiara nel campo `samplingMetadatas` che Data Studio non espone ([reporting-data-expectations](https://developers.google.com/analytics/devguides/reporting/data/v1/reporting-data-expectations)). La soglia dei **10 milioni di eventi** per query (1 miliardo su 360) è documentata per le esplorazioni; per la Data API le fonti lette non la riportano in cifra: **[DA VERIFICARE]**.
- **Riga (other)**: compare quando una dimensione supera il limite di righe della tabella; Google chiama "alta cardinalità" ogni dimensione con **più di 500 valori** (percorso pagina, ID transazione, dimensioni personalizzate usate come ID). Vale anche per le risposte della Data API, quindi per Data Studio; i filtri **non entrano** nella riga (other) ([(other) row](https://support.google.com/analytics/answer/13331684)). Un report per pagina o per query di ricerca su un e-commerce grande va fatto da BigQuery, non dal connettore.
- **Soglie sui dati (thresholding)**: scattano con dati demografici, segnali Google e query di ricerca quando gli utenti sono pochi; sono definite dal sistema e **non regolabili**; allargare il periodo può farle sparire ([data thresholds](https://support.google.com/analytics/answer/9383630)). Con identità **blended/observed** i report sono soggetti a soglie, con **device-based** no; il cambio di identità non tocca i dati raccolti e si può fare avanti e indietro ([reporting identity](https://support.google.com/analytics/answer/10976610)).
- **Combinazioni impossibili**: GA4 conserva alcune combinazioni in tabelle separate che non si interrogano insieme. Casi documentati: **costo/metriche Google Ads con dimensioni evento** (nome evento), **dimensioni item** (ID/nome articolo) con metriche di scopo evento o utente, demografia con alcune dimensioni personalizzate. Nell'interfaccia GA4 le voci si disattivano in grigio; in Data Studio il grafico esce **vuoto o con zeri** senza avviso, oppure con "configurazione non valida" ([data compatibility](https://support.google.com/analytics/answer/11608978)). Il controllo si fa nel GA4 Dimensions & Metrics Explorer (sezione "Compatible fields") prima di promettere un grafico al cliente.
- **Perché i numeri non tornano con l'interfaccia GA4**: (a) **elaborazione 24-48 ore**: un report GA4 tirato il 1° del mese sul mese precedente cambia ancora; l'attribuzione degli eventi chiave si aggiusta fino a **12 giorni** ([data freshness](https://support.google.com/analytics/answer/11198161)); (b) soglie e (other) come sopra; (c) identità di reporting; (d) conteggi unici (utenti attivi, sessioni) stimati con **HyperLogLog++**, non esatti; (e) Data Studio "corrisponde ai report standard, non alle esplorazioni" ([connettore GA4](https://docs.cloud.google.com/looker/docs/studio/connect-to-google-analytics)). Regola per il report mensile: **si genera il PDF non prima del 3 del mese**, e la data di generazione va scritta sul report.
- Non supportati dal connettore nativo: **segmenti e confronti GA4**; i totali della tabella escono `null` se filtrati per campi calcolati, gruppi o intervalli; le barre impilate con filtri complessi su date ISO possono **gonfiare le sessioni** (stessa pagina). Permesso minimo sulla proprietà: **Lettura e analisi**.

---

## 4. Connettore Google Ads

- **"Campi generali dell'account" (Overall Account Fields)** mette in una lista sola tutte le dimensioni e metriche dell'account: è l'unica scelta sensata per un report cliente, le tabelle per singolo rapporto servono solo per casi speciali ([connettore Google Ads](https://docs.cloud.google.com/looker/docs/studio/connect-to-google-ads)).
- **Account amministratore (MCC)**: fino a **50 sotto-account per origine dati**; chi visualizza deve avere accesso **sia all'MCC sia a ogni sotto-account selezionato**, l'accesso al solo sotto-account non basta. Per il cliente singolo si connette **il suo account**, non l'MCC dell'agenzia: altrimenti al termine del rapporto il report smette di funzionare (sez. 2). Con valute miste e "Tutte le valute", i campi di ricavo vengono **convertiti nella valuta dell'MCC di primo livello**: su un report in euro per un cliente italiano si seleziona la sola valuta EUR.
- 🔴 **Conversioni ≠ Tutte le conversioni.** "Conversioni" (Conversions) conta solo le azioni **primarie** usate per le offerte, **esclude** le view-through e le chiamate da tablet/computer; "Tutte le conv." (All conversions) aggiunge le azioni **secondarie**, le view-through, le visite in negozio e le chiamate ([3419678](https://support.google.com/google-ads/answer/3419678), [11461796](https://support.google.com/google-ads/answer/11461796)). Su un report cliente: CPA e ROAS si calcolano su **Conversioni**; "Tutte le conv." si mostra solo con l'etichetta. Esistono anche le varianti **"per data di conversione"** (by conv. date), che riassegnano la conversione al giorno in cui è avvenuta, non al giorno del clic: due colonne dello stesso mese non coincidono, e non è un errore.
- **Costo** è già in valuta dell'account; il **Ricavo/Valore conv.** dipende dai valori passati dal tag. Le entità con **zero impressioni non compaiono** (campagne in pausa da un anno spariscono dalle tabelle, non sono state cancellate).
- Campi rimossi: **Auction Insights** dal 23/09/2024; **estensioni di località** dal 04/05/2026, sostituite dai campi **Asset località**: un report vecchio con quei campi mostra grafici rotti. Per gli asset creativi servono insieme **Tipo annuncio + ID asset** con clic/impressioni, altrimenti i numeri sono sbagliati.

---

## 5. Connettore Search Console

- **Impressione sito vs impressione URL**: due aggregazioni diverse, **una sola per origine dati**. Per vederle insieme servono due origini nello stesso report. Site: web, image, video, news. URL: anche discover e googleNews ([connettore Search Console](https://docs.cloud.google.com/looker/docs/studio/connect-to-search-console)). Regola: query, paesi, dispositivi e date si leggono dall'origine **Sito**; pagine e aspetto nella ricerca dall'origine **URL**. Clic e impressioni delle due origini **non coincidono** per costruzione (una pagina che appare due volte nella stessa SERP conta un'impressione sito e due impressioni URL): non si sommano e non si confrontano fra loro.
- **Query anonimizzate**: Google omette le query rare o con dati personali; in Data Studio escono come **valore vuoto** nella dimensione query, ma restano nei totali dei grafici (i totali del cliente saranno **più alti** della somma della tabella) ([17011259](https://support.google.com/webmasters/answer/17011259)). Si spiega nel report, oppure si filtra "query non è null" sapendo che si perdono clic.
- **16 mesi di storico**: confermato dal blog ufficiale Search Central (2018) e dal pannello, non da una pagina Help leggibile oggi **[DA VERIFICARE la pagina Help]**. Conseguenza: il confronto anno su anno esiste, quello a due anni no. Per lo storico oltre 16 mesi serve l'**export bulk in BigQuery** o un'estrazione mensile su Fogli.
- Gli ultimi giorni possono essere **dati preliminari** ("dataState final" contro "all" nell'API); Data Studio non lo indica. Il report mensile non include i 2-3 giorni finali del periodo se si vuole un numero stabile.

---

## 6. Fogli Google come origine

- Requisiti: **formato tabellare**, **una sola riga di intestazione**, **stesso tipo in ogni colonna**; le celle nascoste e filtrate sono **incluse** di default (ma vale per i filtri, non per le viste filtrate); i file su **Drive condiviso non sono supportati** (Team Drive) ([connettore Fogli](https://docs.cloud.google.com/data-studio/connect-to-google-sheets)).
- **Date**: la colonna deve contenere giorno, mese e anno completi ed essere formattata come **data** in Fogli (Formato → Numero → Data). Una data testuale non riconosciuta si converte con `PARSE_DATE("%d/%m/%Y", campo)` in un campo calcolato ([dates-and-times](https://docs.cloud.google.com/data-studio/dates-and-times)). Il formato italiano `gg/mm/aaaa` scritto a mano in celle "testo" è la causa più frequente di grafici vuoti.
- **Cache**: aggiornamento dei dati di default **15 minuti** (opzioni 1, 4, 12 ore); i valori cambiati e le righe nuove vengono letti alla query successiva, ma **una colonna aggiunta o rinominata non compare** finché non si fa **Aggiorna campi** sull'origine ([manage-data-freshness](https://docs.cloud.google.com/looker/docs/studio/manage-data-freshness)).
- Il periodo di default di un'origine Fogli è **tutto l'intervallo di date del foglio**, non gli ultimi 28 giorni: senza controllo intervallo, una scorecard somma tutta la storia.

---

## 7. BigQuery come origine: quando conviene

- **Si paga per byte letti a ogni query**, e ogni grafico è una query (cache a parte). Il **progetto di fatturazione** (Billing project) si sceglie nell'origine: chi paga può essere diverso da chi possiede i dati, mettendo il progetto dati nel `FROM` della query personalizzata ([connettore BigQuery](https://docs.cloud.google.com/looker/docs/studio/connect-to-google-bigquery)).
- Conviene quando: (a) il connettore GA4 finisce la quota o mostra (other); (b) servono più di 16 mesi di Search Console; (c) si vogliono transazioni e ID articolo insieme a sorgente/canale; (d) più clienti sullo stesso schema con un solo report modello (sez. 16). Non conviene per una PMI con 30.000 sessioni al mese senza export BigQuery già attivo: costa di più in configurazione di quanto rende.
- Regole di costo: tabella **partizionata per data** con la colonna di partizione come intervallo di date del report ("charts render more quickly while minimizing query costs"); tabelle a suffisso `YYYYMMDD` (l'export GA4) leggono **solo gli ultimi 28 giorni di default**; **tabelle materializzate invece di viste** per query pesanti; query personalizzate con `@DS_START_DATE` e `@DS_END_DATE` così il periodo del report limita i byte letti; freschezza di default **12 ore** ([improve-performance](https://docs.cloud.google.com/looker/docs/studio/improve-performance)).
- Con BigQuery si può usare un **account di servizio** come credenziale: è l'unico connettore dove il problema della sez. 2 ha una soluzione strutturale.

---

## 8. Unione dati (blend): join, limiti, errori tipici

- Fino a **5 tabelle** per unione; join **left outer, right outer, inner, full outer, cross**; condizioni solo di **uguaglianza** fra campi (nomi diversi ammessi se i valori coincidono); le join si valutano **da sinistra a destra** ([how-blends-work](https://docs.cloud.google.com/data-studio/how-blends-work), [blending-tips](https://docs.cloud.google.com/data-studio/blending-tips-and-advanced-concepts)).
- 🔴 **Prima della join ogni tabella viene raggruppata e aggregata sulle sue dimensioni; le metriche diventano dimensioni numeriche non aggregate.** Due conseguenze: (a) righe identiche collassano prima della join, quindi il risultato può avere **meno righe** dell'origine; (b) una left join con più corrispondenze **moltiplica le righe** e gonfia costi e conversioni. La spia è un costo Google Ads in unione più alto di quello nel pannello Ads.
- Errori tipici: unire GA4 e Google Ads su **Campagna** senza la **Data** nella condizione (le righe di giorni diversi si incrociano); unire su nomi campagna scritti diversamente nei due sistemi; mettere nel blend campi che nessun grafico usa ("Data Studio calcola tutte le righe del blend anche se il grafico ne usa una"); aspettarsi che un **filtro sul grafico** agisca prima della join: i filtri sulle tabelle del blend sono **pre-join**, quelli sul grafico **post-join**.
- I campi calcolati dentro una tabella del blend vedono **solo quella tabella**; il calcolo fra tabelle (es. costo Ads / conversioni GA4) si fa come **campo calcolato del grafico** sul blend.
- Ogni unione moltiplica le richieste e quindi i token GA4 (sez. 3): sui report dove tutto è unito, prima si prova a fare la metrica in BigQuery.

---

## 9. Campi calcolati: quello su cui si inciampa

- **Non si mescolano dimensioni (non aggregate) e metriche (aggregate) nella stessa formula**: `CASE WHEN Paese = "Italia" AND Conversioni > 100` è rifiutato ([use-functions](https://docs.cloud.google.com/looker/docs/studio/use-functions-in-calculated-fields)). Si aggrega prima (`SUM(Conversioni)`) oppure si fa il raggruppamento nel grafico.
- **CASE**: ogni ramo deve restituire lo **stesso tipo**; senza `ELSE` i non coperti escono `null`, e `null` sparisce dalle tabelle: mettere sempre `ELSE "Altro"`. Il raggruppamento delle campagne per cliente (`CASE WHEN REGEXP_MATCH(Campagna, ".*[Bb]rand.*") THEN "Brand" ...`) va nell'**origine dati**, non nel grafico, così vale per tutto il report.
- **REGEXP_MATCH richiede la corrispondenza dell'intera stringa** (non contiene: serve `.*x.*`), sintassi **RE2**, caratteri speciali con **doppia barra** `"\\."`; per "contiene" si usa `REGEXP_CONTAINS` o `CONTAINS_TEXT`.
- **Date**: `PARSE_DATE` per testi, `DATETIME_DIFF` per differenze, `TODATE` è la funzione della vecchia "modalità compatibilità" e non si usa nei campi nuovi ([dates-and-times](https://docs.cloud.google.com/data-studio/dates-and-times)). Le origini create prima di settembre 2020 possono avere ancora campi data in compatibilità: si aggiornano prima di scrivere formule, sapendo che i campi calcolati dipendenti vanno riscritti.
- I campi calcolati **non si rimappano** quando si sostituisce l'origine dati (sez. 16): vanno ricreati nella nuova origine con lo stesso nome prima della sostituzione.

---

## 10. Intervalli di date, confronto, periodo di default

- **Periodo di default per connettore**: Ads, Analytics e YouTube **ultimi 28 giorni**; Fogli e BigQuery **tutto il set di dati** ([set-report-date-ranges](https://docs.cloud.google.com/data-studio/set-report-date-ranges)). Sul report mensile si imposta a livello di report un intervallo **mobile "mese scorso"** e si lascia il controllo data al cliente.
- Gerarchia: report → pagina → componente; il livello più basso vince. Un grafico con intervallo **fisso** ignora il controllo data del cliente: si usa solo per i grafici "anno in corso" e va detto nel titolo del grafico.
- **Confronto**: periodo precedente, anno precedente, fisso, avanzato (es. "ultimi 30 giorni da ieri, allineati per giorno della settimana"). Lo imposta **solo l'editor**, il visualizzatore cambia il periodo corrente, non il confronto. "Periodo precedente" su un mese di 31 giorni confronta con 31 giorni che scavalcano il mese prima: per il cliente si usa **"mese precedente"** o l'avanzato allineato.
- La settimana parte di **domenica** di default: per l'Italia si sceglie il preset con **lunedì** o la dimensione **Settimana ISO**.
- Il periodo influenza la quota GA4 e i byte BigQuery: 13 mesi in una tabella per giorno su una proprietà grande finiscono in (other) o nel campionamento (sez. 3).

---

## 11. Filtri, controlli, parametri

- I **filtri a livello di report** valgono **solo per i componenti che usano l'origine dati predefinita del report**; un grafico su un'altra origine va filtrato a livello di grafico ([about-filter-properties](https://docs.cloud.google.com/data-studio/about-filter-properties)). Limiti: **10 clausole OR** per filtro, **75 clausole** per componente; dimensioni e metriche **non si mischiano in una clausola OR**; i filtri agiscono per **ID campo**, non per nome visualizzato.
- **Filtri (proprietà)** li vede solo l'editor; **controlli filtro** li muove il cliente. Dal gennaio 2026 i controlli possono filtrare **grafici su origini diverse** ("Filtra fra origini dati"): un solo menu a tendina Campagna può filtrare Ads e GA4 se i campi si chiamano allo stesso modo o vengono mappati ([use-controls-across-data-sources](https://docs.cloud.google.com/data-studio/use-controls-across-data-sources)).
- **Parametri**: testo, numero, booleano; nascono nell'origine dati e si sovrascrivono lungo report → pagina → gruppo → grafico; si passano nell'URL (`params=` con JSON URL-encoded) solo per i parametri spuntati in **Risorsa → Gestisci variabili (parametri)** ([parameters](https://docs.cloud.google.com/looker/docs/studio/parameters)). Uso tipico: un parametro "obiettivo mensile" per la scorecard di avanzamento, oppure il tipo di ricerca Search Console scelto dal cliente.

---

## 12. Freschezza dei dati e cache

- **Aggiornamento dei dati** (Data freshness) di default: **GA4, Google Ads, Search Console: ogni 12 ore, non modificabile**; **Fogli: 15 minuti** (1/4/12 ore); **BigQuery: 12 ore** (da 1 minuto a 12 ore); **Estrai dati: nessuna opzione**, si aggiorna solo con la pianificazione dell'estrazione ([manage-data-freshness](https://docs.cloud.google.com/looker/docs/studio/manage-data-freshness)).
- Le query con le stesse condizioni entro la finestra vengono servite **dalla memoria** (cache). Con credenziali del **proprietario** la cache è **una per tutti**; con credenziali del visualizzatore è **una per utente**, quindi la quota GA4 si consuma per ogni cliente che apre il report.
- **Aggiornamento manuale**: l'editor con Altre opzioni → **Aggiorna dati**; **dal 18/06/2026 anche il visualizzatore**, se l'editor lo abilita nelle impostazioni del report (tasto destro sul componente o pulsante dedicato); un minuto di attesa fra un aggiornamento e l'altro. Regola: per i report GA4 del cliente **si lascia disabilitato**, altrimenti ogni "aggiorna" brucia token e si arriva all'errore di quota il giorno della riunione.
- L'**aggiornamento automatico** del report (auto refresh) è solo **Pro**; e "non attiva un aggiornamento della cache": se la freschezza dell'origine è 12 ore, aggiornare ogni 5 minuti non cambia i numeri ([manage-auto-refresh](https://docs.cloud.google.com/looker/docs/studio/manage-auto-refresh-for-a-report)).

---

## 13. Livello report vs livello pagina

- Un componente è di pagina finché non si fa tasto destro → **Rendi a livello di report** (Make report-level): appare su tutte le pagine, dietro agli altri componenti di default (posizione modificabile in Tema e layout → Layout) ([component-report-level](https://docs.cloud.google.com/data-studio/component-report-level)). Non funziona sui **report responsive**.
- Da mettere a livello di report: **controllo intervallo di date**, logo e intestazione, il selettore Campagna/Canale. Da tenere a livello di pagina: i filtri che definiscono la pagina (es. pagina "Search" filtrata su tipo campagna).
- Un'origine dati sostituita a livello di pagina o report vale **solo per i componenti nuovi**, non per quelli esistenti (sez. 16).

---

## 14. Condivisione, incorporamento, invio programmato

- Per **modificare** serve sempre un account Google; per **vedere** no, se il link è "chiunque abbia il link". ⚠️ **Con un link pubblico anche le origini dati incorporate diventano leggibili da chiunque abbia il link** ([invite-others](https://docs.cloud.google.com/looker/docs/studio/invite-others-to-your-reports)). Con credenziali del proprietario, chi ha il link vede i dati GA4/Ads del cliente senza login: per un cliente PMI **si condivide con persone specifiche**, e il link pubblico si usa solo per report su dati aggregati che possono essere pubblici. Tetto **1.500 principal** per asset; gli amministratori Workspace possono bloccare la condivisione esterna.
- **Copia/download**: chi può modificare può anche condividere, copiare, stampare e scaricare; per i visualizzatori si può togliere download e copia dalle impostazioni di condivisione. La condivisione del report **condivide le origini incorporate ma non quelle riutilizzabili**.
- **Incorporamento (iframe/oEmbed)**: richiede il report condiviso (pubblico, con link, dominio, o persone specifiche con login); il visualizzatore non può aggiornare i dati a mano, il watermark resta, i segnalibri non funzionano ([embed-a-report](https://docs.cloud.google.com/looker/docs/studio/embed-a-report)). Un embed sul sito del cliente è traffico che consuma quota GA4 (sez. 3).
- **Invio programmato** (Condividi → Pianifica invio): PDF via e-mail, **max 50 destinatari**, il creatore è sempre incluso, **max 5 pagine di anteprima** nel corpo (il PDF ha tutte le pagine selezionate); usa i filtri e l'intervallo di default del report, i filtri si cambiano nella scheda Filtri della pianificazione ma non si aggiungono controlli; fuso orario **del sistema operativo di chi pianifica**; versione gratuita: **una pianificazione per report, frequenza massima giornaliera**, quote e-mail **200/giorno e 800/mese** (Workspace 500 / 3.000; Pro senza limiti) ([schedule-automatic-report-delivery](https://docs.cloud.google.com/looker/docs/studio/schedule-automatic-report-delivery)). Se si rimuove un filtro dal report sparisce da tutte le pianificazioni.
- ⚠️ Il PDF programmato del 1° del mese porta dati GA4 non definitivi (sez. 3): si programma **dal 3 in poi**.

---

## 15. Data Studio Pro: cosa aggiunge e quanto costa

- **Prezzo ufficiale: 9 USD per utente per progetto al mese**, prova **30 giorni** senza limite di utenti, poi fatturazione automatica mensile per licenze assegnate anche se inutilizzate; ogni abbonamento è legato a **un solo progetto Google Cloud** ([cloud.google.com/data-studio](https://cloud.google.com/data-studio), [try-pro](https://docs.cloud.google.com/data-studio/try-pro), [pro-subscription-overview](https://docs.cloud.google.com/data-studio/pro-subscription-overview)). Il prezzo in euro e l'IVA dipendono dalla fatturazione Cloud: non si promette al cliente una cifra in euro senza il preventivo Cloud Billing.
- Cosa aggiunge: contenuti **di proprietà dell'organizzazione** (risolve la sez. 2), **spazi di lavoro del team**, fino a **200 pianificazioni per report** con frequenza oraria, invio su **Google Chat e Slack**, oggetto e messaggio personalizzati, **avvisi** sulle metriche, **link personali** ai report, auto-refresh, Gemini, app mobile, CMEK e residenza dei dati (dal 11/06/2026), Cloud Customer Care con piano di supporto a parte ([about-pro](https://docs.cloud.google.com/data-studio/about-pro)).
- Per un consulente con 10 clienti PMI il Pro serve in un caso: quando i report devono **sopravvivere alle persone** (agenzia, turnover). Le licenze gratuite per chi ha Looker non valgono per contratti firmati dopo il **01/08/2026**.

---

## 16. Modelli e copie con sostituzione dell'origine dati

- **Fai una copia** (menu ⋮ → Fai una copia) copia pagine, grafici, controlli, stile e filtri, **non** le origini dati: si scelgono in copia; le origini non condivise appaiono come **"Unknown"**; pianificazioni e permessi **non si copiano** ([copy-a-report](https://docs.cloud.google.com/looker/docs/studio/copy-a-report)).
- ⚠️ **La nuova origine deve avere lo stesso schema**: Data Studio rimappa per ID e nome campo, ma **campi calcolati e definizioni dei filtri non vengono rimappati** e il grafico mostra "Chart configuration incomplete" ([replace-the-data-source](https://docs.cloud.google.com/data-studio/replace-the-data-source-for-a-component-page-or-report)). Procedura per il report modello multi-cliente: (1) i campi calcolati vivono nell'origine, con nomi identici; (2) per il cliente nuovo si crea l'origine dallo stesso connettore e si ricreano i campi calcolati (o si **copia l'origine** e si cambia la connessione); (3) si copia il report scegliendo le origini nuove; (4) si rilegge **tutta** la copia, come Google stesso raccomanda.
- Da un template della galleria: **Modifica e condividi** → **Usa i miei dati** → **Sostituisci dati**, una volta per origine.
- Il proprietario può **vietare la copia** ai visualizzatori: per i report modello dell'agenzia si vieta.

---

## 17. Prestazioni

- **Massimo 50 grafici per pagina** è il limite tecnico; il limite pratico è molto più basso: la guida dice "riduci il numero di grafici per pagina" come primo rimedio ai tempi di caricamento e alla quota GA4 ([add-charts-and-controls](https://docs.cloud.google.com/looker/docs/studio/add-charts-and-controls-to-your-report), [improve-performance](https://docs.cloud.google.com/looker/docs/studio/improve-performance)). Un report cliente: **una pagina per canale, 6-10 componenti per pagina**, regola empirica di chi scrive, non numero Google.
- **Estrai dati** (Extract data): istantanea di **max 100 MB e 750.000 righe** (oltre: errore sui MB, **troncamento silenzioso** sulle righe), aggiornabile a pianificazione; caricamento veloce, niente quota a ogni apertura, e disaggregando l'origine Ads si può riaggregare diversamente ([extract-data](https://docs.cloud.google.com/looker/docs/studio/extract-data-for-faster-performance)). Serve per: tabelle storiche di 13 mesi, report aperti da molte persone, embed. Non serve per: il numero di oggi.
- **Azioni di drill-down** al posto di due grafici; **blend con solo i campi usati**; freschezza alzata dove il dato non cambia (sez. 12); su BigQuery **BI Engine** e tabelle materializzate.

---

## 18. Igiene di un report ereditato: ordine di controllo

1. **Chi possiede le credenziali di ogni origine dati** (Risorsa → Gestisci le origini dati aggiunte → Modifica → credenziali): se è una persona uscita dall'azienda o il consulente precedente, si trasferisce o si riconnette **oggi**, prima che i 20 giorni scadano (sez. 2).
2. **Chi possiede il report** e con quale link è condiviso: "chiunque abbia il link" su dati GA4/Ads con credenziali del proprietario si chiude (sez. 14).
3. **Origini duplicate** della stessa proprietà GA4 (una per grafico): si consolidano in una riutilizzabile (sez. 3).
4. **Campi calcolati** con `TODATE`, campi in modalità compatibilità, campi Google Ads rimossi (Auction Insights, estensioni di località) (sez. 4 e 9).
5. **Intervalli fissi** dimenticati su singoli grafici e confronto "periodo precedente" su mesi (sez. 10).
6. **Blend**: costo o conversioni in unione più alti che nel pannello di origine (sez. 8).
7. **Pianificazioni** attive: destinatari, giorno del mese, chi le ha create (spariscono con il creatore).
8. **Grafici per pagina** e presenza di estrazioni scadute senza pianificazione (sez. 17).
9. **Nome del prodotto** nelle intestazioni e nei PDF: "Looker Studio" va aggiornato in "Data Studio (ex Looker Studio)" (sez. 1).

---

## 19. Meccanica del pannello (da verificare a mano)

- Dopo **Rendi proprietario** su un'origine, le credenziali del vecchio proprietario restano attive finché lui non le revoca: sul pannello del nuovo proprietario compare un avviso, o si scopre solo quando lui le revoca?
- L'opzione **aggiornamento dati per i visualizzatori** (18/06/2026): dove sta esattamente nelle impostazioni del report in italiano, ed è per report o per componente?
- Il connettore **Search Console** offre davvero l'account di servizio fra le credenziali, come dice la sua pagina, o solo BigQuery, come dice la pagina credenziali?
- Sostituendo l'origine GA4 di un cliente con quella di un altro, quanti campi calcolati si rompono in pratica se hanno lo stesso nome ma ID diverso?
- Con credenziali del proprietario, l'errore di quota GA4 visto dal cliente riporta il messaggio ufficiale o un generico "impossibile caricare i dati"?
- La quota e-mail 200/800 conta i destinatari per invio o gli invii?

---

## 20. Cosa non fare mai

- Costruire le origini dati del cliente con il proprio account Google senza un piano di trasferimento.
- Connettere l'MCC dell'agenzia in un report che resterà al cliente.
- Condividere con "chiunque abbia il link" un report con credenziali del proprietario su GA4 o Ads.
- Generare o programmare il PDF mensile il 1° del mese.
- Confrontare "Conversioni" di Ads con "Tutte le conv." o con gli eventi chiave GA4 senza dirlo.
- Sommare o confrontare impressioni sito e impressioni URL di Search Console.
- Unire GA4 e Ads su Campagna senza Data, e fidarsi del costo che ne esce.
- Usare il connettore GA4 per elenchi di pagine, query o transazioni su una proprietà grande: finisce in (other) o nel campionamento, senza avviso.
- Attivare l'aggiornamento manuale per i visualizzatori su report GA4 condivisi con molte persone.
- Promettere al cliente un prezzo in euro del Pro o una soglia di campionamento della Data API senza fonte.

---

## Fonti (verificate 20/09/2026)

**Ufficiali Google, lette:** [Release notes Data Studio (ultima voce 13/08/2026; rinomina 16/04/2026)](https://docs.cloud.google.com/data-studio/release-notes) · [Blog Google Cloud, rinomina 10/04/2026](https://cloud.google.com/blog/products/data-analytics/looker-studio-is-data-studio) · [Data credentials](https://docs.cloud.google.com/data-studio/data-credentials-article) · [About data sources](https://docs.cloud.google.com/data-studio/about-data-sources) · [Transfer ownership (20 giorni, credenziali)](https://docs.cloud.google.com/data-studio/transfer-ownership) · [Connettore Google Analytics](https://docs.cloud.google.com/looker/docs/studio/connect-to-google-analytics) · [GA4 sampling in Data Studio](https://docs.cloud.google.com/looker/docs/studio/google-analytics-4-sampling) · [Troubleshooting (errori quota e rimedi)](https://docs.cloud.google.com/data-studio/troubleshooting-guide) · [Data API quotas](https://developers.google.com/analytics/devguides/reporting/data/v1/quotas) · [Data API reporting data expectations](https://developers.google.com/analytics/devguides/reporting/data/v1/reporting-data-expectations) · [GA4 (other) row 13331684](https://support.google.com/analytics/answer/13331684) · [GA4 data thresholds 9383630](https://support.google.com/analytics/answer/9383630) · [GA4 reporting identity 10976610](https://support.google.com/analytics/answer/10976610) · [GA4 data compatibility 11608978](https://support.google.com/analytics/answer/11608978) · [GA4 data freshness 11198161](https://support.google.com/analytics/answer/11198161) · [Connettore Google Ads](https://docs.cloud.google.com/looker/docs/studio/connect-to-google-ads) · [Google Ads "All conversions" 3419678](https://support.google.com/google-ads/answer/3419678) · [Connettore Search Console](https://docs.cloud.google.com/looker/docs/studio/connect-to-search-console) · [Search Console Performance report 17011259](https://support.google.com/webmasters/answer/17011259) · [Search Analytics API query](https://developers.google.com/webmaster-tools/v1/searchanalytics/query) · [Connettore Fogli Google](https://docs.cloud.google.com/data-studio/connect-to-google-sheets) · [Dates and times](https://docs.cloud.google.com/data-studio/dates-and-times) · [Connettore BigQuery](https://docs.cloud.google.com/looker/docs/studio/connect-to-google-bigquery) · [How blends work](https://docs.cloud.google.com/data-studio/how-blends-work) · [Blending tips](https://docs.cloud.google.com/data-studio/blending-tips-and-advanced-concepts) · [Create, edit and manage blends](https://docs.cloud.google.com/looker/docs/studio/create-edit-and-manage-blends) · [Use functions in calculated fields](https://docs.cloud.google.com/looker/docs/studio/use-functions-in-calculated-fields) · [Set report date ranges](https://docs.cloud.google.com/data-studio/set-report-date-ranges) · [About filter properties](https://docs.cloud.google.com/data-studio/about-filter-properties) · [Parameters](https://docs.cloud.google.com/looker/docs/studio/parameters) · [Manage data freshness](https://docs.cloud.google.com/looker/docs/studio/manage-data-freshness) · [Manage auto refresh](https://docs.cloud.google.com/looker/docs/studio/manage-auto-refresh-for-a-report) · [Component, report-level](https://docs.cloud.google.com/data-studio/component-report-level) · [Invite others to your reports](https://docs.cloud.google.com/looker/docs/studio/invite-others-to-your-reports) · [Ways to share](https://docs.cloud.google.com/data-studio/ways-to-share-your-reports) · [Embed a report](https://docs.cloud.google.com/looker/docs/studio/embed-a-report) · [Schedule automatic report delivery](https://docs.cloud.google.com/looker/docs/studio/schedule-automatic-report-delivery) · [Data Studio (prezzo Pro 9 USD/utente/progetto/mese)](https://cloud.google.com/data-studio) · [About Pro](https://docs.cloud.google.com/data-studio/about-pro) · [Try Pro](https://docs.cloud.google.com/data-studio/try-pro) · [Pro subscription overview](https://docs.cloud.google.com/data-studio/pro-subscription-overview) · [Copy a report](https://docs.cloud.google.com/looker/docs/studio/copy-a-report) · [Replace the data source](https://docs.cloud.google.com/data-studio/replace-the-data-source-for-a-component-page-or-report) · [Create a report from a template](https://cloud.google.com/looker/docs/studio/create-a-report-from-a-template) · [Extract data](https://docs.cloud.google.com/looker/docs/studio/extract-data-for-faster-performance) · [Improve performance](https://docs.cloud.google.com/looker/docs/studio/improve-performance) · [Add charts and controls (50 per pagina)](https://docs.cloud.google.com/looker/docs/studio/add-charts-and-controls-to-your-report).

**Terze parti (contesto, non numeri Google):** [ppc.land sulla rinomina](https://ppc.land/data-studio-is-back-google-kills-looker-studio-name-for-good/) · [dataslayer sulla rinomina](https://www.dataslayer.ai/blog/looker-studio-data-studio-rebrand-2026) · [optizent, combinazioni GA4 non valide in Looker Studio](https://www.optizent.com/blog/invalid-configuration-invalid-combination-of-metrics-and-dimensions-ga4-looker-studio/) · blog vari sulla soglia dei 10 milioni di eventi (samarthanalytics, usercentrics).

**Non leggibili via fetch il 20/09/2026, da ricontrollare a mano:** `support.google.com/looker-studio/answer/9724286` e `.../7020039` (404 o redirect); [Search Console Performance report 7576553](https://support.google.com/webmasters/answer/7576553) (letta, ma senza la cifra dei 16 mesi); [Data API api-schema](https://developers.google.com/analytics/devguides/reporting/data/v1/api-schema) (compatibilità non esplicitata); [cloud.google.com/data-studio/pricing](https://cloud.google.com/data-studio/pricing) (reindirizza al listino Looker, senza il prezzo Pro); `docs.cloud.google.com/looker/docs/studio/work-with-dates-and-times`, `.../report-level-components`, `.../filter-your-data`, `.../case` (404: gli slug sono cambiati, usati gli equivalenti sotto `data-studio`).
