# Audit ga4-performance (20/09/2026)

File auditato: `orig/ga4-performance/SKILL.md` (ultima verifica dichiarata: 12/08/2026).
Metodo: lettura integrale; lettura delle note di rilascio GA4 (https://support.google.com/analytics/answer/9164320) da giugno a settembre 2026; per ogni affermazione di dominio delle sezioni 1, 2, 3, 6, 7, 8, 9 ricerca della pagina ufficiale `support.google.com/analytics` (o `tagmanager`) che la conferma o la smentisce. Le sezioni 4 e 5 (meccanica del pannello) non sono state contraddette da documentazione: sono segnalate solo dove Google ha annunciato qualcosa che le tocca.

Note di rilascio lette, giugno-settembre 2026 (in ordine): 08/06 integrazione Google Business Profile; 11/06 campo *Source group* e aggiornamento *source platform*; 11/06 filtro Hostname; 13/07 collegamento AdMob; 28/07 valuta obbligatoria nell'importazione dati campagne; 30/07 diagnostica per parametri aggregati (gbraid, gad_) mancanti; 10/08 report di validazione dell'importazione dati campagne; 11/08 finestre di conversione personalizzate; 09/09 Dashboard. Nessuna nota, in tutto il 2025-2026, su: limite eventi chiave, stati dei filtri, esplorazioni, Libreria/raccolte, identità dei report, soglie, conservazione, cardinalità, campionamento, Search Console.

---

## Regole smentite o cambiate

### 1. Auto-tagging contro UTM manuali (sezione 7) — SMENTITA
- Frase nella skill: *"Un UTM scritto a mano sopra un URL con auto-tagging **sovrascrive** quei valori e rompe l'importazione delle conversioni."*
- Cosa dice la fonte: in GA4 vale l'opposto. *"If you use manual tagging and auto tagging together, then the source, medium, and other traffic-classification dimensions use the auto-tagged values."* Non esiste in GA4 l'opzione "Allow manual tagging to override auto-tagging" che esisteva in Universal Analytics. Le metriche Google Ads (impressioni, clic, costo) restano agganciate ai valori auto-taggati.
- Fonte: https://support.google.com/analytics/answer/11242870 (Traffic-source dimensions, manual tagging, and auto-tagging). Vedi anche https://support.google.com/analytics/answer/10723328 (Benefits of Google Ads auto-tagging).
- Data del cambio: non è un cambio recente, è il comportamento GA4 da sempre; la regola era sbagliata già il 12/08.
- Nota operativa: la raccomandazione "su Google basta nominare bene la campagna" resta valida, ma la motivazione va riscritta: gli UTM manuali su un URL auto-taggato sono **ignorati** nelle dimensioni cross-channel, non sovrascrivono niente e non rompono l'importazione delle conversioni. Il rischio vero degli UTM su Ads è un altro: se l'auto-tagging è spento, il traffico arriva con gli UTM ma senza gclid, e le conversioni non si importano.

### 2. Modelli di attribuzione (sezione 6) — INCOMPLETA
- Frase nella skill: *"In GA4 restano **basato sui dati** e **ultimo clic**."*
- Cosa dice la fonte: i modelli disponibili sono **tre**: *Data-driven attribution*, *Paid and organic last click*, *Google paid channels last click*. Il testo ufficiale: *"There are 3 attribution models available in the Attribution reports in Google Analytics properties: Data-driven attribution; Paid and organic last click; Google paid channels last click."* Conferma della rimozione: *"The first click, linear, time decay, and position-based attribution models are no longer available as of November 2023."*
- Fonte: https://support.google.com/analytics/answer/10596866 (Get started with attribution) e https://support.google.com/analytics/answer/10597962 (Select attribution settings).
- Data del cambio: rimozione dei modelli a novembre 2023 (già valida al 12/08).

### 3. Cambio di modello di attribuzione come "frattura" (sezioni 6 e 10) — DA RIFORMULARE
- Frasi nella skill: sez. 6 *"Un confronto fra periodi con impostazioni diverse produce differenze che sembrano performance e sono contabilità"*; sez. 10 *"Confrontare periodi a cavallo di una pulizia degli eventi chiave o di un cambio di modello di attribuzione, senza dirlo."*
- Cosa dice la fonte: il cambio di **modello** è retroattivo, il cambio di **finestra di lookback** no. *"Changing the reporting attribution model applies to historical and future data."* e *"Changes to the conversion window apply going forward and will be reflected in all reports."*
- Fonte: https://support.google.com/analytics/answer/10597962 e https://support.google.com/analytics/answer/16291704.
- Conseguenza: la frattura nella serie storica la produce il cambio di **finestra di lookback** (e la pulizia degli eventi chiave), non il cambio di modello, che riscrive anche il passato. La skill mette insieme le due cose nella stessa frase e va separata.

### 4. Thresholding e identità dei report (sezioni 3 e 6) — CAMBIATA NELLA FORMULAZIONE
- Frasi nella skill: sez. 3 *"Compare quando **Google Signals è attivo** nell'identità dei report. Si toglie passando l'identità dei report a *basata su dispositivi*."*; sez. 6 *"L'identità che include **Google Signals** attiva il **thresholding**"*.
- Cosa dice la fonte oggi:
  - Le opzioni di identità dei report sono *Blended* (User-ID, device ID, poi modellazione), *Observed* (User-ID, poi device ID), *Device-based*. Google Signals **non compare** più fra i componenti dell'identità. Le prime due opzioni *"are subject to data thresholds"* perché richiedono abbastanza attività da utenti loggati; quindi passare a *Device-based* riduce ancora le soglie, ma la causa non è "Google Signals nell'identità".
  - La pagina sulle soglie elenca solo due casi in cui i dati vengono trattenuti: dati demografici (o pubblici definiti su dati demografici) e query di ricerca; e due rimedi: allargare l'intervallo di date, esportare in BigQuery.
  - Dal **15/06/2026** l'impostazione Google Signals *"will only control the association of your Google Analytics sourced data with signed in user information for behavioral reporting"*; la raccolta dei cookie/ID Ads è governata dal Consent Mode in Google Ads.
- Fonti: https://support.google.com/analytics/answer/10976610 (Reporting identity), https://support.google.com/analytics/answer/9383630 (About data thresholds), https://support.google.com/analytics/answer/17016975 (Updates to Google Analytics Data Controls, efficace 15/06/2026).
- Cosa cambia in pratica: la regola "righe sparite a volumi bassi → prova a mettere identità *basata su dispositivi*" resta operativamente utile e coerente con 10976610, ma la spiegazione va riscritta: il thresholding scatta su **demografia** e **query di ricerca** quando ci sono pochi utenti; l'identità *Blended/Observed* lo rende più probabile. Dire "Google Signals nell'identità" oggi non corrisponde all'interfaccia.

### 5. Conservazione dei dati: cosa tocca (sezione 8) — IMPRECISA
- Frase nella skill: *"La conservazione riguarda i dati a livello di evento, cioè esplorazioni, segmenti e **confronti**. I report standard aggregati continuano a mostrare periodi più lunghi."*
- Cosa dice la fonte: *"The data retention setting does not affect standard aggregated reports (including primary and secondary dimensions) in your Google Analytics property, even if you create comparisons in the reports. The data retention setting only affects explorations and funnel reports."*
- Fonte: https://support.google.com/analytics/answer/7667196.
- Conseguenza: i **confronti nei report standard** NON sono toccati dalla conservazione; togliere "confronti" dalla frase o precisare "confronti e segmenti dentro le esplorazioni".
- Aggiunte dalla stessa pagina: *"The two-month retention period is always applied to age, gender, and interest data regardless of your settings."*; *"When a standard property becomes Large or a 360 property becomes XL, the event-level data retention setting is automatically reduced to 2 months and event-level data older than 2 months becomes inaccessible and is permanently deleted."*; il cambio di impostazione scatta dopo 24 ore e in quelle 24 ore è reversibile.

### 6. Esclusione referral "finisce in diretto" (sezione 2) — SEMPLIFICAZIONE DA CORREGGERE
- Frase nella skill: *"Il traffico escluso finisce in *diretto* e si perde l'informazione su chi lo ha portato."*
- Cosa dice la fonte: l'esclusione aggiunge `ignore_referrer=true` all'evento, e *"This parameter indicates to Analytics that the referrer should not be displayed as a traffic source."* Ma per via dell'attribuzione last-non-direct-click la sessione può essere attribuita alla sorgente precedente, non necessariamente a diretto: esempio ufficiale in cui la seconda sessione *"is also attributed to Domain B"* pur dopo l'esclusione. Inoltre GA4 gestisce già da solo l'auto-referral: il traffico non viene identificato come referral *"When the referring website matched the same domain of the current page or any of its subdomains."* Limite: 50 referral indesiderati per stream.
- Fonte: https://support.google.com/analytics/answer/10327750.
- Conseguenza: "si esclude solo l'auto-referral" va precisato: per lo stesso dominio e i suoi sottodomini l'esclusione è già automatica; la lista serve per domini diversi (gateway di pagamento, dominio secondario). Il traffico escluso non "finisce in diretto" sempre: eredita la sorgente precedente se c'è.

---

## Novità da aggiungere

- **Finestre di conversione personalizzate (11/08/2026)** — https://support.google.com/analytics/answer/9164320 (voce "Updated Conversion Window Configuration"). Nella sezione *Pubblicità > Gestione conversioni* le **conversioni** (quelle condivise con Google Ads, distinte dagli eventi chiave: https://support.google.com/analytics/answer/13965727) accettano finestre a intero libero: 1-90 giorni per click-through, 1-30 per engaged-view (prima fissa a 3). Perché conta: è un'altra impostazione non retroattiva che può spostare i numeri fra due periodi; va aggiunta alla lista "guardare prima di leggere un report" della sezione 6, e va distinta dalla finestra di lookback degli eventi chiave (7/30 e 30/60/90) che resta a preset.
- **Dashboard (09/09/2026)** — https://support.google.com/analytics/answer/17217303. Nuova superficie dentro **Report** (*+ Crea > Dashboard*): fino a 15 schede per proprietà standard, 30 per 360; *"All published dashboards are shared with the property"*; niente API, niente segmenti, niente confronti a livello di scheda. Perché conta: cambia la risposta della sezione 3/5 "esplorazione o report personalizzato?" — per un cruscotto di KPI condiviso la terza via è la dashboard; e tocca la sezione 5 perché il menu Report ha ora un pulsante *+ Crea* accanto alla Libreria (possibile impatto sull'editor di raccolta osservato il 12/08: da ricontrollare a mano).
- **Filtro Hostname (11/06/2026)** — https://support.google.com/analytics/answer/9164320 e https://support.google.com/analytics/answer/13296761. Terzo tipo di filtro dati accanto a traffico interno e sviluppatore: esclude gli eventi per hostname. Perché conta: è la difesa contro spam/referral fantasma e copie del sito su domini di staging; va nella sezione 2 e nell'ordine di igiene della sezione 9. Conta nel limite dei 10 filtri.
- **Campo Source group (11/06/2026)** — note di rilascio. Raggruppa le sorgenti per piattaforma (Facebook/Instagram/TikTok, e retroattivamente ChatGPT, Perplexity). Perché conta: nuova dimensione nel catalogo di Esplora (la tabella dei nomi italiani della sezione 4 non la include) e utile per leggere il traffico AI.
- **Integrazione Google Business Profile (08/06/2026)** — note di rilascio. Crea una **raccolta dedicata** in Libreria con 7 metriche GBP su finestra mobile di 6 mesi. Perché conta: sezione 5 "quante raccolte esistono": può comparire una raccolta in più non creata da noi, e conta nel limite di 7.
- **Importazione dati campagne: valuta obbligatoria (28/07/2026) e report di validazione (10/08/2026)** — note di rilascio. Perché conta: la sezione 5 dice di togliere *Costo non Google* su siti senza e-commerce; se invece si importano costi Meta o altri, l'import ora richiede il campo valuta e c'è un report che segnala le campagne senza costo/clic/impressioni.
- **Diagnostica parametri aggregati gbraid / gad_ (30/07/2026)** — note di rilascio. Perché conta: nella sezione 7 (Google Ads) il controllo "auto-tagging attivo" ha ora un avviso nativo quando gli URL perdono i parametri aggregati.
- **Google Signals → Consent Mode (efficace 15/06/2026)** — https://support.google.com/analytics/answer/17016975. Perché conta: la voce "Google Signals" nell'Amministrazione non governa più la raccolta di cookie/ID Ads; chi fa igiene di una proprietà ereditata deve guardare il Consent Mode in Google Ads, non solo l'interruttore in GA4.
- **Eventi chiave: fino a 24 ore per comparire nei report standard** — https://support.google.com/analytics/answer/13128484: *"allow for up to 24 hours for it to show up in standard reports."* Perché conta: rafforza la conseguenza 2 della sezione 1 (il giorno della pulizia è misto anche per latenza, non solo perché la pulizia avviene a metà giornata).
- **Copia di report ed esplorazioni fra proprietà** — https://support.google.com/analytics/answer/15401228. Perché conta: per la sezione 3 ("non si creano via API") esiste almeno una via ufficiale per replicare un'esplorazione su un'altra proprietà senza rifarla a mano.

---

## Fonti da agganciare alle regole esistenti

Sezione 1
- *"Contrassegnare o togliere un evento chiave NON è retroattivo"* → https://support.google.com/analytics/answer/13128484 — *"Marking an event as a key event affects reports from time of creation. It doesn't change historic data."*
- *"`[DA VERIFICARE]` limite di eventi chiave per proprietà standard: il valore che gira è 30"* → CONFERMATO: 30 standard, 50 per 360. https://support.google.com/analytics/answer/13128484 e https://support.google.com/analytics/answer/12229528 (Configuration limits). Il tag `[DA VERIFICARE]` si può togliere.
- *"Gli eventi della misurazione avanzata (`form_submit`, `form_start`, `scroll`, `click`, `view_search_results`)"* → https://support.google.com/analytics/answer/9216061 (Enhanced measurement): elenco degli eventi per opzione e conferma che le opzioni si spengono una per una.
- *"Amministrazione, Visualizzazione dei dati, Eventi"* per gli eventi chiave → https://support.google.com/analytics/answer/12844695 (Create or modify key events).

Sezione 2
- *"Prima la regola di traffico interno ... Poi il filtro dati"* → https://support.google.com/analytics/answer/10104470 (Filter out internal traffic): i passi sono nello stesso ordine; *"`traffic_type` is the only event parameter for which you can define a value. `internal` is the default value"*.
- Tabella degli stati Test / Attivo / Inattivo → https://support.google.com/analytics/answer/10104470 e https://support.google.com/analytics/answer/13296662 — *Testing: "Analytics identifies matching data with the 'Test data filter name' dimension"*; *Active: "Analytics applies the data filter to incoming data and makes permanent changes"*; *Inactive: "Analytics isn't evaluating the filter"*. Il fatto che il filtro nasca in Test non è scritto nella documentazione: resta osservazione di pannello (va marcato ✅ VERIFICATO, non come regola documentale).
- *"Il filtro non è retroattivo"* → https://support.google.com/analytics/answer/13296761 (Data filters) — *"Analytics evaluates data filters from the point of creation forward. Data filters do not affect historical data."* e *"Once you apply a data filter, the effect on the data is permanent ... never be available in Google Analytics or BigQuery."* Vedi anche https://support.google.com/analytics/answer/16608575 (Filter out unwanted traffic): *"Traffic filters only apply to new data and won't change previously collected data in your reports."*
- Limite: **10 filtri dati per proprietà** → https://support.google.com/analytics/answer/10104470. Da aggiungere.
- Esclusione referral → https://support.google.com/analytics/answer/10327750 (vedi smentita 6 sopra; 50 voci per stream).

Sezione 3
- *"Non sono condivise di default"* → https://support.google.com/analytics/answer/7579450 — *"When you first create an exploration, only you can see it."*; *"Shared explorations can be viewed, but not edited, by anyone who has the Viewer role."*; *"You must duplicate or copy a shared exploration in order to edit it."*
- Preset mobili contro intervallo personalizzato fisso (✅ del 12/08) → stessa pagina, conferma documentale: esplorazione salvata il 1° maggio con "Last 28 days" mostra il 1° giugno i dati 4-31 maggio; con intervallo personalizzato 1-31 maggio mostra sempre 1-31 maggio.
- Limiti: **200 esplorazioni per utente per proprietà, 500 condivise per proprietà, 10 segmenti per esplorazione, 10 filtri per scheda** → https://support.google.com/analytics/answer/7579450 e https://support.google.com/analytics/answer/12229528.
- *"`[DA VERIFICARE]` la soglia ... 10 milioni di eventi per query"* → CONFERMATO: *"10 million events for standard Google Analytics properties and up to 1 billion events for Google Analytics 360 properties"*, indicato nell'icona di qualità dei dati con la percentuale. https://support.google.com/analytics/answer/13331292 (About data sampling) e https://support.google.com/analytics/answer/12229528. Per 360 il default è 100M con opzione "More detailed results" a 1B: https://support.google.com/analytics/answer/13888627. Il tag `[DA VERIFICARE]` si può togliere.
- *"Non si creano via API"* → nessuna pagina ufficiale lo afferma in negativo. La Data API *"programmatically accesses Google Analytics report data"* (https://developers.google.com/analytics/devguides/reporting/data/v1) e l'Admin API non espone una risorsa "exploration" (https://developers.google.com/analytics/devguides/config/admin/v1). Citare così, come assenza, non come frase ufficiale.
- Cardinalità → sezione 8.

Sezione 6
- *"`[DA VERIFICARE]` finestre di lookback: 30, 60 e 90 giorni per gli eventi chiave, 7 e 30 giorni per l'acquisizione"* → CONFERMATO: *"For acquisition key events (first_open and first_visit), the default lookback window is 30 days. You can switch to 7 days"*; *"For all other key events, the default lookback window is 90 days. You can also choose 30 days or 60 days."*; engaged-view: default 3 giorni. https://support.google.com/analytics/answer/16291704 e https://support.google.com/analytics/answer/10597962. Percorso: Amministrazione > Visualizzazione dei dati > Eventi > Impostazioni di attribuzione. Il tag `[DA VERIFICARE]` si può togliere. (Attenzione alla novità dell'11/08 sulle *conversioni* in Pubblicità, che è un'impostazione diversa.)
- Modelli disponibili e rimossi → https://support.google.com/analytics/answer/10596866 (vedi smentita 2). Le conversioni possono essere riattribuite fino a 7 giorni dopo.
- *"Tre opzioni: mista, basata su utenti, basata su dispositivi"* → https://support.google.com/analytics/answer/10976610; il cambio non è distruttivo: *"You can switch between the options at any time without making any permanent impact on data."*
- Percorsi di conversione → https://support.google.com/analytics/answer/10607798 (Get started with advertising).

Sezione 7
- *"Il collegamento sblocca tre cose: esportazione dei pubblici, importazione degli eventi chiave come conversioni, dimensioni Ads dentro i report"* → https://support.google.com/analytics/answer/9379420 (Link Google Ads and Analytics). Se si scollega, il traffico Ads resta come `google / cpc` o con gli UTM disponibili.
- *"Quello che è evento chiave in GA4 deve essere la primaria su Google Ads"* → https://support.google.com/analytics/answer/13965727 (Conversions vs. key events): solo le conversioni create in *Pubblicità > Gestione conversioni* sono condivise con Ads.
- Search Console: *"I due report compaiono in Libreria ma non in nessuna raccolta pubblicata"* → CONFERMATO: *"The Search Console collection of reports is unpublished by default. You can find the collection under Library"*. Un data stream web si collega a una sola proprietà Search Console e viceversa; 16 mesi di storico; dati disponibili dopo 48 ore. https://support.google.com/analytics/answer/10737381. Report: https://support.google.com/analytics/answer/13682862 (Query) e https://support.google.com/analytics/answer/13682863 (Traffico di ricerca organica Google).
- Container GTM, ID misurazione statico → NON SOURCEABILE su pagina ufficiale. Le pagine GTM (https://support.google.com/tagmanager/answer/13543899, https://support.google.com/tagmanager/answer/12131703, https://support.google.com/tagmanager/answer/14681508) descrivono il Google tag, l'ereditarietà delle impostazioni e la diagnostica *"Missing Google tags"* (*"appears when your event tags in Google Tag Manager don't have matching Google tags"*), ma nessuna dice che l'ID deve essere una costante. Esiste un thread della community (https://support.google.com/tagmanager/thread/265589145) sullo stesso sintomo, non recuperabile in testo. La regola resta ✅ VERIFICATA di persona, e va lasciata così, senza spacciarla per documentale; la diagnostica *Missing Google tags* è la controprova ufficiale più vicina.

Sezione 8
- *"`[DA VERIFICARE]` soglia di cardinalità giornaliera"* → NON ESISTE un numero ufficiale. La pagina https://support.google.com/analytics/answer/13208658 (About the (other) row) dice solo: *"Any dimension with more than 500 values should be considered a high-cardinality dimension"* e *"Analytics 360 properties have higher limits when compared to the limits for standard properties"*, senza dichiarare il limite di righe delle tabelle. Anche https://support.google.com/analytics/answer/13888627 non dà numeri. Quindi il "500" che gira è una **soglia di attenzione**, non un cut-off documentato; scriverlo così e chiudere il `[DA VERIFICARE]` con "Google non pubblica il numero".
- *"Su proprietà standard il massimo è 14 mesi"* → CONFERMATO: opzioni 2 o 14 mesi per standard; 2/14/26/38/50 per 360. https://support.google.com/analytics/answer/7667196. Il "default più basso" = 2 mesi: la pagina non usa la parola *default* per la proprietà nuova (la usa solo per i dati Google signed-in, 26 mesi); i risultati di ricerca sul dominio ufficiale lo riportano come default, ma non l'ho letto verbatim sulla pagina. Scrivere "all'apertura è a 2 mesi" come osservazione, non come citazione.
- *"`[DA VERIFICARE]` dimensioni personalizzate..., parametri per evento, lunghezza dei nomi evento"* → CONFERMATI: 50 dimensioni personalizzate a livello evento, 50 metriche personalizzate, 25 dimensioni a livello utente (= 25 proprietà utente), 25 parametri per evento, nome evento 40 caratteri, nome parametro 40, valore parametro 100 (eccezioni: `page_title` 300, `page_referrer` 420, `page_location` 1000), nome proprietà utente 24, valore 36. https://support.google.com/analytics/answer/12229528 (Configuration limits) e https://support.google.com/analytics/answer/9267744 (Event collection limits); vedi anche https://support.google.com/analytics/answer/14240153. Altri limiti utili dalla stessa pagina: 100 pubblici, 50 confronti salvati, 50 segmenti salvati, 50 insight personalizzati, esportazione 100.000 righe.

Sezione 5 (solo le parti di dominio, non la meccanica)
- *"Massimo 12 metriche per report"* → https://support.google.com/analytics/answer/10445879 — *"You can add up to 12 metrics to a detail report."*; *"Each Google Analytics property can have up to 150 custom reports."*
- *"Una raccolta esiste ma non si vede finché non è pubblicata"* → https://support.google.com/analytics/answer/10460557 — *"After you save a report collection, you must publish the collection to make it available to everyone in the left navigation."* Limiti da aggiungere: **7 raccolte per proprietà, 5 argomenti per raccolta, 10 report per argomento**.
- *"La descrizione ha un limite di 255 caratteri"* → non documentato: resta ✅ verificato a mano.

Sezione 9
- Punto 5 *"Spegnere Interazioni con modulo"* → https://support.google.com/analytics/answer/9216061.
- Punto 4 *"Conservazione dei dati a 14 mesi"* → https://support.google.com/analytics/answer/7667196.
- Punto 10 *"Definizioni personalizzate"* → https://support.google.com/analytics/answer/12229528.

---

## Problemi interni al file

1. **Sezione 7, auto-tagging**: la regola è capovolta rispetto alla documentazione (vedi smentita 1). È l'errore più grave del file perché porta a diagnosticare "importazione rotta" per una causa che non esiste.
2. **Sezioni 3 e 6 dicono la stessa cosa sul thresholding in due punti**, con la stessa spiegazione superata ("Google Signals nell'identità dei report"). Tenerne una sola, in sezione 6, con la formulazione aggiornata; in sezione 3 lasciare il rimando.
3. **Sezione 6 + sezione 10**: "cambio di modello di attribuzione" trattato come frattura della serie storica, ma per Google il cambio di modello riscrive anche il passato; è il cambio di **finestra** a essere solo in avanti. Le due sezioni vanno allineate.
4. **Sezione 8**: "esplorazioni, segmenti e confronti" contro la fonte, che esclude esplicitamente i confronti dentro i report standard.
5. **Sezione 2**: "finisce in diretto" e "si esclude solo l'auto-referral" sono semplificazioni: l'auto-referral su stesso dominio/sottodomini è già gestito, e il traffico escluso può ereditare la sorgente precedente.
6. **Sezione 6**: "restano basato sui dati e ultimo clic" omette che l'ultimo clic esiste in due varianti (*a pagamento e organico* / *canali a pagamento Google*), che danno numeri diversi.
7. **Sezione 1, "Cosa può essere un evento chiave"**: la regola "solo se ha un tag suo nel container" è un criterio di metodo nostro, non una regola GA4. Va bene, ma andrebbe marcata come tale, altrimenti al primo giro un lettore la cerca su una fonte e non la trova.
8. **Sezione 1, `purchase` "compare nell'elenco anche su un sito senza e-commerce"**: non sourceable; è un'osservazione. Marcarla ✅ con data, come le altre.
9. **Sezione 3, "Non si creano via API"**: vero per assenza, non citabile come frase ufficiale (vedi sopra). E ora esiste la copia fra proprietà (15401228), che attenua la conseguenza "esplorazione = non distribuibile".
10. **Sezione 0 e sezione Fonti**: la skill dichiara di non avere fonti e chiede di "aggiungere qui l'elenco degli URL": con questo audit l'elenco esiste e la sezione Fonti va riempita; la data in testa va riscritta.
11. **Tag `[DA VERIFICARE]` chiudibili**: eventi chiave 30/50 (sez. 1), campionamento 10M (sez. 3), lookback 7/30 e 30/60/90 (sez. 6), limiti definizioni personalizzate (sez. 8). **Non chiudibile**: cardinalità (sez. 8), perché Google non pubblica il numero: va riscritto come "soglia di attenzione 500 valori, limite di righe non pubblicato".
12. **Sezione 4 e 5 (meccanica)**: nessuna nota di rilascio contraddice quanto osservato. Due segnali da ricontrollare a mano, non da correggere per documentazione: (a) dal 09/09/2026 il menu Report ha *+ Crea > Dashboard*, quindi il pannello Libreria/raccolte potrebbe essere stato ritoccato; (b) la tabella dei nomi italiani di sezione 4 non include *Source group* (nuova dimensione da giugno 2026) e il conteggio "364 dimensioni / 168 metriche" è probabilmente cambiato.
13. **Sezione 5, "Costo non Google"**: la raccomandazione di toglierlo è corretta per siti senza import; ma con le novità del 28/07 e 10/08 (valuta obbligatoria, report di validazione) va aggiunta la controindicazione per chi importa costi Meta.
14. **Ambiguità terminologica "conversioni" / "eventi chiave"**: la skill usa "conversioni" in senso colloquiale (sez. 1, 5, 7). In GA4 le due parole hanno oggi significati diversi e impostazioni diverse (Amministrazione > Eventi per gli eventi chiave; Pubblicità > Gestione conversioni per le conversioni condivise con Ads, con le nuove finestre 1-90). Un lettore che segue la sezione 6 per la finestra e finisce su Gestione conversioni trova un'altra impostazione.

---

## Confermato senza cambiamenti

- Non retroattività degli eventi chiave (sez. 1): confermata dalla frase ufficiale, oltre che dalla misurazione del 12/08.
- Limite 30 eventi chiave standard / 50 per 360 (sez. 1).
- Ordine regola di traffico interno → filtro dati, parametro `traffic_type` con default `internal`, tre stati del filtro, non retroattività e permanenza del filtro (sez. 2).
- Esplorazioni private alla nascita, condivisione in sola lettura, preset mobili e intervallo personalizzato fisso (sez. 3).
- Campionamento a 10M eventi per query su standard, indicato dall'icona di qualità dei dati (sez. 3).
- Modelli rimossi (primo clic, lineare, decadimento temporale, basato sulla posizione) da novembre 2023 (sez. 6).
- Finestre di lookback degli eventi chiave: acquisizione 30 (o 7), altri 90 (o 30/60), engaged-view 3 (sez. 6).
- Le tre funzioni del collegamento Google Ads (sez. 7).
- Report Search Console in Libreria ma non pubblicati di default; due report Query e Traffico di ricerca organica (sez. 7).
- Conservazione: 2 o 14 mesi su standard, 14 è il massimo; tocca solo esplorazioni (e report canalizzazione), non i report standard aggregati (sez. 8, con la precisazione sui confronti).
- 12 metriche per report dettagliato; raccolte visibili solo se pubblicate (sez. 5, parti documentali).
- Nessuna nota di rilascio fra agosto e il 20/09/2026 tocca: limite eventi chiave, stati dei filtri, esplorazioni, Libreria/raccolte, identità dei report, soglie, conservazione, cardinalità, campionamento, collegamento Search Console.
