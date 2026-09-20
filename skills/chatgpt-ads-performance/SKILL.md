---
name: chatgpt-ads-performance
description: "Regole operative verificate per montare, misurare e diagnosticare campagne su ChatGPT Ads (Ads Manager di OpenAI): apertura account, obiettivi CPM CPC e oCPC, budget minimi, context hints, specifiche creative, pixel oaiq e Conversions API, policy, API inserzionisti."
---

# ChatGPT Ads: regole operative

**Ultima verifica delle fonti: 12 settembre 2026.**

🔴 **Questo canale è in BETA dichiarata, e cambia più in fretta di Meta e Google.** OpenAI scrive che durante la beta cambieranno consegna, inventario, formati e modi di comprare e ottimizzare. Ogni numero qui sotto va ricontrollato prima di applicarlo, e la verifica in pannello vince sempre sulla documentazione.

## 0. Manutenzione (leggere per primo)

1. Su un prodotto in beta il limite di freschezza non è due o tre mesi come per Meta: è **un mese**.
2. Quando il pannello smentisce una riga, si aggiorna la skill **nello stesso turno**, con data e nota.
3. ⚠️ Molte specifiche NON stanno negli articoli di aiuto ma su `developers.openai.com/ads`, o si scoprono solo dal messaggio d'errore. Quando un dato manca, **si dichiara che manca**.
4. Ogni aggiornamento si riallinea nella copia di progetto `Blog/skills/`.

## 1. Che cos'è e chi la vede

Le inserzioni compaiono **sotto le risposte di ChatGPT**, con nome inserzionista, logo, titolo, descrizione, immagine e link. Le vedono gli utenti **Free e Standard**; ⛔ non le vedono **Plus, Pro e Business**, e sono esclusi i **minori di 18 anni**.

La selezione usa **contesto e intento della conversazione in corso**, la pagina di destinazione, titolo e testo, più i *context hints*. Asta **di secondo prezzo pesata sulla rilevanza**. L'inserzionista **non vede le conversazioni** e **la pubblicità non influenza le risposte**: non si compra la risposta, si compra lo spazio sotto.

⚠️ **Non è un motore di ricerca e i context hints non sono parole chiave.** OpenAI lo scrive: non sono corrispondenze esatte, non sono regole di targeting, non garantiscono la comparsa su una conversazione.

## 2. Account

✅ **Italia inclusa nel self-serve** (54 paesi e regioni). ⚠️ La lista dice dove può stare l'inserzionista, **non dove vengono servite le inserzioni**.

Apertura: dati aziendali, **verifica Persona** con coda di revisione, poi Impostazioni. ⛔ **Senza nome account e logo completi le inserzioni non vengono servite.** ⛔ **Paese, valuta e fuso orario non si cambiano più.** Un account per entità giuridica; individui e agenzie non supportati in self-serve a inizio beta.

**Fatturazione postpagata a soglia:** l'account riceve una soglia di pagamento e la carta viene addebitata al raggiungimento. ⛔ La soglia non si cambia, nemmeno chiedendo al supporto. Possibile preautorizzazione da 50 o 100 $ alla registrazione della carta.

## 3. Struttura

| Livello | Cosa si decide |
|---|---|
| **Campagna** | obiettivo e tipo di fatturazione, budget, date, **geografia**, **piattaforme**, pubblici personalizzati, evento di conversione (oCPC) |
| **Gruppo** | **context hints**, strategia di offerta e importo |
| **Inserzione** | titolo, testo, immagine, destinazione |

🔴 **Geografia e piattaforme stanno sulla CAMPAGNA, non sul gruppo.** Per testare due paesi servono due campagne. Chi arriva da Meta sbaglia struttura.

Limiti in caricamento massivo: 5.000 campagne, 5.000 gruppi, 5.000 inserzioni.

## 4. Obiettivi e offerte

**CPM** (mille impression), **CPC** (clic valido), **oCPC** (si paga a **clic** ma si ottimizza sulle conversioni post clic). Il *Bid Cap* è l'offerta massima in asta, non un costo per conversione garantito.

