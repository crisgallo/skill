---
name: "google-ads-performance"
description: "Regole operative verificate per montare, ottimizzare e diagnosticare campagne Google Ads: Search, Demand Gen, Performance Max. Usare ogni volta che si lavora sul pannello Google Ads: tipi di corrispondenza, strategie di offerta, struttura campagne, conversioni, esclusioni, specifiche degli asset. Serve anche per fare l'igiene di un account ereditato."
---

# Google Ads: regole operative

**Ultima verifica delle fonti: 20 settembre 2026.**

**Cosa è cambiato (revisione del 20/09/2026, precedente 11/08/2026):**

- **03/08/2026 → 1–30/09/2026:** bloccata la creazione dell'impostazione di campagna "solo corrispondenza generica"; le campagne che la usano vengono convertite in automatico ad **AI Max** (sez. 1).
- **17/08/2026:** CPA target, ROAS target e CPC target consegnano **al target**, non sotto, sulle campagne limitate dal budget (sez. 2).
- **Giugno 2026:** conversioni avanzate web e per i lead unificate in una sola funzione; **dal 15/06/2026** i caricamenti offline passano solo dalla **Data Manager API** (sez. 4).
- Demand Gen copre anche **Maps e Rete Display**; le campagne Display standalone stanno migrando dentro Demand Gen (sez. 6).
- **Dicembre 2025:** soglia minima remarketing **100 utenti attivi** su tutte le reti (sez. 7).
- Modelli di attribuzione: restano solo **basato sui dati** e **ultimo clic** (sez. 4).
- Aggiunta la sezione **9. Performance Max**, promessa dal titolo e assente.
- Dati storici: CPA reali prima e dopo il 17/08/2026 non sono confrontabili a parità di target; rapporti termini di ricerca prima e dopo la migrazione AI Max vanno letti separando keyword e AI Max.

---

## 0. Manutenzione di questa skill (leggere per primo)

Google cambia soglie, nomi delle strategie di offerta e specifiche degli asset più volte l'anno. Quindi:

1. **Prima di applicare una soglia numerica su un account che spende, ricontrollala.** Se la verifica in cima ha più di **due o tre mesi**, si rifà una ricerca sulle fonti ufficiali prima di toccare il pannello.
2. **Quando una fonte smentisce una regola scritta qui, si aggiorna la skill nello stesso momento.** Una skill che invecchia in silenzio è peggio di nessuna skill: dà sicurezza falsa.
3. Aggiornando, si **riscrive la data** in cima e si annota **cosa è cambiato e da quando**, così si sa quali dati storici restano confrontabili.
4. Segnali che è ora di ricontrollare: il pannello mostra voci che qui non sono descritte; un'impostazione non si trova più dove dovrebbe; un tipo di campagna viene sostituito da uno nuovo.
5. La pagina annunci ufficiale (9048695) è ferma al 20/05/2026: per intercettare i cambi si leggono gli **avvisi in cima alle singole pagine Help** e il Developer Blog, non quella.

---

## 1. La regola che salva più budget: corrispondenza generica solo con i dati

