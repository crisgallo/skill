---
name: "meta-ads-performance"
description: "Regole operative verificate per montare, ottimizzare e diagnosticare campagne Meta Ads (Facebook e Instagram). Usare ogni volta che si lavora su Gestione inserzioni: struttura campagne, fase di apprendimento, budget, pubblici, attribuzione, Conversions API, formati e aree di sicurezza. Serve anche per leggere un pannello altrui e capire cosa è rotto."
---

# Meta Ads: regole operative

**Ultima verifica delle fonti: 20 settembre 2026.**

🔄 **Cosa è cambiato (verifica del 20/09/2026), con la data del cambio di Meta, non quella in cui ce ne siamo accorti:**

- **AEM web: la data scritta qui era sbagliata.** La rimozione della priorità a 8 eventi, della tab *Misurazione aggregata degli eventi*, della selezione del dominio in campagna e dell'obbligo di verifica del dominio è stata **annunciata da Meta il 15/05/2023** e completata su Gestione eventi **entro metà 2025** ([adviso](https://www.adviso.ca/en/blog/evolution-aggregated-measurement-meta) · [segwise, agg. 03/09/2026](https://segwise.ai/blog/facebook-aggregated-event-measurement)). Questa skill se n'è accorta solo il **12/08/2026** e l'aveva registrata come cambio di quel giorno: non lo era, e non è una "modifica del 2026". Verificato anche sul pannello (12/08/2026): le tab di Gestione eventi sono Panoramica, Testa gli eventi, Diagnostica, Cronologia, Impostazioni, e di AEM non c'è traccia né lì né nel pannello del dominio.
- **12/01/2026:** rimosse le finestre 7 giorni view e 28 giorni view (sez. 3). **03/03/2026:** conta come clic solo il clic sul link; interazioni social in *engage-through* a 1 giorno (sez. 3).
- **Febbraio 2026:** flusso di creazione unificato, Advantage+ e budget di campagna preselezionati (sez. 2).
- **18/05/2026:** pubblici da sito/app su evento Acquisto fino a **730 giorni**, esistenti alzati in automatico (sez. 5).
- **01/07/2026:** location fee, **3% in Italia**, fuori dal budget della campagna (sez. 2).
- **27-28/07/2026:** Advantage+ Creative riscrive di default il testo dentro le immagini (sez. 6).
- **06/08/2026:** suddivisioni dispositivo/ora/frequenza opt-in (sez. 7). **10/08/2026:** pubblici di sola esclusione (sez. 5).
- **19-21/08/2026:** avviata la rimozione delle esclusioni di posizionamento a livello di gruppo (sez. 2).

---

## 0. Manutenzione di questa skill (leggere per primo)

Meta cambia le regole più volte l'anno. Nel 2026, alla data di questa verifica, tre modifiche hanno invalidato pratiche consolidate: **12/01/2026** (finestre 7 giorni view e 28 giorni view rimosse), **03/03/2026** (ridefinizione del clic, categoria *engage-through*), **18/05/2026** (retention dei pubblici Acquisto a 730 giorni, con aggiornamento automatico dei pubblici esistenti). Quindi:

1. **Prima di applicare una soglia numerica su un account che spende, ricontrollala.** Se la verifica ha più di **due o tre mesi**, si rifà una ricerca sulle fonti prima di toccare il pannello. Le soglie numeriche che qui sono etichettate "regola empirica di terzi" non sono di Meta: valgono come punto di partenza, non come limite.
2. **Quando una fonte smentisce una regola scritta qui, si aggiorna la skill nello stesso momento**, non "poi". Una skill che invecchia in silenzio è peggio di nessuna skill, perché dà sicurezza falsa.
3. Aggiornando, si **riscrive la data** in cima e si annota **cosa è cambiato e da quando**: serve a capire quali dati storici sono confrontabili e quali no. ⚠️ **"Da quando" è la data del cambio di Meta, non la data in cui ce ne siamo accorti.** L'errore è già stato fatto con AEM (cambio 2023-2025, registrato come 12/08/2026).
4. Segnali che è ora di ricontrollare: il pannello mostra etichette o opzioni che qui non sono descritte; **un'impostazione che dovrebbe esserci non si trova** (è il segnale che ha smascherato la rimozione di AEM); i numeri di un report cambiano senza che nessuno abbia toccato niente.
5. ⚠️ **Il Centro assistenza di Meta si contraddice.** Diverse pagine descrivono ancora gli otto slot AEM come se esistessero. La pagina autorevole è quella sulle *modifiche alle campagne per le conversioni sul sito web*. In caso di conflitto fra due pagine ufficiali, vince **quello che si vede nel pannello**.
6. ⚠️ **Le pagine facebook.com/business/help non si leggono da questo ambiente** (20/09/2026: il fetch restituisce solo il titolo, curl HTTP 400). Vanno ricontrollate a mano in un browser autenticato; finché non lo si fa, le regole che poggiano su quelle pagine sono sostenute solo da fonti secondarie.