⛔ Una campagna esistente **non si converte** in oCPC: si crea nuova, col tracciamento già attivo e almeno un evento standard in arrivo.

Tre strategie: **offerta fissa**, **massimizza i clic**, **massimizza le conversioni**. Sui gruppi nuovi idonei l'automatico è il default. OpenAI dichiara che **non garantisce** CPA, CPC o ROAS obiettivo.

**Offerta di partenza consigliata: 3-5 $ per clic.** ⚠️ È alto per il mercato italiano: va confrontato col costo di una **lettura**, non con un CPC.

Nell'API le offerte sono in **micros** (1 unità = `1000000`); per il CPM si divide prima per 1.000.

⚠️ **Nessun periodo di apprendimento dichiarato.** È un'assenza nella documentazione, non la prova che non esista.

## 5. Budget

🔴 **Minimo giornaliero: 25 $ negli Stati Uniti**, e **varia per mercato e valuta**. ⚠️ Il minimo in euro **non è documentato**: si legge dal pannello, e l'API risponde con l'importo richiesto nell'errore. È il numero che decide se il test si fa.

- La spesa di un giorno **non supera il doppio** del budget giornaliero.
- Su sette giorni il tetto è **sette volte** il giornaliero.
- Cambiando budget a metà giornata vale il **valore più alto attivo** quel giorno; il tetto settimanale si riproporziona fino alla domenica a mezzanotte.

**Pacing:** rallenta se si è avanti di spesa e ⛔ **non garantisce di spendere tutto**. Con data di fine arriva lì, massimo **365 giorni**; senza data di fine il periodo è **60 giorni**.

## 6. Targeting

**Geografia:** paese ISO 3166-1 alpha-2; solo negli **Stati Uniti** stato, **DMA** e **CAP**. Via API fino a 2.500 location ID.

