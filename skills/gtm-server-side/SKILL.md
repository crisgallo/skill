---
name: "gtm-server-side"
description: "Regole operative verificate per montare, controllare e riparare il tracciamento con Google Tag Manager, container web e container server (Stape o Google Cloud): dataLayer ed eventi e-commerce GA4, tag Google e tag evento GA4, attivatori che sparano doppio, Anteprima e Tag Assistant, versioni e permessi, consenso dentro GTM, dominio personalizzato, client GA4, cookie FPID, Meta Conversions API con event_id, piani e limiti Stape, costi. Usala ogni volta che si tocca un container GTM, si installa il server-side, si sposta un pixel sul server, si eredita un container altrui o un numero in GA4 o Meta non torna."
---

# Google Tag Manager, web e server-side: regole operative

**Ultima verifica delle fonti: 20 settembre 2026.**

---

## 0. Manutenzione di questa skill (leggere per primo)

1. **Finestra di freschezza: due mesi.** Google ha cambiato interfaccia e modello dei container il 20/08/2026 (sez. 9) e Stape rivede prezzi e limiti senza preavviso: se la data qui sopra ha più di due mesi, si rileggono release notes e pagina prezzi prima di citare un numero a un cliente.
2. **Quando una fonte smentisce una regola scritta qui, la skill si aggiorna nello stesso turno**, si riscrive la data in cima e si annota cosa è cambiato e da quando.
3. Due metà da tenere distinte: **conoscenza di dominio** (come si comportano GTM, GA4, Meta: si verifica sulle fonti ufficiali) e **meccanica del pannello** (sez. 12: si impara sbagliando, si scrive qui la prima volta). Nulla in questa skill è marcato VERIFICATO sul pannello: è la prima stesura.
4. Dove si guardano i cambiamenti: [Release notes GTM (4620708)](https://support.google.com/tagmanager/answer/4620708?hl=en), [Annunci GTM](https://support.google.com/tagmanager/announcements/15205707?hl=en), [Stape news](https://stape.io/news), [Stape pricing](https://stape.io/price), [Meta CAPI changelog](https://developers.facebook.com/docs/marketing-api/conversions-api).
5. ⚠️ Le regole con soglie numeriche di terzi sono etichettate "regola empirica di terzi, non numero Google/Stape/Meta". Le voci **[DA VERIFICARE]** non si citano a un cliente.

---

## 1. La regola che costa di più: un solo punto di ingresso per ogni ID

**Ogni ID di misurazione (G-, AW-, Pixel Meta) deve essere inizializzato una sola volta per pagina, da un solo posto.** Se lo stesso `G-XXXX` è nel tema, in un plugin (Site Kit, plugin WooCommerce/Shopify) e nel container GTM, ogni evento arriva doppio e nessun report lo dice: sessioni gonfie, tassi di conversione dimezzati, `purchase` doppie. È il primo controllo su ogni sito ereditato, prima di aprire il container ([Tag Diagnostics (14681508)](https://support.google.com/tagmanager/answer/14681508?hl=en) segnala le installazioni multiple; la verifica manuale è cercare `G-` e `gtag(` nel sorgente e nelle richieste di rete).

- **Un solo tag Google per container**, con attivatore **Initialization - All Pages** ([15756616](https://support.google.com/tagmanager/answer/15756616?hl=en)). I tag evento GA4 riusano il Measurement ID e ereditano le impostazioni dal tag Google ([13543899](https://support.google.com/tagmanager/answer/13543899?hl=en)).
- **Il Measurement ID sta in una variabile Costante**, e tutti i tag la referenziano. Non si scrive l'ID a mano in ogni tag e non si usa una tabella di ricerca sull'hostname che, su un dominio non previsto (staging, dominio di test del cliente), restituisce `undefined` e manda i dati nel vuoto senza errore.
- 🔴 **Dal 09/07/2026 il prefisso dell'ID decide cosa può fare il container.** Un container caricato con `GTM-XXXX` esegue tutto; caricato con `G-XXXX` o `AW-XXXX` esegue **solo tag e variabili forniti da Google** (niente HTML personalizzato, niente Meta Pixel). Chi ha installato lo snippet con un percorso non standard o un ID prodotto se lo trova "ristretto" ([Release notes 09/07/2026](https://support.google.com/tagmanager/answer/4620708?hl=en), [17070049](https://support.google.com/tagmanager/answer/17070049?hl=en)).

---

## 2. dataLayer: il push viene prima del tag, sempre

- `window.dataLayer = window.dataLayer || [];` **sopra lo snippet del container**. Si usa solo `.push()`: l'assegnazione `dataLayer = [...]` dopo il caricamento cancella tutto. Il nome è **case-sensitive** (`datalayer` non esiste) e le chiavi devono essere identiche su tutte le pagine ([datalayer](https://developers.google.com/tag-platform/tag-manager/datalayer)).
- **Un push fatto dopo che il tag ha già sparato non viene visto dal tag.** Se il dato serve al `page_view`, va nel dataLayer prima dello snippet; se arriva dopo (AJAX, checkout dinamico), si spinge **con una chiave `event`** e il tag usa un attivatore **Evento personalizzato**, non Visualizzazione di pagina ([datalayer](https://developers.google.com/tag-platform/tag-manager/datalayer)).
- **E-commerce secondo lo schema GA4 consigliato**, nomi esatti: `view_item_list`, `select_item`, `view_item`, `add_to_cart`, `remove_from_cart`, `view_cart`, `begin_checkout`, `add_shipping_info`, `add_payment_info`, `purchase`, `refund`, `view_promotion`, `select_promotion`, `add_to_wishlist`. L'array `items` è obbligatorio, ogni item ha **`item_id` o `item_name`**; `value` va sempre con `currency` (per l'Italia `EUR`, importo con punto decimale, IVA inclusa o esclusa ma sempre uguale); `purchase` e `refund` hanno `transaction_id` ([ecommerce](https://developers.google.com/analytics/devguides/collection/ga4/ecommerce?client_type=gtm)).
- ⚠️ **`dataLayer.push({ ecommerce: null })` prima di ogni push e-commerce.** Senza, gli `items` dell'evento precedente restano dentro e il `purchase` porta con sé gli articoli del `view_item` di due pagine fa ([ecommerce](https://developers.google.com/analytics/devguides/collection/ga4/ecommerce?client_type=gtm)).
- Nel tag evento GA4 i dati e-commerce si leggono con **Altre impostazioni > E-commerce > Invia dati e-commerce, origine Data Layer**; non si ricostruisce `items` a mano con variabili.
- ⚠️ **La pagina di ringraziamento ricaricata rispinge il `purchase`.** `transaction_id` aiuta GA4 a riconoscere il doppione, ma la regola è che il push del `purchase` sia generato **una volta sola** dal sistema (flag server-side o cookie di "già inviato"), non dal template della pagina.

---

## 3. Attivatori e variabili che sparano doppio

Ordine di esecuzione degli attivatori di pagina: **Consent Initialization → Initialization → Page View → DOM Ready → Window Loaded** ([7679319](https://support.google.com/tagmanager/answer/7679319?hl=en)). Le cause di doppio colpo, nell'ordine in cui si incontrano:

1. **ID inizializzato due volte** (sez. 1).
2. **`page_view` dal tag Google + un tag evento `page_view`**, oppure tag Google con "Invia un evento di visualizzazione di pagina" e **attivatore History Change** su un sito che non è una SPA: due `page_view` a ogni cambio di URL.
3. **Misurazione avanzata in GA4 + tag GTM per la stessa azione** (form, scroll, clic esterni, modifiche pagina basate sulla cronologia). Si spegne la voce in GA4 o non si crea il tag; mai entrambi (vedi skill `ga4-performance`).
4. **Attivatore Clic - Tutti gli elementi** su elementi annidati (icona dentro il pulsante): un clic, due eventi. Si usa **Clic - Solo link** o una condizione su `Click Element matches CSS selector`.
5. **Evento personalizzato con regex larga** (`.*checkout.*`) che intercetta più push di quanto si pensi. Si preferisce il nome esatto.
6. **Container server acceso e tag GA4 web ancora diretti**: il tag web manda al server (che rimanda a Google) e un secondo tag web manda a Google direttamente. Un solo tag GA4 web, con `server_container_url` (sez. 6).
7. **Meta Pixel web + Conversions API server senza lo stesso `event_id`** (sez. 8).

Il posto dove si vede il doppio colpo è **DebugView**: due righe uguali nello stesso secondo (sez. 10).

---

## 4. Anteprima, Tag Assistant e come i colpi di debug arrivano in produzione

- L'Anteprima si apre da **Anteprima** nell'area di lavoro, si inserisce l'URL del sito e Tag Assistant apre il sito "Connesso". Il pannello di debug si vede solo nel browser che l'ha attivata o da chi riceve il link **Altre azioni > Condividi** ([6107056](https://support.google.com/tagmanager/answer/6107056?hl=en)).
- 🔴 **In Anteprima i tag sparano davvero.** Tag Assistant aggiunge alla pagina un parametro di debug che "aiuta a vedere gli eventi in altre superfici di debug, come DebugView di Google Analytics" ([10039345](https://support.google.com/tagmanager/answer/10039345?hl=en), [7201382](https://support.google.com/analytics/answer/7201382?hl=en)): i colpi finiscono nella proprietà GA4 reale, nei report reali, e le conversioni di test finiscono in Google Ads e in Meta. Le pagine ufficiali non lo dicono con questa frase, ma è la conseguenza del meccanismo. Quindi: **filtro traffico interno attivo in GA4 prima di iniziare a testare**, mai un `purchase` di prova su Meta senza `test_event_code` (sez. 8), mai un test sulla proprietà del cliente il giorno prima di un report.
- Se il parametro di debug rompe il sito (checkout che rigetta l'URL), si deseleziona **Includi segnale di debug nell'URL** nel dominio dell'Anteprima ([10039345](https://support.google.com/tagmanager/answer/10039345?hl=en)).
- **Anteprima del container server**: pulsante Anteprima sul container server; il pannello sinistro elenca le richieste HTTP in arrivo (`collect?v=2&...`) e sotto ogni richiesta gli eventi creati dal client; le schede **Tags** (sparato / fallito e quante volte), **Variables**, **Event Data**, **Console** (errori dei tag). Un tag che "fallisce" qui fallisce anche in produzione, in silenzio ([debug](https://developers.google.com/tag-platform/tag-manager/server-side/debug)).
- Un container nuovo ha già una versione iniziale, quindi l'Anteprima funziona subito; su un container vecchio senza versioni pubblicate l'Anteprima non si connette ([Release notes](https://support.google.com/tagmanager/answer/4620708?hl=en)).

---

## 5. Aree di lavoro, versioni, pubblicazione, rollback, permessi

- **Container standard: 3 aree di lavoro** (predefinita + 2); illimitate solo in Tag Manager 360 ([7059647](https://support.google.com/tagmanager/answer/7059647?hl=en)). Con un'agenzia che lavora sullo stesso container, le due aree si esauriscono in un pomeriggio: si pubblica e si chiude, non si lasciano aree aperte per settimane.
- Ogni container ha **un solo flusso di versioni**; quando qualcuno pubblica, le altre aree si segnano "non aggiornate" e vanno sincronizzate con **Aggiorna area di lavoro**; i conflitti si risolvono a mano (blu modificato, rosso mancante qui, verde mancante là) ([7059647](https://support.google.com/tagmanager/answer/7059647?hl=en)).
- **Invia > Pubblica e crea versione** con **nome e descrizione sempre compilati** (cosa, dove, perché). **Invia > Crea versione** salva senza pubblicare ([6107163](https://support.google.com/tagmanager/answer/6107163?hl=en)).
- **Rollback**: Versioni > azioni sulla versione precedente > **Pubblica**, oppure **Imposta come versione più recente** per ricaricarla nella bozza e correggerla prima di pubblicare. La cronologia di pubblicazione dice chi ha pubblicato cosa e quando ([6107163](https://support.google.com/tagmanager/answer/6107163?hl=en)).
- **Il flusso di approvazione esiste solo in Tag Manager 360** ([6107163](https://support.google.com/tagmanager/answer/6107163?hl=en)): sul container standard il controllo è solo nei permessi.
- **Permessi**: account **Utente / Amministratore**; container **Nessun accesso / Lettura / Modifica / Approvazione / Pubblicazione**. Modifica crea aree e modifica ma non crea versioni né pubblica; Approvazione crea versioni ma non pubblica; Pubblicazione fa tutto ([6107011](https://support.google.com/tagmanager/answer/6107011?hl=en)). Il cliente è **Amministratore dell'account** (è suo); l'agenzia e lo sviluppatore del tema hanno **Modifica** sul container; **Pubblicazione** solo chi risponde del dato. Il container non si crea mai sull'account del consulente.
- Le note su tag, attivatori e variabili esistono (API v2 e interfaccia): ogni tag creato porta una nota con data e motivo ([Release notes](https://support.google.com/tagmanager/answer/4620708?hl=en)).

---

## 6. Consenso dentro GTM (Italia)

- **Contesto italiano**: Linee guida cookie del Garante, provv. n. 231 del 10/06/2021: consenso preventivo per i cookie non tecnici, lo scroll non è consenso, banner con **X** per chiudere senza acconsentire, riproposizione non prima di **6 mesi**; i cookie analytics sono equiparati ai tecnici solo con IP mascherato almeno nell'ultimo ottetto, statistiche aggregate e nessun incrocio con altri dati ([Garante 9677876](https://www.garanteprivacy.it/web/guest/home/docweb/-/docweb-display/docweb/9677876)). GA4 e i pixel pubblicitari non rientrano nell'equiparazione: **si caricano dopo il consenso o in Consent Mode con default negato**.
- **Attivatore Consent Initialization - All Pages** per il tag della CMP (Iubenda, Cookiebot, CookieYes): "sparerà sempre prima di tutti gli altri tag, compresi gli Initialization" ([10718549](https://support.google.com/tagmanager/answer/10718549?hl=en), [7679319](https://support.google.com/tagmanager/answer/7679319?hl=en)). Il default consent (`denied` per `ad_storage`, `analytics_storage`, `ad_user_data`, `ad_personalization`) deve essere impostato lì, per regione (EEA), non per tutti i visitatori ([9976101](https://support.google.com/analytics/answer/9976101?hl=en)).
- **Tag Google (GA4, Ads, Floodlight) hanno i controlli di consenso integrati**: con `analytics_storage` negato in modalità avanzata mandano ping senza cookie usati per la modellazione; in modalità base restano bloccati fino al consenso e non c'è modellazione ([10718549](https://support.google.com/tagmanager/answer/10718549?hl=en), [9976101](https://support.google.com/analytics/answer/9976101?hl=en)).
- **Tag non Google (Meta Pixel, HTML personalizzato, TikTok) non sanno nulla del consenso**: si imposta **Impostazioni consenso > Richiedi consenso aggiuntivo** (`ad_storage`, e `ad_user_data` per i pixel pubblicitari) su ognuno. **Amministrazione > Impostazioni contenitore > Abilita panoramica consenso** mostra in un colpo quali tag sono "Consenso non configurato" ([10718549](https://support.google.com/tagmanager/answer/10718549?hl=en)).
- **Nel container server il consenso non si configura**: arriva dal tag Google del web container come parametri della richiesta e i tag Google server-side lo rispettano da soli ([consent-mode sGTM](https://developers.google.com/tag-platform/tag-manager/server-side/consent-mode)). ⚠️ I tag server non Google (Meta CAPI) **non hanno controlli integrati**: si aggiunge una condizione sull'attivatore server che legge lo stato del consenso dai dati evento (regola operativa; la pagina ufficiale non copre i tag di terzi).
- [DA VERIFICARE] la pagina ufficiale della policy Google sul consenso UE (Consent Mode obbligatorio per le funzioni pubblicitarie in EEA da marzo 2024): non riletta in questa stesura, la regola "default negato in EEA" vale comunque per il Garante.

---

## 7. Container server: cos'è, dominio proprio, client GA4, cookie

- **Cos'è**: un container che gira "su un server che controlli tu"; il browser manda i dati al tuo endpoint, lì i **client** intercettano le richieste e le trasformano in eventi, i **tag** li spediscono a GA4, Ads, Meta. Si controlla cosa parte e verso chi ([intro](https://developers.google.com/tag-platform/tag-manager/server-side/intro)). Non riduce le richieste dal browser: le sposta.
- 🔴 **Senza dominio proprio il server container non serve quasi a niente.** Sull'endpoint predefinito (`*.run.app` o il dominio Stape) il tagging server è in contesto di terze parti e "può impostare solo cookie JavaScript". Le tre opzioni ufficiali: **stessa origine con percorso** (`www.sito.it/metrics`, la migliore, via CDN o load balancer), **sottodominio** (`metrics.sito.it`, record DNS), **dominio predefinito** (nessun cookie server-set) ([custom-domain](https://developers.google.com/tag-platform/tag-manager/server-side/custom-domain)).
- **Nome del sottodominio**: Stape dice di **evitare** `gtm`, `sgtm`, `tracking`, `analytics`, `metrics`, `ad`, `gtag`, `stape` (finiscono nelle liste degli ad blocker); si usa un nome neutro (`data`, `stats`, `srv`). CNAME con proxy Cloudflare **spento**; due CNAME se si usa la CDN Stape; A/AAAA incompatibili con la CDN; verifica in 2-3 ore, fino a 72 ([add-custom-domain](https://stape.io/helpdesk/documentation/add-custom-domain-in-stape)).
- **Client GA4**: fa da proxy sia per la libreria (`/gtag/js?id=G-...` via "Default gtag.js paths for specific IDs") sia per gli eventi; nel web container si aggiunge al tag Google, in **Impostazioni di configurazione**, il parametro **`server_container_url`** = URL del tagging server ([send-data](https://developers.google.com/tag-platform/tag-manager/server-side/send-data), [sst-fundamentals 5](https://developers.google.com/tag-platform/learn/sst-fundamentals/5-sst-setup-analytics), [15756616](https://support.google.com/tagmanager/answer/15756616?hl=en)). `transport_url` è il nome della vecchia implementazione Universal Analytics: su un container ereditato indica un setup mai migrato.
- **Il server container va nella CSP e nell'X-Frame-Options del sito**: `img-src` e `connect-src` con l'URL del server; il trasporto via service worker richiede che gli iframe dal dominio server non siano bloccati ([send-data](https://developers.google.com/tag-platform/tag-manager/server-side/send-data)).
- **Cookie**: nel client GA4 l'identificazione è **JavaScript Managed** (cookie `_ga` letto dalla richiesta) o **Server Managed** (cookie impostato dal server). Google: "JavaScript Managed è l'unico metodo che funziona finché non cambi le impostazioni del dominio" ([sst-fundamentals 5](https://developers.google.com/tag-platform/learn/sst-fundamentals/5-sst-setup-analytics)). Con dominio proprio si può passare a Server Managed: il cookie si chiama **FPID**, è **HttpOnly** (invisibile al JavaScript e agli script del tema) e il client lo preferisce al `cid` della richiesta (dettagli da [Simo Ahava](https://www.simoahava.com/analytics/fpid-cookie-google-analytics-server-side-tagging/), fonte terza: la pagina ufficiale del client GA4 non era leggibile). ⚠️ Il passaggio da `_ga` a FPID rinnova l'identità degli utenti di ritorno: si fa una volta, si data, e si spiega il gradino di "nuovi utenti".
- **Consent Mode nel server**: solo con dominio proprio e "impostazioni regionali" attive sul tagging server per la modalità avanzata ([consent-mode sGTM](https://developers.google.com/tag-platform/tag-manager/server-side/consent-mode)).

---

## 8. Meta Conversions API dal server e deduplica con event_id

- Il tag ufficiale è **Conversions API Tag** di `facebookincubator` nella Galleria modelli, scritto e mantenuto da Meta; serve **Pixel ID, token di accesso** (generato in Gestione eventi) e `action_source = website` ([gtm-server-side](https://developers.facebook.com/docs/marketing-api/conversions-api/guides/gtm-server-side)). Stape mantiene il proprio **Facebook Conversions API** (Galleria e GitHub) con la modalità **Override** (eventi mappati a mano, preferita) o **Inherit from client** (mappa gli eventi GA4 sugli standard Meta) ([Stape Meta CAPI](https://stape.io/helpdesk/documentation/how-to-set-up-meta-conversions-api)).
- 🔴 **Deduplica: stesso `event_name` e stesso `event_id` sul Pixel web (`eventID`, quarto parametro di `fbq('track', ...)`) e sul tag server (`event_id`).** Meta deduplica solo se il secondo evento arriva **entro 48 ore** dal primo e tiene di norma il primo ricevuto; il metodo alternativo `fbp`/`external_id` funziona solo browser-prima-server e **non scarta il server se il browser non è arrivato** ([deduplicate](https://developers.facebook.com/docs/marketing-api/conversions-api/deduplicate-pixel-and-server-events)). Senza `event_id`, ogni acquisto vale due: il ROAS del pannello Meta raddoppia ed è falso (vedi skill `meta-ads-performance`).
- L'`event_id` si genera **nel web container una volta per push** (variabile Unique Event ID di Stape o un `transaction_id` per il `purchase`) e viaggia sia nel Pixel sia nella richiesta GA4 al server; il tag CAPI lo legge dai dati evento ([unique-event-id](https://stape.io/helpdesk/documentation/unique-event-id)).
- **`fbp` e `fbc`** arrivano da soli se il server è sul dominio proprio; sull'endpoint predefinito vanno passati come variabili Cookie di prima parte dal web container ([gtm-server-side](https://developers.facebook.com/docs/marketing-api/conversions-api/guides/gtm-server-side)). Email e telefono si mandano **hashati SHA-256** e solo con consenso (sez. 6).
- 🔴 **`test_event_code` non è un ambiente di prova.** "Gli eventi inviati con test_event_code non vengono scartati: entrano in Gestione eventi e vengono usati per targeting e misurazione" ([using-the-api](https://developers.facebook.com/docs/marketing-api/conversions-api/using-the-api)). Serve solo a vederli nella scheda Eventi di prova; **si toglie prima di pubblicare** ([gtm-server-side](https://developers.facebook.com/docs/marketing-api/conversions-api/guides/gtm-server-side)).

---

## 9. Cosa ha cambiato Google fra giugno e settembre 2026

- **20/08/2026, "Updates to Google tag and Google Tag Manager"**: nuova pagina Panoramica con sezione **Impostazioni** (impostazioni del container in un posto solo) e sezione **Avanzate** a scomparsa con attivatori, variabili, modelli e cartelle; i **tag Google standalone diventano container GTM** ("non cambia il comportamento in pagina"); **tagging visuale senza codice** in beta, per ora conversioni acquisto Google Ads; i nuovi snippet **non contengono più `gtag('config')`**: si usa l'attivatore `gtm.init`. Tutto **opt-in**, nessuna modifica automatica ([17079602](https://support.google.com/tagmanager/answer/17079602?hl=en), [Stape 21/08/2026](https://stape.io/news/google-tag-gtm-updates)). Conseguenza: un container che segue questa skill (tag Google su Initialization, niente config inline) è già allineato; sui container ereditati si legge il banner di ottimizzazione prima di accettarlo.
- **09/07/2026**: il prefisso dell'ID governa le restrizioni (sez. 1). **01/07/2026**: nuova Panoramica.
- **22/06/2026**: conversioni server-to-server recuperate unendo i segnali browser quando c'è un `gclid` (Floodlight). **01/05/2026**: attribuzione migliorata per proprietà GA4 collegate a Ads sui container server, tramite "segnali browser paralleli" con **Google Signals attivo** ([Release notes](https://support.google.com/tagmanager/answer/4620708?hl=en)). Su un cliente sGTM con Ads collegato, Google Signals acceso non è più solo una scelta di privacy: pesa sull'attribuzione.
- **Google tag gateway for advertisers**: carica il tag e riceve gli eventi **dal tuo dominio**, poi inoltra a Google; **non è un server container** (nessuna trasformazione, nessun tag di terzi), Google raccomanda i due insieme. Integrazioni: Cloudflare (2025), Akamai (29/01/2026), Fastly e Akamai in GTM (14/05/2026), **Google Cloud load balancer in GA dal 01/06/2026** (solo Global external Application LB, non il classic), **Amazon CloudFront dal 03/06/2026**. L'integrazione è gratuita, si paga solo l'uso del load balancer; si attiva da **Amministrazione > Google tag gateway** ([16816376](https://support.google.com/tagmanager/answer/16816376?hl=en), [gateway](https://developers.google.com/tag-platform/tag-manager/gateway), [Release notes](https://support.google.com/tagmanager/answer/4620708?hl=en)). Per un sito italiano su Cloudflare è il primo passo, prima ancora del server container.

---

## 10. Verificare che i colpi arrivino davvero

1. **Anteprima web**: il tag risulta "Fired" e nella riga del `G-` si vede la richiesta. Non basta.
2. **Anteprima server**: la richiesta compare a sinistra, il client GA4 l'ha reclamata, la scheda Tags dice "fired" e la Console è vuota ([debug](https://developers.google.com/tag-platform/tag-manager/server-side/debug)).
3. **GA4 DebugView**: gli eventi dell'Anteprima compaiono in tempo reale grazie al parametro di debug; colonna Secondi (ultimi 60 s) e Minuti (ultimi 30 min). Se non compare niente con consenso negato, è il Consent Mode, non un guasto ([7201382](https://support.google.com/analytics/answer/7201382?hl=en)).
4. **GA4 Tempo reale**: ultimi 30 minuti, **i nuovi utenti non compaiono nelle schede di acquisizione** finché non sono elaborati, attribuzione limitata, massimo 700 righe per scheda ([9271392](https://support.google.com/analytics/answer/9271392?hl=en)). Serve per "arriva sì o no", non per "da dove".
5. **Meta Gestione eventi > Origini dati > Pixel > Eventi di prova**: l'evento deve comparire con origine **Server** e, se il Pixel web è attivo, la coppia deve risultare **deduplicata**; poi si guarda la **Qualità dell'abbinamento eventi** ([using-the-api](https://developers.facebook.com/docs/marketing-api/conversions-api/using-the-api), [Stape Meta CAPI](https://stape.io/helpdesk/documentation/how-to-set-up-meta-conversions-api)).
6. Il giorno dopo: report GA4 standard e colonna Conversioni di Ads/Meta. I punti 1-5 dicono che il colpo parte; solo i report dicono che è stato accettato.

---

## 11. Stape, Google Cloud, costi, ad blocker, ITP

- **Stape, piani sGTM (USD, prezzo pagina, 20/09/2026)**: **Free** 10K richieste/mese, con Custom Loader e CDN; **Pro** 17 $/mese (200 $/anno) 500K richieste, Cookie Keeper standard, log 3 giorni; **Business** 83 $/mese (1.000 $/anno) 5M richieste, multi-zona, Cookie Keeper personalizzato, Multi-Domains fino a 20 domini, log 10 giorni; **Enterprise** 167 $/mese (2.000 $/anno) 20M richieste, 50 domini, export log; **Custom** senza limiti ([Stape pricing](https://stape.io/price)). [DA VERIFICARE] valuta e IVA mostrate a un account italiano; il numero di partita IVA UE si inserisce nelle impostazioni di fatturazione ([how-billing-works](https://stape.io/helpdesk/documentation/how-billing-works)).
- 🔴 **Si paga a richieste, non a eventi GA4 né a sessioni.** Ogni `page_view`, scroll, `view_item`, ping di consenso e ogni evento ricevuto è una richiesta; la quota è **per container**, si azzera alla data di rinnovo (non il 1° del mese) e non si accumula. **A quota esaurita il container smette di servire il traffico fino al rinnovo**, salvo il toggle di **upgrade automatico** che sale di un livello ([how-billing-works](https://stape.io/helpdesk/documentation/how-billing-works)). Un e-commerce che a novembre sfora e non ha l'upgrade automatico perde il Black Friday in silenzio: sul container di un cliente il toggle è acceso e il cliente lo sa. La regola "5-10 richieste per pagina vista" è **empirica di terzi, non numero Stape**.
- **Zona server**: per un cliente italiano si sceglie **Stape Europe** (società registrata in Estonia, cloud Scaleway 100% UE) con zona **EU South (Italia)** o **EU Center (Francia)**; Stape Global ha 15 zone fra cui Belgio, Germania, Finlandia ([server-locations](https://stape.io/helpdesk/documentation/sgtm-server-locations-zones), [Global vs EU](https://stape.io/helpdesk/knowledgebase/what-is-the-difference-between-global-sgtm-hosting-and-eu-sgtm-hosting)). [DA VERIFICARE] se la zona si può cambiare dopo la creazione del container.
- **Power-up**: **Custom Loader** (dal piano Free) carica gtm.js e gtag.js dal dominio proprio e genera lo snippet da sostituire a quello standard: "non far girare i due loader insieme"; rigenerando lo snippet i parametri di ambiente vanno rimessi; con la protezione avanzata gli URL sono cifrati e il debug è più difficile ([custom-loader](https://stape.io/helpdesk/documentation/custom-loader-power-up)). **Cookie Keeper** (Pro per i cookie standard, Business per quelli personalizzati) riscrive la scadenza dei cookie di prima parte che Safari 16.4+ con ITP fa scadere **dopo 7 giorni**: senza, l'utente Safari che torna dopo 8 giorni è un nuovo utente e la conversione va a "diretto" ([cookie-keeper](https://stape.io/helpdesk/documentation/cookie-keeper-power-up)). **Multi-Domains** dal Business.
- **Google Cloud in proprio**: Cloud Run, 1 vCPU e 0,5 GB per istanza a CPU sempre allocata, **minimo 2 istanze**, "circa 45 $/mese per server", più **esattamente 1 preview server** senza autoscaling ([cloud-run](https://developers.google.com/tag-platform/tag-manager/server-side/cloud-run-setup-guide), [manual-setup](https://developers.google.com/tag-platform/tag-manager/server-side/manual-setup-guide)); App Engine flessibile, **minimo 3 server a ~40 $/mese**, 3-6 server reggono 50-200 richieste/s, F1 standard solo per i test ([app-engine](https://developers.google.com/tag-platform/tag-manager/server-side/app-engine-setup)). Ordine di grandezza: **90-130 $/mese** prima di log e load balancer, contro 17-83 $ su Stape; Stape stessa cita ~100 $/mese di log su GCP per 500K richieste ([Stape, 04/09/2025](https://stape.io/blog/how-much-does-server-gtm-cost), fonte Stape non Google). Google Cloud ha senso solo se il cliente ha già un team cloud o vincoli contrattuali sul fornitore.
- **Ad blocker**: bloccano `googletagmanager.com` e `google-analytics.com` per lista. Con gateway (sez. 9) o Custom Loader gli script e i colpi passano dal dominio del sito. Non è aggiramento del consenso: il Consent Mode resta quello che è, e un cookie di profilazione senza consenso resta illecito in Italia (sez. 6). Il recupero dichiarato da Google per il gateway è **"11% di segnali in più" in media sui primi tester** (fonte terza che cita Google, [ppc.land](https://ppc.land/google-tag-gateway/)); non si promette una percentuale al cliente.
- **ITP e Consent Mode insieme**: con consenso negato non c'è cookie da prolungare e i ping sono modellati; il server-side non recupera quello che l'utente ha rifiutato. Quello che recupera: cookie `_ga`/FPID che durano oltre 7 giorni su Safari (dominio proprio), script non bloccati, `fbp`/`fbc` letti dal server.

---

## 12. Igiene di un container ereditato: ordine di controllo

1. **Quante volte è inizializzato ogni ID** sul sito (tema, plugin, GTM, gateway): prima di tutto (sez. 1).
2. **Chi possiede l'account GTM** e chi ha Pubblicazione; account su e-mail personali di ex collaboratori (sez. 5).
3. **Prefisso dell'ID e percorso dello snippet** (sez. 1): container in stato ristretto dal 09/07/2026.
4. **Consenso**: tag CMP su Consent Initialization, default negato per EEA, panoramica consenso con zero "non configurati" (sez. 6).
5. **Tag Google**: uno, su Initialization, `server_container_url` presente se c'è un server container; nessun `transport_url` (sez. 7).
6. **Container server**: dominio proprio o predefinito; client GA4 JavaScript/Server Managed; zona; piano e quota Stape con upgrade automatico (sez. 7 e 11).
7. **Meta**: `event_id` sul Pixel e sul tag CAPI, `test_event_code` vuoto nella versione pubblicata (sez. 8).
8. **dataLayer e-commerce**: nomi evento, `items`, `currency`, `ecommerce: null`, `purchase` una volta sola (sez. 2).
9. **Attivatori doppi** (sez. 3) e misurazione avanzata GA4 sovrapposta ai tag.
10. **Aree di lavoro aperte** e versioni senza nome; ultima pubblicazione e da chi (sez. 5).
11. **Google tag gateway** attivo? Se il sito è su Cloudflare e non lo è, è il primo intervento (sez. 9).

---

## 13. Meccanica del pannello (da verificare a mano)

- Nella nuova Panoramica del 20/08/2026, dove sono finiti esattamente "Aree di lavoro", "Versioni" e "Amministrazione", e il banner di ottimizzazione compare su tutti i container o solo su quelli con tag Google standalone?
- Un colpo in Anteprima con "Includi segnale di debug nell'URL" disattivato compare ancora in DebugView?
- Nel client GA4 di un container su Stape, il passaggio da JavaScript Managed a Server Managed crea il cookie FPID subito sul dominio proprio, e con quale durata?
- Nel tag Facebook Conversions API di Stape in modalità Inherit from client, quale campo del dato evento GA4 viene letto come `event_id` senza configurazione?
- Nel pannello Stape, superata la quota con l'upgrade automatico spento, la dashboard mostra un avviso o il container si ferma senza notifica e-mail?
- Il filtro traffico interno di GA4 esclude anche i colpi che arrivano dal server container (IP del server invece dell'utente)?

---

## 14. Cosa non fare mai

- Mettere un `G-` a mano dentro ogni tag evento, o dedurlo da una tabella di ricerca sull'hostname.
- Testare un `purchase` in Anteprima sulla proprietà del cliente senza filtro traffico interno e senza `test_event_code` su Meta.
- Pubblicare con `test_event_code` compilato o con l'Anteprima server aperta come "ambiente di test": non esiste ambiente di test, esiste solo produzione.
- Attivare il server container sull'endpoint predefinito e dichiarare al cliente "cookie di prima parte".
- Chiamare il sottodominio `gtm.` o `tracking.`.
- Usare Custom Loader e snippet GTM standard insieme.
- Spostare il Pixel Meta sul server senza `event_id` sul web, o togliere il Pixel web pensando che il server basti.
- Lasciare il container Stape di un e-commerce senza upgrade automatico a ottobre.
- Vendere il server-side come "recupero dei dati degli utenti che hanno rifiutato": recupera Safari e ad blocker, non il consenso.
- Creare il container sull'account del consulente o dell'agenzia.
- Pubblicare versioni senza nome.
- Accettare il banner "ottimizza il container" del 20/08/2026 su un container ereditato senza leggere cosa cambia.

---

## Fonti (verificate 20/09/2026)

**Ufficiali Google, lette:** [Release notes GTM (4620708)](https://support.google.com/tagmanager/answer/4620708?hl=en) · [Updates 20/08/2026 (17079602)](https://support.google.com/tagmanager/answer/17079602?hl=en) · [Prefisso ID e restrizioni (17070049)](https://support.google.com/tagmanager/answer/17070049?hl=en) · [Tag Google in GTM (15756616)](https://support.google.com/tagmanager/answer/15756616?hl=en) · [Annuncio tag Google (13543899)](https://support.google.com/tagmanager/answer/13543899?hl=en) · [Eventi GA4 in GTM (13034206)](https://support.google.com/tagmanager/answer/13034206?hl=en) · [Tipi di attivatore (7679319)](https://support.google.com/tagmanager/answer/7679319?hl=en) · [Consenso in GTM (10718549)](https://support.google.com/tagmanager/answer/10718549?hl=en) · [Anteprima (6107056)](https://support.google.com/tagmanager/answer/6107056?hl=en) · [Tag Assistant (10039345)](https://support.google.com/tagmanager/answer/10039345?hl=en) · [Tag Diagnostics (14681508)](https://support.google.com/tagmanager/answer/14681508?hl=en) · [Aree di lavoro (7059647)](https://support.google.com/tagmanager/answer/7059647?hl=en) · [Pubblicazione, versioni, approvazioni (6107163)](https://support.google.com/tagmanager/answer/6107163?hl=en) · [Permessi (6107011)](https://support.google.com/tagmanager/answer/6107011?hl=en) · [Google tag gateway (16816376)](https://support.google.com/tagmanager/answer/16816376?hl=en) · [dataLayer](https://developers.google.com/tag-platform/tag-manager/datalayer) · [E-commerce GA4](https://developers.google.com/analytics/devguides/collection/ga4/ecommerce?client_type=gtm) · [Intro server-side](https://developers.google.com/tag-platform/tag-manager/server-side/intro) · [Dominio personalizzato](https://developers.google.com/tag-platform/tag-manager/server-side/custom-domain) · [Invio dati al server](https://developers.google.com/tag-platform/tag-manager/server-side/send-data) · [SST fundamentals, lezione 5](https://developers.google.com/tag-platform/learn/sst-fundamentals/5-sst-setup-analytics) · [Consent mode server-side](https://developers.google.com/tag-platform/tag-manager/server-side/consent-mode) · [Debug server](https://developers.google.com/tag-platform/tag-manager/server-side/debug) · [Cloud Run](https://developers.google.com/tag-platform/tag-manager/server-side/cloud-run-setup-guide) · [App Engine](https://developers.google.com/tag-platform/tag-manager/server-side/app-engine-setup) · [Setup manuale](https://developers.google.com/tag-platform/tag-manager/server-side/manual-setup-guide) · [Gateway (developers)](https://developers.google.com/tag-platform/tag-manager/gateway) · [DebugView (7201382)](https://support.google.com/analytics/answer/7201382?hl=en) · [Tempo reale (9271392)](https://support.google.com/analytics/answer/9271392?hl=en) · [Consent mode (9976101)](https://support.google.com/analytics/answer/9976101?hl=en).

**Ufficiali Meta, lette:** [Deduplica Pixel e CAPI](https://developers.facebook.com/docs/marketing-api/conversions-api/deduplicate-pixel-and-server-events) · [CAPI Tag per GTM server](https://developers.facebook.com/docs/marketing-api/conversions-api/guides/gtm-server-side) · [Using the API, Test Events](https://developers.facebook.com/docs/marketing-api/conversions-api/using-the-api).

**Ufficiali Stape (documentazione del fornitore, non Google), lette:** [Pricing](https://stape.io/price) · [Plan tiers](https://stape.io/helpdesk/documentation/plan-tiers-and-limits) · [How billing works](https://stape.io/helpdesk/documentation/how-billing-works) · [Custom domain](https://stape.io/helpdesk/documentation/add-custom-domain-in-stape) · [Custom Loader](https://stape.io/helpdesk/documentation/custom-loader-power-up) · [Cookie Keeper](https://stape.io/helpdesk/documentation/cookie-keeper-power-up) · [Zone server](https://stape.io/helpdesk/documentation/sgtm-server-locations-zones) · [Global vs EU](https://stape.io/helpdesk/knowledgebase/what-is-the-difference-between-global-sgtm-hosting-and-eu-sgtm-hosting) · [Meta CAPI setup](https://stape.io/helpdesk/documentation/how-to-set-up-meta-conversions-api) · [Unique Event ID](https://stape.io/helpdesk/documentation/unique-event-id) · [News 21/08/2026](https://stape.io/news/google-tag-gtm-updates) · [Costi GCP vs Stape, 04/09/2025 (blog)](https://stape.io/blog/how-much-does-server-gtm-cost).

**Italia:** [Garante, Linee guida cookie 10/06/2021 (9677876)](https://www.garanteprivacy.it/web/guest/home/docweb/-/docweb-display/docweb/9677876).

**Terze parti (pratica, non numeri ufficiali):** [Simo Ahava, FPID](https://www.simoahava.com/analytics/fpid-cookie-google-analytics-server-side-tagging/) · [ppc.land, gateway](https://ppc.land/google-tag-gateway/) · [usehardal, prezzi Stape (grace period e soglia 10%: non confermati sulle pagine Stape)](https://usehardal.com/blog/stape-pricing).

**Non leggibili via fetch il 20/09/2026, da ricontrollare a mano:** pagina ufficiale del client GA4 e dei cookie server-side su developers.google.com (`server-side/ga4-client`, `server-side/cookies`, `server-side/how-it-works`: 404); `developers.google.com/.../dependency-serving` (restituisce la pagina del gateway, senza le istruzioni sui percorsi gtag.js); `stape.io/pricing` (404, letta `/price`); documentazione Stape del tag Facebook Conversions API (404, letta la guida di setup); pagina Meta `payload-helper` (senza la parte Test Events); pagina ufficiale della policy Google sul consenso in EEA.