---

## 1. La fase di apprendimento è il centro di tutto

**Soglia: 50 eventi di ottimizzazione a settimana per gruppo di inserzioni.** Non per campagna, per gruppo. Sotto quella soglia il gruppo resta in *Apprendimento limitato* e la consegna è instabile. (Confermata da più fonti che citano il Centro assistenza, fra cui [pigeondigital 01/04/2026](https://www.pigeondigital.com/insight/facebook-ads-learning-phase-50-conversions-rule-2026); pagina ufficiale non leggibile via fetch il 20/09/2026.)

Non è un numero magico: è il volume minimo perché l'algoritmo prenda decisioni statisticamente sensate. Conta anche la **costanza** del segnale, non solo il totale.

### Cosa RESETTA l'apprendimento (verificato 08/2026)

Nota del 20/09/2026: lista confermata dalle fonti terze; nessun annuncio Meta fra agosto e settembre 2026 tocca la fase di apprendimento. La pagina ufficiale *Modifica significativa* ([942374239243867](https://www.facebook.com/business/help/942374239243867)) non è leggibile via fetch e va ricontrollata a mano.

- modificare il **budget di oltre il 20-25%** — ⚠️ regola empirica di terzi, non soglia Meta ([withblip](https://withblip.com/blog/meta-ads-learning-phase-bulk-editing/), senza data). Posizione ufficiale: un cambio di budget o di offerta «può essere significativo, ma **dipende dalla magnitudine**».
- cambiare l'**evento di ottimizzazione**
- toccare il **targeting**
- **aggiungere o togliere inserzioni** dal gruppo
- cambiare **strategia di offerta**
- mettere in **pausa il gruppo per 7 giorni o più** — ⚠️ i 7 giorni sono regola empirica di terzi, non soglia Meta (withblip); per Meta qualunque pausa può contare, e dipende dalla durata.

### Regole di condotta che ne derivano

1. **Quattordici giorni senza toccare niente** dopo il lancio. Le decisioni su struttura, creatività e targeting si prendono *prima*, con una lista di controllo, non aggiustando in corsa.
2. Se una modifica è inevitabile, **falle tutte insieme**: un reset solo invece di tre.
3. Le variazioni di budget si fanno **a scaglioni sotto il 20%**, distanziate (stessa regola empirica di terzi: il numero non è di Meta, la cautela sì).
4. *Apprendimento limitato* non si cura aggiungendo budget a pioggia: si cura **consolidando**. Unire i gruppi che si sovrappongono fa confluire gli eventi in un posto solo.

---

## 2. Struttura: nel 2026 si consolida, non si segmenta

La direzione è **pochi gruppi grandi con molte creatività dentro**, non venti gruppi per venti interessi.

- **1-3 gruppi di inserzioni per campagna.** ⚠️ Regola empirica, non soglia Meta, e non presente in nessuna delle fonti citate: il criterio vero è **50 eventi a settimana ÷ budget**, il numero di gruppi ne discende.
- Con budget totale **sotto i 50 $ al giorno: non più di 3-4 gruppi in tutto l'account.** Con 20 €/giorno significa **uno o due gruppi, punto.** (Stessa regola empirica.) Dal 01/07/2026 quei 20 € sono al lordo della location fee, vedi sotto.
- Meglio più creatività dentro lo stesso gruppo che più gruppi con poche creatività. Dal 26/08/2026 la colonna **Diversità creativa** (Bassa/Media/Alta per gruppo, "stimata e in sviluppo") e dal 25/08/2026 la colonna **Spesa stimata** rendono leggibile nel pannello la varietà per gruppo ([admakeai](https://admakeai.com/blog/meta-ads-updates-september-2026) · [adsuploader](https://adsuploader.com/blog/meta-ads-updates)).
- **Budget di campagna (CBO) e Advantage+: da febbraio 2026 il default è "tutto acceso".** Meta ha unificato i flussi Manuale e Advantage+ Shopping/Sales: per ogni nuova campagna Vendite, Contatti e Promozione app sono **preselezionati** pubblico Advantage+, posizionamenti Advantage+, miglioramenti creativi Advantage+ e budget di campagna, ciascuno disattivabile singolarmente; le campagne Advantage+ Sales hanno di nuovo i gruppi di inserzioni (tetto 50 inserzioni per gruppo, dal 2025). Su un pannello ereditato si controllano **gli interruttori**, non solo il CBO. Il CBO resta la scelta pratica sugli account piccoli: evita di spostare soldi a mano. Fonti: [superscale](https://superscale.ai/learn/cbo-vs-abo-advantage-plus/) · [admanage](https://admanage.ai/blog/meta-advantage-plus-shopping-campaigns) · [1clickreport](https://www.1clickreport.com/blog/meta-advantage-plus-campaign-setup-2026); pagina ufficiale [153514848493595](https://www.facebook.com/business/help/153514848493595) non leggibile via fetch il 20/09/2026. (Corretto il 20/09/2026: prima qui c'era "CBO default dal 2024", senza fonte che lo sostenesse.)

**L'errore classico su budget piccoli:** dieci pubblici da 5 € al giorno. Ogni gruppo resta sotto la soglia, nessuno esce dall'apprendimento, e si paga il prezzo dell'instabilità su tutti.

### Location fee (dal 01/07/2026)

Sulle inserzioni viste in Europa Meta addebita un sovrapprezzo per Paese **fuori dal budget della campagna**, come voce separata in Fatturazione: **Italia 3%**, Francia 3%, Spagna 3%, UK 2%, Austria 5%, Turchia 5%. Il ROAS letto dal pannello è al lordo di quel 3%. Fonti: [tdmp](https://www.tdmp.co.uk/insights/meta-location-fees-dst-landing-july-2026-costs-billing-and-affected-ads-explained) · [almcorp](https://almcorp.com/blog/meta-location-fees-2026-ad-price-increase-six-countries/) · [digitalapplied](https://www.digitalapplied.com/blog/meta-europe-location-fees-july-2026-advertiser-guide).

### Posizionamenti (aggiornato 20/09/2026)

- 🔴 **Le esclusioni di posizionamento a livello di gruppo stanno sparendo** (notifica in-product dal 19-21/08/2026, rollout graduale, nessuna data finale annunciata): non si potranno più escludere singoli posizionamenti, piattaforme, dispositivi o sistemi operativi dal gruppo. Restano i controlli a livello di account e le *value rules* (offerta ridotta fino a -90%, che non è un'esclusione). Chi esclude Audience Network o Reels per proteggere il CPA perde lo strumento. Fonti: [socialmediatoday 20/08/2026](https://www.socialmediatoday.com/news/meta-removes-option-to-exclude-ad-placements/828461/) · [jonloomer](https://www.jonloomer.com/meta-removing-placement-controls-ad-sets/) · [admakeai](https://admakeai.com/blog/meta-ads-updates-september-2026) · [commonthreadco](https://commonthreadco.com/blogs/coachs-corner/meta-ads-changes-2026).
- **Messenger Stories** rimosso come posizionamento (interfaccia dal 27/08/2026, API dal 27/10/2026); **Instagram Explore Feed** rimosso nell'API v26.0 (29/07/2026). Il budget si ridistribuisce da solo; nei confronti storici per posizionamento spariscono due righe. Fonti: [goodmorningco](https://goodmorningco.com/blog/meta-ads-update-august-2026) · [adsuploader](https://adsuploader.com/blog/meta-ads-updates).

---

## 3. Attribuzione: cosa è cambiato nel 2026

- **Default oggi per un gruppo con conversione sul sito: 7 giorni dal clic + 1 giorno engage-through + 1 giorno dalla visualizzazione** (modello standard). Corretto il 20/09/2026: prima qui mancava l'engage-through. Fonti: [jonloomer](https://www.jonloomer.com/meta-ads-attribution-2026/) · [jetfuel 29/03/2026](https://jetfuel.agency/meta-ads-attribution-settings-2026/).
- **12/01/2026:** le finestre *7 giorni dalla visualizzazione* e *28 giorni dalla visualizzazione* sono state **rimosse**. La finestra **28 giorni dal clic resta disponibile** in reporting per confronto. Chi usava le finestre lunghe ha visto crollare le conversioni attribuite: le fonti danno **30-40%** sulla finestra 8-28 giorni (20-40% nel B2B). Il "15-30% per la sola 7d view" scritto qui prima è una stima empirica di terzi non ritrovata nelle fonti citate, non soglia Meta. Fonte: [dataslayer 19/01/2026](https://www.dataslayer.ai/blog/meta-ads-attribution-window-removed-january-2026).
- **03/03/2026:** ridefinito cosa conta come clic: **solo il clic sul link**. Le interazioni social sono state spostate in una categoria a parte, *engage-through*, con finestra di **1 giorno**; la soglia video per l'engaged view è scesa da **10 a 5 secondi**. Fonte: [dataslayer 09/04/2026](https://www.dataslayer.ai/blog/meta-attribution-change-2026-what-engage-through-attribution-is-and-why-your-numbers-look-different).

**Conseguenza pratica:** confrontare periodi a cavallo di quelle date senza saperlo produce cali che sembrano performance e sono contabilità. Prima di dire "è calato", verificare che la finestra sia la stessa.

⚠️ Su un account vecchio le finestre sono spesso **disomogenee fra campagne** (1 giorno contro 7). Uniformarle prima di confrontare qualsiasi cosa.

📌 **Regola di Cristiano (chat Cowork del 19/09/2026, progetto Sceglinatura):** spesa, risultati, costo per risultato e ROAS si leggono **nel pannello che ha speso i soldi**: Meta da Gestione inserzioni, Google da Google Ads. GA4 serve per **tendenze**, stagionalità, confronti fra periodi, vendite per prodotto totali e comportamento sul sito, **non per attribuire conversioni ai canali**. ⛔ Le due fonti non si mescolano nella stessa tabella di rendimento: se servono entrambe, sono due misure diverse, ciascuna con scritto quale pannello la dice. Il caso che l'ha generata: nel funnel GA4 per sessione gli acquisti senza sorgente erano 170 su 185 a luglio 2026 (92%) e 103 su 116 ad agosto (89%); `google/cpc` risultava 1 acquisto a luglio e 0 ad agosto mentre Google Ads ne dichiarava 120 e 93. I due sistemi non diranno mai lo stesso numero, e non è un difetto da riparare.

---

## 4. Pixel e Conversions API

**Pixel da solo non basta più.** Lo standard è **Pixel + CAPI insieme**: gli eventi lato server aggirano i limiti del browser, e alzano l'**Event Match Quality**.

- **EMQ sotto 6: la finestra di attribuzione che scegli conta poco**, perché una quota alta di conversioni è modellata e non osservata. (Il 6/10 come soglia "buona" è confermato da [conversios 26/03/2026](https://www.conversios.io/blog/meta-attribution-window-changes-2026-fix-your-tracking/); il nesso con la finestra è un'inferenza operativa di questa skill, non è nella fonte.)
- In Gestione eventi, la colonna **Metodo di collegamento** dice la verità: se su tutti gli eventi c'è scritto solo **Browser**, la CAPI non esiste. Quando è a posto, dice *Browser e server*.
- Vie possibili: container server-side (Stape e simili hanno piani d'ingresso) oppure integrazione diretta lato CMS.
- 🔴 **Browser e server devono mandare lo stesso nome evento e lo stesso `event_id`**, altrimenti Meta conta due volte invece di deduplicare. Se un container server-side riscrive il nome evento con una trasformazione, quella trasformazione va cambiata **nello stesso giro** in cui si cambia il nome lato browser: due pubblicazioni distanti lasciano una finestra in cui gli eventi non deduplicano.
- ⚠️ **Marketing API: la v24.0 scade il 06/10/2026**; le rimozioni della v26.0 si estendono a tutte le versioni il 27/10/2026, e le chiamate a versioni scadute vengono eseguite in silenzio come versione successiva. Un'integrazione CAPI o GTM server-side pinnata alla v24 va aggiornata prima di ottobre. Fonti: [admakeai agosto 2026](https://admakeai.com/blog/meta-ads-updates-august-2026) · [kitchn](https://www.kitchn.io/blog/meta-marketing-api-q2-2026-update).
- ✅ **AEM per gli eventi web: non c'è più niente da configurare** (annuncio Meta 15/05/2023, tab rimossa entro metà 2025; qui registrato solo il 12/08/2026, vedi intestazione). Otto slot per dominio, priorità degli eventi, insiemi di valori e dominio di conversione in campagna: rimossi per il web. Gli eventi vengono elaborati da Meta senza intervento. Quindi la vecchia raccomandazione "verifica il dominio e imposta la priorità prima di spendere" **non vale più**: aggiungere un nome evento nuovo non consuma nessuno slot e non richiede riordini. Fonti: [adviso](https://www.adviso.ca/en/blog/evolution-aggregated-measurement-meta) · [segwise agg. 03/09/2026](https://segwise.ai/blog/facebook-aggregated-event-measurement); pagina ufficiale [721422165168355](https://www.facebook.com/business/help/721422165168355) non leggibile via fetch il 20/09/2026.
- ⚠️ **Per le campagne app iOS il modello a 8 eventi prioritizzati resta in vigore**, e così sugli account che Meta non ha ancora migrato (segwise, 03/09/2026). **Se in un pannello la tab AEM c'è ancora**, lì la priorità conta e le vecchie regole valgono. Si guarda, non si presume.

---

## 5. Pubblici

- **Due soglie, non una.** Corretto il 20/09/2026: prima qui c'era "circa 1000 persone, sotto non è pubblicabile e non genera lookalike", ed era impreciso. **Minimo tecnico per creare un lookalike: 100 persone dello stesso Paese** nella fonte; 1.000-5.000 è la raccomandazione di qualità. **Minimo pratico per la consegna: ~1000**: sotto, Meta mostra l'avviso "pubblico troppo piccolo" e rallenta o limita la consegna, non blocca la pubblicazione. Un lookalike "non disponibile" quasi sempre significa **fonte troppo magra**, non un errore. Fonti: [jonloomer](https://www.jonloomer.com/meta-ads-lookalike-audiences/) · [adnabu](https://blog.adnabu.com/facebook/facebook-lookalike-audiences/) · [tribeupacademy](https://tribeupacademy.com/meta-ads-retargeting-audience-too-small/); pagina ufficiale [1523083297982009](https://www.facebook.com/business/help/1523083297982009) non leggibile via fetch il 20/09/2026.
- Le fonti **non sono equivalenti**: su un profilo con poco traffico web, le **interazioni con il profilo Instagram a 365 giorni** possono valere decine di migliaia di persone mentre i visitatori del sito a 180 giorni restano sotto mille. **Guardare i numeri prima di decidere su cosa poggiare il retargeting.**
- Le interazioni sono un bacino **largo ma tiepido**: chi ha guardato un profilo non è chi vuole comprare. Il lookalike all'1% serve a stringere.
- Un pubblico da sito appena creato **si popola con lo storico già raccolto dal pixel**: crearlo oggi con finestra 180 giorni vale come averlo avuto sei mesi fa. **Crearli presto costa zero e vale molto.**
- Finestre: 180 giorni per i visitatori, 365 per interazioni e lead. ⚠️ **Eccezione dal 18/05/2026: i pubblici da sito e app basati sull'evento Acquisto arrivano a 730 giorni**, e quelli esistenti a 180 giorni **sono stati alzati in automatico a 730** salvo opt-out manuale per singolo account; il tetto di 180 resta per gli altri eventi web. Un'esclusione "acquirenti ultimi 180 giorni" può oggi escludere due anni di clienti dalle campagne fredde: su ogni account ereditato si controlla la retention effettiva dei pubblici Acquisto. Fonti: [comunicazione del rep Meta, via X](https://x.com/oliverwhudson/status/2054897286254145872) · [davidtamachi 06/06/2026](https://davidtamachi.ca/blog-meta-730-day-custom-audience-expansion); pagina ufficiale non verificata direttamente. Le finestre corte (30 giorni) si svuotano nei periodi di silenzio editoriale.
- Nei pubblici da URL mettere **anche i vecchi indirizzi** delle pagine che hanno cambiato slug: chi è passato prima del redirect ha il vecchio URL nel pixel.

### Trappole del pannello

- Creando un pubblico da profilo Instagram o pagina Facebook, **l'origine preselezionata può essere di un altro cliente** collegato al Business Manager. Va sempre controllata.
- **Non si elimina un pubblico se qualcuno ci ha costruito sopra un lookalike:** prima i simili, poi le fonti.
- **I pubblici salvati non si eliminano insieme ai personalizzati:** due operazioni separate.
- Eliminando un pubblico usato da una campagna, Meta chiede se mettere in pausa la campagna. **Rispondere consapevolmente**: quel messaggio è anche un modo per scoprire campagne attive che i filtri non mostravano.
- **Pubblici di sola esclusione (dal 10/08/2026):** pubblico da lista clienti usabile solo per escludere, contrassegnato in libreria, **non convertibile in pubblico normale e non usabile come fonte di lookalike**. Fonti: [socialmediatoday 10/08/2026](https://www.socialmediatoday.com/news/meta-adds-dedicated-ad-exclusion-audiences/827520/) · [jonloomer](https://www.jonloomer.com/exclusion-only-custom-audiences/) · [commonthreadco](https://commonthreadco.com/blogs/coachs-corner/meta-exclusion-only-audiences-ecommerce-2026).
- **Etichette sui pubblici (dal 16/07/2026):** lookalike e pubblici salvati **non sono etichettabili**, non cercarli per etichetta ([admakeai agosto 2026](https://admakeai.com/blog/meta-ads-updates-august-2026)).
- **Meta One (abbonamento, dal 15/09/2026):** Competitive Insights, Custom Audience Insights, programmazione e badge verificati sono dietro paywall. Se uno strumento di lettura dei pubblici manca, può essere l'abbonamento e non un errore: da verificare sul pannello ([adsuploader](https://adsuploader.com/blog/meta-ads-updates)).

---

## 6. Formati e aree di sicurezza

- **Marzo 2026: Meta ha unificato Facebook Stories, Facebook Reels, Instagram Stories e Instagram Reels in un'unica area di sicurezza 9:16.** Un solo verticale corretto vale per tutti e quattro ([billo 16/06/2026](https://billo.app/blog/meta-ads-safe-zones/)).
- **Verticale 9:16:** coperti il **14% in alto**, **fino al 35% in basso** (670 px su 1920: è il caso peggiore, Reels; Stories circa 20%) e il **6% per lato**. Si progetta per il 35%: l'area utile è poco più di metà schermo. Le fonti 2026 raccomandano **1440x2560**; 1080x1920 resta il minimo ([adnabu](https://blog.adnabu.com/meta-ads/meta-safe-zones/) · [superscale](https://superscale.ai/learn/meta-ad-sizes)).
- Nella zona coperta ci va **solo estensione di sfondo**: mai testo, logo o richiamo all'azione.
- Feed: **4:5 (1080x1350, o 1440x1800)** è il formato che occupa più schermo; l'1:1 come secondo asset.
- I video vanno pensati **muti**: in feed l'audio parte spento.
- Se un elemento di firma (nome del prodotto, dominio, richiamo) sta ai bordi del fotogramma, nel verticale finisce **sotto l'interfaccia**. Va ancorato all'area sicura, non al bordo.
- ⚠️ **Dal 27-28/07/2026 Advantage+ Creative riscrive di default il testo dentro le immagini caricate:** genera fino a 8 varianti di titolo sull'immagine mantenendo font, colori e layout. Il controllo su testo e area sicura non è più solo del file: si disattiva per singola creatività, oppure si limitano i termini in Branding (parole vietate, tono). Fonti: [commonthreadco](https://commonthreadco.com/blogs/coachs-corner/meta-ads-changes-2026) · [admakeai agosto 2026](https://admakeai.com/blog/meta-ads-updates-august-2026).

---

## 7. Come si legge un pannello che non si conosce

Ordine di lettura che fa emergere i problemi veri:

1. **Campagne con l'interruttore acceso**, anche se in bozza: sono spese pronte a partire. ⚠️ Spegnere una campagna **non spegne i suoi gruppi di inserzioni**: si controllano anche quelli.
2. **Filtro sulle inserzioni attive** per vedere cosa sta davvero spendendo. Non è esaustivo: una campagna può risultare attiva altrove e non comparire lì.
3. **Modifiche non pubblicate** in sospeso, spesso con errori dentro.
4. **Gestione eventi**: quali eventi arrivano, da quale metodo, con quale EMQ, e **quali sono fermi da settimane** (di solito rotti da un restyling del sito e mai riparati).
5. **Pubblici**: dimensioni, non nomi. E la **retention effettiva dei pubblici Acquisto** (180 o 730, sez. 5).
6. **Verifica del dominio**: utile per l'autorità sul dominio, **non più necessaria per la configurazione degli eventi** (vedi sezione 4).
7. **Nomi e finestre di attribuzione**: se sono disomogenei, nessun confronto storico regge.
8. **Interruttori Advantage+ e posizionamenti** nei gruppi: cosa è preselezionato e quali esclusioni sono ancora in piedi (sez. 2).
9. **Suddivisioni per dispositivo, ora e frequenza (opt-in dal 06/08/2026):** se non attivate in Colonne > Suddivisioni aggiuntive (API `POST /act_<ID>/insights/feature-settings`) le righe escono **vuote o a zero senza alcun errore**. Uno zero lì può essere un opt-in mancante, non un dato. Fonti: [goodmorningco](https://goodmorningco.com/blog/meta-ads-update-august-2026) · [admakeai agosto 2026](https://admakeai.com/blog/meta-ads-updates-august-2026).
10. **Impostazioni business > Integrazioni > Ads MCP Server:** il server MCP ufficiale Meta Ads (16/07/2026) ha un pannello permessi (11/08/2026) che nasce con **tutte e 7 le azioni di scrittura attive**. Su un account ereditato si controlla chi può scrivere da lì ([admakeai settembre 2026](https://admakeai.com/blog/meta-ads-updates-september-2026)).

---

## 8. Cosa non fare mai

- Ottimizzare per **copertura** quando lo scopo è costruire un bacino di retargeting: la copertura non lascia un pubblico su cui tornare, il traffico sì.
- Spendere su **pubblico freddo B2B** senza aver prima verificato come si comporta il traffico freddo già acquistato: su un caso seguito i tassi di coinvolgimento erano ridicoli rispetto ad altre fonti (osservazione, non regola generale).
- Confrontare periodi con finestre di attribuzione diverse.
- Toccare una campagna durante l'apprendimento perché "non sta andando".
- Giudicare una campagna di costruzione bacino sui lead: misura la cosa sbagliata.
- **Dichiarare un prerequisito che non hai verificato sul pannello corrente.** Il 12/08/2026 la priorità AEM è stata data per necessaria basandosi su questa skill: non esisteva più.
- **Dare per scontata un'esclusione di posizionamento** montata mesi fa: dal 19-21/08/2026 può non essere più applicabile (sez. 2).

---

## Fonti (verificate 20/09/2026)

**Ufficiali Meta**, tutte (pagina ufficiale non leggibile via fetch il 20/09/2026, da ricontrollare a mano): [Misurazione aggregata degli eventi](https://www.facebook.com/business/help/721422165168355) · [Fase di apprendimento](https://www.facebook.com/business/help/112167992830700) · [Modifica significativa](https://www.facebook.com/business/help/942374239243867) · [Dimensione dei pubblici da sito](https://www.facebook.com/business/help/1523083297982009) · [Advantage+ e flusso di creazione](https://www.facebook.com/business/help/153514848493595).

**Apprendimento:** [Regola dei 50 eventi (pigeondigital, 01/04/2026; copre solo la soglia, non i reset)](https://www.pigeondigital.com/insight/facebook-ads-learning-phase-50-conversions-rule-2026) · [Cosa resetta l'apprendimento; regole empiriche 20-25% e 7 giorni (withblip, senza data)](https://withblip.com/blog/meta-ads-learning-phase-bulk-editing/).

**Struttura e Advantage+:** [Consolidamento 2026 (creative-brackets, 11/05/2026; non sostiene "CBO default" né i numeri di gruppi)](https://creative-brackets.com/blog/meta-ads-account-structure-in-2026/) · [CBO, ABO e flusso unificato (superscale)](https://superscale.ai/learn/cbo-vs-abo-advantage-plus/) · [Advantage+ Shopping (admanage)](https://admanage.ai/blog/meta-advantage-plus-shopping-campaigns) · [Setup Advantage+ 2026 (1clickreport)](https://www.1clickreport.com/blog/meta-advantage-plus-campaign-setup-2026) · [Advantage+ Sales pre-flusso unificato (bir.ch, 08/08/2025; non parla di budget piccoli)](https://bir.ch/blog/advantage-plus-sales-campaigns-guide).

**Attribuzione:** [Impostazioni 2026 (jetfuel, 29/03/2026)](https://jetfuel.agency/meta-ads-attribution-settings-2026/) · [Rimozione finestre 12/01/2026 (dataslayer, 19/01/2026)](https://www.dataslayer.ai/blog/meta-ads-attribution-window-removed-january-2026) · [Engage-through 03/03/2026 (dataslayer, 09/04/2026)](https://www.dataslayer.ai/blog/meta-attribution-change-2026-what-engage-through-attribution-is-and-why-your-numbers-look-different) · [Attribuzione 2026 (jonloomer; HTTP 403 via fetch, letto da estratti)](https://www.jonloomer.com/meta-ads-attribution-2026/).

**Pixel, CAPI, AEM, API:** [CAPI, EMQ e deduplicazione (conversios, 26/03/2026)](https://www.conversios.io/blog/meta-attribution-window-changes-2026-fix-your-tracking/) · [Annuncio AEM 15/05/2023 (adviso)](https://www.adviso.ca/en/blog/evolution-aggregated-measurement-meta) · [Tab AEM rimossa, riserva iOS (segwise, agg. 03/09/2026)](https://segwise.ai/blog/facebook-aggregated-event-measurement) · [Marketing API Q2 2026 (kitchn)](https://www.kitchn.io/blog/meta-marketing-api-q2-2026-update).

**Pubblici:** [Retention 730 giorni, testo del rep Meta (X)](https://x.com/oliverwhudson/status/2054897286254145872) · [Retention 730 giorni (davidtamachi, 06/06/2026)](https://davidtamachi.ca/blog-meta-730-day-custom-audience-expansion) · [Lookalike, minimo 100 per Paese (jonloomer; 403 via fetch)](https://www.jonloomer.com/meta-ads-lookalike-audiences/) · [Lookalike (adnabu)](https://blog.adnabu.com/facebook/facebook-lookalike-audiences/) · [Pubblico troppo piccolo (tribeupacademy)](https://tribeupacademy.com/meta-ads-retargeting-audience-too-small/) · [Pubblici di sola esclusione (socialmediatoday, 10/08/2026)](https://www.socialmediatoday.com/news/meta-adds-dedicated-ad-exclusion-audiences/827520/) · [Pubblici di sola esclusione (jonloomer; 403 via fetch)](https://www.jonloomer.com/exclusion-only-custom-audiences/) · [Pubblici di sola esclusione, e-commerce (commonthreadco)](https://commonthreadco.com/blogs/coachs-corner/meta-exclusion-only-audiences-ecommerce-2026).

**Formati, posizionamenti, pannello:** [Aree di sicurezza (billo, 16/06/2026)](https://billo.app/blog/meta-ads-safe-zones/) · [Aree di sicurezza (adnabu)](https://blog.adnabu.com/meta-ads/meta-safe-zones/) · [Dimensioni (superscale)](https://superscale.ai/learn/meta-ad-sizes) · [Rimozione esclusioni posizionamento (socialmediatoday, 20/08/2026)](https://www.socialmediatoday.com/news/meta-removes-option-to-exclude-ad-placements/828461/) · [Rimozione esclusioni posizionamento (jonloomer; 403 via fetch)](https://www.jonloomer.com/meta-removing-placement-controls-ad-sets/) · [Cambi Meta Ads 2026: posizionamenti, Advantage+ Creative (commonthreadco)](https://commonthreadco.com/blogs/coachs-corner/meta-ads-changes-2026) · [Aggiornamenti agosto 2026: Advantage+ Creative, suddivisioni, etichette, API v24 (admakeai)](https://admakeai.com/blog/meta-ads-updates-august-2026) · [Aggiornamenti settembre 2026: posizionamenti, colonne, MCP (admakeai)](https://admakeai.com/blog/meta-ads-updates-september-2026) · [Aggiornamenti agosto 2026: suddivisioni opt-in, Messenger Stories (goodmorningco)](https://goodmorningco.com/blog/meta-ads-update-august-2026) · [Aggiornamenti: Explore Feed, colonne, Meta One (adsuploader)](https://adsuploader.com/blog/meta-ads-updates) · [Location fee (tdmp)](https://www.tdmp.co.uk/insights/meta-location-fees-dst-landing-july-2026-costs-billing-and-affected-ads-explained) · [Location fee (almcorp)](https://almcorp.com/blog/meta-location-fees-2026-ad-price-increase-six-countries/) · [Location fee (digitalapplied)](https://www.digitalapplied.com/blog/meta-europe-location-fees-july-2026-advertiser-guide).
