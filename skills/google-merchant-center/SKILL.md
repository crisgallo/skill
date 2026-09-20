---
name: "google-merchant-center"
description: "Regole operative verificate per aprire, alimentare e tenere pulito un account Google Merchant Center di un e-commerce italiano: feed e origini dati, attributi obbligatori, GTIN, prezzo e disponibilità che non combaciano, spedizione e resi, disapprovazioni e sospensioni, collegamento con Shopping e Performance Max, migrazione alla Merchant API. Usala ogni volta che un prodotto è disapprovato, una campagna Shopping o PMax non spende, il feed va rifatto, arriva un avviso di sospensione, o si eredita un Merchant Center da mettere in ordine, anche se Merchant Center non viene nominato."
---

# Google Merchant Center: regole operative

**Ultima verifica delle fonti: 20 settembre 2026.**

## 0. Manutenzione di questa skill (leggere per primo)

Merchant Center cambia nomi di menu, attributi obbligatori e date di enforcement più volte l'anno; nel 2026 ha perso il nome "Next", ha spento la Content API e ha riscritto i report. Quindi:

1. **Finestra di freschezza: due mesi.** Se la data in cima è più vecchia, si rileggono il [registro annunci (6192467)](https://support.google.com/merchants/announcements/6192467?hl=en) e la [pagina aggiornamenti della specifica (16989427)](https://support.google.com/merchants/answer/16989427?hl=en) prima di toccare un account che spende.
2. **Quando una fonte smentisce una regola scritta qui, si aggiorna la skill nello stesso turno**, si riscrive la data in cima e si annota cosa è cambiato e da quando, così si sa quali dati storici restano confrontabili.
3. Due metà da tenere distinte: **conoscenza di dominio** (verificata sulle pagine ufficiali, con URL accanto) e **meccanica del pannello** (sez. 16: si impara sbagliando e si scrive qui la prima volta).
4. Dove si guardano i cambiamenti: [annunci Merchant Center](https://support.google.com/merchants/announcements/6192467?hl=en) · [Merchant API latest updates](https://developers.google.com/merchant/api/latest-updates) · [blog Ads & Commerce](https://blog.google/products/ads-commerce/).
5. Le pagine Help hanno ID numerici stabili ma i titoli cambiano ("Diagnostica" è diventata "Richiede attenzione"): si cita sempre l'ID.

---

## 1. Prezzo e disponibilità: la disapprovazione che costa di più

**Il prezzo nel feed deve essere identico, al centesimo e nella stessa valuta, a quello che Googlebot legge sulla pagina di destinazione.** Google confronta il feed con la pagina e con i dati strutturati; se non combaciano il prodotto è disapprovato ("Mismatched value (page crawl) [price]") e i mismatch ripetuti sono trattati come **errori critici che possono portare alla sospensione dell'account** ([6098334](https://support.google.com/merchants/answer/6098334?hl=en), [14916353](https://support.google.com/merchants/answer/14916353?hl=en)).

- 🔴 **Prezzo caricato via JavaScript dopo il load = errore.** Google lo dice testualmente. Il prezzo va nell'HTML iniziale, e nei dati strutturati `Product/Offer` in JSON-LD nell'HTML iniziale ([merchant-listing](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing), [6069143](https://support.google.com/merchants/answer/6069143?hl=en)).
- **I dati strutturati devono mostrare lo stesso valore che vede il cliente**; una pagina che cambia prezzo per IP o browser viola le linee guida ([6069143](https://support.google.com/merchants/answer/6069143?hl=en)). Ogni variante con URL proprio ha il suo markup: il link nel feed punta alla variante, non al prodotto padre.
- **Prezzo barrato:** se il sito mostra un prezzo barrato, nel feed servono **entrambi** `price` (il barrato) e `sale_price` (quello pagato), con `sale_price_effective_date` e fuso orario corretti; un barrato in pagina senza `sale_price` nel feed è una disapprovazione a sé ([15621352](https://support.google.com/merchants/answer/15621352?hl=en)).
- **Aggiornamenti automatici degli articoli** (Prodotti → Automazioni): attivi di default, correggono `price`, `sale_price`, `availability`, `condition` leggendo schema.org; coprono una piccola parte del catalogo e **non sostituiscono il feed**; se gli estrattori non trovano il valore, il prodotto viene disapprovato lo stesso ([3246284](https://support.google.com/merchants/answer/3246284?hl=en)). Si lasciano accesi, non ci si affida.
- **Ordine di sincronizzazione:** prima si aggiorna il sito, poi il feed (via API subito dopo, o fetch programmato a ridosso). Feed prima del sito = mismatch garantito ([14916353](https://support.google.com/merchants/answer/14916353?hl=en)).
- Dopo la correzione: la nuova richiesta di verifica del sito richiede **fino a 12 ore** e nel frattempo non se ne può inviare un'altra; il recrawl dei prodotti arriva "nelle ore o nei giorni successivi" ([6098334](https://support.google.com/merchants/answer/6098334?hl=en)). Il crawl budget si alza da Search Console ([15621352](https://support.google.com/merchants/answer/15621352?hl=en)).
- ⚠️ Prezzo in Italia **IVA inclusa**; l'attributo `tax` è solo per USA/Canada e in UE non si usa ([7052112](https://support.google.com/merchants/answer/7052112?hl=en)).

---

## 2. Sospensione dell'account e "Rappresentazione ingannevole"

**Un problema a livello di account spegne tutto il catalogo, e con esso Shopping e la parte Shopping di Performance Max.** Quando Merchant Center è sospeso le campagne Shopping in Google Ads smettono di pubblicare ([13359353](https://support.google.com/google-ads/answer/13359353?hl=en)).

- **Avviso:** per la maggior parte delle violazioni arriva un'email di avviso **almeno 7 giorni prima** della sospensione, con i prodotti che restano visibili ma "a rendimento limitato" ([6150118](https://support.google.com/merchants/answer/6150118?hl=en), [12153802](https://support.google.com/merchants/answer/12153802?hl=en)). Per le violazioni "egregie" (Misrepresentation, malware) **nessun avviso: sospensione immediata** ([6150127](https://support.google.com/merchants/answer/6150127?hl=en)). [DA VERIFICARE] alcune pagine citano finestre di 28 giorni per casi specifici: non trovato su pagina ufficiale leggibile.
- **Revisione:** si richiede da Home → "Rivedi e correggi" o da Richiede attenzione; dura **3-7 giorni lavorativi**; ogni revisione fallita allunga il **periodo di attesa** in cui il pulsante è disabilitato e l'account resta sospeso ([13693195](https://support.google.com/merchants/answer/13693195?hl=en)). Quindi **non si chiede la revisione prima di aver sistemato tutto**: ogni tentativo bruciato costa giorni.
- **Cosa Google pretende sul sito, non nel feed** (Misrepresentation, [6150127](https://support.google.com/merchants/answer/6150127?hl=en)): ragione sociale e contatti reali (per l'Italia: P.IVA, indirizzo fisico, email e telefono funzionanti), **politica di reso e rimborso** visibile senza login, condizioni di spedizione, metodi di pagamento, prezzi completi senza costi nascosti. Un e-commerce senza pagina resi o con la P.IVA solo nel footer di una landing è il sospeso tipico italiano.
- **Collegamento con account Google Ads sospesi** è di per sé una violazione "Abuso della rete" ([6150118](https://support.google.com/merchants/answer/6150118?hl=en)): prima di collegare un Ads ereditato si controlla il suo stato.
- Il rendimento "limitato" durante l'avviso non si vede quasi mai in Google Ads: si controlla in Merchant Center, non nelle campagne.

---

## 3. Account: verifica del sito, collegamenti, agenzia

- **Verifica** (dimostrare che il sito è tuo) e **rivendicazione** (legarlo in esclusiva a un account) sono due passi distinti; **un URL può essere rivendicato da un solo account**: se un'agenzia precedente lo ha rivendicato altrove, si sovrascrive dal nuovo account e i prodotti dell'altro smettono di servire ([176793](https://support.google.com/merchants/answer/176793?hl=en)). Metodi: tag HTML/file, Google Tag Manager (serve amministrazione a livello di account), Google Analytics con accesso amministratore, email; Google può verificare da solo se già usa GA sul sito.
- **Collegamento Google Ads:** Impostazioni → Accesso e servizi → App e servizi → Google Ads; lo avvia un admin di Merchant Center, lo approva un admin di Google Ads; **non si collega un account amministratore (MCC)**, solo l'account cliente; fino a 500 account Ads per Merchant Center; scollegando, le campagne che usano i prodotti smettono di servire ([6159060](https://support.google.com/merchants/answer/6159060?hl=en)). Con la verifica in due passaggi attiva sull'account Google, va gestita prima del link.
- **Merchant Center for Agencies:** disponibile in tutto il mondo dall'11/05/2026, cruscotto unico su tutti i clienti con rilevamento anticipato dei problemi; si richiede a Google, non si apre da soli ([17072077](https://support.google.com/merchants/answer/17072077?hl=en)). Per un consulente con più e-commerce è lo strumento giusto al posto del giro quotidiano di login.
- **Termini di servizio:** regola empirica di terzi, non numero Google: fonti di settore riportano nuovi Termini dal **15/06/2026** con uso dei contenuti del merchant su superfici AI e indicizzazione delle email di marketing attiva di default (searchen 27/05/2026, lemon-web). La pagina ufficiale [160173](https://support.google.com/merchants/answer/160173?hl=en) è solo un indice per paese: [DA VERIFICARE] leggere i Termini Italia e l'opzione di opt-out sul pannello.

---

## 4. Origini dati: quale scegliere

**Ordine di preferenza per un e-commerce italiano:** 1) integrazione nativa della piattaforma o **Merchant API** (aggiornamenti frequenti, sincronizzati con il sito); 2) **file con recupero programmato** (fetch) da URL; 3) Google Sheets solo per cataloghi piccoli; 4) **scansione del sito** (website crawl / "Aggiungi prodotti dal tuo negozio online") solo come rete di sicurezza, mai come origine principale ([14990942](https://support.google.com/merchants/answer/14990942?hl=en), [12158480](https://support.google.com/merchants/answer/12158480?hl=en)).

- 🔴 **Un feed file scade dopo 30 giorni** senza aggiornamento e le campagne Shopping che lo usano smettono di servire ([13359353](https://support.google.com/google-ads/answer/13359353?hl=en)). Un caricamento manuale fatto una volta è una bomba a orologeria.
- ⛔ **Content API for Shopping spenta il 18/08/2026; dal 01/09/2026 le richieste ricevono errori progressivi.** Plugin, script e middleware devono essere già su Merchant API; per chi non ce la fa esiste un modulo di proroga ([compatibility overview](https://developers.google.com/merchant/api/guides/compatibility/overview), [latest updates](https://developers.google.com/merchant/api/latest-updates)). Su un account ereditato si chiede al fornitore del plugin (WooCommerce, PrestaShop, Magento) **quale API usa**: se risponde "Content API v2.1" il feed smetterà di aggiornarsi senza avviso in Merchant Center. Terze parti riportano la stessa migrazione per Google Ads Scripts (digitalapplied).
- **Prodotti "Trovati da Google" (scansione automatica):** Google scansiona il sito almeno ogni 24 ore, aggiunge i prodotti dai dati strutturati e **se lo stesso prodotto è anche nel feed caricato vince la versione caricata**; l'opt-out è in Origini dati; nascondere richiede 4-8 ore ([12158480](https://support.google.com/merchants/answer/12158480?hl=en)). Va bene per non perdere le novità, non per governare titoli e categorie.
- **Shopify / WooCommerce:** l'app ufficiale sincronizza ma raramente espone `custom_label`, `product_type` puliti o il `link` della variante: si affianca un'origine supplementare (sez. 8).
- **Feed label:** fino a 20 caratteri, solo A-Z maiuscole, 0-9, trattino e underscore; **non si cambia dopo la creazione dell'origine**; per un solo paese si usa il codice paese `IT` ([14994087](https://support.google.com/merchants/answer/14994087?hl=en)).

---

## 5. Attributi per l'Italia

Fonte: [specifica dati prodotto (7052112)](https://support.google.com/merchants/answer/7052112?hl=en) e [aggiornamenti 2026 (16989427)](https://support.google.com/merchants/answer/16989427?hl=en). Nomi italiani del pannello fra virgolette.

| Attributo | Regola |
|---|---|
| `id` | max 50 caratteri, unico e **stabile nel tempo**: cambiarlo azzera lo storico del prodotto in Ads |
| `title` "Titolo" | max 150; coerente con la pagina; per le varianti include colore/taglia |
| `description` "Descrizione" | max 5.000; coerente con la pagina |
| `link` | dominio verificato, https, niente interstitial, URL della variante |
| `image_link` "Link immagine" | **min 500×500 px con enforcement dal 31/01/2027**, avvisi già dal 14/04/2026; niente testo promozionale, watermark, bordi |
| `price` "Prezzo" | IVA inclusa, mai 0, formato `19.90 EUR` |
| `availability` "Disponibilità" | `in_stock`, `out_of_stock`, `preorder`, `backorder` (+ `availability_date` per preorder) |
| `shipping` "Spedizione" | **obbligatoria per l'Italia** (a livello prodotto o nelle impostazioni account) ([6324484](https://support.google.com/merchants/answer/6324484?hl=en)) |
| `brand` "Marca" | max 70; obbligatorio per i prodotti nuovi tranne libri, film, musica; vietato "Generico"/"N/A" |
| `gtin` / `mpn` | sez. 6 |
| `condition` "Condizione" | obbligatorio solo per usato/ricondizionato |
| `item_group_id`, `is_bundle`, `multipack` | **obbligatori in Italia** quando esistono varianti, bundle o multipack |
| `certification` | obbligatorio per i prodotti con etichetta energetica UE: `EC:EPREL:<codice>`; `energy_efficiency_class` non vale per l'UE |
| `google_product_category` | ID o percorso della tassonomia Google; decide policy e formati |
| `product_type` "Tipo di prodotto" | max 750; percorso proprio (`Casa > Cucina > Pentole`), è quello che si usa per i gruppi in Ads |
| `custom_label_0..4` | 5 etichette, fino a 1.000 valori ciascuna per account, 1-100 caratteri; compaiono in Ads in 24-48 ore ([6275295](https://support.google.com/google-ads/answer/6275295?hl=en)) |
| `video_link` | nuovo 2026: validazione tecnica dal 14/04/2026, pubblicazione e avvisi di qualità dal 30/06/2026 |
| `minimum_order_value`, `handling_cutoff_time` | nuovi dal 14/04/2026; **obbligatori dal 30/09/2026 in SEE/UK/CH per i prodotti con ritiro in negozio** insieme a `pickup_cost` (sez. 7) |

Le etichette `custom_label` sono l'unica leva pulita per separare margine, stagionalità e best seller in PMax: si compilano nel feed, non si improvvisano nei gruppi di schede.

---

## 6. Identificatori: il GTIN

**Se il prodotto ha un GTIN assegnato dal produttore e non lo si invia, il prodotto può essere disapprovato; se lo si inventa, peggio.** Google: "non indovinare né inventare un valore"; prefissi vietati 02, 04, 2 e range coupon 05, 98, 99 ([6324461](https://support.google.com/merchants/answer/6324461?hl=en)). Il GTIN è anche il requisito per i **benchmark di prezzo** (sez. 11).

- Senza GTIN: `brand` + `mpn` (MPN solo se assegnato dal produttore) ([6098295](https://support.google.com/merchants/answer/6098295?hl=en)).
- **`identifier_exists: no`** solo per artigianato, su misura, vintage, pezzi unici; se Google trova prova che un identificatore esiste, arriva un avviso ([6324478](https://support.google.com/merchants/answer/6324478?hl=en)). Un feed che mette `no` su tutto il catalogo per "far sparire gli errori" è un account che perde visibilità in silenzio.
- Bundle creati dal merchant: GTIN del prodotto principale, non dei componenti ([6324461](https://support.google.com/merchants/answer/6324461?hl=en)).

---

## 7. Spedizione, resi, valore minimo, qualità del negozio

- **Spedizione** ("Spedizione e resi" nel pannello): fino a 20 norme di spedizione per paese; tempi = "Tempo di elaborazione (giorni)" + "Tempo di transito (giorni)" + "Orario limite per ordinare"; le festività nazionali aggiungono un giorno automaticamente ([6069284](https://support.google.com/merchants/answer/6069284?hl=en)). Se nel feed si invia `shipping` con `price`, **le impostazioni account vengono ignorate per quel prodotto/paese, tempi e valore minimo compresi** ([6324484](https://support.google.com/merchants/answer/6324484?hl=en)): non si mischiano i due sistemi senza saperlo.
- **Resi:** la norma di reso in Merchant Center è **facoltativa ma raccomandata** e migliora il rendimento; deve coprire resi per difetto e non, con finestra, metodo, costi e tempi di rimborso; `return_policy_label` collega i prodotti a norme diverse ([10220642](https://support.google.com/merchants/answer/10220642?hl=en)). Quella **sul sito** invece è obbligatoria per Misrepresentation (sez. 2). Per l'Italia il minimo legale è il recesso di 14 giorni: una norma "no resi" è sospensione.
- **Valore minimo ordine e costo ritiro:** dal **30/09/2026** obbligatori in SEE, UK e Svizzera per i prodotti con ritiro in negozio ([annunci 28/04/2026](https://support.google.com/merchants/announcements/6192467?hl=en), [16989009](https://support.google.com/merchants/answer/16989009?hl=en)); il `minimum_order_value` a livello prodotto va inviato ogni volta che si usa `shipping` nel feed, altrimenti il minimo dell'account non viene applicato.
- **Qualità del negozio (Store Quality):** pagina "Qualità del negozio"; quattro aree (spedizione: tempi e costi; resi: finestra e costi, esclusi "no resi" e "solo difettosi"; navigazione: immagini alta risoluzione, immagini per articolo, velocità desktop e mobile; acquisto: promozioni disapprovate e wallet accettati come PayPal, Google Pay, Apple Pay); scala Basso → Eccezionale; calcolo giornaliero pesato sulle impressioni; una modifica alle norme impiega **fino a 30 giorni** a riflettersi ([14261098](https://support.google.com/merchants/answer/14261098?hl=en)).
- ⚠️ **Badge "Top Quality Store": non disponibile in Italia** (solo AU, CA, GB, IN, JP, NZ, US) ([14261098](https://support.google.com/merchants/answer/14261098?hl=en), [15215732](https://support.google.com/merchants/answer/15215732?hl=en)). Non si promette a un cliente italiano.

---

## 8. Origini supplementari e regole attributi

- Un'**origine dati supplementare** integra o sovrascrive attributi dell'origine principale, abbinata per `id`; **non aggiunge né rimuove prodotti** e non vive da sola ([15624457](https://support.google.com/merchants/answer/15624457?hl=en), [15157604](https://support.google.com/merchants/answer/15157604?hl=en)). Uso tipico: Google Sheet con `id`, `custom_label_0`, `product_type`, `google_product_category` sopra il feed del plugin.
- **Regole attributi** (Origini dati → regole): "Imposta su", "Estrai", "Prendi più recente" ([14994083](https://support.google.com/merchants/answer/14994083?hl=en)); se si cambia l'`id` in principale e supplementare, prima la principale ([14993352](https://support.google.com/merchants/answer/14993352?hl=en)). Le regole si usano per etichette e categorie, **non per "correggere" prezzo o disponibilità**: quello va sistemato alla fonte, altrimenti si fabbrica il mismatch della sez. 1.

---

## 9. Collegamento con Google Ads: Shopping e Performance Max

- **In PMax l'account Merchant Center non si cambia dopo la creazione della campagna**: account sbagliato = campagna da rifare; si scelgono anche paese di vendita o feed label ([13717096](https://support.google.com/google-ads/answer/13717096?hl=en)). **Una sola feed label per campagna**, valida per Shopping, PMax e Demand Gen ([14994087](https://support.google.com/merchants/answer/14994087?hl=en)).
- **Multi-paese:** si aggiungono i paesi nelle impostazioni dell'origine dati, con spedizione per ogni paese nella **stessa valuta dell'offerta**; la conversione automatica di valuta è ammessa ma l'utente capisce che non sei locale; il targeting geografico della campagna deve coprire i paesi dell'origine ([15404838](https://support.google.com/merchants/answer/15404838?hl=en)); `shopping_ads_excluded_country` per escludere un paese dagli annunci ma non dalle schede gratuite ([9837523](https://support.google.com/merchants/answer/9837523?hl=en-GB)).
- **Prodotti disapprovati:** non servono, e in una PMax la spesa si sposta sul resto del catalogo e sugli altri canali senza alcun avviso di campagna; si controlla la scheda Prodotti della campagna cercando gli stati diversi da "Approvato" ([13359353](https://support.google.com/google-ads/answer/13359353?hl=en)). Un calo del ROAS PMax si legge prima in Merchant Center, poi in Ads.
- Le regole di struttura PMax e Shopping (gruppi di asset, esclusioni, target) stanno nella skill `google-ads-performance`, sez. 9.

---

## 10. "Richiede attenzione" e stati dei prodotti

- La scheda **Prodotti → Richiede attenzione** (ex Diagnostica) mostra 3 card con i problemi a maggior impatto e il numero di prodotti colpiti; l'interruttore **"Correzioni prioritarie"** nasconde i problemi a impatto basso: **si spegne** quando si fa igiene, altrimenti gli avvisi minori spariscono dalla vista; "Visualizza cronologia" dà l'andamento degli stati per periodo, paese e con/senza annunci; ogni vista si scarica in CSV ([12476548](https://support.google.com/merchants/answer/12476548?hl=en)).
- Stati: Approvato, Limitato (solo alcuni paesi o metodi), Non approvato, In revisione, In elaborazione; la revisione richiede **fino a 3-5 giorni lavorativi per Shopping e "alcune settimane" per le schede gratuite** ([12488713](https://support.google.com/merchants/answer/12488713?hl=en)). "Visibilità" la controlla il merchant, "Stato" lo controlla Google.
- I problemi a livello prodotto restano isolati; quelli a livello account colpiscono tutto ([12153802](https://support.google.com/merchants/answer/12153802?hl=en)). Si parte sempre dalle card in alto, non dall'elenco.

---

## 11. Report in Merchant Center

- **Prezzi (Analytics → Prezzi):** benchmark = prezzo medio che tende a vincere più aste, click e conversioni sugli stessi GTIN; senza GTIN valido non c'è benchmark; con conversioni con dati carrello, `cost_of_goods_sold` e `auto_pricing_min_price` arrivano i suggerimenti di prezzo scontato con uplift stimato ([9626903](https://support.google.com/merchants/answer/9626903?hl=en)). Va letto **prima** di alzare un'offerta su un prodotto che perde le aste per prezzo.
- **Prodotti popolari (best seller):** rango per frequenza di ricerca, fascia di prezzo, in stock/fuori stock, filtrabile per paese e categoria, dati settimanali con 2 settimane di ritardo; report potenziato a giugno 2026, quindi ranghi e copertura prima/dopo non sono confrontabili; i dati non si rivendono né si espongono pubblicamente ([13299535](https://support.google.com/merchants/answer/13299535?hl=en), [annunci](https://support.google.com/merchants/announcements/6192467?hl=en)).
- 🔴 **Report rendimento cambiati dal 24/08/2026** con ricalcolo retroattivo al 01/07/2026: il traffico affiliato YouTube esce da "Organico" (calo apparente una tantum), le definizioni di click e impressioni organiche YouTube sono state riallineate, il report prodotti Ads include ora PMax, Video, App e Demand Gen (impressioni e click in aumento apparente); in arrivo la dimensione "Rete" ([17103877](https://support.google.com/merchants/answer/17103877?hl=en)). **Confronti anno su anno su questi report: solo da luglio 2026 in poi.**
- **Insight AI (AI Mode, AI Overview, Gemini):** annunciati il 27/05/2026, in rollout solo su US, CA, AU, IN, NZ ([17117204](https://support.google.com/merchants/answer/17117204?hl=en)): per l'Italia non c'è ancora nulla da leggere.
- Report personalizzati: componente aggiuntivo "Report personalizzati" ([9967959](https://support.google.com/merchants/answer/9967959?hl=en)).

---

## 12. Norme che colpiscono gli shop italiani

- **Consolidamento norme:** annuncio del 15/07/2026, in vigore da settembre 2026: norme Shopping ads e schede gratuite in un solo set, con indicazione di quali valgono solo per gli annunci; **nessun cambiamento sostanziale** ([annunci](https://support.google.com/merchants/announcements/6192467?hl=en), [6149970](https://support.google.com/merchants/answer/6149970?hl=en)).
- **Promozioni:** da gennaio 2026 ammessi sconti sugli abbonamenti (`redemption_restriction: subscribe_and_save`) e abbreviazioni come BOGO ([16796881](https://support.google.com/merchants/answer/16796881?hl=en)); le promozioni disapprovate pesano sulla Qualità del negozio (sez. 7). Per l'Italia il prezzo barrato deve rispettare il prezzo più basso dei 30 giorni precedenti (Codice del consumo, art. 17-bis): un barrato gonfiato è insieme mismatch e Misrepresentation.
- **Salute e farmaci:** farmaci con ricetta ammessi solo US/CA; OTC fuori dagli USA solo per farmacie certificate (LegitScript, poi domanda a Google, 5 giorni lavorativi); integratori non approvati vietati; per l'Italia vietati esplicitamente aborto e pillola del giorno dopo; **claim terapeutici su integratori e cosmetici = Misrepresentation** ([6150151](https://support.google.com/merchants/answer/6150151?hl=en)). Il catalogo "benessere" italiano va letto riga per riga.
- **Alcol:** Italia fra i paesi **ammessi con limitazioni**; niente minori, niente claim su prestazioni o salute, niente consumo con veicoli; nessuna certificazione richiesta ([12077694](https://support.google.com/merchants/answer/12077694?hl=en)). Le enoteche passano, i testi "vino che fa bene al cuore" no.
- Restano soggetti a restrizioni: adulti, gioco d'azzardo, marchi, alimenti HFSS ([6149970](https://support.google.com/merchants/answer/6149970?hl=en)).

---

## 13. Inventario locale (in breve)

Annunci di inventario locale e schede locali gratuite servono un negozio fisico: profilo dell'attività collegato, origine dati di inventario locale (o inventario aggiunto in automatico dal negozio online), verifica del negozio; opzioni "Ritiro oggi" e "Ritiro più tardi" ([3057972](https://support.google.com/merchants/answer/3057972?hl=en), [13461162](https://support.google.com/merchants/answer/13461162?hl=en)). Dal 30/09/2026 `pickup_cost` e `minimum_order_value` obbligatori nel SEE per i prodotti con ritiro (sez. 7). Per un e-commerce puro non si attiva.

---

## 14. Cosa è cambiato fra giugno e settembre 2026

- **15/06/2026:** nuovi Termini di servizio (fonte terza, sez. 3).
- **Giugno 2026:** report Prodotti popolari potenziato (sez. 11). **30/06/2026:** `video_link` in pubblicazione con avvisi di qualità (sez. 5).
- **Luglio 2026:** "Merchant Center Next" torna a chiamarsi Merchant Center; nessuna azione richiesta ([17252069](https://support.google.com/merchants/answer/17252069?hl=en)). **15/07/2026:** annuncio del consolidamento delle norme (sez. 12). Checkout links estesi a FR, PL e altri: non Italia.
- **18/08/2026:** Content API spenta; **01/09/2026** errori progressivi (sez. 4). Nella Merchant API: sovrascrittura resi a livello offerta (`returns`), integrazione UCP, notifiche `ACCOUNT_SERVICE` ([latest updates](https://developers.google.com/merchant/api/latest-updates)).
- **24/08/2026:** report rendimento riscritti, retroattivi al 01/07/2026 (sez. 11).
- **Settembre 2026:** norme unificate nel Centro assistenza (sez. 12). **30/09/2026:** obbligo `pickup_cost` e `minimum_order_value` per il ritiro in negozio nel SEE (sez. 7).
- Prossima scadenza: **31/01/2027** immagini sotto 500×500 px non più accettate (sez. 5).

---

## 15. Igiene di un account ereditato: ordine di controllo

1. **Stato dell'account** (Home e Richiede attenzione, card in alto): avvisi a livello account, email di avviso in corso, periodo di attesa attivo. Se c'è un avviso, la scadenza detta tutto il resto.
2. **Sito:** pagina resi, contatti con P.IVA e indirizzo, condizioni di vendita, metodi di pagamento, prezzi con IVA (sez. 2). Rivendicazione del dominio: su quale account è, e chi altro lo ha rivendicato (sez. 3).
3. **Origini dati:** tipo, data ultimo aggiornamento, scadenza a 30 giorni, plugin su Content API vs Merchant API (sez. 4); prodotti "Trovati da Google" attivi o no.
4. **Mismatch prezzo/disponibilità:** numero di prodotti disapprovati per page crawl, prezzo via JavaScript, prezzo barrato senza `sale_price`, ordine sito → feed (sez. 1). Automazioni attive.
5. **Identificatori:** GTIN mancanti su prodotti di marca, `identifier_exists: no` a tappeto (sez. 6).
6. **Spedizione e resi:** norma di spedizione per l'Italia, tempi realistici, `shipping` nel feed che sovrascrive l'account, norma di reso collegata (sez. 7).
7. **Collegamento Google Ads:** quale account, non MCC, stato dell'Ads collegato; feed label e paese usati dalle campagne PMax/Shopping (sez. 9).
8. **Categorie ed etichette:** `google_product_category` generica ("Abbigliamento" per tutto), `product_type` vuoto, `custom_label` assenti: senza queste PMax non si segmenta (sez. 5).
9. **Norme di settore:** salute, integratori, alcol, promozioni disapprovate (sez. 12).
10. **Report:** benchmark prezzo sui best seller e serie storiche spezzate al 01/07/2026 (sez. 11).
11. **Immagini** sotto 500×500 px: quante, prima del 31/01/2027 (sez. 5).

---

## 16. Meccanica del pannello (da verificare a mano)

- Dove sta l'interruttore delle Automazioni nella versione italiana ("Prodotti → Automazioni"?) e se disattivare "prezzo" spegne anche "disponibilità".
- Con "Correzioni prioritarie" acceso, quali avvisi GTIN e immagini spariscono dalla vista?
- Su un account con plugin WooCommerce/Shopify: nel dettaglio origine dati compare la dicitura dell'API usata (Merchant API vs Content API)?
- Se il feed invia `shipping` con `price` per l'Italia, la pagina "Spedizione e resi" segnala da qualche parte che le impostazioni account sono ignorate per quei prodotti?
- Dopo una revisione fallita, il pannello mostra la durata del periodo di attesa o solo il pulsante disabilitato?
- L'opt-out sull'uso delle email di marketing (Termini 15/06/2026): in quale menu sta, se esiste?

---

## 17. Cosa non fare mai

- Caricare un feed a mano "una volta" e non programmare il recupero: scade a 30 giorni.
- Correggere il prezzo con una regola attributo o in un'origine supplementare invece che sul sito.
- Mettere `identifier_exists: no` per far sparire gli errori GTIN.
- Chiedere la revisione dell'account prima di aver sistemato **tutte** le pagine del sito: ogni fallimento allunga l'attesa.
- Rivendicare un dominio senza sapere quale account lo perde.
- Creare una PMax scegliendo l'account Merchant Center sbagliato: non si cambia, si rifà.
- Promettere a un cliente italiano il badge Top Quality Store o gli insight AI: non disponibili in Italia.
- Confrontare i report rendimento di Merchant Center a cavallo del 01/07/2026 senza dirlo al cliente.
- Lasciare in feed un plugin che parla ancora Content API dopo il 01/09/2026.
- Mettere in Shopping integratori con claim terapeutici o vini con claim salutistici.

---

## Fonti (verificate 20/09/2026)

**Ufficiali Google, lette:** [Specifica dati prodotto (7052112)](https://support.google.com/merchants/answer/7052112?hl=en) · [Aggiornamenti specifica 2026 (16989427)](https://support.google.com/merchants/answer/16989427?hl=en) · [Registro annunci (6192467)](https://support.google.com/merchants/announcements/6192467?hl=en) · [Aggiornamenti automatici (3246284)](https://support.google.com/merchants/answer/3246284?hl=en) · [Dati strutturati per Merchant Center (6069143)](https://support.google.com/merchants/answer/6069143?hl=en) · [Merchant listing structured data](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing) · [Prezzo non corrispondente (6098334)](https://support.google.com/merchants/answer/6098334?hl=en) · [Aggiornamenti automatici: prezzo non corrispondente (14916353)](https://support.google.com/merchants/answer/14916353?hl=en) · [Prezzo barrato (15621352)](https://support.google.com/merchants/answer/15621352?hl=en) · [GTIN (6324461)](https://support.google.com/merchants/answer/6324461?hl=en) · [identifier_exists (6324478)](https://support.google.com/merchants/answer/6324478?hl=en) · [GTIN mancante (6098295)](https://support.google.com/merchants/answer/6098295?hl=en) · [Misrepresentation (6150127)](https://support.google.com/merchants/answer/6150127?hl=en) · [Abuso della rete, avviso 7 giorni (6150118)](https://support.google.com/merchants/answer/6150118?hl=en) · [Problemi in Merchant Center (12153802)](https://support.google.com/merchants/answer/12153802?hl=en) · [Avvisi e sospensioni (13693195)](https://support.google.com/merchants/answer/13693195?hl=en) · [Norme Shopping (6149970)](https://support.google.com/merchants/answer/6149970?hl=en) · [Salute e farmaci (6150151)](https://support.google.com/merchants/answer/6150151?hl=en) · [Alcolici (12077694)](https://support.google.com/merchants/answer/12077694?hl=en) · [Promozioni, aggiornamento norme (16796881)](https://support.google.com/merchants/answer/16796881?hl=en) · [Verifica e rivendicazione sito (176793)](https://support.google.com/merchants/answer/176793?hl=en) · [Collegamento Google Ads (6159060)](https://support.google.com/merchants/answer/6159060?hl=en) · [Merchant Center for Agencies (17072077)](https://support.google.com/merchants/answer/17072077?hl=en) · [Next diventa Merchant Center (17252069)](https://support.google.com/merchants/answer/17252069?hl=en) · [Crea origine dati (14990942)](https://support.google.com/merchants/answer/14990942?hl=en) · [Prodotti aggiunti automaticamente (12158480)](https://support.google.com/merchants/answer/12158480?hl=en) · [Feed label (14994087)](https://support.google.com/merchants/answer/14994087?hl=en) · [Più paesi (15404838)](https://support.google.com/merchants/answer/15404838?hl=en) · [Origine supplementare (15624457)](https://support.google.com/merchants/answer/15624457?hl=en) · [Regole attributi (14994083)](https://support.google.com/merchants/answer/14994083?hl=en) · [Spedizione, attributo (6324484)](https://support.google.com/merchants/answer/6324484?hl=en) · [Spedizione, impostazioni (6069284)](https://support.google.com/merchants/answer/6069284?hl=en) · [Resi (10220642)](https://support.google.com/merchants/answer/10220642?hl=en) · [Valore minimo ordine (16989009)](https://support.google.com/merchants/answer/16989009?hl=en) · [Qualità del negozio (14261098)](https://support.google.com/merchants/answer/14261098?hl=en) · [Badge Top Quality Store (15215732)](https://support.google.com/merchants/answer/15215732?hl=en) · [Schede gratuite (9199328)](https://support.google.com/merchants/answer/9199328?hl=en) · [Richiede attenzione (12476548)](https://support.google.com/merchants/answer/12476548?hl=en) · [Stato prodotti (12488713)](https://support.google.com/merchants/answer/12488713?hl=en) · [Prezzi, benchmark (9626903)](https://support.google.com/merchants/answer/9626903?hl=en) · [Prodotti popolari (13299535)](https://support.google.com/merchants/answer/13299535?hl=en) · [Report rendimento 24/08/2026 (17103877)](https://support.google.com/merchants/answer/17103877?hl=en) · [Insight AI (17117204)](https://support.google.com/merchants/answer/17117204?hl=en) · [Inventario locale (3057972)](https://support.google.com/merchants/answer/3057972?hl=en) · [Google Ads: PMax e Merchant Center (13717096)](https://support.google.com/google-ads/answer/13717096?hl=en) · [Google Ads: problemi Merchant Center (13359353)](https://support.google.com/google-ads/answer/13359353?hl=en) · [Google Ads: etichette personalizzate (6275295)](https://support.google.com/google-ads/answer/6275295?hl=en) · [Merchant API: migrazione (compatibility)](https://developers.google.com/merchant/api/guides/compatibility/overview) · [Merchant API: latest updates](https://developers.google.com/merchant/api/latest-updates) · [blog.google: Google Marketing Live 2026](https://blog.google/products/ads-commerce/google-marketing-live-2026-collection/).

**Terze parti (dichiarate come tali):** [productsup: migrazione Merchant API](https://www.productsup.com/blog/google-merchant-api-migration-what-changes-before-the-august-2026-deadline-and-how-to-prepare/) · [digitalapplied: Ads Scripts e Merchant API](https://www.digitalapplied.com/blog/merchant-api-google-ads-scripts-april-22-migration) · [searchen 27/05/2026: nuovi Termini](https://www.searchen.com/2026/05/27/google-expands-merchant-data-usage-in-new-merchant-center-terms-as-ai-shopping-evolves/) · [lemon-web: Termini 15/06/2026](https://www.lemon-web.net/lemon-blog/web-development/google-merchant-center-terms-are-changing-on-15-june-2026-what-store-owners-should-know) · [ppc.land: consolidamento norme](https://ppc.land/google-merges-two-shopping-policy-sets-but-adds-zero-merchant-restrictions/).

**Non leggibili o non confermate al 20/09/2026:** il troubleshooter prezzi [14280358](https://support.google.com/merchants/troubleshooter/14280358?hl=en) (solo albero interattivo, corpo non recuperato via fetch); la pagina Termini di servizio [160173](https://support.google.com/merchants/answer/160173?hl=en) (solo indice per paese: testo dei Termini Italia e data 15/06/2026 da ricontrollare a mano); la finestra di avviso di 28 giorni citata da snippet di ricerca ma non trovata in nessuna pagina letta.
