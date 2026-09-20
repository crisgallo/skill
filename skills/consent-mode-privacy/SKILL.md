---
name: "consent-mode-privacy"
description: "Regole operative verificate per Google Consent Mode v2, banner cookie e privacy di misurazione sui siti italiani: i sette tipi di consenso, default e update, modalità basic e advanced, soglie di modellazione, obbligo SEE da marzo 2024, CMP (iubenda, Cookiebot) e template GTM, UET Microsoft e Meta Pixel, Linee guida cookie del Garante 2021, audit del sito prima e dopo il consenso, lettura dello stato in GA4 e Google Ads. Usala ogni volta che si tocca un banner cookie, un container GTM, un tag Google/Meta/Microsoft, o quando conversioni e pubblici calano e nessuno sa perché."
---

# Consent Mode e privacy cookie: regole operative

**Ultima verifica delle fonti: 20 settembre 2026.**

**Cosa è cambiato nel 2026 (per chi arriva da una configurazione del 2024-2025):**

- **15/06/2026:** Google Analytics smette di usare Google Signals come interruttore dei dati pubblicitari; il solo controllo è **`ad_storage` di Consent Mode** (sez. 6).
- **03/08/2026:** Google usa gli **indirizzi IP** per misurazione e personalizzazione degli annunci in SEE, UK e Svizzera (sez. 6).
- **"Entro fine 2026", data non pubblicata:** `ad_personalization` diventa l'unico controllo della personalizzazione in Google Ads; gli IP raccolti dal tag Google fluiscono cifrati all'account Ads collegato (sez. 6).
- **19/02/2026:** Microsoft annuncia l'Advanced Consent Mode con modellazione per UET (sez. 8).
- **11/02/2026:** parere congiunto EDPB-EDPS sul Digital Omnibus; norme cookie **ancora in negoziazione**, nulla cambia oggi (sez. 10).

---

## 0. Manutenzione di questa skill (leggere per primo)

⛔ **Questa skill è scritta da un consulente marketing, non da un avvocato.** La parte legale si limita a quello che pubblicano il Garante e l'EDPB, citato con link. Un parere su un caso concreto (cookie wall, base giuridica, trasferimenti extra-UE) lo dà un legale; qui si decide cosa fare sul container e sul banner.

