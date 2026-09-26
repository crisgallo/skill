---
name: chatgpt-ads-performance
description: "Regole operative verificate per montare, misurare e diagnosticare campagne su ChatGPT Ads (Ads Manager di OpenAI): apertura account, obiettivi CPM CPC e oCPC, budget minimi, context hints, specifiche creative, pixel oaiq e Conversions API, policy, API inserzionisti."
---

# ChatGPT Ads: regole operative

**Ultima verifica delle fonti: 26 settembre 2026.**

🔴 **Questo canale è in BETA dichiarata, e cambia più in fretta di Meta e Google.** OpenAI scrive che durante la beta cambieranno consegna, inventario, formati e modi di comprare e ottimizzare. Ogni numero qui sotto va ricontrollato prima di applicarlo, e la verifica in pannello vince sempre sulla documentazione.

## 0. Manutenzione (leggere per primo)

1. Su un prodotto in beta il limite di freschezza non è due o tre mesi come per Meta: è **un mese**.
2. Quando il pannello smentisce una riga, si aggiorna la skill **nello stesso turno**, con data e nota.
3. ⚠️ Molte specifiche NON stanno negli articoli di aiuto ma su `developers.openai.com/ads`, o si scoprono solo dal messaggio d'errore. Quando un dato manca, **si dichiara che manca**.
4. Ogni aggiornamento si riallinea nella copia di progetto `Blog/skills/`.
5. 🔴 A ogni verifica si legge **il changelog** di `developers.openai.com/ads` (o l'export `developers.openai.com/ads/llms-full.txt`): la verifica del 12/09 non lo aveva letto e si era persa tre cambi già pubblicati (`obref` 16/07, pubblici 25/08, piattaforme 10/09).
6. ⚠️ `help.openai.com`, `openai.com` e `ads.openai.com` rispondono **403** al fetch automatico (Cloudflare): la prossima verifica si fa **da browser** (vedi Fonti).

**Cosa è cambiato dal 12/09/2026** (verifica del 20/09/2026):

- 16/07/2026: cookie `__obref` e campo `user.obref` nella Conversions API (changelog API).
- 24/08/2026: inserzioni servite in 31 mercati europei, **Italia inclusa**.
- 25/08/2026: pubblici personalizzati con add/remove/replace, identificatori misti, bid multiplier 0,1x-10x.
- Agosto 2026: policy v1.4 (annunci di lavoro e immobiliari singoli, wellness claims, scams, temi sensibili).
- 03/09 e 16/09/2026: plugin **Ads Manager dentro ChatGPT**.
- 09/09/2026: limiti di spesa account, solo per account a fattura.
- 10/09/2026: **cinque piattaforme** (`desktop_web`, `ios_web`, `android_web` aggiunti in API).
- 16/09/2026: **oCPM generally available**; finestre post clic 7/14/30 e view-through 0/1 giorno; testo AI-customizzato e tradotto; creatività suggerite dall'AI; integrazione HubSpot; app Shopify (USA, internazionale dal 23/09); Sponsored Agents in alpha USA.
- Settembre 2026: policy v1.6, rifiuto discrezionale per conflitto con interessi commerciali di OpenAI.
- ~17/09/2026: Basics e Overview aggiornati: piano **«Go»** (non «Standard»); personalizzazione con segnali dall'esperienza ChatGPT, **non in EEA/CH**.
- 19-20/09/2026: Billing aggiornata: importo del blocco carta mostrato nel setup; saldo residuo addebitato a fine mese; pausa efficace entro 24 ore.
- Pagina Campaigns: tabella **«Minimum Campaign Spend» con EUR 15 €/giorno**; account nuovi limitati al paese di casa; 56 paesi self-serve al 20/09, «più di 60» dal 24/09 (§2); multi-account ammesso (tetto 10); Bid Cap oCPC = offerta CPA.

## 1. Che cos'è e chi la vede

Le inserzioni compaiono **sotto le risposte di ChatGPT**, con nome inserzionista, logo, titolo, descrizione, immagine e link. Le vedono gli utenti **Free e Go** (il piano si chiama Go, non «Standard»: nessuna fonte usa quel nome); ⛔ non le vedono **Plus, Pro, Business, Enterprise ed Edu**, e sono esclusi i **minori di 18 anni**. Non compaiono nelle **Temporary Chat** né nel browser **Atlas**; l'utente Free può scegliere «Ads-Free» (meno messaggi, niente inserzioni). Verificato 20/09/2026: https://help.openai.com/en/articles/20001047-ads-in-chatgpt · https://help.openai.com/en/articles/20001207-ads-in-chatgpt-the-basics

**Dove vengono servite** (24/08/2026): USA dal 09/02/2026, poi UK, Messico, Brasile, Giappone, Corea e altri, poi **31 mercati europei compresa l'Italia dal 24/08/2026**, «over 40 countries». https://openai.com/index/chatgpt-ads-expands-across-europe/

La selezione usa **contesto e intento della conversazione in corso**, la pagina di destinazione, titolo e testo, più i *context hints*. ⚠️ Da ~17/09/2026, «when ads personalization is enabled», entrano anche segnali dall'esperienza ChatGPT dell'utente (chat passate, memoria, interazioni con gli ads); ✅ la personalizzazione **non è attiva in EEA e Svizzera**, quindi per gli utenti italiani vale ancora il solo contesto (vedi 2.1). Asta **di secondo prezzo pesata sulla rilevanza**. L'inserzionista **non vede le conversazioni** e **la pubblicità non influenza le risposte**: non si compra la risposta, si compra lo spazio sotto.

⚠️ **Non è un motore di ricerca e i context hints non sono parole chiave.** OpenAI lo scrive: non sono corrispondenze esatte, non sono regole di targeting, non garantiscono la comparsa su una conversazione.

**Sponsored Agents** (16/09/2026): conversazione con un agente sponsorizzato dopo il clic; alpha con inserzionisti selezionati USA, «not accepting early access requests». ⛔ Non si promette il formato. https://help.openai.com/en/articles/20001524-sponsored-agents-in-chatgpt-ads

## 2. Account

✅ **Italia inclusa nel self-serve** (**56** paesi e regioni al 20/09/2026, erano 54 al 12/09; dal 24/09/2026 OpenAI annuncia sette mercati asiatici in più, Indonesia, Malesia, Filippine, Singapore, Thailandia, Vietnam e Taiwan, e «più di 60 paesi»: l'annuncio su openai.com e la pagina Availability rispondono 403 al controllo del 26/09/2026, conteggio ripreso da [Marketing-Interactive, 24/09/2026](https://www.marketing-interactive.com/chatgpt-ads-makes-its-southeast-asia-debut) (terzi), `[DA VERIFICARE]` sul pannello). ⚠️ La lista dice dove può stare l'inserzionista, **non dove vengono servite le inserzioni** (§1). https://help.openai.com/en/articles/20001245-ads-manager-availability

Apertura: dati aziendali, flusso di **verifica di identità o aziendale** con coda di revisione, poi Impostazioni. Il nome del fornitore «Persona» non trovato in nessuna fonte al 20/09/2026, da verificare sul pannello. Le campagne **possono non essere servite finché setup obbligatorio e revisione non sono completi**; nome brand e icona identificano l'inserzionista nelle inserzioni (la formula «senza nome e logo non si serve» non compare verbatim nelle fonti al 20/09/2026). ⛔ **Paese, valuta e fuso orario non si cambiano più.**

✅ **Più account per azienda** ammessi (brand, entità giuridiche, team diversi); ⛔ chi appartiene già a **10 o più** ad account non può crearne altri (20/09/2026). Individui non supportati. L'agenzia **non può creare** l'account per il cliente, ma **può essere invitata** dopo che il cliente lo ha creato. https://help.openai.com/en/articles/20001213-ads-manager-beta-account-setup · https://help.openai.com/en/articles/20001217-troubleshooting-common-issues

Apertura e gestione anche dal **plugin Ads Manager dentro ChatGPT** (`chatgpt.com/apps/chatgpt-ads-manager`, 03/09 e 16/09/2026): account, campagne, gruppi, inserzioni e insight in linguaggio naturale, con conferma prima di applicare. https://openai.com/index/reimagining-advertising-with-ai/

**Fatturazione postpagata a soglia** (Billing aggiornata 19-20/09/2026): soglia bassa all'inizio (esempio in pagina: 25 $) che sale con lo storico pagamenti; ⛔ non si cambia, nemmeno chiedendo al supporto. ⚠️ **Il saldo residuo a fine mese viene addebitato comunque**, anche sotto soglia. Alla registrazione della carta la banca può mostrare un **blocco temporaneo**: l'importo atteso è mostrato nella pagina di setup, rilasciato dopo la verifica, visibile fino a 8 giorni. Le cifre «50 o 100 $» non trovate in nessuna fonte al 20/09/2026, da verificare sul pannello. https://help.openai.com/en/articles/20001216-billing-payment

- **Limiti di spesa account** (giornaliero e per intervallo di date, 09/09/2026): **solo account a fattura postpagata**; con la carta esistono solo budget campagna e soglia. https://developers.openai.com/ads
- **Pausa non immediata:** dopo la pausa gli annunci possono uscire ancora **fino a 24 ore** e la spesa resta fatturabile. https://help.openai.com/en/articles/20001216-billing-payment
- **Credito di benvenuto:** ads.openai.com espone «Get $500 ad credit when you spend $500»; la scadenza a 90 giorni è di fonti terze, non di OpenAI. https://ads.openai.com/
- **Integrazioni** (16/09/2026): **HubSpot** ovunque ChatGPT Ads è attivo, Italia inclusa (campagne, lead nel CRM, performance); app **Shopify** USA dal 16/09, **internazionale dal 23/09/2026** (sync catalogo + pixel server). https://help.openai.com/en/articles/20001522-set-up-chatgpt-ads-in-hubspot · https://openai.com/index/reimagining-advertising-with-ai/

### 2.1 🔴 Vincoli specifici per Italia / EEA (verificati 20/09/2026)

- ⛔ **Pubblici personalizzati non supportati** per campagne verso EEA o Svizzera, «where personalized ads are not yet available»: per una campagna sull'Italia le liste non servono né in inclusione né in esclusione. https://help.openai.com/en/articles/20001210-create-campaigns-for-chatgpt-ads · https://developers.openai.com/ads/custom-audiences
- ⛔ **Account self-serve nuovi limitati al paese di casa**: «Some new self-serve ad accounts can initially advertise only in their home country… Selecting other countries does not override this restriction.» Si sblocca solo dopo verifica identità approvata **e** una spesa minima (non quantificata) nel paese di casa. Un account italiano nuovo può non riuscire a targetizzare altri paesi. https://help.openai.com/en/articles/20001210-create-campaigns-for-chatgpt-ads · https://help.openai.com/en/articles/20001217-troubleshooting-common-issues
- ⚠️ **Targeting sub-nazionale in Italia: non verificato sul pannello.** Dal 22/09/2026 la pagina https://developers.openai.com/ads/campaign-targeting documenta il sub-nazionale via location ID presi dall'endpoint di lookup geografico, con esclusioni di regioni dentro un paese incluso; le campagne da product feed restano solo a livello paese. Quali località italiane esistano nel catalogo resta da vedere. La FAQ dice «states or regions, cities, markets, and postal codes where available… may vary by country»; il catalogo `ads.openai.com/assets/openai-geotargets.csv` non era scaricabile (challenge Cloudflare). Si legge dal pannello.
- Personalizzazione non attiva in EEA/CH (§1); il testo AI-customizzato traduce nella lingua dell'utente (§7).
- Contesto UE: ppc.land riporta la designazione di ChatGPT come «very large online search engine» (DSA) il 31/08/2026; non verificato su fonte primaria. https://ppc.land/openai-lets-advertisers-run-chatgpt-ads-from-hubspot-and-shopify/

## 3. Struttura

| Livello | Cosa si decide |
|---|---|
| **Campagna** | obiettivo e tipo di fatturazione (CPM, CPC, oCPC, oCPM), **budget giornaliero o totale**, date, **geografia**, **piattaforme (cinque)**, pubblici personalizzati (non in EEA), evento di conversione |
| **Gruppo** | **context hints** (e `exclusion_hints` via bulk API), strategia di offerta e importo, bid multiplier sui pubblici |
| **Inserzione** | titolo, testo, immagine, destinazione, parametri URL dinamici |

🔴 **Geografia e piattaforme stanno sulla CAMPAGNA, non sul gruppo.** Per testare due paesi servono due campagne, e con un account nuovo il secondo paese può non essere ammesso (2.1). Chi arriva da Meta sbaglia struttura.

Limiti in caricamento massivo: 5.000 campagne, 5.000 gruppi, 5.000 inserzioni. ⚠️ Il bulk CSV accetta solo obiettivo «Views or Clicks» e non crea campagne da feed (20/09/2026). https://help.openai.com/en/articles/20001218-bulk-upload-campaign-schema-checklist

## 4. Obiettivi e offerte

**CPM** (mille impression), **CPC** (clic valido), **oCPC** (si paga a **clic**, si ottimizza sulle conversioni post clic), **oCPM** (si paga a **impression**, si ottimizza su conversioni post clic **e post visualizzazione**; «generally available» e modello consigliato da OpenAI dal **16/09/2026**). https://help.openai.com/en/articles/20001412-conversion-optimized-campaigns · https://openai.com/index/reimagining-advertising-with-ai/

🔴 **Sulle campagne a conversione il Bid Cap è un'offerta per CONVERSIONE (CPA), non un CPC:** «the maximum amount you are willing to bid for a conversion»; nell'API `max_bid_micros` di un gruppo oCPC «is the CPA bid; for example, `100000000` is a $100.00 CPA bid». Chi mette 3-5 $ di Bid Cap su una campagna oCPC non consegna. Per le campagne a conversione «There is no recommended bid amount at this time» (20/09/2026). https://developers.openai.com/ads/conversion-optimized-campaigns

⛔ Una campagna esistente **non si converte** in oCPC né in oCPM, né tra loro: si crea nuova, col tracciamento già attivo e almeno un evento standard in arrivo.

Tre strategie: **offerta fissa** («Manual: Max bid»), **massimizza i clic**, **massimizza le conversioni**. 🔴 **Maximize results è il default sui gruppi nuovi idonei**: l'offerta fissa va scelta esplicitamente. OpenAI dichiara che **non garantisce** CPA, CPC o ROAS obiettivo. https://help.openai.com/en/articles/20001425-maximize-results-bid-strategy

**Offerta di partenza consigliata: 3-5 $ per clic, solo per CPC.** ⚠️ È alto per il mercato italiano: va confrontato col costo di una **lettura**, non con un CPC.

🔴 **Budget giornaliero ≥ offerta più alta** (Daily Budgets, 20/09/2026): con budget giornaliero e offerta fissa il budget deve essere almeno l'offerta effettiva per evento più alta tra i gruppi non archiviati, bid multiplier inclusi. Bid Cap CPA da 100 € → almeno 100 €/giorno. Non vale per Maximize results né per budget totale. https://help.openai.com/en/articles/20001413-daily-budgets

Il pannello mostra un giudizio di **bid strength** e l'avviso **«Low bid»** basato su dati d'asta osservati. https://help.openai.com/en/articles/20001217-troubleshooting-common-issues

Nell'API le offerte sono in **micros** (1 unità = `1000000`); per il CPM si divide prima per 1.000.

⚠️ **Nessun periodo di apprendimento dichiarato.** È un'assenza nella documentazione, non la prova che non esista.

⛔ **oCPC: un solo evento di conversione standard attivo per campagna, niente eventi custom come obiettivo, e obiettivo ed evento non si cambiano dopo la creazione**: per ottimizzare su un altro evento si crea una campagna nuova. Si paga sempre il clic valido, mai la conversione; `max_bid_micros` è l'offerta CPA usata come input di ottimizzazione (https://developers.openai.com/ads/conversion-optimized-campaigns, letta il 23/09/2026).

## 5. Budget

🔴 **Minimo giornaliero documentato per valuta** (tabella «Minimum Campaign Spend», pagina Campaigns, 20/09/2026): **EUR 15 €/giorno**, GBP 15, CHF 20, **USD 25**, PLN 65, SEK 175 (23 valute). Il developers doc dice solo «Daily minimums depend on the account currency». ⚠️ Si conferma comunque sul pannello: l'API risponde con l'importo richiesto nell'errore. https://help.openai.com/en/articles/20001210-create-campaigns-for-chatgpt-ads · https://developers.openai.com/ads/bidding-and-budgets

Due tipi di budget: **giornaliero** e **totale di campagna**. ⛔ Il passaggio da totale a giornaliero **non è reversibile**. https://help.openai.com/en/articles/20001515-budget-pacing

Budget giornaliero:
- La spesa di un giorno **non supera il doppio** del budget giornaliero.
- Su sette giorni il tetto è **sette volte** il giornaliero.
- Cambiando budget a metà giornata vale il **valore più alto attivo** quel giorno; il tetto settimanale si riproporziona fino alla domenica a mezzanotte.
- Con offerta fissa, budget ≥ offerta più alta (§4).

**Pacing:** rallenta se si è avanti di spesa e ⛔ **non garantisce di spendere tutto**. Solo col **budget totale**: con data di fine arriva lì, massimo **365 giorni**; senza data di fine il periodo è **60 giorni**. Col giornaliero non esiste un periodo di pacing.

## 6. Targeting

**Geografia:** paese ISO 3166-1 alpha-2. Sub-nazionale (stati/regioni, città, mercati, CAP) «where available», «may vary by country»: non più limitato agli USA nella FAQ, ma per l'Italia **non verificato** (2.1). ⛔ Campagne da product feed: solo paese. Via API fino a 2.500 location ID. https://help.openai.com/en/articles/20001210-create-campaigns-for-chatgpt-ads · https://developers.openai.com/ads/campaign-targeting

**Piattaforme (cinque, dal 10/09/2026; confermate il 23/09/2026 dalla pagina platform-targeting, che elenca `android_app`, `android_web`, `desktop_web`, `ios_app`, `ios_web` più `web` come gruppo legacy di tutto il web; `targeting.platforms` omesso o `null` = nessuna restrizione, https://developers.openai.com/ads/platform-targeting):** Android app, Android web, Desktop web, iOS app, iOS web, in pannello e in Insights; nell'API `android_app`, `android_web`, `desktop_web`, `ios_app`, `ios_web`, con `web` che resta come gruppo di tutto il web. https://developers.openai.com/ads

**Context hints:** fino a **2.000 per gruppo**, scritti come **frasi naturali e descrittive**, non come elenchi di termini. Articolo dedicato (20/09/2026): schema what/who/when, «a clear, natural phrase focused on one idea»; ⛔ gli hint «cannot enforce geographic limits, schedules, or exclusions». Nel Bulk API i gruppi hanno anche `exclusion_hints` (hint negativi), non documentati nell'help: da verificare se esposti nel pannello. https://help.openai.com/en/articles/20001521-write-context-hints-for-chatgpt-ads · https://developers.openai.com/ads/bulk-api

**Pubblici personalizzati:** ⛔ **non per campagne EEA/Svizzera (2.1).** Fuori EEA: solo **liste caricate** (email, telefono, varianti SHA-256, GAID), ⛔ nessun retargeting da pixel; **minimo 25.000 utenti corrispondenti** per l'inclusione, sotto valgono solo in esclusione («Ready — Exclusion only»), consigliati ≥100.000. CSV o TXT UTF-8 fino a 500 MB, hash SHA-256 a 64 caratteri, telefoni E.164 prima dell'hash. Dal **25/08/2026**: add/remove/replace membri senza ricreare, identificatori misti nello stesso file, oltre 5M membri, **bid multiplier 0,1x-10x** a livello gruppo. File eliminati entro 24 h dal caricamento; processing 20-30 min. https://help.openai.com/en/articles/20001346-set-up-custom-audiences-for-your-campaign · https://developers.openai.com/ads/custom-audiences

⚠️ Non documentati: targeting per lingua (esiste solo la traduzione automatica del testo, §7), fasce orarie, frequency cap. Non si promettono.

## 7. Creatività

| Elemento | Regola |
|---|---|
| Titolo | **16-24 caratteri consigliati, 50 massimo** |
| Testo | **32-48 consigliati, 100 massimo** |
| Immagine | **quadrata**, **massimo 1200 x 1200**, PNG o JPG, URL pubblico diretto |
| Destinazione | link valido, pagina **più pertinente** e non la home, UTM e parametri dinamici ammessi (§9) |

**Assistenza:** «Suggested ad drafts» dai metadata del sito (senza AI) e, dal 16/09/2026, copy e immagini suggeriti dall'AI dalla landing, modificabili prima dell'uso. Opt-in **«AI-powered text customization»** (16/09/2026): riscrive titolo e descrizione sul contesto e **traduce nella lingua dell'utente**; «An ad's language may differ from your conversation or interface language». https://help.openai.com/en/articles/20001212-create-ads-for-chatgpt-ads · https://openai.com/index/reimagining-advertising-with-ai/

**Campagne da product feed** (open beta, 20/09/2026): CSV/TXT, URL o SFTP; ⛔ gli item **scadono dopo 2 settimane**; per le immagini serve lasciar passare anche `OAI-SearchBot`; geo solo paese; il bulk CSV non le crea. https://help.openai.com/en/articles/20001268-create-campaigns-from-product-feeds

🔴 **La destinazione deve lasciar passare `OAI-AdsBot`** (e si consiglia `OAI-SearchBot`, obbligatorio per le immagini da feed), altrimenti la revisione non passa e ⛔ **non esiste bypass manuale**. In `robots.txt` servono le due direttive `Allow: /`; gli IP stabili stanno in `openai.com/adsbot.json` e `openai.com/searchbot.json`. Blocchi di WAF, CDN, anti-bot, CAPTCHA o login fermano tutto. Sistemato l'accesso, l'inserzione va ricaricata o rimandata in revisione.

## 8. Tracciamento

Pixel `oaiq`, SDK da `https://bzrcdn.openai.com/sdk/oaiq.min.js`:

```
oaiq("init", { pixelId: "<PIXEL-ID>", debug: true })
oaiq("measure", eventName, eventData, options)
```

`eventData` vuole `type`; `options` accetta `event_id`, `custom_event_name`, `opt_out`.

**Eventi standard:** `page_viewed`, `contents_viewed`, `items_added`, `checkout_started`, `order_created`, `lead_created`, `registration_completed`, `appointment_scheduled`, `subscription_created`, `trial_started`, `app_installed`, `app_opened`, `custom`. `plan_id` su `subscription_created` e `trial_started` è **opzionale**, non richiesto (20/09/2026). ⚠️ I due eventi app **solo via Conversions API** con `action_source` a `mobile_app`. https://developers.openai.com/ads/supported-events

🔑 **Gli importi si mandano come interi nell'unità minima ISO 4217:** 129,99 € si scrive `12999`.

Il parametro di clic è **`oppref`**, appeso alla destinazione; il pixel lo mette in un cookie di prima parte `__oppref`, aggiunge `source_url`, fa da solo l'hash SHA-256 dell'advanced matching e ha anche l'advanced matching automatico dai moduli. Esiste anche il cookie **`__obref`** (browser reference): dal **16/07/2026** si passa alla CAPI come `events[].user.obref`, **senza hash**, per le integrazioni ibride pixel+server. https://developers.openai.com/ads/conversions-api

**Conversions API:** endpoint **`https://bzr.openai.com/v1/events?pid=<PIXEL-ID>`**, autenticazione **Bearer**. Fino a **1.000 eventi** per richiesta; ogni evento ha `id`, `type`, `timestamp_ms`, `action_source`, `user`, `data`. ⛔ Timestamp **entro 7 giorni** e non oltre 10 minuti nel futuro. ⛔ **Se un evento fallisce, fallisce tutto il lotto.**

🔴 **Deduplicazione:** `id` della API uguale a `event_id` del pixel, stesso Pixel ID, stesso `custom_event_name` sugli eventi custom. Vince il primo arrivato. È la stessa forma della CAPI di Meta.

**Qualità degli eventi** (20/09/2026): per ogni data source c'è un **punteggio** e nove avvisi con nome e rimedio: email/customer ID mancanti, `oppref` non collegato, eventi CAPI in ritardo oltre 1 ora, match da rivedere, troppe conversioni sulla stessa interazione, matching aggiuntivo scarso, pochi tipi di evento, poca attività pixel/CAPI, goal senza eventi. Aggiornata ogni giorno su sette giorni pieni. ⚠️ La scala 1-10 è riportata da ppc.land, non vista nella pagina OpenAI: si lavora sugli avvisi. https://help.openai.com/en/articles/20001513-understand-and-improve-event-quality

**Integrazioni di misurazione:** Measurement Partner e Mobile Measurement Partner (articoli dedicati), app Shopify con pixel server (§2), HubSpot (§2). https://help.openai.com/en/articles/20001416-set-up-measurement-partner-integrations · https://help.openai.com/en/articles/20001372-set-up-mobile-measurement-partner-integrations

## 9. Report

Impression, clic, spesa, CTR, CPC medio, CPM medio, conversioni, per campagna, gruppo e inserzione, con esportazione CSV cumulativa o giornaliera. **Segmentazioni: dispositivo, paese e piattaforma** (20/09/2026); ⚠️ via API il segmento platform non supporta le conversioni. Via API Insights (26/09/2026): al massimo **2.000 righe** per richiesta, oltre arriva un **413** senza risultati parziali (si spezza il periodo o la lista di entità); fino a **365 giorni** per richiesta entro gli ultimi 5 anni; granularità oraria, giornaliera, mensile o totale; il breakdown platform distingue `web` (storico aggregato) da `android_web`, `desktop_web` e `ios_web` (https://developers.openai.com/ads/api-reference/insights). Nuove colonne: eventi singoli, Order Created Sales e Order Created ROAS (solo da `order_created`), Click-through e View-through separate, «Conversions (by conv. time)». https://help.openai.com/en/articles/20001214-measure-results · https://developers.openai.com/ads/api-reference/insights

🔴 **Ritardi da non scambiare per guasti:** clic e CTR rapidi, **spesa fino a 7 ore**, **conversioni 24-48 ore**, e prima di segnalare un problema di consegna si aspettano **24 ore dal lancio**.

**Attribuzione** (16/09/2026): finestra post clic **7, 14 o 30 giorni**; view-through **0 Day (disattivata) o 1 Day**. Solo reporting, last-touch, non tocca il bidding. 🔴 **Con 1 Day la colonna Conversions include le view-through**: per confrontare con GA4 si mette 0 Day o si legge la colonna Click-through. ⚠️ OpenAI avverte che i numeri **non coincideranno** con analytics di terze parti, anche per via della **misurazione modellata**. Quindi il pannello si usa per costo e consegna, il giudizio lo dà GA4. https://help.openai.com/en/articles/20001214-measure-results · https://openai.com/index/reimagining-advertising-with-ai/

**Parametri URL dinamici** `{campaign_id}`, `{ad_group_id}`, `{ad_id}`, `{ad_account_id}`, impostabili a livello campagna, gruppo o inserzione: il gruppo si legge in GA4 senza scrivere UTM a mano. https://help.openai.com/en/articles/20001214-measure-results

## 10. Policy

**Vietati:** adulti e dating, alcolici sopra 0,5% e nicotina, droghe e cannabis, gioco d'azzardo con denaro vero, contraffazione, **contenuti politici**, sessuale o violento esplicito. Aggiunti in v1.4 (agosto 2026): **annunci di lavoro e immobiliari singoli**, scams e frodi, «sensitive topics or events» (aborto, immigrazione, razza, religione, identità di genere), **wellness claims** (diet pills, detox, integratori con claim, health coaching). https://openai.com/policies/ad-policies/

🔴 **v1.6 (settembre 2026):** OpenAI si riserva di rifiutare annunci «where they conflict with our advertising principles, business interests, or competitive position». Pesa per chi vende software o AI concorrente.

**Ristretti con verifica e SOLO negli Stati Uniti:** servizi finanziari, sanità, servizi legali. ⛔ Fuori dagli Stati Uniti finanziario e legale restano generalmente vietati.

**Creatività:** affermazioni veritiere, linguaggio professionale, distinzione chiara dall'interfaccia. La destinazione non può introdurre contenuti non ammessi dopo l'approvazione.

**Contesti sensibili:** la policy attuale parla genericamente di «sensitive user contexts» e «brand unsafe contexts»; dalla v1.1 (aprile 2026) i contesti di consiglio medico, legale e finanziario non sono più esclusi a priori; l'help utenti cita solo «personal health, mental health, or politics». L'elenco puntuale della versione precedente di questa skill (salute mentale, crisi, vulnerabilità, minori, terrorismo, armi, disinformazione, odio, privacy) non trovato in nessuna fonte al 20/09/2026, da verificare sul pannello. https://openai.com/policies/ad-policies/ · https://help.openai.com/en/articles/20001047-ads-in-chatgpt

## 11. API inserzionisti

`developers.openai.com/ads` documenta gestione campagne, offerte e budget, targeting, feed di prodotto, tracciamento, reporting e account, con riferimento per autenticazione, ad account, campagne, gruppi, inserzioni, insights, file e conversioni. 🔑 Il canale si può governare da script invece che a clic. Regole operative (20/09/2026):

- **Bulk API** (limited preview, attivata per singolo ad account dal team OpenAI, 23/09/2026): fino a **1.000 operazioni per job**, corpo massimo 16 MiB, 512 KiB per operazione; tetti 5.000 campagne, 5.000 gruppi, 5.000 inserzioni attive o in pausa per account. https://developers.openai.com/ads/bulk-api
- **Rate limit:** 600 richieste/min per endpoint, 1.200/min complessive per account e per IP; bulk job 10 richieste ogni 10 s.
- **Offerte in micros** (1 unità = `1000000`); CPM diviso per 1.000; nel bulk il campo CPM è `max_cpm_bid_micros`.
- `bidding_type`: `impressions`, `clicks`, `conversions`. Su un gruppo oCPC `max_bid_micros` è un **CPA** (§4).
- Le campagne nascono in stato **`paused`**.
- Piattaforme: `android_app`, `android_web`, `desktop_web`, `ios_app`, `ios_web`, `web` (10/09/2026). Geo: fino a 2.500 location ID, catalogo `ads.openai.com/assets/openai-geotargets.csv`.
- Gruppi: `context_hints` e `exclusion_hints` (bulk API). Pubblici: add/remove/replace membri, bid multiplier (25/08/2026).
- CAPI: `events[].user.obref` senza hash (16/07/2026). Insights: segmento platform senza conversioni.
- Budget minimo: l'errore restituisce l'importo richiesto nella valuta dell'account.
- 🔑 Il **changelog** in `developers.openai.com/ads` è la fonte più rapida sui cambi: si legge a ogni verifica (§0.5).

https://developers.openai.com/ads · https://developers.openai.com/ads/bulk-api · https://developers.openai.com/ads/conversion-optimized-campaigns · https://developers.openai.com/ads/location-targeting · https://developers.openai.com/ads/platform-targeting · https://developers.openai.com/ads/custom-audiences · https://developers.openai.com/ads/api-reference/insights

## 12. Quello che NON c'è

⛔ Benchmark di performance pubblicati. ⛔ Retargeting da pixel. ⛔ Pubblici personalizzati per campagne EEA/Svizzera. ⛔ Targeting per lingua, fasce orarie, frequency cap. ⛔ Finestra di apprendimento dichiarata. ⛔ Offerta consigliata per oCPC/oCPM. ⛔ Sponsored Agents fuori dall'alpha USA. ⛔ Segmentazione per context hint: **quale gancio ha funzionato dal pannello non si sa**, si separa in gruppi e si legge in GA4 con `{ad_group_id}` (§9). ✅ Non più assenti dal 20/09/2026: il minimo in euro (§5) e i mercati dove le inserzioni vengono servite (§1).

## 13. Come si monta un test di spesa onesto

1. Aprire l'account (anche dal plugin in ChatGPT) e superare la verifica: **fin qui non si spende**. Con account nuovo si parte dalla sola Italia (2.1).
2. **Minimo giornaliero: 15 €/giorno documentato** (§5); si conferma sul pannello e sull'errore API prima di partire.
3. Sistemare `robots.txt` per `OAI-AdsBot` e **verificare che la pagina sia raggiungibile davvero**, non solo che la riga sia scritta.
4. Mettere il pixel dallo stesso container e agganciare l'evento che misura il risultato vero, non il clic. Su Shopify l'app (internazionale dal 23/09), su HubSpot l'integrazione.
5. **Un gruppo solo, CPC, offerta fissa: scegliere esplicitamente «Manual: Max bid»**, perché Maximize results è il default. Niente liste: sull'Italia non servono.
6. **Context hints come frasi**, sui temi e non sul nome del prodotto: chi cerca il nome è già arrivato.
7. **View-through a 0 Day**, o si legge solo Click-through: altrimenti la colonna Conversions include le visualizzazioni.
8. **Soglia scritta prima di partire**, in unità di risultato e non in CPC.
9. **Lettura finale in GA4**, con `{campaign_id}` e `{ad_group_id}` nell'URL più gli UTM, non nel pannello.

## Fonti

Tutte consultate il 20/09/2026. ⚠️ `help.openai.com`, `openai.com` e `ads.openai.com` rispondono **HTTP 403** al fetch diretto (Cloudflare «Just a moment», anche con user-agent browser): sono state lette tramite reader proxy (`r.jina.ai`) e, a campione, dalla Wayback Machine. **La prossima verifica si fa da browser.** `developers.openai.com/ads/*`, `openai.com/adsbot.json` e `openai.com/searchbot.json` rispondono 200 direttamente; l'export `developers.openai.com/ads/llms-full.txt` contiene tutta la documentazione API col changelog.

Help center: [Ads in ChatGPT (utenti)](https://help.openai.com/en/articles/20001047-ads-in-chatgpt) · [The Basics](https://help.openai.com/en/articles/20001207-ads-in-chatgpt-the-basics) · [Availability](https://help.openai.com/en/articles/20001245-ads-manager-availability) · [Account Setup](https://help.openai.com/en/articles/20001213-ads-manager-beta-account-setup) · [Overview](https://help.openai.com/en/articles/20001206-ads-manager-beta-overview) · [Campaigns](https://help.openai.com/en/articles/20001210-create-campaigns-for-chatgpt-ads) · [Ad Groups](https://help.openai.com/en/articles/20001211-create-ad-groups-for-chatgpt-ads) · [Ads](https://help.openai.com/en/articles/20001212-create-ads-for-chatgpt-ads) · [Context Hints](https://help.openai.com/en/articles/20001521-write-context-hints-for-chatgpt-ads) · [Product Feeds](https://help.openai.com/en/articles/20001268-create-campaigns-from-product-feeds) · [Daily Budgets](https://help.openai.com/en/articles/20001413-daily-budgets) · [Budget Pacing](https://help.openai.com/en/articles/20001515-budget-pacing) · [Maximize Results](https://help.openai.com/en/articles/20001425-maximize-results-bid-strategy) · [oCPC/oCPM](https://help.openai.com/en/articles/20001412-conversion-optimized-campaigns) · [Conversion Measurement](https://help.openai.com/en/articles/20001409-conversion-measurement) · [Measure Results](https://help.openai.com/en/articles/20001214-measure-results) · [Custom Audiences](https://help.openai.com/en/articles/20001346-set-up-custom-audiences-for-your-campaign) · [Event Quality](https://help.openai.com/en/articles/20001513-understand-and-improve-event-quality) · [Measurement Partners](https://help.openai.com/en/articles/20001416-set-up-measurement-partner-integrations) · [MMP](https://help.openai.com/en/articles/20001372-set-up-mobile-measurement-partner-integrations) · [HubSpot](https://help.openai.com/en/articles/20001522-set-up-chatgpt-ads-in-hubspot) · [Sponsored Agents](https://help.openai.com/en/articles/20001524-sponsored-agents-in-chatgpt-ads) · [Crawler](https://help.openai.com/en/articles/20001243-advertiser-guidance-for-allowing-openai-web-crawlers) · [Billing](https://help.openai.com/en/articles/20001216-billing-payment) · [Bulk Upload Schema](https://help.openai.com/en/articles/20001218-bulk-upload-campaign-schema-checklist) · [FAQ](https://help.openai.com/en/articles/20001220-frequently-asked-questions) · [Troubleshooting](https://help.openai.com/en/articles/20001217-troubleshooting-common-issues)

Developers e OpenAI: [Ads API + changelog](https://developers.openai.com/ads) · [llms-full.txt](https://developers.openai.com/ads/llms-full.txt) · [Measurement Pixel](https://developers.openai.com/ads/measurement-pixel) · [Conversions API](https://developers.openai.com/ads/conversions-api) · [Supported Events](https://developers.openai.com/ads/supported-events) · [Bidding and Budgets](https://developers.openai.com/ads/bidding-and-budgets) · [Targeting](https://developers.openai.com/ads/campaign-targeting) · [Location Targeting](https://developers.openai.com/ads/location-targeting) · [Platform Targeting](https://developers.openai.com/ads/platform-targeting) · [Custom Audiences API](https://developers.openai.com/ads/custom-audiences) · [Conversion-Optimized API](https://developers.openai.com/ads/conversion-optimized-campaigns) · [Bulk API](https://developers.openai.com/ads/bulk-api) · [Insights](https://developers.openai.com/ads/api-reference/insights) · [ads.openai.com](https://ads.openai.com/) · [Ad Policies](https://openai.com/policies/ad-policies/) · [Reimagining advertising with AI (16/09/2026)](https://openai.com/index/reimagining-advertising-with-ai/) · [Expands across Europe (24/08/2026)](https://openai.com/index/chatgpt-ads-expands-across-europe/) · [New ways to buy ChatGPT ads](https://openai.com/index/new-ways-to-buy-chatgpt-ads/) · [Expanding access](https://openai.com/index/expanding-access-to-ai-with-chatgpt-ads/) · Terze parti (non primarie): [ppc.land](https://ppc.land/openai-lets-advertisers-run-chatgpt-ads-from-hubspot-and-shopify/)

⚠️ **Niente è stato verificato su un pannello**: alla prima apertura si riverificano minimo giornaliero in euro (15 € documentati), importo del blocco carta, soglia di pagamento, credito di benvenuto, località sub-nazionali per l'Italia, presenza di `exclusion_hints`, scala del punteggio di qualità eventi e limiti reali dei caratteri.
