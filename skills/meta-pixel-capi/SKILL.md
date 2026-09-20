---
name: "meta-pixel-capi"
description: "Regole operative verificate per installare, controllare e riparare il tracciamento Meta su siti italiani: Meta Pixel, dataset in Gestione eventi, Conversions API (CAPI) via GTM server-side (Stape), CAPI Gateway, plugin WooCommerce, Shopify e PrestaShop; eventi standard e parametri obbligatori (Purchase con value e currency, content_ids), event_id e deduplica, cookie _fbp e _fbc, fbclid, Event Match Quality, Advanced Matching, Testa gli eventi e Diagnostica, consenso UE e Business Tools Terms, versioni Marketing API. Usala ogni volta che un acquisto risulta doppio o mancante, l'EMQ è bassa, il pixel scatta prima del banner, si eredita un dataset altrui o si monta la CAPI da zero."
---

# Meta Pixel e Conversions API: regole operative

**Ultima verifica delle fonti: 20 settembre 2026.**

Questa skill approfondisce la sezione 4 della skill `meta-ads-performance` e non la contraddice: la fase di apprendimento, le finestre di attribuzione e i pubblici restano lì. Qui c'è il tracciamento: cosa arriva a Meta, come, e come si capisce se è rotto.

---

## 0. Manutenzione di questa skill (leggere per primo)