1. **Finestra di freschezza: due mesi.** Google ha cambiato i controlli dati tre volte fra giugno e agosto 2026 e ha promesso un altro cambio "entro fine anno". Se la data in cima ha più di due mesi, si rileggono le tre pagine di sez. 6 prima di toccare un sito.
2. **Quando una fonte smentisce una regola scritta qui, si aggiorna la skill nello stesso turno**, si riscrive la data e si annota cosa è cambiato e da quando.
3. Due metà da tenere distinte: **conoscenza di dominio** (verificata su Google, Garante, EDPB) e **meccanica del pannello** (sez. 14: si impara sbagliando, si scrive qui la prima volta).
4. Dove si guardano i cambiamenti: [Updates to Google Analytics Data Controls](https://support.google.com/analytics/answer/17016975?hl=en), [Updates to consent mode for EEA traffic](https://support.google.com/google-ads/answer/13695607?hl=en), [Garante, tema Cookie](https://www.garanteprivacy.it/temi/cookie), [EDPB news](https://www.edpb.europa.eu/news/news_en), blog Microsoft Advertising.

---

## 1. La regola che costa di più: senza segnali di consenso, gli utenti SEE spariscono da pubblici e conversioni

**Da marzo 2024, per gli utenti in SEE, UK e Svizzera, Google Ads accetta dati per pubblici, remarketing, Customer Match e misurazione solo se arrivano insieme ai segnali `ad_user_data` e `ad_personalization` a `granted`.** Senza, "you will lose ads personalization capabilities" e "this may lead to loss in data" ([13695607](https://support.google.com/google-ads/answer/13695607?hl=en), [14009343](https://support.google.com/google-ads/answer/14009343?hl=en)). Base: la [EU user consent policy](https://www.google.com/about/company/user-consent-policy/), che impone anche di **conservare le prove del consenso** e di indicare come revocarlo.

Conseguenze operative sul pannello:

- 🔴 **Gli elenchi di remarketing non si riempiono di utenti SEE nuovi.** Un elenco che nel 2026 resta sotto i 100 utenti attivi (soglia unica Google Ads da dicembre 2025) spesso non ha un problema di traffico: ha un problema di consenso non trasmesso.
- 🔴 **Le conversioni degli utenti che rifiutano non si osservano.** Si recuperano solo per modellazione, e solo in modalità advanced con soglie raggiunte (sez. 5). Un calo di conversioni il giorno in cui è andato online un banner nuovo è contabilità, non performance: va scritto nel report.
- ⚠️ Customer Match e caricamenti offline in SEE richiedono entrambi i campi di consenso a GRANTED per riga ([14009343](https://support.google.com/google-ads/answer/14009343?hl=en)).

---

## 2. I sette tipi di consenso e cosa chiudono

Fonte: [tabella ufficiale dei consent types](https://developers.google.com/tag-platform/security/concepts/consent-mode).

| tipo | cosa chiude quando è `denied` | chi lo legge |
|---|---|---|
| `ad_storage` | cookie e identificatori pubblicitari (`_gcl_*`, click ID, conversion linker); dal 15/06/2026 è l'unico interruttore dei dati Ads raccolti anche dal tag GA4 | Google Ads, Floodlight, GA4 |
| `ad_user_data` | invio a Google di dati utente per fini pubblicitari (conversioni avanzate, Customer Match, misurazione Ads) | Google Ads, GA4 collegato ad Ads |
| `ad_personalization` | remarketing e personalizzazione; equivale a `allow_ad_personalization_signals`: in conflitto vince il divieto | Google Ads |
| `analytics_storage` | cookie `_ga`, `_ga_*`, durata visita, utenti, sessioni | GA4 |
| `functionality_storage` | storage funzionale (lingua, impostazioni) | tag terzi tramite "consenso aggiuntivo" in GTM |
| `personalization_storage` | storage di personalizzazione (raccomandazioni) | idem |
| `security_storage` | autenticazione, antifrode | idem; di regola `granted` di default |

⚠️ **`ad_user_data` e `ad_personalization` sono "v2" (novembre 2023) e sono quelli che decidono la sez. 1.** Un'implementazione con soli `ad_storage` e `analytics_storage` è v1 e in SEE non basta.

⚠️ I tre `*_storage` funzionali non hanno controlli integrati nei tag Google: servono solo se in GTM li si impone come consenso aggiuntivo sui tag di terzi (chat, video, A/B test).

---

## 3. `default` e `update`: l'ordine decide tutto

**Il comando `default` deve eseguire prima che carichi qualunque tag Google, su ogni pagina, in modo sincrono.** "If your consent code is called out of order, consent defaults won't work" e "Don't set default consent states asynchronously" ([guida implementazione](https://developers.google.com/tag-platform/security/guides/consent), [debug](https://developers.google.com/tag-platform/security/guides/consent-debugging)).

```js
gtag('consent', 'default', {
  'ad_storage': 'denied', 'ad_user_data': 'denied',
  'ad_personalization': 'denied', 'analytics_storage': 'denied',
  'wait_for_update': 500
});
// dopo l'interazione con il banner:
gtag('consent', 'update', { 'ad_storage': 'granted', 'ad_user_data': 'granted',
  'ad_personalization': 'granted', 'analytics_storage': 'granted' });
```

- `wait_for_update` (ms): tempo concesso al CMP per mandare l'`update` prima che i tag scattino. Serve quando il CMP è asincrono; 500 è il valore dell'esempio Google, non un obbligo.
- `region`: codici ISO 3166-2; con due `default` sulla stessa pagina vince quello con la regione più specifica. Su un sito italiano che vende solo in Italia: un solo `default` senza `region`, tutto `denied`.
- `url_passthrough: true`: con `ad_storage` negato, il click ID viaggia nell'URL fra le pagine. `ads_data_redaction: true`: con `ad_storage` negato, i click ID vengono oscurati nelle richieste. Sono opzioni di accuratezza, non di conformità: la scelta di attivarle si concorda con chi firma la cookie policy.
- 🔴 **In GTM il `default` va sull'attivatore "Inizializzazione del consenso - Tutte le pagine"** (Consent Initialization - All Pages), che scatta prima di ogni altro attivatore ([10718549](https://support.google.com/tagmanager/answer/10718549)). Un `default` su "Visualizzazione di pagina" o "Inizializzazione" arriva tardi a caso.

---

## 4. Basic e advanced: cosa parte davvero

Fonte: [tabella di confronto](https://developers.google.com/tag-platform/security/concepts/consent-mode), [10000067](https://support.google.com/google-ads/answer/10000067).

| | **basic** | **advanced** |
|---|---|---|
| caricamento tag Google | bloccato finché l'utente non interagisce con il banner | i tag caricano subito con default `denied` |
| cosa parte prima del consenso | **niente** | **ping senza cookie** |
| modellazione | generale | specifica dell'inserzionista (più precisa) |

**Il ping senza cookie contiene:** timestamp, user agent, referrer, URL della pagina, stato booleano del consenso, un numero casuale generato a ogni caricamento di pagina. Non scrive né legge cookie. Nelle richieste di rete si legge nei parametri `gcs`, `gcd`, `dma`.

⚠️ **Advanced non è "conforme di default".** Manda dati (IP compreso, che è dato personale per l'EDPB) prima del consenso. Google la propone come misurazione; se è ammissibile su quel sito lo decide chi firma la policy, non il consulente. Prassi prudenziale: si presenta al cliente la scelta con la tabella sopra e si mette per iscritto chi ha deciso.

⚠️ **Basic + GA4 hardcoded nel tema = advanced senza saperlo.** Se il tag Google è nel `<head>` del tema e non passa dal CMP, carica sempre. Si verifica in rete, non nel container (sez. 11).

---

## 5. Modellazione: soglie Google e come vederla

- **Conversioni Google Ads:** consent mode (o TCF v2) implementato correttamente **e almeno 700 clic sugli annunci in 7 giorni per combinazione dominio × paese**. Le conversioni modellate finiscono **nella colonna Conversioni senza etichetta separata** e in tutti i report a valle ([10548233](https://support.google.com/google-ads/answer/10548233?hl=en)). Chi blocca i ping (basic) può avere modellazione generale ma "our systems will be unable to generate advertiser-specific calibration factors".
- **Comportamento GA4:** **almeno 1.000 eventi al giorno con `analytics_storage='denied'` per 7 giorni** e **almeno 1.000 utenti giornalieri con `analytics_storage='granted'` in 7 dei 28 giorni precedenti**, consent mode su tutte le pagine, **identità per i report "Mista" (Blended)**. Raggiungere le soglie non garantisce: il modello valuta anche rapporto nuovi/di ritorno e utenti/sessioni. Non si applica a pubblici, esplorazioni utente e coorti, segmenti con sequenze, fidelizzazione, export BigQuery ([11161109](https://support.google.com/analytics/answer/11161109?hl=en)).
- **Come si vede che è attiva:** in GA4 l'icona qualità dei dati nel report dice "Including estimated user data. As of [data]..."; in Google Ads lo stato nella scheda Diagnostica dell'azione di conversione dice "Consent mode is implemented and modeling is active", con l'uplift mostrato per 4 settimane ([14218557](https://support.google.com/google-ads/answer/14218557?hl=en)).
- 🔴 **Conseguenza per una PMI italiana:** 700 clic in 7 giorni su `.it × IT` è ~100 clic/giorno pagati; 1.000 utenti al giorno con consenso è oltre la scala della maggior parte dei siti. **Sotto soglia la modellazione non esiste**, e l'unica cosa che si può fare è alzare il tasso di consenso e non promettere recuperi. "Fino al 70% delle conversioni recuperate" è una cifra di blog CMP (iubenda), non un numero Google.

---

## 6. Cosa è cambiato nel 2026 e cosa si controlla

1. **15/06/2026: Consent Mode è il solo controllo dei dati Ads in GA.** Google Signals ora "will only control the association of your Google Analytics sourced data with signed in user information for behavioral reporting"; i cookie e ID pubblicitari raccolti dal tag GA4 sono governati da `ad_storage` ([17016975](https://support.google.com/analytics/answer/17016975?hl=en)). ⚠️ Chi teneva Google Signals spento "per prudenza" e ha `ad_storage` mal configurato ora manda dati Ads che prima erano fermi. Si controlla lo stato di `ad_storage` in Tag Assistant su ogni proprietà, non lo switch Signals.
2. **"Later this year", data non pubblicata al 20/09/2026:** `ad_personalization` di Consent Mode "will exclusively control if data is used for personalization in your Ads account"; gli IP "will be encrypted and flow to your linked Google Ads account" (stessa pagina). Da rileggere a ogni giro di manutenzione.
3. **03/08/2026: IP usati per misurazione e personalizzazione annunci in SEE/UK/CH.** Comunicato via email agli editori AdSense/Ad Manager il 17/06/2026 e con l'aggiunta della Feature 3 TCF ("Identify devices based on information transmitted automatically") al vendor 755; **nessuna pagina Help pubblica trovata**, fonti terze: [ppc.land](https://ppc.land/google-to-bring-ip-based-ads-to-eea-publishers-from-august-3/), [iubenda blog](https://www.iubenda.com/en/blog/google-ip-addresses-ads/). Per un inserzionista significa: la cookie policy che descrive Google Ads deve nominare l'IP come identificatore; il testo lo scrive il legale.

---

## 7. CMP e GTM: la catena che regge

- **Si usa un CMP del programma partner Google** (Gold: iubenda, Cookiebot/Usercentrics, OneTrust, Didomi, CookieYes, Axeptio; Silver: Complianz) ([cmppartnerprogram.withgoogle.com](https://cmppartnerprogram.withgoogle.com/)). Un banner fatto in casa è ammesso ma allora `default`/`update` e il registro dei consensi li si scrive e li si prova da soli.
- **Ordine di caricamento: CMP prima di GTM, GTM prima di tutto il resto.** Con il template GTM del CMP (galleria community) l'ordine è garantito solo se il tag template ha l'attivatore **Inizializzazione del consenso - Tutte le pagine**. Con lo script CMP nel `<head>` deve stare **sopra** lo snippet GTM.
- **iubenda:** template "Controlli per la privacy e soluzione per cookie iubenda", attivatore Inizializzazione del consenso, configurazione incollata dalla sezione *Incorpora* con "Automaticamente tramite modello GTM", consensi predefiniti per scopo tutti negati; Consent Mode v2 si attiva anche con l'autoblocking ([14546074](https://support.google.com/tagmanager/answer/14546074?hl=it), [iubenda help](https://www.iubenda.com/en/help/161602-attiva-google-consent-mode-con-iubenda/)).
- **Cookiebot:** template "Cookiebot CMP" con il Domain Group ID sull'attivatore Inizializzazione del consenso; Consent Mode attivo di default; Google consiglia di sostituire gli attivatori "page load" dei tag terzi con l'evento personalizzato `cookie_consent_update` ([14546767](https://support.google.com/tagmanager/answer/14546767?hl=en)). Mappatura categorie → tipi: statistiche → `analytics_storage`; marketing → `ad_storage`, `ad_user_data`, `ad_personalization`; preferenze → `functionality_storage`, `personalization_storage` (pagina Cookiebot 403 il 20/09/2026, mappatura da documentazione terza).
- **In GTM, Amministrazione → Impostazioni contenitore → "Abilita panoramica consenso"**: apre la scheda che divide i tag in *Consenso non configurato* e *Consenso configurato* e permette modifiche in blocco ([10718549](https://support.google.com/tagmanager/answer/10718549)). I tag Google hanno i controlli integrati; **Meta, LinkedIn, TikTok, Hotjar, Clarity no**: su ognuno si imposta *Richiedi consenso aggiuntivo* con i tipi giusti (Meta: `ad_storage` + `ad_user_data`; Hotjar/Clarity: `analytics_storage`).

---

## 8. Microsoft UET e Meta: in breve

- **Microsoft Advertising, dal 05/05/2025:** obbligatorio trasmettere `ad_storage` (`granted`/`denied`) per il traffico SEE/UK/CH, altrimenti "will impact your advertising performance" su conversioni e pubblici; tre vie alternative: codice UET, TCF v2 via CMP, template GTM ufficiale ([blog Microsoft 31/03/2025](https://about.ads.microsoft.com/en/blog/post/march-2025/providing-user-consent-signals-on-your-microsoft-campaigns-by-may-5-2025)). Default `denied`; ogni evento UET porta `asc=G` o `asc=D`. **Fino al 2025 nessuna modellazione**; il 19/02/2026 Microsoft ha annunciato l'**Advanced Consent Mode** con stima delle conversioni negate, caricando UET nel `<head>` prima del banner ([blog 19/02/2026](https://about.ads.microsoft.com/en/blog/post/february-2026/advanced-consent-mode-preserving-accurate-measurement-while-respecting-user-privacy)). `[DA VERIFICARE]` la sintassi esatta `uetq.push('consent','default',{ad_storage:'denied'})`: la pagina Help Microsoft non è leggibile via fetch, sintassi da documentazione terza.
- **Meta:** non ha un consent mode. I *Meta Business Tools Terms* impongono di garantire "in a verifiable manner" tutti i consensi **prima** che il Pixel scriva o legga cookie nelle giurisdizioni UE, più una "clear and prominent notice" su ogni pagina con il pixel ([technology_terms](https://www.facebook.com/legal/technology_terms)). Strumento: `fbq('consent','revoke')` **prima di `init`** su ogni pagina, `fbq('consent','grant')` dopo il consenso ([doc GDPR pixel](https://developers.facebook.com/docs/meta-pixel/implementation/gdpr)); in GTM equivale al consenso aggiuntivo del punto sopra. ⛔ **Limited Data Use (`dataProcessingOptions: ['LDU']`) è per gli stati USA, non per l'Europa** ([data-processing-options](https://developers.facebook.com/docs/marketing-apis/data-processing-options)): metterlo su un sito italiano non è conformità, è un flag che limita retargeting e misurazione per niente. ⚠️ La Conversions API non aggira il consenso: il server manda gli stessi dati personali, e i cookie `_fbp`/`_fbc` che la alimentano nascono sul browser.

---

## 9. Garante: Linee guida cookie del 10/06/2021 (in vigore dal 09/01/2022)

Fonte: [provvedimento 9677876](https://www.garanteprivacy.it/web/guest/home/docweb/-/docweb-display/docweb/9677876), [comunicato 9679893](https://www.garanteprivacy.it/home/docweb/-/docweb-display/docweb/9679893). Regole che decidono il disegno del banner:

1. **Nessun cookie non tecnico prima del consenso.** È la violazione più contestata e la più facile da provare (sez. 11).
2. **La X in alto a destra chiude il banner senza consenso** e deve avere la stessa evidenza degli altri comandi; proseguire senza consentire dev'essere "immediato, usabile e accessibile". Quindi **Rifiuta con lo stesso peso di Accetta**: stessa dimensione, stesso livello. Il "Rifiuta" grigio piccolo è quello che il Garante e la taskforce EDPB chiamano dark pattern.
3. **Lo scroll non è consenso**: "il semplice 'scroll down' del cursore di pagina è inadatto in sé alla raccolta di un idoneo consenso". Neanche "continuando la navigazione accetti" (ammonimento Vremar, [10162286](https://www.garanteprivacy.it/home/docweb/-/docweb-display/docweb/10162286), 10/07/2025).
4. **Cookie wall vietato**, salvo alternativa equivalente senza tracciamento (tema "consent or pay": qui si ferma il consulente, parla il legale).
5. **Secondo livello granulare** con un link dal banner: scelte per finalità, **tutte disattivate di default**, caselle preselezionate non valide (anche per la CGUE, Planet49).
6. **Non si ripropone il banner** a chi ha scelto, salvo cambio sostanziale del trattamento, impossibilità di sapere se il cookie è già sul dispositivo, o **almeno 6 mesi** dalla precedente presentazione. Banner a ogni accesso = violazione (ammonimento 27/02/2025, [10118222](https://www.garanteprivacy.it/web/guest/home/docweb/-/docweb-display/docweb/10118222)). Operativamente: il cookie di preferenza del CMP dura 6-12 mesi, non 30 giorni.
7. **Registro del consenso**: le scelte "siano registrate e siano dunque debitamente documentabili, anche mediante evidenze informatiche". Il CMP a pagamento serve a questo; un banner gratuito senza log non lo fa.
8. **Cookie analytics senza consenso** solo se: IP mascherato almeno nel quarto ottetto, nessuna combinazione con altri dati o trasmissione a terzi, uso statistico del solo editore. **GA4 non rientra** in questa lettura per prassi corrente del settore e il Garante con il provvedimento del 09/06/2022 ([9782874](https://www.garanteprivacy.it/home/docweb/-/docweb-display/docweb/9782874)) ha bloccato Universal Analytics per i trasferimenti USA; il Data Privacy Framework del 2023 ha cambiato la base dei trasferimenti, non la natura del cookie. Regola operativa: **GA4 dietro `analytics_storage`, sempre**.
9. **Cookie policy raggiungibile con un clic dal banner**, con tutte le informazioni degli artt. 12-13 GDPR; nomi delle categorie comprensibili ("esperienza" è stato bocciato, Vremar).

Sanzioni: art. 122 Codice privacy rientra nella fascia alta GDPR (fino a 20 M€ o 4% del fatturato); nei casi cookie del 2025 il Garante ha chiuso con **ammonimenti e ordini correttivi**, non multe. **Nessun provvedimento cookie trovato fra giugno e settembre 2026** sul sito del Garante (i provvedimenti 2026 letti riguardano Character.AI, RTI, Ambrosetti).

---

## 10. DMA, EDPB e Digital Omnibus

- **DMA (dal 06/03/2024):** Google come gatekeeper deve chiedere all'utente UE se collegare i servizi (Ricerca, YouTube, Ads, Play, Chrome, Shopping, Maps); senza collegamento, meno personalizzazione ([14202510](https://support.google.com/accounts/answer/14202510?hl=en)). È il motivo per cui esistono `ad_user_data` e `ad_personalization` e il parametro `dma` nei ping. Per il sito non c'è nulla da configurare: è lato utente Google.
- **EDPB, Linee guida 2/2023** (versione finale 16/10/2024): l'art. 5(3) ePrivacy copre anche pixel, tracking via URL e identificatori, non solo i cookie ([pagina EDPB](https://www.edpb.europa.eu/our-work-tools/our-documents/guidelines/guidelines-22023-technical-scope-art-53-eprivacy-directive_en); PDF non letto). **Rapporto taskforce banner (01/2023):** senza pulsante di rifiuto il consenso non è valido; contrasto illeggibile e caselle preselezionate sono pratiche ingannevoli.
- **Digital Omnibus:** proposta della Commissione del 25/11/2025 che sposta le regole cookie nel GDPR (artt. 88a/88b, segnali del browser vincolanti); parere congiunto EDPB-EDPS 2/2026 dell'11/02/2026 favorevole al principio, contrario al restringimento della nozione di dato personale ([EDPB](https://www.edpb.europa.eu/news/news/2026/digital-omnibus-edpb-and-edps-support-simplification-and-competitiveness-while_en)). Al 20/09/2026 in trilogo, applicazione non prima del 2027 (fonti terze). ⛔ **Non si toglie il banner "perché sta per cambiare la legge".**

---

## 11. Audit di un sito: cosa si guarda nel browser

Finestra anonima, DevTools aperti (Rete + Applicazione → Cookie), Tag Assistant collegato.

**Prima di qualunque clic sul banner:**
1. Cookie presenti: ammessi solo tecnici (sessione, carrello, lingua, cookie del CMP stesso). 🔴 **Non devono esistere** `_ga`, `_ga_*`, `_gid`, `_gcl_au`, `_gcl_aw`, `_fbp`, `_fbc`, `_uetsid`, `_uetvid`, `IDE`, `test_cookie`, `_hjSession*`, `_clck`/`_clsk`, `ttp`/`_tt_*`.
2. Rete, filtro `collect` e `google-analytics`/`googleads`/`facebook.com/tr`/`bat.bing`: in basic non parte niente; in advanced parte solo il ping Google con `gcs=G100` (lettura del parametro da documentazione terza: `G100` = entrambi negati, `G111` = entrambi concessi). `facebook.com/tr` e `bat.bing.com` prima del consenso sono violazioni.
3. Tag Assistant, scheda **Consenso**: colonna *On-page Default* con i quattro parametri a *Denied* sul **primo** evento Consent. Scheda vuota = consent mode assente o tag Google bloccato. Errore "Ad tag has already read or written a cookie before the default consent is set" = default troppo tardi ([consent-debugging](https://developers.google.com/tag-platform/security/guides/consent-debugging), [14522438](https://support.google.com/google-ads/answer/14522438?hl=en)).

**Dopo "Accetta tutto":** *On-page Update* con i quattro a *Granted*; compaiono `_ga`, `_gcl_au`, `_fbp`; nella scheda Tag, i tag terzi risultano scattati. **Dopo "Rifiuta":** nessun cookie nuovo, i tag terzi in *bloccato*, e alla ricarica il banner **non** riappare.

**Guasti ricorrenti, nell'ordine di frequenza:**
- tag GA4/Ads/Meta **fuori da GTM** (tema, plugin Site Kit, PixelYourSite, MonsterInsights, WooCommerce for Google): scattano prima del CMP;
- attivatore **Inizializzazione del consenso** mai usato: il template CMP gira su "Tutte le pagine";
- **CMP caricato dopo GTM** o via GTM su Page View;
- `default` presente ma **`update` mai inviato** (CMP configurato per il solo blocco script);
- tag terzi senza **consenso aggiuntivo** in GTM;
- `region` impostato su un paese e sito che vende anche altrove;
- cookie di preferenza del CMP a 30 giorni: banner ogni mese, utenti che rifiutano per esasperazione.

---

## 12. Leggere lo stato in GA4 e Google Ads

- **GA4:** Amministrazione → Raccolta e modifica dei dati → **Impostazioni del consenso** (Consent settings): tre blocchi, *segnali di consenso pubblicitari* (`ad_user_data`, `ad_personalization`), *segnali di consenso analisi del comportamento*, *impostazioni*. Se la proprietà è collegata ad Ads e uno stream ha visitatori SEE, GA4 avvisa quando **non riceve consenso affermativo** ([14275483](https://support.google.com/analytics/answer/14275483?hl=en)). Identità per i report: Amministrazione → Visualizzazione dei dati → Identità per i report → **Mista** per vedere i dati modellati.
- **Google Ads:** Obiettivi → Conversioni → Riepilogo → azione di conversione → scheda **Diagnostica**: stato "Consent mode is implemented" (attivo, soglie non raggiunte) oppure "...and modeling is active". Lo stato attivo compare dopo **48 ore, fino a 2 settimane** ([14218557](https://support.google.com/google-ads/answer/14218557?hl=en)). Allerte possibili: scheda consenso vuota, default non impostato, default impostato tardi, consenso che non si aggiorna, nessun adattamento regionale, risultati d'impatto mancanti (soglie), uplift basso ([14522438](https://support.google.com/google-ads/answer/14522438?hl=en)).
- ⚠️ Lo stato "implemented" dice che i ping arrivano, **non** che il banner è conforme. Un sito con default `granted` risulta perfettamente "implemented".

---

## 13. Igiene di un sito ereditato: ordine di controllo

1. **Cookie prima del consenso** (sez. 11, punto 1). Se ce ne sono, si ferma tutto e si trova la sorgente fuori GTM.
2. **Ordine di caricamento**: CMP → `default` su Inizializzazione del consenso → tag Google → tag terzi.
3. **Versione**: i quattro parametri, non due. Tag Assistant, primo evento Consent.
4. **`update` reale** su Accetta e su Rifiuta, e cookie di preferenza a 6-12 mesi.
5. **Consenso aggiuntivo** su ogni tag non Google (panoramica consenso in GTM).
6. **Banner**: X e Rifiuta con lo stesso peso di Accetta, secondo livello tutto spento, link alla policy, niente scroll/prosecuzione.
7. **Registro dei consensi** attivo nel CMP e chi può esportarlo.
8. **Stato in GA4** (Impostazioni del consenso) **e in Google Ads** (Diagnostica): entrambi, perché guardano cose diverse.
9. **Basic o advanced**: scritto da qualche parte chi l'ha deciso. Se non c'è, si fa decidere ora.
10. **Cookie policy**: nomina Google Ads con IP (dal 03/08/2026), Meta, Microsoft, e i tag che il container contiene davvero. Confrontare lista policy e lista tag: devono coincidere.

---

## 14. Meccanica del pannello (da verificare a mano)

- Nel CMP iubenda, "Consent Mode v2" attivato dal wizard: manda davvero `update` anche su *Rifiuta*, o solo su *Accetta*? Verificare in Tag Assistant sul secondo evento Consent.
- Con Cookiebot in `data-blockingmode="auto"` e GTM: il blocco automatico riscrive gli script del tema con `type="text/plain"`? E i tag caricati da GTM restano governati solo dal consent mode?
- Google Ads, scheda Diagnostica: lo stato di consent mode è per **azione di conversione** o per **account**? Un'azione importata da GA4 lo mostra?
- GA4, Impostazioni del consenso: l'avviso "non riceve consenso affermativo" compare con quale percentuale di `denied`, o alla prima sessione senza segnale?
- Tag Assistant su un sito con `region: ['IT']`: simulando la geolocalizzazione dall'estero i default cambiano davvero, o serve una VPN?
- Il template GTM "Controlli per la privacy e soluzione per cookie iubenda" su "Inizializzazione del consenso": in Anteprima, l'evento Consent compare **prima** di `gtm.init`?

---

## 15. Cosa non fare mai

- **Mettere il `default` su un attivatore diverso da Inizializzazione del consenso.**
- **Dichiarare un sito conforme guardando solo Tag Assistant.** Tag Assistant vede i tag Google; i cookie di Meta, Hotjar e del tema si vedono in DevTools.
- **Lasciare un tag GA4 o Meta fuori da GTM "perché lo mette il plugin".** È la prima causa di cookie prima del consenso.
- **Usare Limited Data Use di Meta come misura per l'Europa.**
- **Promettere il recupero delle conversioni via modellazione a un sito sotto le soglie** (700 clic/7 gg per Ads; 1.000/1.000 per GA4).
- **Confrontare conversioni a cavallo della messa online di un banner o del passaggio basic/advanced** senza dirlo.
- **Disegnare Rifiuta in grigio piccolo** e Accetta in colore brand: è il caso da manuale dell'ammonimento.
- **Riproporre il banner prima di 6 mesi** a chi ha rifiutato.
- **Togliere Google Signals pensando di fermare i dati Ads.** Dal 15/06/2026 non ferma niente: si agisce su `ad_storage`.
- **Scrivere la cookie policy o decidere su cookie wall e advanced mode al posto del legale.** Si prepara la lista dei tag e dei cookie reali, e si passa.

---

## Fonti (verificate 20/09/2026)

**Google, ufficiali**
- Consent mode, concetti e tabella dei tipi: https://developers.google.com/tag-platform/security/concepts/consent-mode
- Guida implementazione (`default`, `update`, `wait_for_update`, `region`, `url_passthrough`, `ads_data_redaction`): https://developers.google.com/tag-platform/security/guides/consent
- Debug con Tag Assistant: https://developers.google.com/tag-platform/security/guides/consent-debugging
- Google Ads 10000067 About consent mode; 10548233 modellazione (700 clic/7 gg); 14218557 verifica stato; 14522438 troubleshooting; 13695607 aggiornamenti SEE; 14009343 Obtain user consent; 16142339 verifica segnali SEE
- GA4 11161109 modellazione comportamentale (1.000/1.000, Mista); 14275483 Impostazioni del consenso; 17016975 Updates to Data Controls (15/06/2026)
- GTM 10718549 consent overview e Inizializzazione del consenso; 14546074 iubenda (hl=it); 14546767 Cookiebot
- EU user consent policy: https://www.google.com/about/company/user-consent-policy/ ; DMA linked services 14202510 (accounts); CMP partner program: https://cmppartnerprogram.withgoogle.com/
- **Non leggibili via fetch il 20/09/2026, da ricontrollare a mano:** google-ads 13554116, 13695824, 14319609 (404); analytics 12334045 (solo glossario); nessuna pagina Help pubblica sull'uso degli IP dal 03/08/2026.

**Garante ed EDPB, ufficiali**
- Linee guida cookie 10/06/2021, docweb 9677876; comunicato 9679893; tema Cookie: https://www.garanteprivacy.it/temi/cookie
- Ammonimenti banner: 27/02/2025 docweb 10118222; 10/07/2025 docweb 10162286 (Vremar); provvedimento GA 09/06/2022 docweb 9782874
- EDPB Linee guida 2/2023 (pagina; PDF non letto); parere congiunto EDPB-EDPS 2/2026 sul Digital Omnibus (11/02/2026)

**Microsoft e Meta, ufficiali**
- Microsoft blog 31/03/2025 (scadenza 05/05/2025) e 19/02/2026 (Advanced Consent Mode); pagina Help UET consent mode **non leggibile via fetch il 20/09/2026**
- Meta Business Tools Terms: https://www.facebook.com/legal/technology_terms ; pixel GDPR `fbq('consent')`: https://developers.facebook.com/docs/meta-pixel/implementation/gdpr ; LDU: https://developers.facebook.com/docs/marketing-apis/data-processing-options ; business help 348535683460989 e 1076458978496976 **non leggibili**

**Terze parti (etichettate nel testo)**
- ppc.land e iubenda blog sugli IP dal 03/08/2026; usercentrics knowledge hub su UET (`asc=G/D`, niente modellazione); iubenda help 142541 (70% è cifra iubenda); support.cookiebot.com 360016047000 (403 il 20/09/2026); dataprotectionlaw.it 15/09/2026 (nessun provvedimento 2026 citato); secureprivacy/cookiebeam sul Digital Omnibus (trilogo, 2027).
