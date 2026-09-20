---
name: "google-search-console"
description: "Regole operative verificate per leggere e usare Google Search Console: proprietà e verifica, rapporto Rendimento (limiti 16 mesi, 1.000 righe, query anonimizzate, totali che non tornano), indicizzazione, Controllo URL, sitemap, Core Web Vitals, link, azioni manuali, rimozioni, collegamento GA4, export BigQuery, API, migrazioni e novità 2026 (report IA generativa). Usala ogni volta che si prepara un report SEO mensile, si confrontano clic GSC e sessioni GA4, si costruiscono le keyword di una campagna Search dalle query reali, si eredita una proprietà o si legge GSC durante un rebranding o un cambio dominio, anche se Search Console non viene nominata."
---

# Google Search Console: regole operative

**Ultima verifica delle fonti: 20 settembre 2026.**

---

## 0. Manutenzione di questa skill (leggere per primo)

1. **Finestra di freschezza: due mesi.** Nel 2026 Search Console ha aggiunto rapporti e impostazioni a ritmo mensile (report IA generativa a giugno, platform properties a luglio, rollout mondiale il 31/08). Se la data in cima ha più di due mesi, prima di citare un numero a un cliente si rileggono le fonti.
2. **Quando una fonte smentisce una regola scritta qui, si aggiorna la skill nello stesso turno**, si riscrive la data e si annota cosa è cambiato e da quando, così si sa quali serie storiche restano confrontabili.
3. Due metà da tenere distinte: **conoscenza di dominio** (come GSC conta e aggrega, verificata su support.google.com/webmasters e developers.google.com/search) e **meccanica del pannello** (sezione 13: si impara sbagliando, si scrive qui la prima volta).
4. Dove si guardano i cambiamenti: [What's new della documentazione](https://developers.google.com/search/updates) (ultima voce letta: 18/09/2026), [Search Central Blog](https://developers.google.com/search/blog), [Reports at a glance 9133276](https://support.google.com/webmasters/answer/9133276?hl=en) per vedere se è comparso un rapporto nuovo.
5. 🔴 Le righe marcate `[DA VERIFICARE]` non hanno fonte ufficiale al 20/09/2026: non si citano a un cliente.

---

## 1. Proprietà: la scelta sbagliata costa dati che non si recuperano

**Si crea una proprietà Dominio, non un prefisso URL.** La proprietà Dominio "include tutti i sottodomini (m, www ecc.) e più protocolli (http, https, ftp)"; il prefisso URL "include solo gli URL con il prefisso specificato, protocollo compreso": http e https, www e non-www sono proprietà separate ([34592](https://support.google.com/webmasters/answer/34592?hl=en)). Un sito con www + non-www + http residuo letto da un solo prefisso URL sottostima clic e impressioni e nasconde il problema dei canonical.

- La proprietà Dominio si verifica **solo con record DNS** (TXT o CNAME dal registrar); il prefisso URL con file HTML, tag HTML, Google Analytics (servono diritti di modifica GA e snippet gtag nell'`<head>`), Google Tag Manager (permesso Pubblica o Amministratore sul container) ([9008080](https://support.google.com/webmasters/answer/9008080?hl=en)).
- ⚠️ **La verifica scade.** "Verification lasts as long as Search Console can confirm the presence and validity of your verification token": se l'agenzia cambia tema o DNS e il token sparisce, dopo un periodo di tolleranza i permessi decadono. Il record DNS è il token che sopravvive ai redesign.
- **Il cliente deve essere proprietario verificato, il consulente proprietario delegato o utente completo.** "If all verified owners are removed, then all remaining users and delegated owners will lose access to the property after a grace period" ([2451999](https://support.google.com/webmasters/answer/2451999?hl=en)). Un consulente che è l'unico verificato porta via l'accesso del cliente quando se ne va. Limiti: 100 utenti non proprietari per proprietà.
- Ai fini GDPR i dati GSC sono aggregati e senza identificativi utente: non entra nel registro trattamenti come dato personale, ma **l'accesso va dato a account nominativi**, mai a un Gmail condiviso dell'agenzia.
- Le **platform properties** (Instagram, TikTok, X, YouTube) sono disponibili a tutti dal 29/07/2026 e mostrano il rendimento dei post su Search, Discover e Google News; si aggiungono da Search Console e si collegano al Search profile ([blog 29/07/2026](https://developers.google.com/search/blog/2026/07/platform-properties-social-video-guide)). Servono ai clienti che spingono i video su YouTube, non a un e-commerce.

---

## 2. Rapporto Rendimento: come si legge un numero prima di metterlo in un report

**Il totale di un rapporto Rendimento dipende da cosa si è raggruppato e filtrato. Due numeri presi con dimensioni diverse non si confrontano né si sommano.** Le regole, tutte ufficiali:

1. **Aggregazione per proprietà vs per pagina.** "Data grouped by Queries, Countries, Devices, or Dates is aggregated by property. Data grouped by Pages or Search appearance is aggregated by page" ([7576553](https://support.google.com/webmasters/answer/7576553?hl=en)). Per proprietà, una SERP con tre risultati del sito conta **una** impressione; per pagina ne conta tre. Quindi "CTR e posizione media sono in genere più alti aggregando per proprietà" ([17011364](https://support.google.com/webmasters/answer/17011364?hl=en)). Nel report mensile la CTR di sito e la CTR delle pagine sono due metriche diverse e vanno etichettate.
2. **Query anonimizzate.** "Anonymized queries are those that aren't issued by more than a few dozen users over a two-to-three month period"; sono **omesse dalla tabella ma incluse nei totali del grafico, tranne quando si filtra per query** ([blog 10/2022](https://developers.google.com/search/blog/2022/10/performance-data-deep-dive), [17011259](https://support.google.com/webmasters/answer/17011259?hl=en)). Conseguenza: la somma delle righe query non fa il totale, e un filtro "query contenenti brand" + "query non contenenti brand" non ricostruisce il totale. Su un B2B di nicchia la quota anonimizzata può essere metà dei clic.
3. **1.000 righe in interfaccia ed export**, sia tabella sia download ("The maximum you can export through the Search Console user interface is 1,000 rows"). Per un e-commerce con migliaia di URL la tabella pagine è un campione ordinato per clic: le code lunghe si vedono solo da API o BigQuery (sezione 9). Per Paesi, dispositivi e aspetto nella ricerca invece "Search Console will display and export all the data".
4. **16 mesi di storico.** "Search Console keeps data for the last 16 months" ([10737381](https://support.google.com/analytics/answer/10737381?hl=en)). Il confronto anno su anno si fa ogni mese, finché c'è; chi vuole più di 16 mesi deve aver acceso l'export BigQuery prima.
5. **Il clic va al canonical.** "The click counts toward the canonical URL, not the URL the user visits" ([17011259](https://support.google.com/webmasters/answer/17011259?hl=en)). Le varianti con parametri, mobile o AMP confluiscono nel canonical scelto da Google: filtrare per una URL variante dà zero anche se riceve traffico.
6. **Fuso orario Pacifico.** "In all views (except the 24-hour view), the Performance report tracks and labels daily data in Pacific Time" ([17011364](https://support.google.com/webmasters/answer/17011364?hl=en)). Il giorno GSC non coincide con il giorno GA4 (fuso della proprietà, in Italia Roma): i confronti giornalieri sono sfasati di 8-9 ore, quelli mensili quasi non ne risentono.
7. **Dati preliminari.** Gli ultimi giorni sono "preliminary, meaning it's still being collected and may change in the next few hours" (linea tratteggiata). Il report mensile si estrae **non prima di 3 giorni** dopo la fine del mese; la disponibilità dichiarata è "48 hours after it is collected" ([10737381](https://support.google.com/analytics/answer/10737381?hl=en)).
8. **Confronto di periodi:** "You can have only one comparison at a time"; si confrontano due valori di **una sola** dimensione (date, Paese, dispositivo, pagina, query) ([17011165](https://support.google.com/webmasters/answer/17011165?hl=en)). Per neutralizzare stagionalità e giorno della settimana si confrontano periodi di uguale lunghezza allineati sul giorno della settimana, con granularità settimanale o mensile.
9. **Filtri con regex:** "Custom (regex)", sintassi RE2, corrispondenza parziale di default, `(?-i)` all'inizio per il case-sensitive. È lo strumento per separare brand e non-brand (`^(marca|marca\s.*)$`) e per isolare categorie (`/scarpe/|/borse/`).
10. **Aspetto nella ricerca** (Search appearance): la lista ufficiale al 20/09/2026 contiene AMP, Discussion forums, Job listings, Merchant listings, Product snippets, Q&A, Recipe, Review snippet, Subscribed content, Translated results, Videos, Web Stories e simili; **non esiste un filtro "AI Overviews" o "AI Mode" nel rapporto principale** ([17011259](https://support.google.com/webmasters/answer/17011259?hl=en)). Per un e-commerce contano *Merchant listings* e *Product snippets*: il loro CTR va letto separatamente perché è aggregato per pagina.
11. **Tipi di ricerca:** Web, Immagini, Video, Notizie sono filtri del rapporto Risultati di ricerca; **Discover e Google News hanno rapporti propri** che compaiono solo con "un numero minimo di impressioni negli ultimi 3 mesi" ([10268906](https://support.google.com/webmasters/answer/10268906?hl=en)). La posizione media nelle immagini si conta "da sinistra a destra, poi dall'alto in basso" ([7042828](https://support.google.com/webmasters/answer/7042828?hl=en)).
12. **La posizione è "the average topmost position for pages from your site"**: cambia con i sitelink, i risultati multipli e le feature della SERP. Google stesso: "focus more on trends in impressions and clicks than on position alone" ([17010961](https://support.google.com/webmasters/answer/17010961?hl=en)). Nel report al cliente la posizione media si mostra per query o gruppo di query, mai come KPI di sito.

⚠️ **La vista 24 ore usa l'ora del browser, non PT, e mostra dati orari preliminari**: serve a vedere se una pagina nuova è già in SERP, non a misurare.

---

## 3. Perché i clic GSC e le sessioni GA4 non tornano (e non devono tornare)

**I clic di Search Console non sono sessioni GA4 e nessun report deve presentarli come la stessa metrica.** Motivi documentati da Google ([1308626](https://support.google.com/analytics/answer/1308626?hl=en), [7042828](https://support.google.com/webmasters/answer/7042828?hl=en)):

- GSC aggrega sui **canonical**, GA4 sulla **pagina di destinazione reale** (anche dopo redirect).
- GA4 conta solo con JavaScript eseguito e consenso dato; GSC conta il clic in SERP a prescindere. **In Italia, con il banner cookie in modalità consenso di base, GA4 perde una quota di sessioni che GSC vede**: il rapporto sessioni/clic sotto 1 è normale, non è un errore di tracciamento.
- Un utente che clicca, torna indietro e riclicca lo stesso risultato "counts as only one click" in GSC; GA4 può contare una sessione sola o due a seconda del timeout.
- Fuso PT contro fuso della proprietà GA4; ritardo di 48 ore contro il quasi tempo reale.
- GSC ha un tetto di 1.000 URL di destinazione al giorno per sito nell'integrazione GA; GA4 no.
- "Data is shown only for links that send the user to the current Search Console property": clic verso un altro dominio (es. blog su sottodominio con proprietà separata) non compaiono.

✅ Nel report mensile: **GSC per visibilità e domanda (impressioni, query, CTR), GA4 per comportamento e conversioni (sessioni organiche, eventi chiave, ricavi).** Si mette una riga "clic GSC / sessioni organic google GA4" come indicatore di salute del tracciamento: se il rapporto cambia bruscamente è rotto qualcosa nel consenso o nel tag, non nella SEO.

---

## 4. Novità 2026: report IA generativa, controllo IA, EEA

- **Rapporti "Rendimento IA generativa" (Search e Discover)**, annunciati il 03/06/2026, disponibili a tutti dal 31/08/2026 ([blog 03/06/2026](https://developers.google.com/search/blog/2026/06/gen-ai-performance-reports), [16984139](https://support.google.com/webmasters/answer/16984139?hl=en), [16983858](https://support.google.com/webmasters/answer/16983858?hl=en)). Mostrano **solo impressioni** in AI Overviews e AI Mode (Search) e nelle feature IA di Discover, per **pagina, Paese, dispositivo (solo Search), data**. **Niente clic, niente CTR, niente query.** Gli esperimenti Search Labs sono esclusi. Quei dati "sono inclusi nel rapporto Rendimento complessivo" (tipo Web): il rapporto IA è una vista, non una somma aggiuntiva. Il rapporto non compare se le impressioni IA sono poche.
- ⚠️ Nel report al cliente le impressioni IA si presentano come **"quota di visibilità in feature IA"**, non come traffico: non c'è un clic da attribuire. Un calo di CTR sul tipo Web con impressioni stabili è il segnale tipico dell'AI Overview che risponde senza clic; la prova è il confronto impressioni IA / impressioni Web per pagina.
- **Controllo "IA generativa nella Ricerca"** (Impostazioni > Search generative AI): opzioni *Includi* (default), *Escludi*, *Eredita dalla proprietà padre*. Escludere toglie il sito da AI Overviews, AI Mode e feature IA di Discover; "isn't used as a ranking or inclusion signal affecting other parts of Search"; effetto in "a few days"; **non riguarda l'addestramento dei modelli**, che dipende da Google-Extended in robots.txt ([16908024](https://support.google.com/webmasters/answer/16908024?hl=en)). ⛔ Non si esclude un cliente da queste feature senza una decisione scritta del cliente: "sites that opt out will not receive traffic or impressions from our generative AI features" ([blog.google 03/06/2026](https://blog.google/products-and-platforms/products/search/new-controls-website-owners/)).
- **Site reputation policy nell'EEA dal 30/08/2026**: l'azione manuale viene notificata in Search Console ma "for users inside the EEA, the impact of the manual action won't apply"; la sezione può essere separata nei sistemi Google e "ranks independently"; fuori dall'EEA l'effetto resta ([blog 28/08/2026](https://developers.google.com/search/blog/2026/08/update-site-reputation-policy)). Per un cliente italiano con sezioni ospiti/affiliate: la notifica va presa sul serio lo stesso, perché l'effetto sul ranking in Italia può arrivare dalla separazione, non dalla penalità.
- **Cambi di documentazione giugno-settembre 2026** rilevanti ([What's new](https://developers.google.com/search/updates)): 17/06 guida ai site move aggiornata sulle varianti di sottodominio; 12/06 rimossa la documentazione del rich result FAQ (non più una feature da inseguire); 15/06 chiarito che llms.txt non è usato da Google Search; 10/07 troubleshooting dei canonical con i tempi di rivalutazione.

---

## 5. Dalle query GSC alle keyword di una campagna Search

**Le query di Search Console sono l'unico elenco di domanda reale, gratuito e senza campionamento del cliente. Vanno estratte via API o export, mai dalla tabella a 1.000 righe.**

1. Periodo: **ultimi 12 mesi** (stagionalità completa), tipo Web, dimensioni `query` + `page`, aggregazione per pagina. Si scarta ogni riga sotto una soglia di impressioni decisa caso per caso (le query anonimizzate non ci sono comunque).
2. Si separa brand e non-brand con la regex; il brand va in una campagna a sé o in esclusione, come da skill `google-ads-performance`.
3. **Query con impressioni alte e CTR bassa in posizione 1-5 sono le prime candidate a Search**: la SERP le intercetta (annunci, shopping, AI Overview) e l'organico non basta. Query con CTR alta in posizione 1 sono le ultime: si pagherebbe un clic che arriva gratis.
4. Query in **posizione 8-20 con impressioni** rilevanti: candidate a Search a corrispondenza a frase e insieme a un intervento SEO sulla pagina che GSC dice già associata.
5. Le pagine `page` associate alle query dicono **quale landing usare**: se GSC associa la query a una categoria, la landing dell'annuncio è quella categoria, non la home.
6. ⚠️ Il volume GSC è **impressioni reali su quel sito**, non volume di ricerca: sottostima le query dove il sito non appare. Per stimare il volume si usa il Keyword Planner; GSC serve a dire quali query convertono già e quali landing rispondono.
7. I **termini di ricerca** di Google Ads e le **query** di GSC si incrociano in un foglio: una query che in Ads converte e in GSC è in posizione 15 è un brief SEO; una query che in GSC è in posizione 1 con CTR alta e in Ads costa è un candidato all'esclusione o al test di spegnimento.

---

## 6. Indicizzazione: Pagine, Controllo URL, sitemap, canonical

**Il rapporto Pagine (Indicizzazione > Pagine) è la lista di dove Google ha deciso di non indicizzare, e la maggior parte delle voci è normale.** "Don't expect every URL on your site to be indexed" ([7440203](https://support.google.com/webmasters/answer/7440203?hl=en)). Ogni elenco è limitato a 1.000 righe di esempio.

**Stati che contano (fonte sito, azione nostra):**
- **Errore del server (5xx)**, **Errore di reindirizzamento** (catene, loop), **Soft 404** (pagina "non trovato" con codice 200: tipico delle categorie e-commerce vuote e dei prodotti esauriti), **Bloccata da robots.txt** quando la pagina doveva essere indicizzata, **Bloccata 401/403**.
- **Duplicato, Google ha scelto una pagina canonica diversa dall'utente**: il canonical dichiarato non convince Google; su un e-commerce sono le varianti colore/taglia e le pagine con parametri di ordinamento. Si sistema il canonical o si consolidano i contenuti.
- **Indicizzata ma bloccata da robots.txt** e **Pagina indicizzata senza contenuti**: nella sezione "migliora l'aspetto della pagina", vanno chiuse.

**Stati normali (non si aprono ticket):**
- **Pagina alternativa con tag canonical corretto**, **Pagina con reindirizzamento**, **Esclusa dal tag noindex** se il noindex è voluto (filtri, carrello, account, ricerca interna), **Non trovata (404)** per URL davvero rimossi (un 404 non "penalizza"; si rimuove dalla sitemap e si aggiornano i link interni, non si reindirizza tutto alla home).
- **Scansionata, attualmente non indicizzata** e **Rilevata, attualmente non indicizzata**: Google ha deciso che non vale la pena. Su migliaia di pagine prodotto simili è un giudizio di qualità e di crawl budget, non un bug: si migliora il contenuto o si toglie dalla sitemap. Se cresce di colpo dopo un rilascio, è un problema di rendering o di template.

**Convalida della correzione:** "Validation typically takes up to about two weeks, but in some cases can take much longer"; si preme *Convalida correzione* solo dopo aver corretto **tutte** le istanze, altrimenti fallisce e si riparte.

**Controllo URL** ([9012289](https://support.google.com/webmasters/answer/9012289?hl=en)): mostra l'ultima versione **indicizzata**, non quella live; il **test live** dice se la pagina è scansionabile adesso ma "does not check for the presence of the URL in any sitemaps" e non decide canonical o duplicati, che si decidono all'indicizzazione. Confrontare *canonical dichiarato* e *canonical scelto da Google*: se differiscono il problema è nel sito, non in GSC. "URL is on Google" significa idonea, "not guaranteed to be there". Le richieste di indicizzazione hanno "a daily limit ... for each property" senza numero pubblicato; `[DA VERIFICARE]` il tetto di circa 10 richieste al giorno riportato dai blog. Non si usa per forzare centinaia di URL: si usa la sitemap.

**Sitemap** ([7451001](https://support.google.com/webmasters/answer/7451001?hl=en)): stati *Riuscito*, *Errori*, *Impossibile recuperare*; max 50.000 URL e 50 MB non compressi per file, indice di sitemap max 50.000 sitemap e "can't list other sitemap index files". "Pagine rilevate" è quante URL sono state lette, "there is no guarantee that a page URL discovered in a sitemap has been or will be crawled or indexed". La sitemap contiene **solo URL canonici, indicizzabili, con 200**: un e-commerce che mette in sitemap varianti e pagine noindex produce un rapporto Pagine pieno di "duplicati" auto-inflitti. Il rapporto Pagine si legge filtrato per sitemap: la differenza fra "inviate" e "indicizzate" è il numero che va nel report.

---

## 7. Esperienza, link, azioni manuali, sicurezza, rimozioni

- **Core Web Vitals** ([9205520](https://support.google.com/webmasters/answer/9205520?hl=en)): dati reali CrUX (field), non laboratorio. Soglie: LCP buono ≤ 2,5 s, scarso > 4 s; INP buono ≤ 200 ms, scarso > 500 ms; CLS buono ≤ 0,1, scarso > 0,25. Lo stato è per **gruppo di URL** al 75° percentile, e conta il peggiore dei tre. **Su un sito con poco traffico il rapporto è vuoto**: non è un errore, CrUX non ha campione; si usa PageSpeed Insights sapendo che è laboratorio e "an individual URL might be an outlier in its group". *Avvia monitoraggio* apre una finestra di 28 giorni. Mobile e desktop hanno stati separati: si riporta il mobile.
- **HTTPS** ([11396518](https://support.google.com/webmasters/answer/11396518?hl=en)): solo per proprietà Dominio e prefissi https; conta URL indicizzati http vs https, è un campione. Voci da chiudere: *HTTP con tag canonical*, *la sitemap punta a HTTP*, *certificato non valido*, *HTTPS reindirizza*. Obiettivo: zero URL http.
- **Link** ([9049606](https://support.google.com/webmasters/answer/9049606?hl=en)): "isn't a comprehensive list of every link", tabelle a 1.000 righe, export fino a 100.000 righe, siti raggruppati per dominio radice (protocollo e sottodomini tolti). Serve a vedere i link interni più ricevuti (se la home ha tutto e le categorie niente, è un problema di architettura) e le anchor esterne; **non è uno strumento di link audit** e non c'è più il disavow come pratica routinaria: si usa solo con un'azione manuale per link.
- **Azioni manuali** ([9044175](https://support.google.com/webmasters/answer/9044175?hl=en)): revisore umano, parziale (pattern di URL) o su tutto il sito. Si corregge su **tutte** le pagine, si documenta ("the exact quality issue, steps you've taken to fix, outcome"), si invia una sola richiesta di riconsiderazione e si aspetta: "several days or weeks". Non si reinvia prima della risposta. Tipi che toccano PMI ed e-commerce: dati strutturati ingannevoli (recensioni finte, prezzi non corrispondenti), link innaturali, contenuti scarni, site reputation (sezione 4).
- **Problemi di sicurezza** ([9044101](https://support.google.com/webmasters/answer/9044101?hl=en)): contenuti compromessi, malware, social engineering; producono etichette in SERP e interstitial in Chrome, quindi il traffico crolla prima ancora del ranking. Si pulisce, si chiude la falla, si chiede la revisione; la comunicazione arriva solo via email ai proprietari: **l'email del proprietario verificato deve essere una casella letta**.
- **Rimozioni** ([9689846](https://support.google.com/webmasters/answer/9689846?hl=en)): "A successful request lasts only about six months", "does not prevent Google from crawling your page, only from showing it". Per URL esatto o per prefisso. Rimozione permanente solo con 404/410, noindex o password. ⛔ Mai usare *Rimuovi per prefisso* su una cartella viva durante una migrazione: si nasconde mezzo catalogo per sei mesi.

---

## 8. Collegamento GA4 e rapporto Insights

- **Il collegamento è uno a uno**: "You can link a web data stream to only one Search Console property" e viceversa; serve un **proprietario verificato** GSC con ruolo **Editor** su GA4 ([10737381](https://support.google.com/analytics/answer/10737381?hl=en)). Con proprietà Dominio si collega quella, non il prefisso.
- Sblocca in GA4 i rapporti *Query di ricerca organica Google* e *Traffico di ricerca organica Google* (landing page con clic/impressioni GSC accanto a sessioni, eventi chiave e ricavi GA4). La raccolta **nasce non pubblicata**: va pubblicata dalla Libreria, altrimenti il cliente non la vede (vedi skill `ga4-performance`, sezione 5). Le metriche GSC si incrociano solo con landing page, dispositivo e Paese, e solo 16 mesi.
- ✅ È il modo più veloce per ottenere **ricavi per landing page organica**: la domanda che un e-commerce fa davvero. Le query invece restano quelle di GSC, con gli stessi limiti di anonimizzazione.
- **Rapporto Insights** in Search Console ([12945954](https://support.google.com/webmasters/answer/12945954?hl=en)): sostituisce il vecchio Search Console Insights beta; schede clic/impressioni, contenuti, query, Paesi, **brand vs non-brand** (assente su sottoproprietà e siti con poche impressioni), fonti aggiuntive, canali social sperimentali. Non richiede GA4. Va bene come pagina da mandare al cliente fra un report e l'altro, non come fonte del report: le definizioni di "brand" sono di Google e non si controllano.

---

## 9. Export collettivo su BigQuery e API

**L'export su BigQuery non è retroattivo: "The first export includes data for the day of the export"** ([12917675](https://support.google.com/webmasters/answer/12917675?hl=en)). Ogni giorno senza export è storico perso oltre i 16 mesi. Si accende il primo giorno su ogni cliente che vale un contratto annuale, anche se non lo si userà per mesi.

- Requisiti: progetto Google Cloud con fatturazione attiva, API BigQuery e BigQuery Storage, ruoli *BigQuery Job User* e *BigQuery Data Editor* al service account `search-console-data-export@system.gserviceaccount.com`; primo export "up to 48 hours" dopo la configurazione; dataset che inizia sempre con `searchconsole`; **non toccare lo schema** o l'export fallisce; impostare la scadenza delle partizioni (≥ 14 giorni) per i costi, che oltre il livello gratuito sono a carico del progetto.
- Tabelle ([12917991](https://support.google.com/webmasters/answer/12917991?hl=en)): `searchdata_site_impression` (per proprietà), `searchdata_url_impression` (per URL), `ExportLog`. Le query anonimizzate ci sono come righe con `query` null e `is_anonymized_query` true: **è l'unico posto dove si vede quanto pesano**. Posizione media = `SUM(sum_top_position)/SUM(impressions) + 1`.
- Quando vale la pena: e-commerce con più di qualche migliaio di URL o query (il tetto di 1.000 righe e i 50.000/giorno dell'API tagliano la coda), clienti pluriennali, dashboard Looker Studio che devono confrontare più di 16 mesi. Per una PMI con 200 pagine è sovradimensionato: basta l'API.
- **API Search Analytics** ([query](https://developers.google.com/webmaster-tools/v1/searchanalytics/query), [limits](https://developers.google.com/webmaster-tools/limits)): `rowLimit` default 1.000, max **25.000**, paginazione con `startRow`; dimensioni country, device, page, query, searchAppearance, date, hour; `type` web/image/video/news/discover/googleNews; `dataState` final (default) o all (dati freschi); `aggregationType` auto/byPage/byProperty ("If you group or filter by page, you cannot aggregate by property"). Quote: 1.200 richieste/minuto per sito e per utente; URL Inspection API 2.000/giorno e 600/minuto per sito. Il tetto di **50.000 righe al giorno per sito per tipo di ricerca** viene dal blog ufficiale del 10/2022 e il connettore Looker Studio ha lo stesso limite; `[DA VERIFICARE]` se vale ancora nel 2026, la pagina dei limiti non lo cita. "The API ... does not guarantee to return all data rows but rather top ones."
- ⚠️ Il connettore Search Console di Looker Studio passa dall'API: una dashboard con query per pagina su un sito grande non fa il totale del rapporto. Il totale si prende con un'estrazione **senza** dimensioni query/pagina.

---

## 10. Rebranding e migrazione: come si legge GSC quando tutto si muove

**Prima della migrazione si esportano 16 mesi di query e pagine della vecchia proprietà via API: dopo, la vecchia proprietà si svuota e i 16 mesi scorrono.** Poi, nell'ordine ([site move](https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes), [9370220](https://support.google.com/webmasters/answer/9370220?hl=en)):

1. Nuova proprietà Dominio verificata **prima** del go-live, stesso account proprietario di entrambe.
2. Redirect **301/308 server side** URL per URL, mantenuti "generally at least 1 year". Non alla home.
3. **Modifica dell'indirizzo** (Impostazioni) solo per cambio di dominio o sottodominio: "You cannot move properties at the path level"; **non si usa per http→https né per www/non-www** (lì bastano redirect e canonical); non copre i sottodomini sotto quello spostato. Google tratta i due siti come collegati per **180 giorni**, poi "treats the sites as unrelated". Per annullare, prima si tolgono i redirect e si mettono quelli inversi, poi *Annulla trasferimento*.
4. Si invia la sitemap nuova e si **lascia la vecchia** inviata: nel rapporto Sitemap si vede il travaso.
5. Si monitorano **entrambe le proprietà**: sul vecchio sito le pagine indicizzate scendono e passano a *Pagina con reindirizzamento*; sul nuovo salgono; nel Rendimento le impressioni migrano. "The visibility of your content in Search may fluctuate temporarily during the move. This is normal."
6. Nel report mensile a cavallo della migrazione si sommano le due proprietà e si scrive una nota: **il confronto anno su anno per pagina è impossibile** (URL diversi), quello per query regge. Un rebranding cambia anche la regex brand: se ne tengono due (vecchio e nuovo nome) e si osserva quanto il vecchio brand resiste nelle query.
7. ⛔ Non si chiude la vecchia proprietà, non si toglie il DNS del vecchio dominio, non si mette il vecchio dominio in Rimozioni.

---

## 11. Igiene di una proprietà ereditata: ordine di controllo

1. **Tipo di proprietà e proprietari**: esiste una proprietà Dominio? Chi è verificato e con quale token? Il cliente è proprietario verificato? Utenti sconosciuti da togliere.
2. **Azioni manuali e Problemi di sicurezza**: prima di leggere qualunque numero.
3. **Impostazioni > Search generative AI**: qualcuno ha messo *Escludi*? (dal 2026 è una leva che può azzerare visibilità in silenzio).
4. **Rendimento, ultimi 16 mesi, confronto**: cadute nette datate, da incrociare con rilasci, migrazioni e core update.
5. **Pagine**: rapporto inviate/indicizzate sulle sitemap; picchi di *Scansionata, attualmente non indicizzata* e *Google ha scelto un canonical diverso*.
6. **Sitemap**: quali sono inviate, se contengono URL noindex/redirect/404, ultima lettura.
7. **HTTPS** e residui http in canonical e sitemap.
8. **Core Web Vitals mobile**: se vuoto, annotare che CrUX non ha campione.
9. **Collegamento GA4** e pubblicazione della raccolta Search Console; **collegamento Google Ads** dalla parte Ads se si vuole il rapporto annunci e organico.
10. **Export BigQuery**: acceso? Da quando? Se no, si accende oggi.
11. **Modifica dell'indirizzo** attiva o scaduta, rimozioni temporanee in corso.
12. **Statistiche di scansione** (Impostazioni, solo proprietà radice, 90 giorni): errori host e 5xx; "if you have a site with fewer than a thousand pages, you should not need to use this report" ([9679690](https://support.google.com/webmasters/answer/9679690?hl=en)).

---

## 12. Meccanica del pannello (da verificare a mano)

- Nell'interfaccia italiana il controllo IA si chiama davvero "Search generative AI" o è stato tradotto? Dove sta esattamente sotto Impostazioni?
- Il rapporto "Rendimento IA generativa" compare come voce di menu separata o come scheda dentro Rendimento, e su una proprietà piccola compare o resta nascosto?
- L'export a 1.000 righe da interfaccia: con un filtro per pagina attivo esporta 1.000 query per pagina o 1.000 righe totali?
- Il selettore di date personalizzato: accetta davvero 16 mesi indietro al giorno, o arrotonda al primo giorno disponibile?
- Le annotazioni di Search Console citate nel blog del 29/07/2026: dove si creano, chi le vede, compaiono nel confronto?
- Dopo *Convalida correzione* fallita, il pulsante si riattiva subito o dopo un intervallo?

---

## 13. Cosa non fare mai

- **Sommare le righe della tabella query e chiamarla "totale"**: mancano le anonimizzate e tutto oltre la riga 1.000.
- **Confrontare CTR per pagina con CTR per proprietà** nello stesso grafico.
- **Presentare i clic GSC come sessioni**, o cercare di farli tornare con GA4.
- **Presentare le impressioni IA generativa come traffico**: non hanno clic.
- **Escludere un sito dalle feature IA** senza decisione scritta del cliente.
- **Usare la posizione media come KPI di sito.**
- **Aprire ticket sugli stati normali del rapporto Pagine** (canonical corretto, redirect, noindex voluto, 404 di pagine tolte).
- **Chiedere l'indicizzazione URL per URL** al posto della sitemap.
- **Usare Rimozioni come noindex**, o su un prefisso vivo.
- **Usare Modifica dell'indirizzo per http→https o www.**
- **Migrare senza aver esportato i 16 mesi** della vecchia proprietà e senza export BigQuery acceso sulla nuova.
- **Essere l'unico proprietario verificato** di una proprietà del cliente.
- **Fidarsi di un dato degli ultimi 2-3 giorni** in un report: è preliminare.

---

## Fonti (verificate 20/09/2026)

**Ufficiali, lette:**
[34592 tipi di proprietà](https://support.google.com/webmasters/answer/34592?hl=en) · [9008080 verifica](https://support.google.com/webmasters/answer/9008080?hl=en) · [2451999 utenti e permessi](https://support.google.com/webmasters/answer/2451999?hl=en) · [7576553 rapporto Rendimento](https://support.google.com/webmasters/answer/7576553?hl=en) · [17010961 metriche](https://support.google.com/webmasters/answer/17010961?hl=en) · [17011165 filtri e confronto](https://support.google.com/webmasters/answer/17011165?hl=en) · [17011259 dimensioni e raggruppamenti](https://support.google.com/webmasters/answer/17011259?hl=en) · [17011364 discrepanze](https://support.google.com/webmasters/answer/17011364?hl=en) · [7042828 conteggio clic/impressioni/posizione](https://support.google.com/webmasters/answer/7042828?hl=en) · [10268906 rapporti Rendimento Search/News/Discover](https://support.google.com/webmasters/answer/10268906?hl=en) · [16984139 IA generativa Search](https://support.google.com/webmasters/answer/16984139?hl=en) · [16983858 IA generativa Discover](https://support.google.com/webmasters/answer/16983858?hl=en) · [16908024 controllo IA generativa](https://support.google.com/webmasters/answer/16908024?hl=en) · [12945954 Insights](https://support.google.com/webmasters/answer/12945954?hl=en) · [7440203 Pagine](https://support.google.com/webmasters/answer/7440203?hl=en) · [9012289 Controllo URL](https://support.google.com/webmasters/answer/9012289?hl=en) · [7451001 Sitemap](https://support.google.com/webmasters/answer/7451001?hl=en) · [9205520 Core Web Vitals](https://support.google.com/webmasters/answer/9205520?hl=en) · [11396518 HTTPS](https://support.google.com/webmasters/answer/11396518?hl=en) · [9049606 Link](https://support.google.com/webmasters/answer/9049606?hl=en) · [9044175 Azioni manuali](https://support.google.com/webmasters/answer/9044175?hl=en) · [9044101 Problemi di sicurezza](https://support.google.com/webmasters/answer/9044101?hl=en) · [9689846 Rimozioni](https://support.google.com/webmasters/answer/9689846?hl=en) · [9679690 Statistiche di scansione](https://support.google.com/webmasters/answer/9679690?hl=en) · [9133276 Reports at a glance](https://support.google.com/webmasters/answer/9133276?hl=en) · [12917675 export BigQuery](https://support.google.com/webmasters/answer/12917675?hl=en) · [12917991 tabelle export](https://support.google.com/webmasters/answer/12917991?hl=en) · [9370220 Modifica dell'indirizzo](https://support.google.com/webmasters/answer/9370220?hl=en) · [site move con cambio URL](https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes) · [AI features](https://developers.google.com/search/docs/appearance/ai-features) · [API searchanalytics.query](https://developers.google.com/webmaster-tools/v1/searchanalytics/query) · [API limits](https://developers.google.com/webmaster-tools/limits) · [API how-to search analytics](https://developers.google.com/webmaster-tools/v1/how-tos/search_analytics) · [Analytics 10737381 collegamento GSC-GA4](https://support.google.com/analytics/answer/10737381?hl=en) · [Analytics 1308626 differenze GSC/GA](https://support.google.com/analytics/answer/1308626?hl=en) · [What's new](https://developers.google.com/search/updates) · Blog Search Central: [deep dive limiti 10/2022](https://developers.google.com/search/blog/2022/10/performance-data-deep-dive), [report IA generativa 03/06/2026](https://developers.google.com/search/blog/2026/06/gen-ai-performance-reports), [platform properties 29/07/2026](https://developers.google.com/search/blog/2026/07/platform-properties-social-video-guide), [site reputation 28/08/2026](https://developers.google.com/search/blog/2026/08/update-site-reputation-policy) · [blog.google 03/06/2026 nuovi controlli](https://blog.google/products-and-platforms/products/search/new-controls-website-owners/).

**Terze parti (solo conferma di rollout, nessun numero preso da qui):** [Search Engine Journal 31/08/2026](https://www.searchenginejournal.com/google-search-console-ai-reports-rolled-out-worldwide/587836/) · [seroundtable EEA](https://www.seroundtable.com/google-site-reputation-policy-eea-41968.html).

**Non leggibili via fetch il 20/09/2026, da ricontrollare a mano:** [Search Engine Land 486269](https://searchengineland.com/google-search-console-ai-performance-reports-and-search-generative-ai-control-rolling-out-globally-486269) (403); [9128668](https://support.google.com/webmasters/answer/9128668?hl=en) e [9128669](https://support.google.com/webmasters/answer/9128669?hl=en) restituiscono pagine introduttive, non i rapporti attesi; la pagina Help sulla vista 24 ore e sull'export (limite righe per download in Fogli/CSV) non è stata individuata: il limite di 1.000 righe da interfaccia è preso dal blog ufficiale 10/2022 e da 17011364.