1. **Finestra di freschezza: due mesi.** Nel 2026 Meta ha cambiato tre volte la superficie del tracciamento (Pixel con AI e CAPI a un clic il 15/04/2026, Marketing API v25 il 18/02 e v26 il 29/07, scadenza v24 il 06/10/2026) e ha spostato la documentazione su un nuovo dominio (`developers.facebook.com/documentation/ads-commerce/...`, con i vecchi URL `docs/marketing-api/conversions-api/...` in parte in redirect 301 e in parte 404). Se la data qui sopra ha più di due mesi, si rileggono changelog e pagine parametri prima di citare un numero.
2. Quando una fonte smentisce una regola scritta qui, la skill si aggiorna **nello stesso turno**, si riscrive la data in cima e si annota cosa è cambiato e **da quando** (data del cambio di Meta, non del giorno in cui ce ne si accorge: l'errore AEM registrato in `meta-ads-performance` non si ripete).
3. Due metà da tenere distinte: **conoscenza di dominio** (come si comportano Pixel e CAPI: si verifica su developers.facebook.com) e **meccanica del pannello** (sez. 13: si impara sbagliando e si scrive qui la prima volta). Nulla in questa skill è stato osservato sul pannello: è la prima stesura.
4. Dove si guardano i cambiamenti: [Marketing API changelog](https://developers.facebook.com/documentation/ads-commerce/marketing-api/marketing-api-changelog) · [Graph API changelog e date di scadenza](https://developers.facebook.com/docs/graph-api/changelog/) · [Meta for Business news](https://www.facebook.com/business/news) · [Stape news](https://stape.io/news).
5. ⚠️ **Le pagine `facebook.com/business/help/<ID>` non si leggono da questo ambiente** (20/09/2026: WebFetch restituisce solo il titolo, curl HTTP 200 con corpo "Sorry, something went wrong", alcune 404). Vanno aperte a mano in un browser autenticato. Qui sono citate con l'ID; la fonte primaria è developers.facebook.com, che si legge. Le voci **[DA VERIFICARE]** e le "regole empiriche di terzi" non si citano a un cliente come numeri Meta.

---

## 1. Dataset, Pixel e CAPI: cosa deve esserci

- **In Gestione eventi il Pixel si chiama dataset e l'ID è lo stesso.** Un dataset raccoglie eventi da sito (Pixel), server (CAPI), app, offline e messaggistica in un solo oggetto; l'ID dataset che si incolla nel sito è il vecchio ID Pixel ([theadspend](https://theadspend.com/blog/meta-ads-conversion-tracking) · [leadsie](https://www.leadsie.com/blog/all-you-need-to-know-about-facebook-metas-new-datasets); pagina ufficiale [750785952855662](https://www.facebook.com/business/help/750785952855662) non leggibile via fetch il 20/09/2026). Un dataset per sito, non uno per campagna e non uno per agenzia.
- 🔴 **Lo standard è Pixel e CAPI insieme, in ridondanza**, con deduplica (sez. 4). La colonna **Metodo di collegamento** in Panoramica dice la verità: *Browser* soltanto significa che la CAPI non c'è; a posto dice *Browser e server* (stessa regola di `meta-ads-performance`, sez. 4). Meta dichiara **-17,8% di costo per risultato** medio con la CAPI attiva: è un numero promozionale di Meta, non una promessa per il singolo account ([annuncio 15/04/2026](https://www.facebook.com/business/news/pixel-conversionsapi-updates)).
- **Il codice base va in `<head>` su ogni pagina, una volta sola**: `fbq('init', '<ID>')` più `fbq('track','PageView')`, con il fallback `<noscript><img>` ([get-started](https://developers.facebook.com/docs/meta-pixel/get-started)). Due `init` dello stesso ID (tema + plugin, o plugin + GTM) raddoppiano ogni evento; è il primo controllo su un sito ereditato (sez. 11).
- **Dal 15/04/2026 esistono due scorciatoie dentro Gestione eventi** ([annuncio Meta](https://www.facebook.com/business/news/pixel-conversionsapi-updates) · [segwise](https://segwise.ai/blog/meta-pixel-conversions-api-ai-updates-2026) · [weltpixel](https://weltpixel.com/blogs/news/metas-one-click-conversions-api-what-it-does-and-what-it-leaves-out)):
  - **Pixel con AI**: Meta arricchisce da sé gli eventi con nome prodotto, disponibilità e dati di pagina. Per i Pixel esistenti c'è stata una **finestra di 30 giorni** di avviso, poi si è **acceso da solo**; si spegne da Gestione eventi e l'opt-out resta. Su un dataset ereditato si guarda se è acceso e cosa sta aggiungendo, perché altera `custom_data` senza che nessuno l'abbia scritto.
  - **CAPI abilitata da Meta (a un clic)**: Meta genera il lato server **replicando gli eventi già ricevuti dal browser**. Zero codice e zero costo, ma non recupera nulla che il Pixel non ha mandato (ad blocker, consenso negato, pagina chiusa), non copre eventi personalizzati, app e offline, e non aggiunge dati cliente oltre a quelli del browser. "Metodo di collegamento: Browser e server" con questa via **non vale** come una CAPI dal server del sito: sul dataset si controlla da dove arrivano davvero gli eventi server. [DA VERIFICARE] come il pannello etichetta questa origine.

---

## 2. Eventi standard, parametri, eventi personalizzati, conversioni personalizzate

Fonte: [riferimento Pixel](https://developers.facebook.com/docs/meta-pixel/reference) · [conversion-tracking](https://developers.facebook.com/docs/meta-pixel/implementation/conversion-tracking).

- 🔴 **`Purchase` richiede `value` e `currency`**, sono gli unici parametri obbligatori di tutto il riferimento. `value` numero (non stringa con la virgola), `currency` ISO a tre lettere (`EUR`). Un Purchase con `value` e senza `currency` è un acquisto che Meta non sa contare in euro: la Diagnostica lo segnala come *Invalid Purchase Currency Code* / *Invalid Purchase Value Parameter* ([adsuploader](https://adsuploader.com/blog/meta-pixel-standard-events), terza parte).
- **Per le inserzioni da catalogo (Advantage+ catalog) servono `content_ids` o `contents`** su `ViewContent`, `AddToCart`, `Search`, `Purchase`, con `content_type` = `product` oppure `product_group` a seconda di quale ID si manda. `contents` è un array di oggetti con **`id` e `quantity` obbligatori**. 🔴 Gli ID devono essere **gli stessi del feed di catalogo** (di norma lo SKU o l'ID variante, non il post ID di WooCommerce): se non coincidono, il retargeting dinamico mostra prodotti sbagliati o niente.
- `Lead`, `CompleteRegistration`, `Contact`, `Schedule`, `Subscribe`, `StartTrial`, `AddPaymentInfo`, `InitiateCheckout`: tutti i parametri sono facoltativi; `value`+`currency` sui lead servono solo se si vuole ottimizzare sul valore. `num_items` su InitiateCheckout, `predicted_ltv` su Subscribe, `search_string` su Search, `status` booleano su CompleteRegistration.
- **Eventi personalizzati:** `fbq('trackCustom','NomeEvento', {...})`, nome stringa **max 50 caratteri**. Le chiavi dei parametri usate per i pubblici **non devono contenere spazi**. Un evento personalizzato non è ottimizzabile come uno standard finché non lo si mappa in una conversione personalizzata: quando esiste lo standard (`Lead`, non `richiesta_preventivo`) si usa lo standard.
- **Conversioni personalizzate:** regole su URL (`/grazie`) o su evento+parametro, **massimo 100 per account pubblicitario**. Si contano dal momento della creazione, non retroattive: si creano il giorno in cui si apre l'account. [DA VERIFICARE] se il limite di 100 vale per account o per Business.
- ⚠️ **AEM per il web non esiste più**: nessun evento nuovo consuma slot e non c'è priorità da impostare (dettaglio in sez. 7).

---

## 3. Conversions API: il payload

Fonte: [parametri](https://developers.facebook.com/docs/marketing-api/conversions-api/parameters) · [evento server](https://developers.facebook.com/docs/marketing-api/conversions-api/parameters/server-event) · [using-the-api](https://developers.facebook.com/docs/marketing-api/conversions-api/using-the-api) · [end-to-end](https://developers.facebook.com/docs/marketing-api/conversions-api/guides/end-to-end-implementation).

- Endpoint: `POST https://graph.facebook.com/v<versione>/<DATASET_ID>/events?access_token=<token>`, corpo con array `data`. **Fino a 1.000 eventi per richiesta**; 🔴 **se un solo evento del batch è invalido, Meta rifiuta l'intero batch**.
- **Per ogni evento sono obbligatori:** `event_name`, `event_time` (UNIX in secondi), `action_source`, `user_data`; per gli eventi web anche **`event_source_url`** e **`client_user_agent`** dentro `user_data`.
- **`action_source`** ammette solo `email`, `website`, `app`, `phone_call`, `chat`, `physical_store`, `system_generated`, `business_messaging`, `other`. Per un sito è `website`, e Meta chiede di dichiarare che il valore è accurato ([gtm-server-side](https://developers.facebook.com/docs/marketing-api/conversions-api/guides/gtm-server-side)). Chi manda un lead da CRM con `website` sta dichiarando il falso: si usa `system_generated` o `other`.
- 🔴 **`event_time` può stare al massimo 7 giorni nel passato**: "if any `event_time` in `data` is greater than 7 days in the past, we return an error for the entire request and process no events". Per `physical_store` la finestra è **62 giorni** ([offline-events](https://developers.facebook.com/documentation/ads-commerce/conversions-api/offline-events)). Ma la freschezza utile è un'altra: Meta chiede l'invio **in tempo reale o entro 1 ora**; oltre le 2 ore la resa in ottimizzazione cala (end-to-end). Un caricamento notturno "batch" è ammesso, non è equivalente.
- **`event_id`**: stringa unica scelta dall'inserzionista (numero ordine, transaction id, UUID); serve alla deduplica (sez. 4). **`opt_out: true`** esclude l'evento dall'ottimizzazione e lo tiene solo per l'attribuzione.
- **`custom_data`**: stessi nomi del Pixel (`value`, `currency`, `content_ids`, `content_type`, `contents`, `num_items`, `order_id`). Le regole di sez. 2 valgono identiche sul server.
- **`user_data` e hashing** ([customer-information-parameters](https://developers.facebook.com/docs/marketing-api/conversions-api/parameters/customer-information-parameters)): si **hashano in SHA-256** dopo normalizzazione `em` (trim, minuscolo), `ph` (solo cifre con prefisso internazionale, niente zeri iniziali, quindi `39333...` per un cellulare italiano), `fn`, `ln`, `ct` (minuscolo, senza spazi né punteggiatura), `st`, `zp` (minuscolo, senza spazi né trattino), `country` (ISO alpha-2 minuscolo: `it`), `db` (`YYYYMMDD`), `ge` (`f`/`m`); `external_id` raccomandato hashato. 🔴 **Non si hashano mai** `client_ip_address`, `client_user_agent`, `fbc`, `fbp`, `subscription_id`, `fb_login_id`, `lead_id`, `ctwa_clid`. Un'email hashata due volte o un telefono hashato con lo `+` non matcha niente e l'EMQ crolla in silenzio. Meta chiede di mandare `country` **anche se tutti i clienti sono italiani**.
- **`test_event_code`** va nel payload solo in test e **si toglie in produzione**: gli eventi di test **non vengono scartati**, finiscono nel dataset e vengono usati per targeting e misurazione (using-the-api).

---

## 4. Deduplica, `_fbp`, `_fbc`, `fbclid`

Fonte: [deduplicate](https://developers.facebook.com/docs/marketing-api/conversions-api/deduplicate-pixel-and-server-events) · [fbp-and-fbc](https://developers.facebook.com/docs/marketing-api/conversions-api/parameters/fbp-and-fbc).

- 🔴 **Meta deduplica solo se coincidono entrambi: `eventID` del Pixel = `event_id` della CAPI, e `event` del Pixel = `event_name` della CAPI.** Stesso `event_id` con `purchase` sul browser e `Purchase` sul server sono **due acquisti**. La finestra è **48 ore** dal primo evento ricevuto; a parità di contenuto Meta tiene **il primo arrivato**. Identico a `meta-ads-performance` sez. 4 e `gtm-server-side` sez. 8.
- Il metodo alternativo (`event_name` + `fbp` e/o `external_id`) **funziona solo browser-prima-server**: se il browser non arriva, il server non viene scartato. Non ci si affida.
- Sul Pixel l'ID si passa come quarto argomento: `fbq('track','Purchase',{...},{eventID:'<id>'})`. Per l'acquisto l'`event_id` giusto è **il numero d'ordine**: è unico, lo conoscono sia la pagina di ringraziamento sia il server, e rende innocuo il ricaricamento della pagina (stesso ID, stessa finestra di 48 ore).
- **`_fbp`** è il cookie di prima parte scritto dal Pixel: `fb.1.<timestamp ms>.<numero casuale>`. **`_fbc`** è il click id: `fb.1.<timestamp ms>.<fbclid>`, creato quando l'URL di atterraggio contiene `fbclid`; se il cookie manca ma `fbclid` c'è nell'URL, il server lo costruisce con `fb.1.<timestamp di prima osservazione>.<fbclid>`, scadenza **90 giorni**. Meta raccomanda di mandare `fbc` **con ogni evento** e di rinfrescare i valori, che cambiano fra sessioni.
- Sul dominio proprio del container server i due cookie arrivano da soli; sull'endpoint predefinito vanno passati dal web container ([gtm-server-side](https://developers.facebook.com/docs/marketing-api/conversions-api/guides/gtm-server-side)). Il tag Stape può **generare `_fbp` se manca** ([Stape](https://stape.io/helpdesk/documentation/how-to-set-up-meta-conversions-api)).
- ⚠️ **Sul sito i cookie di Meta sono solo `_fbp` e `_fbc`.** Cookie con altri prefissi (`_ga`, `_gcl_*`, `_gid`, `_uet*`, `_ttp`, `__ob*`, `_hj*`, `_clck`) sono di altri fornitori e non vanno né mandati nella CAPI né confusi in un audit; `fr`, `datr`, `c_user`, `xs` sono di Meta ma vivono su facebook.com, come terza parte, e il sito non li legge. Un `fbclid` **senza `_fbc`** significa che il Pixel non è partito su quella pagina (consenso negato o script bloccato): è diagnosi, non rumore.

---

## 5. Event Match Quality e Advanced Matching

- **EMQ è un punteggio da 0 a 10 per evento**, "indica quanto le informazioni cliente di un evento server possono essere efficaci nell'abbinarlo a un account Meta"; oggi esiste **solo per gli eventi web** ([best-practices](https://developers.facebook.com/docs/marketing-api/conversions-api/best-practices)). La pagina ufficiale sulle soglie ([765081237991954](https://www.facebook.com/business/help/765081237991954)) non è leggibile via fetch: le fasce **Scarso <4, OK 4-5,9, Buono 6-7,9, Ottimo 8+** sono riportate da terzi ([customerlabs](https://www.customerlabs.com/blog/improve-your-event-match-quality-from-ok-to-great/) · [triplewhale](https://www.triplewhale.com/blog/event-match-quality)) e **6 come "buono"** coincide con `meta-ads-performance` sez. 4 ([conversios](https://www.conversios.io/blog/meta-attribution-window-changes-2026-fix-your-tracking/)). Obiettivo pratico su `Purchase` e `Lead`: **8**, perché lì ci sono email e telefono. Un `PageView` a 4 è normale.
- **Cosa la alza, nell'ordine di priorità della tabella Meta** (gtm-server-side, "high/medium/low priority"): **email e click ID (`fbc`)** in alto; poi telefono, `fbp`, nome, indirizzo, `external_id`; `client_ip_address` e `client_user_agent` **sempre**, su tutti gli eventi ("may help improve event matching and could also help improve ad delivery"). In Panoramica il pannello di dettaglio dell'evento elenca **quali parametri arrivano e in che percentuale**: si parte da quelli a 0% su Purchase.
- 🔴 **Un'EMQ bassa sul Purchase dopo aver attivato la CAPI è quasi sempre normalizzazione sbagliata** (sez. 3), non mancanza di dati: il telefono con `+39`, l'email con maiuscole, il nome con accenti non in UTF-8.
- **Advanced Matching automatico** si accende in Gestione eventi > Impostazioni: il Pixel legge da solo i campi dei form. **Non è disponibile per Pixel `<img>`, Pixel dentro iframe e verticali regolamentate** (salute, finanza): lì si usa il manuale ([1993001664341800](https://www.facebook.com/business/help/1993001664341800) e [611774685654668](https://www.facebook.com/business/help/611774685654668), non leggibili via fetch; riportate da [adnabu](https://blog.adnabu.com/shopify/advanced-matching-in-facebook-pixel/)). **Advanced Matching manuale**: terzo argomento di `init`, `fbq('init','<ID>',{em:'...', ph:'...'})`; il Pixel **hasha da solo** in SHA-256, si può passare chiaro normalizzato o già hashato ([advanced-matching](https://developers.facebook.com/docs/meta-pixel/advanced/advanced-matching)). ⚠️ Tutti e due mandano dati personali: **solo dopo il consenso** (sez. 8).

---

## 6. Testa gli eventi e Diagnostica

- **Testa gli eventi** (Gestione eventi > dataset > *Testa gli eventi*): si naviga il sito e si vedono gli eventi in tempo reale con colonna *Ricevuto da* (Browser / Server) e lo stato di deduplica; per il server si copia il codice `TEST12345` nel campo Test ID del tag o in `test_event_code` ([using-the-api](https://developers.facebook.com/docs/marketing-api/conversions-api/using-the-api) · [Stape](https://stape.io/helpdesk/documentation/how-to-set-up-meta-conversions-api)). Pagine ufficiali [1624255387706033](https://www.facebook.com/business/help/1624255387706033) e [2040882565969969](https://www.facebook.com/business/help/2040882565969969) non leggibili via fetch. Regola empirica di terzi: il codice si rigenera a ogni apertura della tab e l'attività resta visibile **24 ore** ([anytrack](https://readme.anytrack.io/docs/meta-capi-test-mode)).
- 🔴 **Un test riuscito in Testa gli eventi prova che il colpo parte, non che sia attribuito.** Il giorno dopo si guardano Panoramica (eventi ricevuti, abbinati, deduplicati) e la colonna Risultati in Gestione inserzioni. Panoramica ha **15-20 minuti di ritardo** (regola empirica di terzi, [adsuploader](https://adsuploader.com/blog/meta-events-manager)); Meta dice che gli eventi CAPI si verificano "entro 20 minuti" (using-the-api).
- **Diagnostica** elenca per gravità: parametri mancanti (`currency`, `value`), codice valuta non valido, **eventi duplicati senza `event_id`**, eventi server senza `event_id`, calo improvviso di volume, Pixel che ha smesso di scattare. Si legge **prima** di ogni report al cliente e prima di aprire un ticket: nove volte su dieci il problema è lì.
- **Cronologia**: token generati, caricamenti, modifiche di configurazione. Su un dataset ereditato dice chi ha toccato cosa.
- ⛔ **Un `test_event_code` lasciato in una versione pubblicata** significa che ogni acquisto vero appare nella tab di test **e** viene contato: si controlla il campo prima di pubblicare, e nella lista di igiene (sez. 12).

---

## 7. AEM e verifica del dominio: cosa resta

- ✅ **Per gli eventi web AEM è chiuso**: priorità a 8 eventi, tab *Misurazione aggregata degli eventi*, selezione del dominio in campagna e obbligo di verifica del dominio rimossi, **annuncio Meta 15/05/2023, completamento entro metà 2025** ([adviso](https://www.adviso.ca/en/blog/evolution-aggregated-measurement-meta) · [segwise agg. 03/09/2026](https://segwise.ai/blog/facebook-aggregated-event-measurement); pagina ufficiale [721422165168355](https://www.facebook.com/business/help/721422165168355) non leggibile via fetch). Stesse fonti e stessa regola di `meta-ads-performance` sez. 4.
- ⚠️ **Per le app iOS il modello a eventi prioritizzati resta** (segwise): la CAPI per app usa ancora l'*App Aggregated Event Measurement* nei deep link ([app-events](https://developers.facebook.com/documentation/ads-commerce/conversions-api/app-events)). Se in un pannello la tab AEM c'è ancora, lì le vecchie regole valgono: si guarda, non si presume.
- **Verifica del dominio**: non serve più per gli eventi, ma resta necessaria per **la proprietà del link** (modificare titolo e immagine dell'anteprima nelle inserzioni) e per le configurazioni app iOS ([segwise](https://segwise.ai/blog/facebook-aggregated-event-measurement) · [conversios](https://www.conversios.io/blog/meta-aggregated-event-measurement/); pagina ufficiale [286768115176155](https://www.facebook.com/business/help/286768115176155) non leggibile via fetch). Si fa comunque, con record DNS TXT, perché costa dieci minuti e blocca l'uso del dominio da parte di altri Business.

---

## 8. Consenso UE, Business Tools Terms, Limited Data Use

- 🔴 **I [Business Tools Terms](https://www.facebook.com/legal/technology_terms) impongono al sito**: "a clear and prominent notice on each web page where our pixels are used" e, nelle giurisdizioni che richiedono il consenso per i cookie, "you must ensure, in a verifiable manner, that an end user provides all necessary consents before you use Meta Business Tools". Per i dati UE sito e Meta Ireland sono **contitolari** (Joint Controllers, Controller Addendum). È vietato mandare dati di **minori di 13 anni** e **dati sanitari, finanziari, o altre categorie sensibili**: un e-commerce di integratori o una clinica non mette il nome del prodotto in `content_name`.
- **Meta non ha un consent mode.** Lo strumento è `fbq('consent','revoke')` **prima di `init`, su ogni pagina**, e `fbq('consent','grant')` dopo l'accettazione: fra i due il Pixel accoda e non spedisce ([gdpr](https://developers.facebook.com/docs/meta-pixel/implementation/gdpr)). In GTM equivale a **Richiedi consenso aggiuntivo: `ad_storage` + `ad_user_data`** sul tag Pixel, e sul container server a una condizione sull'attivatore del tag CAPI, che non ha controlli integrati (stesse regole di `consent-mode-privacy` sez. 7-8 e `gtm-server-side` sez. 6).
- ⚠️ **La CAPI non aggira il consenso**: manda gli stessi dati personali, e `_fbp`/`_fbc` nascono sul browser. Un acquisto "recuperato" dal server per un utente che ha rifiutato è una violazione, non un'ottimizzazione. Con consenso negato Meta non ha eventi modellati equivalenti a Google: il buco resta.
- ⛔ **Limited Data Use è per gli Stati USA, non per l'Europa**: `data_processing_options: ['LDU']` con `country` 1/0 e `state` (1000 California, ...) copre California, Colorado, Connecticut, Delaware, Florida, Montana, Nebraska, New Hampshire, New Jersey, Oregon, Texas, Minnesota, Maryland, Rhode Island ([data-processing-options](https://developers.facebook.com/docs/marketing-apis/data-processing-options)). Su un sito italiano è un flag che limita retargeting e misurazione per niente; l'opzione LDU nei tag Stape e Meta resta spenta.
- **Contesto italiano**: banner secondo le [Linee guida cookie del Garante del 10/06/2021](https://www.garanteprivacy.it/home/docweb/-/docweb-display/docweb/9677876), nessun cookie `_fbp` prima del clic su Accetta, Meta nominata nella cookie policy (dettaglio in `consent-mode-privacy`). Il [provvedimento n. 284 del 17/04/2026](https://www.garanteprivacy.it/home/docweb/-/docweb-display/docweb/10241943) riguarda i **pixel nelle e-mail** (adeguamento entro il 28/10/2026): non è il Meta Pixel, ma è lo stesso standard di consenso preventivo, e chi usa i pixel di apertura di Meta/Klaviyo nelle newsletter è dentro.

---

## 9. Vie di implementazione: cosa manda ciascuna

| Via | Lato browser | Lato server | Note operative |
|---|---|---|---|
| **GTM web + GTM server (Stape)** | Tag Pixel nel web container con `eventID` | **Conversions API Tag** di `facebookincubator` (ufficiale Meta) o **Facebook Conversions API** di Stape | La via che dà il controllo pieno: `event_id` generato una volta per push, `fbp`/`fbc` dal dominio proprio, hashing fatto dal tag |
| **CAPI Gateway** | Pixel esistente, configurato a inviare anche al Gateway | Gateway **self-hosted su AWS EKS, AWS ECS Express o GCP**, nel cloud del cliente | "Senza sviluppatori": specchia gli eventi del Pixel, `event_id` generato e propagato da solo, costo = risorse cloud; multi-dominio e multi-Pixel ([gateway](https://developers.facebook.com/documentation/ads-commerce/gateway-products/conversions-api-gateway)) |
| **CAPI abilitata da Meta (15/04/2026)** | Pixel | Meta replica il browser | Sez. 1: non recupera niente che il browser non ha mandato |
| **Meta for WooCommerce** (ufficiale) | Pixel del plugin | CAPI "out of the box", deduplica su `event_id` | La pagina di documentazione su WooCommerce.com avvisa che il prodotto "non è più disponibile su WooCommerce.com" e la doc non verrà aggiornata ([doc](https://woocommerce.com/document/facebook-for-woocommerce/)); [DA VERIFICARE] distribuzione via wordpress.org e lista esatta degli eventi inviati |
| **Shopify, canale Facebook & Instagram** | Pixel | CAPI ai livelli *Avanzato* e *Massimo* | Livelli: **Standard** = solo Pixel; **Avanzato** = Pixel + CAPI con dati personali (nome, email, telefono, località); **Massimo** = come Avanzato + "ultima tecnologia" Meta. Eventi: PageView, ViewContent, Search, AddToCart, InitiateCheckout, AddPaymentInfo, Purchase; il valore è **il totale ordine, tasse, dazi e sconti compresi** ([Shopify](https://help.shopify.com/en/manual/promoting-marketing/analyze-marketing/meta-data-sharing)) |
| **PrestaShop, modulo ufficiale "PrestaShop Facebook"** | Pixel | [DA VERIFICARE] | Pagina [922442221236307](https://www.facebook.com/business/help/922442221236307) non leggibile; i moduli di terzi (mypresta, prestahouse) mandano Purchase via CAPI con logiche proprie: si legge la doc del modulo installato prima di aggiungere GTM |

Regole trasversali:

- 🔴 **Una via sola per il Pixel e una via sola per la CAPI.** Plugin WooCommerce/Shopify **più** GTM con lo stesso ID è la prima causa di acquisti doppi. Se si sceglie GTM, il Pixel del plugin si spegne (o si toglie l'ID); se si tiene il plugin, in GTM non c'è alcun tag Meta. Stape lo scrive per i suoi plugin: "make sure you are not using any other plugins that insert GTM script" ([Stape WordPress](https://stape.io/blog/facebook-conversion-api-for-wordpress)).
- **Il tag ufficiale Meta per GTM server** mappa da solo gli eventi GA4 (`purchase`→`Purchase`, `add_to_cart`→`AddToCart`, `page_view`→`PageView`), richiede `action_source = website` e ha il campo Test Event Code da **svuotare prima di pubblicare** ([gtm-server-side](https://developers.facebook.com/docs/marketing-api/conversions-api/guides/gtm-server-side)). Il tag Stape ha due modi: **Inherit from client** (mappa i GA4 sugli standard, ricade su custom se non trova) e **Override** ("the preferred way, even though it's more complex"); campi Pixel ID, token, Action Source, Test ID, generazione `_fbp` ([Stape](https://stape.io/helpdesk/documentation/how-to-set-up-meta-conversions-api)).
- **Token di accesso**: si genera in Gestione eventi > Impostazioni > Conversions API; è un segreto, sta nel container server e mai nel web container o nel sorgente. Su un dataset ereditato si rigenera quando l'agenzia precedente esce.
- **Signals Gateway** è il successore in spirito del CAPI Gateway, con ambizioni più ampie; [DA VERIFICARE] su fonte Meta ([jonloomer](https://www.jonloomer.com/qvt/signals-gateway/), HTTP 403 via fetch). Per una PMI italiana la scelta resta fra GTM server su Stape e la CAPI del plugin.

---

## 10. Versioni Marketing API

- 🔴 **Marketing API v24.0 scade il 06/10/2026** ([Graph API changelog](https://developers.facebook.com/docs/graph-api/changelog/)); v25.0 dal 18/02/2026 e v26.0 dal 29/07/2026 con scadenza "TBD". Le chiamate CAPI pinnate a `graph.facebook.com/v24.0/` vanno portate a v26 prima di ottobre; stessa data in `meta-ads-performance` sez. 4. Le versioni Graph API hanno date diverse (v24 Graph fino al 18/02/2028): non confondere le due tabelle.
- Il tag Stape e il tag ufficiale Meta scelgono la versione da soli: si aggiornano i **template** dalla Galleria; il codice fatto in casa (plugin custom, script PHP) è quello che resta indietro.

---

## 11. Guasti tipici, dal più costoso

1. **Purchase doppio**: Pixel e server senza `event_id` uguale, oppure con `event_id` uguale e nome diverso (`purchase`/`Purchase`), oppure Pixel installato due volte (tema + plugin, plugin + GTM). Sintomo: Diagnostica "eventi duplicati", ROAS del pannello doppio di quello del gestionale. Verifica: Testa gli eventi con un ordine di prova e `test_event_code`, poi si conta.
2. **`value` senza `currency`, o valore stringa** (`"1.234,50"`): Diagnostica lo segnala, ottimizzazione sul valore cieca. Si usa il totale ordine numerico con il punto; scelta dichiarata e costante su imponibile/IVA/spedizione, la stessa per Pixel e server.
3. **Eventi prima del consenso**: `_fbp` presente in DevTools prima del clic sul banner. Causa: Pixel nel tema o nel plugin, fuori dal CMP; o `revoke` mancante.
4. **`content_ids` diversi dal catalogo**: retargeting dinamico che mostra prodotti sbagliati. Confronto a campione fra `content_ids` dell'evento e colonna `id` del feed.
5. **`test_event_code` in produzione** (sez. 6).
6. **Hashing sbagliato** (sez. 3): EMQ bassa nonostante email e telefono "inviati".
7. **Evento fermo da settimane** dopo un restyling: Panoramica lo mostra a zero, nessuno guarda. Si mette un promemoria mensile su Panoramica.
8. **Token scaduto o revocato**: gli eventi server spariscono di colpo, il browser continua; Cronologia dice quando.

---

## 12. Igiene di un dataset ereditato: ordine di controllo

1. **Chi possiede il dataset** (Business, non account personale) e chi ha i permessi; token attivi in Cronologia.
2. **Quante volte è installato il Pixel**: sorgente pagina, richieste di rete a `facebook.com/tr`, Meta Pixel Helper; tema, plugin, GTM.
3. **Metodo di collegamento** per evento in Panoramica: Browser, Server, Browser e server; e **da dove** arriva il server (plugin, sGTM, Gateway, CAPI abilitata da Meta).
4. **Diagnostica**: duplicati, parametri mancanti, eventi senza `event_id`.
5. **Purchase**: `value`, `currency`, `content_ids` = feed, `event_id` = numero ordine su entrambi i lati.
6. **EMQ** per evento e parametri a 0%; Advanced Matching automatico acceso o spento, e perché.
7. **Consenso**: cookie prima del banner, `revoke`/`grant`, tag CAPI condizionato.
8. **Pixel con AI**: acceso? cosa aggiunge? (sez. 1).
9. **`test_event_code`** vuoto nella versione pubblicata; LDU spento.
10. **Versione API** del codice fatto in casa (sez. 10); verifica del dominio fatta.
11. **Conversioni personalizzate**: quante delle 100 sono usate, quante puntano a URL che non esistono più.

---

## 13. Meccanica del pannello (da verificare a mano)

- In Panoramica, gli eventi server generati dalla **CAPI abilitata da Meta** hanno un'etichetta diversa da quelli del container server, o compaiono come *Browser e server* senza distinzione?
- In **Impostazioni**, il toggle del Pixel con AI dove sta, e spegnendolo gli eventi già arricchiti restano tali nei report?
- In **Testa gli eventi**, dopo quanti minuti di inattività il codice `TEST...` cambia, e un evento server con codice scaduto compare comunque in Panoramica?
- La pagina 765081237991954 sull'EMQ, letta in un browser autenticato, riporta le fasce Scarso/OK/Buono/Ottimo con gli stessi numeri delle fonti terze?
- Nel dettaglio EMQ di un evento, la percentuale per parametro si riferisce agli eventi **ricevuti** o a quelli **abbinati**?
- Il modulo ufficiale PrestaShop manda eventi server e con quale `event_id`?

---

## 14. Cosa non fare mai

- Attivare la CAPI (plugin, Gateway, un clic) **senza prima verificare `event_id` e `event_name` sul Pixel**: si raddoppiano gli acquisti dal primo minuto.
- Mandare un `Purchase` senza `currency`, o con `value` stringa.
- Hashare `fbp`, `fbc`, IP o user agent; mandare email o telefono non normalizzati.
- Testare un acquisto sul dataset del cliente **senza `test_event_code`** e senza un ordine di prova riconoscibile.
- Pubblicare un container con `test_event_code` o Test ID compilato.
- Usare LDU su un sito italiano come misura di conformità.
- Lasciare il Pixel nel tema "perché tanto c'è anche in GTM".
- Mandare un lead da CRM con `action_source: website`.
- Caricare eventi con `event_time` più vecchio di 7 giorni in un batch: cade tutto il batch.
- Dichiarare "Browser e server" come CAPI a posto senza sapere da dove arriva il lato server.

---

## Fonti (verificate 20/09/2026)

**Ufficiali Meta, lette (developers.facebook.com):** [Parametri CAPI](https://developers.facebook.com/docs/marketing-api/conversions-api/parameters) · [Evento server: event_time 7 giorni, action_source](https://developers.facebook.com/docs/marketing-api/conversions-api/parameters/server-event) · [Customer information parameters e hashing](https://developers.facebook.com/docs/marketing-api/conversions-api/parameters/customer-information-parameters) (anche al nuovo URL `documentation/ads-commerce/conversions-api/parameters/customer-information-parameters`) · [Deduplica Pixel e server](https://developers.facebook.com/docs/marketing-api/conversions-api/deduplicate-pixel-and-server-events) · [fbp e fbc](https://developers.facebook.com/docs/marketing-api/conversions-api/parameters/fbp-and-fbc) · [Using the API: batch 1.000, test_event_code](https://developers.facebook.com/docs/marketing-api/conversions-api/using-the-api) · [End-to-end: freschezza 1 ora](https://developers.facebook.com/docs/marketing-api/conversions-api/guides/end-to-end-implementation) · [Best practices: EMQ](https://developers.facebook.com/docs/marketing-api/conversions-api/best-practices) · [CAPI Tag per GTM server](https://developers.facebook.com/docs/marketing-api/conversions-api/guides/gtm-server-side) · [Offline events: 62 giorni](https://developers.facebook.com/documentation/ads-commerce/conversions-api/offline-events) · [App events](https://developers.facebook.com/documentation/ads-commerce/conversions-api/app-events) · [CAPI Gateway](https://developers.facebook.com/documentation/ads-commerce/gateway-products/conversions-api-gateway) · [Riferimento Pixel: eventi standard](https://developers.facebook.com/docs/meta-pixel/reference) · [Conversion tracking: custom events 50 caratteri, 100 conversioni personalizzate](https://developers.facebook.com/docs/meta-pixel/implementation/conversion-tracking) · [Get started](https://developers.facebook.com/docs/meta-pixel/get-started) · [Advanced Matching](https://developers.facebook.com/docs/meta-pixel/advanced/advanced-matching) · [GDPR: fbq consent](https://developers.facebook.com/docs/meta-pixel/implementation/gdpr) · [Data processing options (LDU)](https://developers.facebook.com/docs/marketing-apis/data-processing-options) · [Graph API changelog: v24 fino al 06/10/2026](https://developers.facebook.com/docs/graph-api/changelog/) · [Business Tools Terms](https://www.facebook.com/legal/technology_terms) · [Annuncio 15/04/2026: Pixel con AI e CAPI a un clic](https://www.facebook.com/business/news/pixel-conversionsapi-updates).

**Ufficiali Meta, non leggibili via fetch il 20/09/2026, da ricontrollare a mano (solo titolo o errore):** [EMQ 765081237991954](https://www.facebook.com/business/help/765081237991954) · [Verifica dominio 286768115176155](https://www.facebook.com/business/help/286768115176155) · [Dataset 750785952855662](https://www.facebook.com/business/help/750785952855662) · [Installazione Pixel 952192354843755](https://www.facebook.com/business/help/952192354843755) · [AEM 721422165168355](https://www.facebook.com/business/help/721422165168355) · [Business Tools e dati 348535683460989](https://www.facebook.com/business/help/348535683460989) · [Testa gli eventi server 1624255387706033](https://www.facebook.com/business/help/1624255387706033) · [Testa gli eventi web/app 2040882565969969](https://www.facebook.com/business/help/2040882565969969) · [Advanced Matching automatico 1993001664341800](https://www.facebook.com/business/help/1993001664341800) · [Advanced Matching web 611774685654668](https://www.facebook.com/business/help/611774685654668) · [PrestaShop 922442221236307](https://www.facebook.com/business/help/922442221236307) · developers: `conversions-api/conversions-api-gateway`, `conversions-api/payload-helper` (senza la parte Test Events), `conversions-api/app-events-via-conversions-api`, `documentation/ads-commerce/conversions-api/event-match-quality` (troncata): 404 o vuote.

**Piattaforme e fornitori, lette:** [Shopify: livelli di condivisione dati](https://help.shopify.com/en/manual/promoting-marketing/analyze-marketing/meta-data-sharing) · [Meta for WooCommerce (doc non più aggiornata)](https://woocommerce.com/document/facebook-for-woocommerce/) · [Stape: tag Facebook Conversions API](https://stape.io/helpdesk/documentation/how-to-set-up-meta-conversions-api) · [Stape: CAPI su WordPress](https://stape.io/blog/facebook-conversion-api-for-wordpress) · [Garante: provvedimento 284 del 17/04/2026](https://www.garanteprivacy.it/home/docweb/-/docweb-display/docweb/10241943).

**Terze parti (pratica e soglie empiriche, non numeri Meta):** [EMQ fasce (customerlabs)](https://www.customerlabs.com/blog/improve-your-event-match-quality-from-ok-to-great/) · [EMQ (triplewhale)](https://www.triplewhale.com/blog/event-match-quality) · [EMQ 6 buono (conversios, 26/03/2026)](https://www.conversios.io/blog/meta-attribution-window-changes-2026-fix-your-tracking/) · [Pixel AI e CAPI a un clic (segwise)](https://segwise.ai/blog/meta-pixel-conversions-api-ai-updates-2026) · [CAPI a un clic, limiti (weltpixel)](https://weltpixel.com/blogs/news/metas-one-click-conversions-api-what-it-does-and-what-it-leaves-out) · [AEM 15/05/2023 (adviso)](https://www.adviso.ca/en/blog/evolution-aggregated-measurement-meta) · [AEM, riserva iOS, verifica dominio (segwise, agg. 03/09/2026)](https://segwise.ai/blog/facebook-aggregated-event-measurement) · [AEM e dominio (conversios)](https://www.conversios.io/blog/meta-aggregated-event-measurement/) · [Dataset (theadspend)](https://theadspend.com/blog/meta-ads-conversion-tracking) · [Dataset (leadsie)](https://www.leadsie.com/blog/all-you-need-to-know-about-facebook-metas-new-datasets) · [Gestione eventi, tab (adsuploader)](https://adsuploader.com/blog/meta-events-manager) · [Eventi standard e Diagnostica (adsuploader)](https://adsuploader.com/blog/meta-pixel-standard-events) · [Test events 24 ore (anytrack)](https://readme.anytrack.io/docs/meta-capi-test-mode) · [Advanced Matching limiti (adnabu)](https://blog.adnabu.com/shopify/advanced-matching-in-facebook-pixel/) · [Signals Gateway (jonloomer; 403 via fetch)](https://www.jonloomer.com/qvt/signals-gateway/).