**Piattaforme:** app e web per iOS e Android più desktop web (nell'API: `ios_app`, `android_app`, `web`).

**Context hints:** fino a **2.000 per gruppo**, scritti come **frasi naturali e descrittive**, non come elenchi di termini.

**Pubblici personalizzati:** solo **liste caricate** (email, telefono, varianti SHA-256, GAID). ⛔ Nessun retargeting da pixel. **Minimo 25.000 utenti corrispondenti** per l'inclusione; sotto quella soglia valgono **solo in esclusione**. File CSV o TXT UTF-8 fino a 500 MB, hash SHA-256 a 64 caratteri, telefoni in E.164 prima dell'hash.

⚠️ Non documentati: lingua, fasce orarie, frequency cap. Non si promettono.

## 7. Creatività

| Elemento | Regola |
|---|---|
| Titolo | **16-24 caratteri consigliati, 50 massimo** |
| Testo | **32-48 consigliati, 100 massimo** |
| Immagine | **quadrata**, **massimo 1200 x 1200**, PNG o JPG, URL pubblico diretto |
| Destinazione | link valido, pagina **più pertinente** e non la home, UTM ammessi |

🔴 **La destinazione deve lasciar passare `OAI-AdsBot`** (e si consiglia `OAI-SearchBot`), altrimenti la revisione non passa e ⛔ **non esiste bypass manuale**. In `robots.txt` servono le due direttive `Allow: /`; gli IP stabili stanno in `openai.com/adsbot.json` e `openai.com/searchbot.json`. Blocchi di WAF, CDN, anti-bot, CAPTCHA o login fermano tutto. Sistemato l'accesso, l'inserzione va ricaricata o rimandata in revisione.

## 8. Tracciamento

Pixel `oaiq`, SDK da `https://bzrcdn.openai.com/sdk/oaiq.min.js`:

```
oaiq("init", { pixelId: "<PIXEL-ID>", debug: true })
oaiq("measure", eventName, eventData, options)
```

`eventData` vuole `type`; `options` accetta `event_id`, `custom_event_name`, `opt_out`.

**Eventi standard:** `page_viewed`, `contents_viewed`, `items_added`, `checkout_started`, `order_created`, `lead_created`, `registration_completed`, `appointment_scheduled`, `subscription_created` (vuole `plan_id`), `trial_started`, `app_installed`, `app_opened`, `custom`. ⚠️ I due eventi app **solo via Conversions API** con `action_source` a `mobile_app`.

🔑 **Gli importi si mandano come interi nell'unità minima ISO 4217:** 129,99 € si scrive `12999`.

Il parametro di clic è **`oppref`**, appeso alla destinazione; il pixel lo mette in un cookie di prima parte `__oppref`, aggiunge `source_url`, fa da solo l'hash SHA-256 dell'advanced matching e ha anche l'advanced matching automatico dai moduli.

**Conversions API:** endpoint **`https://bzr.openai.com/v1/events?pid=<PIXEL-ID>`**, autenticazione **Bearer**. Fino a **1.000 eventi** per richiesta; ogni evento ha `id`, `type`, `timestamp_ms`, `action_source`, `user`, `data`. ⛔ Timestamp **entro 7 giorni** e non oltre 10 minuti nel futuro. ⛔ **Se un evento fallisce, fallisce tutto il lotto.**

🔴 **Deduplicazione:** `id` della API uguale a `event_id` del pixel, stesso Pixel ID, stesso `custom_event_name` sugli eventi custom. Vince il primo arrivato. È la stessa forma della CAPI di Meta.

**Qualità degli eventi:** diagnostica aggiornata ogni giorno su sette giorni pieni. ⚠️ Scala e soglie non documentate: si leggono gli avvisi, non si insegue un punteggio.

## 9. Report

Impression, clic, spesa, CTR, CPC medio, CPM medio, conversioni, per campagna, gruppo e inserzione, con esportazione CSV cumulativa o giornaliera. **Segmentazioni: dispositivo e paese, e basta.**

🔴 **Ritardi da non scambiare per guasti:** clic e CTR rapidi, **spesa fino a 7 ore**, **conversioni 24-48 ore**, e prima di segnalare un problema di consegna si aspettano **24 ore dal lancio**.

**Attribuzione:** finestra post clic configurabile, **view-through fisse a 1 giorno**. ⚠️ OpenAI avverte che i numeri **non coincideranno** con analytics di terze parti, anche per via della **misurazione modellata**. Quindi il pannello si usa per costo e consegna, il giudizio lo dà GA4.

## 10. Policy

**Vietati:** adulti e dating, alcolici sopra 0,5% e nicotina, droghe e cannabis, gioco d'azzardo con denaro vero, contraffazione, **contenuti politici**, sessuale o violento esplicito.

**Ristretti con verifica e SOLO negli Stati Uniti:** servizi finanziari, sanità, servizi legali. ⛔ Fuori dagli Stati Uniti finanziario e legale restano generalmente vietati.

**Creatività:** affermazioni veritiere, linguaggio professionale, distinzione chiara dall'interfaccia. La destinazione non può introdurre contenuti non ammessi dopo l'approvazione.

**Contesti sensibili esclusi comunque:** salute mentale, crisi personali, vulnerabilità, sicurezza dei minori, terrorismo, armi, disinformazione, odio, privacy.

## 11. API inserzionisti

`developers.openai.com/ads` documenta gestione campagne, offerte e budget, targeting, feed di prodotto, tracciamento, reporting e account, con riferimento per autenticazione, ad account, campagne, gruppi, inserzioni, insights, file e conversioni. 🔑 Il canale si può governare da script invece che a clic.

## 12. Quello che NON c'è

⛔ Benchmark di performance pubblicati. ⛔ Retargeting da pixel. ⛔ Dati su dove le inserzioni vengono servite. ⛔ Minimo in euro documentato. ⛔ Finestra di apprendimento dichiarata. ⛔ Segmentazione per context hint: **quale gancio ha funzionato dal pannello non si sa**, si separa in gruppi e si legge dagli UTM.

## 13. Come si monta un test di spesa onesto

1. Aprire l'account e superare la verifica: **fin qui non si spende**.
2. **Accertare il minimo giornaliero in euro dal pannello.** È il numero che decide se il test si fa.
3. Sistemare `robots.txt` per `OAI-AdsBot` e **verificare che la pagina sia raggiungibile davvero**, non solo che la riga sia scritta.
4. Mettere il pixel dallo stesso container e agganciare l'evento che misura il risultato vero, non il clic.
5. **Un gruppo solo, CPC, offerta fissa.** Senza volume di conversioni l'ottimizzazione non ha da imparare.
6. **Context hints come frasi**, sui temi e non sul nome del prodotto: chi cerca il nome è già arrivato.
7. **Soglia scritta prima di partire**, in unità di risultato e non in CPC.
8. **Lettura finale in GA4 con gli UTM**, non nel pannello.

## Fonti

Tutte consultate il 12/09/2026: [ads.openai.com](https://ads.openai.com/) · [Ads in ChatGPT: The Basics](https://help.openai.com/en/articles/20001207-ads-in-chatgpt-the-basics) · [Availability](https://help.openai.com/en/articles/20001245-ads-manager-availability) · [Account Setup](https://help.openai.com/en/articles/20001213-ads-manager-beta-account-setup) · [Overview](https://help.openai.com/en/articles/20001206-ads-manager-beta-overview) · [Campaigns](https://help.openai.com/en/articles/20001210-create-campaigns-for-chatgpt-ads) · [Ad Groups](https://help.openai.com/en/articles/20001211-create-ad-groups-for-chatgpt-ads) · [Ads](https://help.openai.com/en/articles/20001212-create-ads-for-chatgpt-ads) · [Daily Budgets](https://help.openai.com/en/articles/20001413-daily-budgets) · [Budget Pacing](https://help.openai.com/en/articles/20001515-budget-pacing) · [Maximize Results](https://help.openai.com/en/articles/20001425-maximize-results-bid-strategy) · [oCPC](https://help.openai.com/en/articles/20001412-conversion-optimized-campaigns) · [Conversion Measurement](https://help.openai.com/en/articles/20001409-conversion-measurement) · [Measure Results](https://help.openai.com/en/articles/20001214-measure-results) · [Custom Audiences](https://help.openai.com/en/articles/20001346-set-up-custom-audiences-for-your-campaign) · [Event Quality](https://help.openai.com/en/articles/20001513-understand-and-improve-event-quality) · [Crawler](https://help.openai.com/en/articles/20001243-advertiser-guidance-for-allowing-openai-web-crawlers) · [Billing](https://help.openai.com/en/articles/20001216-billing-payment) · [Bulk Upload Schema](https://help.openai.com/en/articles/20001218-bulk-upload-campaign-schema-checklist) · [FAQ](https://help.openai.com/en/articles/20001220-frequently-asked-questions) · [Troubleshooting](https://help.openai.com/en/articles/20001217-troubleshooting-common-issues) · [Measurement Pixel](https://developers.openai.com/ads/measurement-pixel) · [Conversions API](https://developers.openai.com/ads/conversions-api) · [Supported Events](https://developers.openai.com/ads/supported-events) · [Bidding and Budgets](https://developers.openai.com/ads/bidding-and-budgets) · [Targeting](https://developers.openai.com/ads/campaign-targeting) · [Ad Policies](https://openai.com/policies/ad-policies/) · [New ways to buy ChatGPT ads](https://openai.com/index/new-ways-to-buy-chatgpt-ads/) · [Expanding access](https://openai.com/index/expanding-access-to-ai-with-chatgpt-ads/)

⚠️ **Niente è stato verificato su un pannello**: alla prima apertura si riverificano minimo giornaliero in euro, soglia di pagamento, incentivo di benvenuto e limiti reali dei caratteri.