**La corrispondenza generica (broad match) funziona solo accoppiata a Smart Bidding e a un tracciamento delle conversioni solido.** Google la ammette solo con Massimizza conversioni, Massimizza valore, CPA target o ROAS target ([10195720](https://support.google.com/google-ads/answer/10195720?hl=en)). Richiede volume:

- **Numero Google:** almeno **30 conversioni** negli ultimi 30 giorni per valutare lo Smart Bidding, **50 per ROAS target** ([7065882](https://support.google.com/google-ads/answer/7065882?hl=en), [6268632](https://support.google.com/google-ads/answer/6268632?hl=en)).
- **Regola empirica, non numero Google:** **30-50 conversioni al mese per campagna** come minimo di funzionamento, **50-100 al mese** perché abbia dati sufficienti a guidare davvero (blog: stackmatix 13/09/2026, infrontmarketing 21/04/2026).
- **Fascia 10-30 conversioni al mese**, la più comune sui conti piccoli: **scelta da fare caso per caso**: frase ed esatta con Massimizza conversioni finché il volume cresce, oppure si consolida in una sola campagna per superare le 30. Nessuna regola Google copre questa fascia.

⚠️ **Su un account nuovo o con budget limitato la generica è la scelta sbagliata:** massimizza la copertura e brucia il budget prima di aver imparato qualcosa. Si parte con **frase ed esatta**, si guardano i termini di ricerca reali, e si allarga solo quando il volume di conversioni lo sostiene.

⚠️ **AI Max sostituisce la "generica di campagna" (dal 03/08/2026, conversione automatica 1–30/09/2026).** L'impostazione di campagna "solo corrispondenza generica" non si crea più (UI, Editor, API); le campagne che la usavano vengono convertite ad AI Max, con il solo "search term matching" attivo (anche "text customization" se avevano asset creati automaticamente). Le DSA migrano da febbraio 2027. Dopo la conversione si controlla: **search term matching, text customization ed espansione URL finale** sono attivabili singolarmente; le esclusioni negative continuano a valere; il rapporto termini di ricerca si separa in **keyword / AI Max**. Fonti: [13389795](https://support.google.com/google-ads/answer/13389795?hl=en), [blog.google](https://blog.google/products/ads-commerce/dsa-upgrade-to-ai-max-2026/), [Developer Blog 12/08/2026](https://ads-developers.googleblog.com/2026/08/migrate-campaign-level-broad-match-and.html), [ppc.land](https://ppc.land/google-ads-broad-match-campaigns-face-ai-max-auto-upgrade-on-september-1/).

🔴 **Frase ed esatta non tengono fuori dalle superfici AI.** Dal 04/09/2026 Google conferma un test in cui keyword esatte e a frase servono annunci anche in AI Mode (intento diretto). Nessuna pagina Help ufficiale trovata; fonte: [ppc.land](https://ppc.land/exact-and-phrase-match-keywords-gain-ai-mode-ads-in-google-test/).

**Le esclusioni contano più della scelta delle keyword.** Con la generica servono liste di **parole chiave escluse a livello di account**, non solo di campagna, per bloccare interi temi in un colpo. Limite: **1.000 parole chiave** per elenco account; vale per Search, Performance Max, App, Shopping, Smart e Local; la pagina ufficiale **non cita Demand Gen** ([11396330](https://support.google.com/google-ads/answer/11396330?hl=en)).

---

## 2. Strategie di offerta: la sequenza per un account senza storico

1. **Massimizza le conversioni senza target**, per **due-quattro settimane** (**regola empirica, non numero Google**: la pagina Smart Bidding non raccomanda una durata; fonte groas 23/04/2026). Il numero Google è sul volume, non sul tempo: **almeno 30 conversioni** prima di giudicare, 50 per ROAS target.
2. Poi si aggiunge un **CPA target** ricavato dal costo per conversione **reale osservato**, non desiderato.
3. Il CPA target deciso a tavolino su un account senza storico è il modo più veloce per non avere consegna: se è troppo basso, la campagna semplicemente non gira.
4. 🔴 **Dal 17/08/2026 (rollout completato il 27/08) il target è un target, non un tetto.** Sulle campagne limitate dal budget, CPA target, ROAS target e CPC target (Demand Gen) **consegnano al valore impostato** invece di sovraperformarlo: con target 10 € e CPA reale 5 €, il CPA reale sale verso 10 €. Un target lasciato largo ora **costa**. Si rivedono tutti i target con il **Bid Target Adjustment Tool** (dal 06/07/2026) oppure si torna a Massimizza conversioni. Interessate: Search, Shopping, Performance Max, Demand Gen, Display, Hotel, Travel; escluse App e Video reach/view. Fonti: [17061251](https://support.google.com/google-ads/answer/17061251?hl=en), [17125145](https://support.google.com/google-ads/answer/17125145?hl=en-GB).

⚠️ Con budget molto piccoli e conversioni rare (poche al mese) nessuna strategia automatica ha dati sufficienti. In quel caso l'obiettivo della campagna **non è convertire, è imparare quali query esistono**: si accetta di ottimizzare su clic e si legge il rapporto sui termini di ricerca.

---

## 3. Struttura: temi ampi, non keyword singole

- Campagne organizzate per **tema o linea di servizio**, con gruppi di annunci **consolidati**.
- Poche campagne larghe battono molte campagne strette: Smart Bidding ha bisogno che le conversioni si accumulino in un posto solo.
- La segmentazione fine per keyword spezza i dati: sotto le 30 conversioni per campagna (sez. 1) non c'è niente da ottimizzare.
- ⚠️ **Targeting per lingua rimosso da Search e dalla parte Search di Performance Max** (da fine settembre 2026; resta per YouTube, Display, Discover e Gmail dentro PMax). Google abbina lingua dell'annuncio e della pagina. Chi separa le campagne per lingua deve saperlo: la separazione regge solo tramite annunci e pagine nella lingua giusta. Fonti: [1722078](https://support.google.com/google-ads/answer/1722078?hl=en), [Developer Blog 13/08/2026](https://ads-developers.googleblog.com/2026/08/google-ads-language-targeting-changes.html).

---

## 4. Conversioni: la parte che decide tutto il resto

- **Una sola azione primaria.** Se sono primarie anche le visualizzazioni di pagina o i clic sul telefono, l'algoritmo ottimizza sul segnale debole, che è più frequente e più facile.
- Tutto il resto va impostato come **secondario**: si misura ma non guida le offerte.
- Eccezione da conoscere: la conversione **"Ricerche di brand"** (YouTube e Demand Gen) compare come "Primaria" ma è solo di reporting: finisce in "Tutte le conv.", non in "Conversioni"; finestra 7 giorni (1–30 personalizzabile); richiede il brand mapping tramite il rappresentante ([16212033](https://support.google.com/google-ads/answer/16212033?hl=en)).
- **Conversioni avanzate** (Enhanced Conversions): alzano il tasso di corrispondenza e recuperano attribuzione persa. **Da giugno 2026 web e lead sono una sola funzione con un unico interruttore**; chi aveva già accettato i termini sui dati dei clienti è stato migrato in automatico. **Dal 15/06/2026** conversioni offline e conversioni avanzate per i lead si caricano solo con la **Data Manager API** (bloccate nella Google Ads API) ([16884284](https://support.google.com/google-ads/answer/16884284?hl=en)).
- **Lead chiusi offline**: su cicli di vendita lunghi, dove il modulo compilato non è la vendita, rimandare a Google il lead chiuso è il pezzo che pesa di più: insegna all'algoritmo **quale modulo vale davvero**. Limiti di caricamento: 90 giorni (offline), 63 giorni (lead) ([15081888](https://support.google.com/google-ads/answer/15081888?hl=en-IE)). ⚠️ Segnalato il 22/08/2026 da fonte terza, **non verificato su pagina ufficiale**: le conversioni caricate **oltre 7 giorni** dall'evento restano nelle colonne ma escono dal modello basato sui dati che alimenta lo Smart Bidding ([ppc.land](https://ppc.land/google-ads-attribution-ignores-offline-conversions-uploaded-after-7-days/)). Si carica presto, non a fine mese.
- **Modello di attribuzione**: verificarlo prima di leggere qualsiasi report. Restano solo **basato sui dati** (default) e **ultimo clic**; primo clic, lineare, decadimento temporale e in base alla posizione non sono più supportati ([6259715](https://support.google.com/google-ads/answer/6259715?hl=en); data della rimozione non verificata, la fonte con le date risponde 403).

---

## 5. Tagging e misurazione

- **Tagging automatico attivo** (Amministrazione → Impostazioni account → Tagging automatico). Con quello acceso, il `gclid` porta in GA4 campagna, gruppo e parola chiave.
- ⚠️ **Non si stratificano UTM manuali sugli URL di Google Ads.** Non perché rompano qualcosa: la guida ufficiale dice che **il tagging automatico ha la priorità sul tagging manuale** e gli UTM non bloccano l'importazione delle conversioni ([3095550](https://support.google.com/google-ads/answer/3095550?hl=en)). Il motivo è che non aggiungono niente al `gclid` e creano due nomenclature da riconciliare. Basta **nominare bene la campagna**. Gli UTM servono solo per strumenti che non leggono il `gclid`.
- **Applicazione automatica dei consigli: disattivata** ([10279006](https://support.google.com/google-ads/answer/10279006?hl=en)). Con quella accesa Google modifica keyword, budget e asset da solo, e ci si ritrova con modifiche che nessuno ha deciso.
- ⚠️ **Esperimenti: da aprile 2026 l'applicazione automatica dei risultati è attiva di default.** La regola sopra non la copre: si controlla **su ogni esperimento** creato ([ppcnewsfeed](https://ppcnewsfeed.com/ppc-news/2026-04/auto-apply-option-added-experiments/); Search Engine Land 473266 non leggibile, 403).
- Collegamento con **GA4** attivo: serve per importare i pubblici e per leggere i **percorsi di conversione** invece del solo ultimo clic.

---

## 6. Demand Gen

- Copre **YouTube (feed e Shorts), Discover, Gmail, Maps e Rete Display**, più i video partner ([13695777](https://support.google.com/google-ads/answer/13695777?hl=en)).
- ⚠️ **Le campagne Display standalone stanno migrando dentro Demand Gen**: annuncio maggio 2026, strumento di migrazione da giugno 2026, poi creazione solo dentro Demand Gen e migrazione automatica delle restanti (fonti terze: gennaio 2027; la pagina ufficiale dice "coming later"). Nelle campagne migrate la Rete Display è attiva e **non deselezionabile durante la migrazione** ([17051545](https://support.google.com/google-ads/answer/17051545?hl=en), [blog.google](https://blog.google/products/ads-commerce/google-display-ads-demand-gen/)).
- **Caricare tutti i rapporti d'aspetto**: 16:9, 1:1 e 9:16 (ammesso anche 4:5). Senza il 9:16 si perde l'inventory Shorts: un asset verticale in Demand Gen porta oltre il **35% di conversioni in più su Shorts** ([9128498](https://support.google.com/google-ads/answer/9128498?hl=en)).
- **Le misure delle immagini non coincidono con quelle dei video.** Immagini: orizzontale **1200x628 (1,91:1)**, quadrata **1200x1200**, verticale **960x1200 (4:5)**, verticale **1080x1920 (9:16)**. Massimo **5 MB** per asset ([13704860](https://support.google.com/google-ads/answer/13704860), [17140672](https://support.google.com/google-ads/answer/17140672)); fino a **20 immagini per annuncio** ([15701616](https://support.google.com/google-ads/answer/15701616)).
- Video: **1–5 per annuncio**, minimo 5 s, sotto i 10 s non serve su In-stream, consigliati **oltre 15 s** ([17141078](https://support.google.com/google-ads/answer/17141078)).
- **Aree di sicurezza (Shorts, fonte Google):** tenere testo e loghi fuori dal **10% in alto, 25% in basso, 10% a destra** (nome canale, didascalia, pulsanti) ([9128498](https://support.google.com/google-ads/answer/9128498?hl=en), [Shorts ads](https://business.google.com/us/ad-solutions/youtube-ads/shorts-ads/)). Il vecchio "centro 90% orizzontale e 80% verticale" è una regola di blog per il 16:9, non un numero Google.
- Budget: **minimo 5 USD/giorno** (o equivalente) imposto via API dal 01/04/2026 su campagne nuove o modificate; per il CPA target Google raccomanda **almeno 10× il target CPA** al giorno (prima 15–20×; abbassato a settembre 2026) ([13695777](https://support.google.com/google-ads/answer/13695777?hl=en), [Developer Blog 27/02/2026](https://ads-developers.googleblog.com/2026/02/minimum-budget-requirement-for-demand.html), [ppc.land](https://ppc.land/google-to-enforce-5-minimum-daily-budget-on-demand-gen-campaigns-from-april/), [twooctobers 01/09/2026](https://twooctobers.com/blog/digital-marketing-updates-september-2026/)). **5 € al giorno resta sotto la soglia pratica**: meglio meno giorni con più budget che due mesi di consegna inutile.
- I video possono durare fino a 3 minuti, ma **nel feed Shorts si vedono solo i primi 60 secondi**, con un rimando alla pagina di visione a 50 secondi ([16041697](https://support.google.com/google-ads/answer/16041697?hl=en)).
- Pubblici: **da marzo 2026 i segmenti lookalike sono "suggerimenti", non vincoli** (opt-out via modulo). Un lookalike caricato non limita la consegna a quel pubblico ([13541369](https://support.google.com/google-ads/answer/13541369?hl=en)).

---

## 7. Igiene di un account ereditato

Ordine di controllo che fa emergere i problemi:

1. **Tagging automatico**, **applicazione automatica dei consigli** e **applicazione automatica dei risultati sugli esperimenti** (sez. 5).
2. **Quale conversione è primaria** e quali secondarie; "Ricerche di brand" non conta (sez. 4).
3. **Conversioni avanzate** (voce unica web + lead da giugno 2026) e, per i lead offline, **chi carica e da dove** (Data Manager API dal 15/06/2026): spesso mai configurate.
4. **Collegamento GA4**.
5. **Elenco delle parole chiave escluse a livello di account**: se è vuoto, si stanno pagando clic sbagliati.
6. **Contatto per la protezione dei dati** (Amministrazione → Preferenze → Contatti per la protezione dei dati; il pannello lo segnala con avviso) ([7687725](https://support.google.com/google-ads/answer/7687725?hl=en)).
7. **Campagne vecchie in pausa**: non si riaccendono mai a scatola chiusa, ma il loro **rapporto sui termini di ricerca** è oro. Sono anni di query già pagate, ed è la base migliore per costruire keyword ed esclusioni di una campagna nuova, molto meglio di una lista immaginata.
8. **Segmenti di pubblico per il remarketing**: esistono? Superano i **100 utenti attivi negli ultimi 30 giorni**, soglia unica su Search, Display e YouTube da dicembre 2025 (il vecchio 1.000 per Search non vale più) ([2472738](https://support.google.com/google-ads/answer/2472738?hl=en))? **Elenchi Customer Match**: dal 18/08/2026 Google assegna da solo il **tipo cliente** agli elenchi non classificati, e quel tipo alimenta gli obiettivi nuovi clienti / riattivazione dello Smart Bidding: si classificano a mano prima che lo faccia Google ([12080169](https://support.google.com/google-ads/answer/12080169?hl=en), [digitalapplied](https://www.digitalapplied.com/blog/google-ads-customer-type-labeling-2026-advertiser-guide)).
9. **Modello di attribuzione** (basato sui dati o ultimo clic) e coerenza fra campagne.
10. **Target CPA/ROAS impostati prima del 17/08/2026**: ricontrollarli tutti (sez. 2).
11. **Performance Max**: impostazione del ridimensionamento video con IA generativa (sez. 9).

---

## 8. Search: cosa non fare

- Accendere la generica su un account senza conversioni.
- Impostare un CPA target prima di avere dati; lasciare un CPA target largo dopo il 17/08/2026.
- Riattivare una campagna vecchia perché "c'è già": geografia, keyword e pagina di destinazione sono quasi sempre di un altro progetto.
- Giudicare una campagna Search di agosto con i criteri di settembre: **la domanda è stagionale, l'asta anche**.
- Aspettarsi che Search porti volume su una nicchia dove le ricerche non esistono: se il volume non c'è, la campagna che intercetta il **problema** (e non il prodotto) diventa la principale.
- Dare per scontato che una campagna convertita ad AI Max si comporti come prima: si rilegge il rapporto termini di ricerca nella parte AI Max (sez. 1).

---

## 9. Performance Max

Solo quello che le fonti verificate sostengono; nessuna soglia numerica inventata.

- **Gruppi di asset per tema o linea di prodotto**, non uno solo per tutto: ogni gruppo con tutti i formati (testo, immagini, video 16:9 / 9:16 / 1:1), altrimenti Google li genera da solo. Regola operativa, pagina Help non verificata in questa revisione.
- **Esclusioni**: le parole chiave escluse a livello di campagna esistono anche in PMax (fino a 10.000 per campagna); l'elenco a livello di account vale anche per PMax ([11396330](https://support.google.com/google-ads/answer/11396330?hl=en)).
- **Rapporto per canale**: prima di giudicare il CPA si guarda dove è andata la spesa (Search, Shopping, YouTube, Display, Discover, Gmail, Maps). Un PMax che spende in Display con CPA da Search sta raccontando una storia diversa.
- **Esclusione dei clienti esistenti** (impostazione di acquisizione): senza, PMax ricompra i clienti già acquisiti e il CPA sembra buono; dal 18/08/2026 dipende anche dall'etichettatura del tipo cliente su Customer Match (sez. 7).
- 🔴 **Ridimensionamento video con IA generativa**: dal 17/08/2026 i 16:9 caricati vengono tagliati in 9:16 e 1:1 da un modello; loghi e testo ai bordi sono a rischio. Opt-out entro il **04/09/2026**; su un account ereditato si verifica l'impostazione e si caricano i verticali a mano ([Search Engine Land 485252](https://searchengineland.com/google-ads-will-use-generative-ai-to-resize-performance-max-video-ads-485252)).
- Targeting per lingua rimosso dalla parte Search (sez. 3); i target consegnano al target dal 17/08/2026 anche qui (sez. 2).

---

## Fonti (verificate 20/09/2026)

**Ufficiali Google, confermate:** [Generica ammessa solo con Smart Bidding (10195720; nessuna soglia di conversioni, nessuna regola sulle esclusioni)](https://support.google.com/google-ads/answer/10195720?hl=en) · [Smart Bidding, almeno 30 conversioni (7065882)](https://support.google.com/google-ads/answer/7065882?hl=en) · [CPA target (6268632)](https://support.google.com/google-ads/answer/6268632?hl=en) · [AI Max (13389795)](https://support.google.com/google-ads/answer/13389795?hl=en) · [Target che consegnano al target (17061251)](https://support.google.com/google-ads/answer/17061251?hl=en) · [Bid Target Adjustment Tool (17125145)](https://support.google.com/google-ads/answer/17125145?hl=en-GB) · [Conversioni avanzate unificate e Data Manager (16884284)](https://support.google.com/google-ads/answer/16884284?hl=en) · [Limiti caricamento offline (15081888)](https://support.google.com/google-ads/answer/15081888?hl=en-IE) · [Modelli di attribuzione (6259715)](https://support.google.com/google-ads/answer/6259715?hl=en) · [Ricerche di brand (16212033)](https://support.google.com/google-ads/answer/16212033?hl=en) · [Auto-tagging (3095550)](https://support.google.com/google-ads/answer/3095550?hl=en) · [Applicazione automatica consigli (10279006)](https://support.google.com/google-ads/answer/10279006?hl=en) · [Esclusioni a livello di account (11396330)](https://support.google.com/google-ads/answer/11396330?hl=en) · [Targeting per lingua (1722078)](https://support.google.com/google-ads/answer/1722078?hl=en) · [Remarketing, 100 utenti (2472738)](https://support.google.com/google-ads/answer/2472738?hl=en) · [Customer Match (12080169)](https://support.google.com/google-ads/answer/12080169?hl=en) · [Contatti protezione dati (7687725)](https://support.google.com/google-ads/answer/7687725?hl=en) · [Demand Gen, reti e budget (13695777)](https://support.google.com/google-ads/answer/13695777?hl=en) · [Display → Demand Gen (17051545)](https://support.google.com/google-ads/answer/17051545?hl=en) · [Demand Gen, specifiche asset (13704860)](https://support.google.com/google-ads/answer/13704860) · [Demand Gen, immagini (17140672)](https://support.google.com/google-ads/answer/17140672) · [Demand Gen, video (17141078)](https://support.google.com/google-ads/answer/17141078) · [20 immagini per annuncio (15701616)](https://support.google.com/google-ads/answer/15701616) · [Shorts, +35% e safe zone (9128498)](https://support.google.com/google-ads/answer/9128498?hl=en) · [YouTube Shorts, specifiche (16041697)](https://support.google.com/google-ads/answer/16041697?hl=en) · [Lookalike Demand Gen (13541369)](https://support.google.com/google-ads/answer/13541369?hl=en) · [Formati, cheat sheet (13676244; numeri dentro immagini, fonte debole)](https://support.google.com/google-ads/answer/13676244?hl=en) · [Shorts ads, safe zone](https://business.google.com/us/ad-solutions/youtube-ads/shorts-ads/) · [blog.google: DSA e generica → AI Max](https://blog.google/products/ads-commerce/dsa-upgrade-to-ai-max-2026/) · [blog.google: Display → Demand Gen](https://blog.google/products/ads-commerce/google-display-ads-demand-gen/).

**Terze parti (pratica, non numeri Google):** [Tipi di corrispondenza, stackmatix (aggiornato 13/09/2026, dopo la verifica precedente; oggi 30–50 conv./mese e split 50/35/15)](https://www.stackmatix.com/blog/google-ads-keyword-match-types-guide) · [infrontmarketing 21/04/2026](https://infrontmarketing.ca/blog/google-ads/google-ads-match-types-in-2026-how-to-control-spend-without-killing-scale/) · [groas 23/04/2026 (sequenza Max conversioni → tCPA)](https://www.groas.com/post/google-ads-best-practices-2026-rules-that-actually-matter) · [ppc.land: AI Max](https://ppc.land/google-ads-broad-match-campaigns-face-ai-max-auto-upgrade-on-september-1/) · [ppc.land: AI Mode](https://ppc.land/exact-and-phrase-match-keywords-gain-ai-mode-ads-in-google-test/) · [ppc.land: minimo Demand Gen](https://ppc.land/google-to-enforce-5-minimum-daily-budget-on-demand-gen-campaigns-from-april/) · [ppc.land: offline oltre 7 giorni](https://ppc.land/google-ads-attribution-ignores-offline-conversions-uploaded-after-7-days/) · [ppcnewsfeed: esperimenti](https://ppcnewsfeed.com/ppc-news/2026-04/auto-apply-option-added-experiments/) · [twooctobers 01/09/2026](https://twooctobers.com/blog/digital-marketing-updates-september-2026/) · [digitalapplied: tipo cliente](https://www.digitalapplied.com/blog/google-ads-customer-type-labeling-2026-advertiser-guide) · [Search Engine Land 485252: video PMax](https://searchengineland.com/google-ads-will-use-generative-ai-to-resize-performance-max-video-ads-485252) · [Search Engine Land 469400: lookalike](https://searchengineland.com/google-shifts-lookalike-to-ai-signals-in-demand-gen-469400).

**Non leggibili al 20/09/2026:** i post del Google Ads Developer Blog del [27/02](https://ads-developers.googleblog.com/2026/02/minimum-budget-requirement-for-demand.html), [12/08](https://ads-developers.googleblog.com/2026/08/migrate-campaign-level-broad-match-and.html) e [13/08/2026](https://ads-developers.googleblog.com/2026/08/google-ads-language-targeting-changes.html) (solo titolo e data, corpo non recuperato); Search Engine Land 473266 e 433352 (403). La pagina ufficiale sui rapporti di attribuzione citata da ppc.land per la regola dei 7 giorni non è stata verificata.
