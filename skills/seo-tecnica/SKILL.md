---
name: "seo-tecnica"
description: "Regole operative verificate su Google Search Central per audit SEO tecnici e on-page di e-commerce e siti B2B italiani: robots.txt, noindex, canonical, duplicati da filtri e varianti, redirect di migrazione, sitemap, hreflang, dati strutturati, Core Web Vitals, JavaScript, AI Overviews, core update. Usala ogni volta che si audita un sito ereditato, si segue un restyling, un rebranding o un cambio dominio, si controlla la consegna di un'agenzia prima del go-live, si legge un calo in Search Console o si deve dire a un SEO specialist cosa verificare e in che ordine."
---

# SEO tecnica (Google Search): regole operative

**Ultima verifica delle fonti: 20 settembre 2026.**

---

## 0. Manutenzione di questa skill (leggere per primo)

1. **Finestra di freschezza: tre mesi.** Le regole di scansione e indicizzazione cambiano poco; cambiano in fretta le funzioni di Search Console, i dati strutturati ammessi e tutto ciò che riguarda AI Overviews e AI Mode (sez. 6, 13). Se la data qui sopra ha più di tre mesi, prima di citare una regola a un cliente si ricontrolla; per la sezione 13 basta un mese.
2. **Quando una fonte smentisce una regola scritta qui, si aggiorna la skill nello stesso turno**, si riscrive la data in cima e si annota cosa è cambiato e da quando.
3. Due metà da tenere distinte: **conoscenza di dominio** (cosa fa Google: verificata su developers.google.com/search/docs e sulla guida di Search Console) e **meccanica del pannello** (sez. 17: come si comporta Search Console quando ci lavori dentro, si impara sbagliando e si scrive qui la prima volta).
4. Dove si guardano i cambiamenti: [aggiornamenti della documentazione](https://developers.google.com/search/updates) · [Search Central Blog](https://developers.google.com/search/blog) · [Search Status Dashboard](https://status.search.google.com/summary) (ranking update e incidenti) · [What's new in Search Console](https://support.google.com/webmasters/answer/9270309).
5. Questa skill non sostituisce il SEO specialist: dice al consulente cosa pretendere, in che ordine e con quale fonte in mano.

---

## 1. Scansione e indicizzazione: le tre leve che decidono tutto il resto

**robots.txt, noindex e canonical fanno tre cose diverse e non sono intercambiabili.** Confonderle è l'errore che costa di più: pagine che restano indicizzate, o pagine buone che spariscono.

| leva | cosa fa | cosa NON fa | fonte |
|---|---|---|---|
| `robots.txt` Disallow | impedisce la **scansione** | non impedisce l'indicizzazione: un URL bloccato ma linkato può comparire in SERP senza descrizione | [robots intro](https://developers.google.com/search/docs/crawling-indexing/robots/intro) |
| `noindex` (meta o `X-Robots-Tag`) | toglie la pagina dall'indice quando Googlebot la **legge** | non funziona se la pagina è bloccata da robots.txt: Google non la legge e non vede il noindex | [block-indexing](https://developers.google.com/search/docs/crawling-indexing/block-indexing) |
| `rel="canonical"` | **segnale forte, non direttiva**: suggerisce quale URL mostrare fra duplicati | non blocca né scansione né indicizzazione; Google può scegliere un canonical diverso | [consolidate-duplicate-urls](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls) |

- ⛔ **Mai "noindex + Disallow" sulla stessa pagina**: il Disallow impedisce di leggere il noindex. Per de-indicizzare si lascia scansionabile con noindex, e si aspetta la riscansione: "può richiedere mesi" per pagine poco importanti ([block-indexing](https://developers.google.com/search/docs/crawling-indexing/block-indexing)); si accelera con Controllo URL → Richiedi indicizzazione.
- ⛔ **Staging e ambienti di test si proteggono con password**, non con robots.txt: Google stesso indica "noindex o protezione con password" come unici modi per tenere fuori una pagina ([robots intro](https://developers.google.com/search/docs/crawling-indexing/robots/intro)).
- **robots.txt**: vale solo per host+protocollo+porta dove è servito; limite **500 KiB** (oltre, ignorato); cache **fino a 24 ore**; campi supportati solo `user-agent`, `allow`, `disallow`, `sitemap` (`crawl-delay` e `noindex` nel robots non esistono per Google); a parità di conflitto vince la regola **più lunga**, poi la meno restrittiva. **4xx (tranne 429) = come se il file non esistesse, tutto scansionabile**; **5xx = 12 ore di stop alla scansione, poi 30 giorni con l'ultima versione buona** ([robots_txt spec](https://developers.google.com/search/docs/crawling-indexing/robots/robots_txt)). Conseguenza: un robots.txt che risponde 500 dopo un deploy ferma la scansione del sito intero.
- **Ordine dei segnali di canonicalizzazione** per Google: 1) redirect, 2) `rel="canonical"`, 3) inclusione in sitemap (segnale debole). Google preferisce HTTPS e gli URL dentro cluster hreflang. Non si usa robots.txt per canonicalizzare, non si dichiarano canonical diversi con tecniche diverse, non si mette un frammento `#` come canonical; il self-canonical sulla pagina canonica va messo ([consolidate-duplicate-urls](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls)).
- **Rapporto Indicizzazione delle pagine, le due voci che spaventano** ([7440203](https://support.google.com/webmasters/answer/7440203)): **"Rilevata, attualmente non indicizzata"** = trovata ma non ancora scansionata, "in genere Google voleva scansionare l'URL ma questo avrebbe sovraccaricato il sito, quindi ha riprogrammato" (problema di capacità del server o di volume di URL inutili, sez. 10); **"Scansionata, attualmente non indicizzata"** = scansionata e scartata, "potrebbe essere indicizzata in futuro; non serve rinviarla" (problema di qualità o duplicazione, non tecnico). **"Duplicato, Google ha scelto un canonical diverso dall'utente"** = il canonical dichiarato non è creduto: si guarda perché (contenuti identici, link interni che puntano altrove, redirect).
- Un 2xx non garantisce nulla: "i sistemi di indicizzazione possono indicizzare il contenuto, ma non è garantito" ([http-network-errors](https://developers.google.com/search/docs/crawling-indexing/http-network-errors)).

---

## 2. Duplicati su e-commerce: varianti, filtri, paginazione, parametri

- **Navigazione a faccette** ([faceted navigation](https://developers.google.com/search/docs/crawling-indexing/crawling-managing-faceted-navigation)): i filtri generano URL "nuovi" che Google scansiona a valanga e rubano tempo agli URL utili. Se i filtri **non** devono essere indicizzati: **robots.txt Disallow sulle combinazioni di parametri è il metodo più efficace**; in alternativa i filtri via frammento `#` (Google non lo scansiona); `rel="canonical"` e `nofollow` sono "generalmente meno efficaci nel lungo periodo". Se invece **devono** essere indicizzati (filtro = intento di ricerca, es. "scarpe running donna"): separatore `&` standard, **ordine dei parametri sempre uguale**, niente filtri duplicati nella stessa combinazione, **404 vero sui risultati vuoti** (non redirect, non soft 404).
- **Paginazione** ([pagination](https://developers.google.com/search/docs/specialty/ecommerce/pagination-and-incremental-page-loading)): `rel="prev/next"` **non è più usato**. Ogni pagina ha il **proprio canonical** ("non usare la prima pagina come canonical della sequenza"); URL con `?page=n`, mai frammenti; le varianti di ordinamento della stessa lista si tengono fuori con `noindex`. "Carica altro" e scroll infinito: Google segue gli `href` degli `<a>` e "non attiva funzioni JavaScript che richiedono azioni dell'utente", quindi servono link `<a href>` sequenziali reali.
- **Varianti prodotto** ([URL structure](https://developers.google.com/search/docs/specialty/ecommerce/designing-a-url-structure-for-ecommerce-sites)): ogni variante può avere un URL proprio (`/t-shirt/verde` o `/t-shirt?colore=verde`); se il parametro è opzionale, **il canonical è l'URL senza parametro**. I frammenti (`#nero`) sono la stessa pagina per Google. Mai session ID, codici di tracciamento o valori relativi all'utente nei link interni. Nei dati strutturati le varianti si dichiarano con `ProductGroup` / `isVariantOf` (sez. 6).
- Parole chiave nel path sì (`/product/maglia-nera-colletto-bianco`, non `/product/3243`), parametri come `?chiave=valore`.

---

## 3. Migrazioni, restyling, rebranding: redirect

**Un cambio di URL senza mappa di redirect testata è una perdita di traffico programmata.** Fonte unica di riferimento: [site move with URL changes](https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes) e [redirects](https://developers.google.com/search/docs/crawling-indexing/301-redirects).

- **Permanenti** (Google mostra la destinazione): **301, 308**, meta refresh e HTTP refresh a 0 secondi; redirect JavaScript solo come ultima risorsa. **Temporanei** (Google continua a mostrare l'origine): **302, 303, 307**, refresh > 0 s. Per una migrazione si usano **redirect permanenti lato server**; i "crypto redirect" (link "siamo andati qui") non contano.
- **Catene**: Google segue **fino a 10 hop**, ma raccomanda **massimo 3** ([site move](https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes), [http-network-errors](https://developers.google.com/search/docs/crawling-indexing/http-network-errors)). Su un sito ereditato le catene vecchie (http→https→www→nuovo path) si accorciano al primo salto.
- ⛔ **Mai redirect di massa alla home**: Google li tratta come **soft 404**. Ogni vecchio URL va a una pagina equivalente; quello che non ha equivalente risponde **404 o 410** (per Google sono uguali: entrambi tolgono l'URL dall'indice).
- **Durata**: i redirect si tengono "il più a lungo possibile, in genere **almeno 1 anno**". Le fluttuazioni di ranking durante la riscansione sono normali: per un sito medio "alcune settimane o più" prima che i nuovi URL siano mostrati, di più per siti grandi. **Nessuna promessa di zero perdita** sta nella documentazione: chi la fa, la fa per conto suo.
- **Capacità server**: Google "scansionerà temporaneamente il nuovo sito più del solito"; un hosting sottodimensionato al go-live produce 5xx, e i **5xx persistenti tolgono URL dall'indice**; il 429 è trattato come errore server ([http-network-errors](https://developers.google.com/search/docs/crawling-indexing/http-network-errors)).
- **Cambio di indirizzo** (Search Console → Impostazioni → Cambio di indirizzo, [9370220](https://support.google.com/webmasters/answer/9370220)): solo per **cambio di dominio o sottodominio**, non per http→https, www/non-www o cambio di path. Prerequisiti: entrambe le proprietà verificate dallo stesso account, proprietà a livello di dominio, **301 dalla vecchia home alla nuova**. Google inoltra i segnali per **180 giorni**; dopo, "non riconosce alcuna relazione fra i due siti". Si annulla solo entro i 180 giorni, rimuovendo prima i 301.
- **Sitemap**: si carica la sitemap nuova e si tengono verificate entrambe le proprietà per seguire nel rapporto Sitemap e in Indicizzazione delle pagine il travaso fra vecchi e nuovi URL. [DA VERIFICARE] il paragrafo esatto della guida che consiglia di lasciare in Search Console anche una sitemap con i vecchi URL per far scoprire prima i redirect: la pratica è comune e non contraddice la guida, ma non è stata riletta il 20/09/2026.
- **Errori tipici elencati da Google**: noindex o robots.txt dello staging lasciati in produzione; redirect verso URL inesistenti; sitemap non aggiornate; server insufficiente.
- **Restyling senza cambio URL** (stesso dominio, stessi path): non serve il Cambio di indirizzo; serve comunque il confronto pre/post di title, canonical, hreflang, dati strutturati, link interni e CWV, perché sono le cose che un tema nuovo rompe in silenzio (sez. 16).

---

## 4. Sitemap

Fonte: [build-sitemap](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap).

- Limiti: **50 MB non compressi o 50.000 URL per file**; oltre, si spezza e si usa un sitemap index. UTF-8 obbligatorio. Un sitemap in una sottocartella vale solo per quella cartella, salvo invio da Search Console: si mette nella root.
- **`<lastmod>` è usato solo se "coerente e verificabile"**: deve essere la data dell'ultima modifica significativa. Una sitemap con lastmod = oggi su tutte le pagine insegna a Google a ignorarlo. **`<priority>` e `<changefreq>` sono ignorati**.
- Estensioni: immagini, video, notizie, versioni localizzate (hreflang, sez. 5). Sitemap immagini: **fino a 1.000 `<image:image>` per `<url>`**, immagini su CDN o altro dominio ammesse se quel dominio è verificato in Search Console; i tag `caption`, `geo_location`, `title`, `license` sono deprecati ([image-sitemaps](https://developers.google.com/search/docs/crawling-indexing/sitemaps/image-sitemaps)).
- Invio: rapporto Sitemap in Search Console, API, riga `Sitemap:` nel robots.txt. La sitemap è un **segnale debole** di canonical: ci vanno solo URL canonici, 200, indicizzabili. Sitemap piena di URL con redirect, noindex o 404 = rapporto Sitemap che segnala errori e crawl sprecato.

---

## 5. Siti internazionali e hreflang

Fonte: [localized-versions](https://developers.google.com/search/docs/specialty/international/localized-versions).

- Tre metodi equivalenti: `<link rel="alternate" hreflang>` nell'HTML, header HTTP (per PDF), **sitemap** (`xhtml:link`). Su un e-commerce con molte lingue la sitemap è la più manutenibile.
- **Reciprocità obbligatoria**: "se due pagine non si puntano a vicenda, i tag vengono ignorati". Ogni versione elenca **se stessa e tutte le altre**.
- Codici: solo **ISO 639-1** per la lingua e **ISO 3166-1 alpha-2** per la regione (`it`, `it-IT`, `it-CH`, `de-CH`); mai la sola regione; `UK` ed `EU` **non esistono** per Google (si usa `gb`). `x-default` per la pagina di scelta lingua o come fallback.
- Hreflang e canonical convivono: ogni versione localizzata ha il **proprio self-canonical**; se il contenuto principale **non è tradotto**, per Google sono duplicati e la canonicalizzazione prevale.
- Senza hreflang Google "può comunque trovare" le versioni, ma su un sito .it/.ch/.de con la stessa lingua italiana in due paesi non lo fa in modo affidabile.

---

## 6. Dati strutturati che Google usa nel 2026

Fonte: [galleria](https://developers.google.com/search/docs/appearance/structured-data/search-gallery) e [intro](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data). Formato **JSON-LD**; il markup deve descrivere **contenuto visibile**; i requisiti danno **eleggibilità, non garanzia** di visualizzazione. Si valida con il **Rich Results Test** (eleggibilità Google) e si monitora nei rapporti "Miglioramenti" di Search Console; lo Schema Markup Validator controlla solo la sintassi schema.org, non l'eleggibilità.

- **Product**: due famiglie. **Merchant listing** = pagine dove **si può comprare** (non pagine che rimandano ad altri venditori); obbligatori `name`, `image`, `offers` con `price` **> 0** e `priceCurrency`; raccomandati `availability`, `shippingDetails`, `hasMerchantReturnPolicy`, `gtin`/`sku`, `brand`, `itemCondition`; varianti con `ProductGroup` / `isVariantOf` / `inProductGroupWithID`; markup sulle pagine prodotto, **non sulle liste** ([merchant-listing](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing)). **Product snippet** = pagine senza acquisto diretto, più proprietà per le recensioni ([product](https://developers.google.com/search/docs/appearance/structured-data/product)). Novità 20/05/2026: proprietà `hasAdultConsideration` su Merchant listing e Product variant ([updates](https://developers.google.com/search/updates)). Prezzo, disponibilità e resi nel markup devono coincidere con il feed Merchant Center, altrimenti si perde in entrambi.
- **Organization**: in home o nella pagina "chi siamo"; nessuna proprietà obbligatoria; per un'azienda italiana si mettono `vatID` (partita IVA), `iso6523Code`, `address`, `telephone`, `logo` (min 112×112), `sameAs`; ospita anche la **return policy e il programma fedeltà a livello di merchant** ([organization](https://developers.google.com/search/docs/appearance/structured-data/organization)).
- **Breadcrumb**: `ListItem` con `position`, `name`, `item`; l'ultimo elemento può omettere `item` ([breadcrumb](https://developers.google.com/search/docs/appearance/structured-data/breadcrumb)). Deve rispecchiare la navigazione visibile.
- **Article**: nessuna proprietà obbligatoria; `headline`, `image` (più formati 16:9, 4:3, 1:1, min 50.000 px totali), `datePublished`/`dateModified` in ISO 8601 con fuso, `author` uno per campo con solo il nome in `author.name` ([article](https://developers.google.com/search/docs/appearance/structured-data/article)).
- 🔴 **FAQ e HowTo**: il rich result **HowTo non esiste più** (da settembre 2023); **FAQ** solo per "siti governativi e sanitari noti e autorevoli" ([faqpage](https://developers.google.com/search/docs/appearance/structured-data/faqpage)). Un e-commerce con FAQPage su ogni scheda non ottiene nulla: si toglie dal backlog, non si vende come "ottimizzazione". La **Sitelinks search box** non è più nella galleria.
- Regola per il backlog: solo i tipi in galleria; tutto il resto (`WebPage`, `Person` a caso, `speakable` su un catalogo) è lavoro senza effetto misurabile.

---

## 7. Core Web Vitals e page experience

Fonti: [core-web-vitals](https://developers.google.com/search/docs/appearance/core-web-vitals), [web.dev/vitals](https://web.dev/articles/vitals), [rapporto CWV di Search Console (9205520)](https://support.google.com/webmasters/answer/9205520), [page-experience](https://developers.google.com/search/docs/appearance/page-experience).

| metrica | buono | da migliorare | scarso |
|---|---|---|---|
| **LCP** (caricamento) | ≤ 2,5 s | ≤ 4 s | > 4 s |
| **INP** (reattività, ha sostituito FID nel 2024) | ≤ 200 ms | ≤ 500 ms | > 500 ms |
| **CLS** (stabilità visiva) | ≤ 0,1 | ≤ 0,25 | > 0,25 |

- Si misura al **75° percentile** delle visite reali, **mobile e desktop separati**; lo stato del gruppo di URL è quello della **metrica peggiore**. **Dati di campo (CrUX)** sono quelli che contano; **Lighthouse è laboratorio** (usa TBT come proxy dell'INP) e serve a trovare la causa, non a dichiarare il risultato. Un sito con poco traffico non compare nel rapporto CWV: "dati insufficienti" non vuol dire "tutto bene".
- **Ranking**: Google dice che i CWV "sono in linea con ciò che i sistemi di ranking premiano" e che **"non esiste un singolo segnale"** di page experience; "Google mostra sempre il contenuto più pertinente anche se la page experience è mediocre" e un buon rapporto CWV **non garantisce** posizioni. Conseguenza: i CWV si sistemano per conversione e per non essere penalizzati a parità di contenuto, non si vendono come leva di ranking primaria. Punteggio Lighthouse 100 non è un KPI.
- Autovalutazione page experience (Google): CWV buoni, HTTPS, resa su mobile, niente interstitial invadenti, pubblicità che non copre il contenuto, contenuto principale distinguibile.
- Dopo una modifica, i dati di campo cambiano con **28 giorni** di finestra CrUX: regola empirica di terzi ampiamente citata, non riletta su fonte ufficiale il 20/09/2026 [DA VERIFICARE la finestra esatta sul rapporto CrUX].

---

## 8. JavaScript: cosa Google vede e cosa no

Fonte: [javascript-seo-basics](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics), [dynamic-rendering](https://developers.google.com/search/docs/crawling-indexing/javascript/dynamic-rendering).

- Tre fasi: **scansione → rendering (coda) → indicizzazione**. Il rendering usa una **Chromium evergreen**; la coda può richiedere "pochi secondi, ma anche di più". Google "vede solo il contenuto visibile nell'HTML renderizzato": **contenuto che compare dopo clic, scroll, tab o filtri non esiste per Google**.
- Routing con **History API**, mai frammenti `#`. Link solo come `<a href>`: gli `onclick` non vengono seguiti.
- ⚠️ **Rimuovere o cambiare un `noindex` via JavaScript "può non funzionare come atteso"**: se l'HTML iniziale ha noindex, il rendering può non avvenire. Il noindex va deciso lato server.
- **Il rendering dinamico è "una soluzione tampone, non raccomandata"**; le alternative sono SSR, rendering statico, hydration. Un e-commerce headless in consegna deve servire nell'HTML iniziale titolo, canonical, hreflang, dati strutturati, prezzo, testo e link di categoria: si verifica con Controllo URL → Visualizza pagina sottoposta a scansione → HTML e screenshot, non con "Visualizza sorgente" del browser.
- Lazy loading di immagini e contenuti secondo le linee guida Google, altrimenti le immagini non entrano in Google Immagini.

---

## 9. Title, meta description, heading, immagini

- **Title link** ([title-link](https://developers.google.com/search/docs/appearance/title-link)): generazione "completamente automatica" dal `<title>`, dall'H1/titolo visibile, da `og:title`, dal testo prominente, dagli anchor in entrata, dal `WebSite` structured data. Google riscrive quando il title è mezzo vuoto, obsoleto, boilerplate ripetuto, keyword stuffing, lingua sbagliata, nome sito duplicato. **Non c'è limite di lunghezza**: viene troncato "in base alla larghezza del dispositivo". I "60 caratteri" sono una regola empirica di terzi, non un numero Google. Ogni pagina ha un title unico, descrittivo, brand breve con separatore.
- **Meta description** ([snippet](https://developers.google.com/search/docs/appearance/snippet)): Google la usa "a volte", quando descrive meglio del contenuto; **nessun limite di lunghezza**; descrizioni identiche su tutto il sito sono inutili. Controlli: `nosnippet`, `max-snippet`, `data-nosnippet` (valgono anche per AI Overviews, sez. 13).
- **Heading** ([SEO starter guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide)): l'ordine semantico serve agli screen reader, "dal punto di vista di Google Search non importa se sono fuori ordine"; nessun numero ideale. Il **meta keywords non è usato**; la **lunghezza del contenuto da sola non conta**; ripetere parole chiave è contro le policy spam. Un audit che conta H1 e densità di keyword sta misurando il nulla.
- **Immagini** ([google-images](https://developers.google.com/search/docs/appearance/google-images)): l'**alt è l'attributo più importante**, descrittivo e non stuffing; nomi file parlanti (indizio "molto leggero"); `<img src>` con `srcset`/`<picture>` e fallback; **le immagini in CSS background non sono indicizzate**; formati BMP, GIF, JPEG, PNG, WebP, SVG, AVIF; immagine vicina al testo pertinente; sitemap immagini per cataloghi grandi. Su un e-commerce l'alt vuoto sulle foto prodotto è il difetto più frequente e il più economico da sistemare.

---

## 10. Link interni e crawl budget

Fonte: [crawl budget](https://developers.google.com/search/docs/crawling-indexing/large-site-managing-crawl-budget).

- **Il crawl budget è un problema solo per**: siti con **oltre 1 milione di pagine uniche** che cambiano con moderata frequenza, siti con **oltre 10.000 pagine** che cambiano **ogni giorno**, siti con molti URL in "Rilevata, attualmente non indicizzata". Sono "stime, non soglie esatte". **Una PMI con 3.000 URL non ha un problema di crawl budget**: ha un problema di URL inutili o di server, e si chiama con il suo nome.
- Crawl budget = **capacità** (quanto il server regge) × **domanda** (quanto Google vuole quel sito: dimensione, aggiornamenti, qualità). Cosa aiuta: consolidare duplicati, **404/410 sulle pagine rimosse**, sitemap con lastmod affidabile, risposte veloci, `304` sui contenuti immutati, niente soft 404 e catene. Cosa **non** aiuta: `noindex` (Google "richiede comunque la pagina e poi la scarta"), robots.txt "temporaneo" per spostare budget, `nofollow` sui link interni.
- **Link interni**: Google scopre URL dagli `href`; una pagina senza link interni in entrata vive solo di sitemap (segnale debole). Su e-commerce: categorie raggiungibili dal menu, prodotti dalle categorie con paginazione reale, breadcrumb coerenti col markup; anchor text descrittivi ([SEO starter guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide)). Le pagine orfane (nel sitemap ma non linkate) si trovano confrontando crawl del sito e sitemap.
- Statistiche di scansione: Search Console → Impostazioni → Statistiche di scansione. Si guardano risposte 5xx/429, tempo medio di risposta, e "per scopo" (aggiornamento vs scoperta): sono i numeri che spiegano "Rilevata, non indicizzata".

---

## 11. Controlli: `site:`, Controllo URL, rapporti

- **`site:`** ([search operators](https://developers.google.com/search/docs/monitor-debug/search-operators/all-search-site)): "non restituisce necessariamente tutti gli URL indicizzati", **non ordina i risultati**, e `site:https://www.example.com` dà risultati diversi da `site:example.com`. È "pensato per gli utenti": serve a verificare se una singola pagina è indicizzata, a trovare spam (`site:esempio.it viagra casino`) e URL vecchi/di staging sopravvissuti, **non a contare l'indice**. Il conteggio vero è in Indicizzazione delle pagine.
- **Controllo URL**: indice Google (canonical scelto, ultima scansione, noindex visto o no) e test live (HTML renderizzato, screenshot, risorse bloccate). È l'unico modo per sapere se Google vede il noindex, il canonical e il contenuto JS.
- Rapporti da aprire in ordine su un sito ereditato: Indicizzazione delle pagine → Sitemap → Impostazioni/Statistiche di scansione → Segnali web essenziali → Miglioramenti (dati strutturati) → Rendimento con confronto di periodo → Azioni manuali e Problemi di sicurezza.

---

## 12. E-E-A-T, contenuti utili, policy spam

- **E-E-A-T non è un fattore di ranking** ("No, non lo è", [SEO starter guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide)); è la lente dei quality rater e "una miscela di fattori" che i sistemi cercano di premiare; **la fiducia (Trust) è la più importante**, le altre contribuiscono ([creating-helpful-content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content)). Non si vende "ottimizzazione E-E-A-T"; si sistemano le cose concrete: chi firma (autore visibile), come è fatto (trasparenza anche sull'uso di IA "dove ragionevolmente atteso"), perché esiste (per le persone, non per il ranking).
- **Il "helpful content system" non esiste più come sistema separato**: "a marzo 2024 è diventato parte dei sistemi di ranking principali" ([ranking-systems-guide](https://developers.google.com/search/docs/appearance/ranking-systems-guide)). Un calo non si attribuisce più a "HCU": si legge come core update (sez. 14).
- **Contenuti generati con IA**: consentiti; è spam se prodotti "con lo scopo primario di manipolare il ranking" (**scaled content abuse**). Altre policy che toccano PMI ed e-commerce: **cloaking**, **doorway pages** (una pagina per ogni città con lo stesso testo), **redirect ingannevoli**, **expired domain abuse** ([spam-policies](https://developers.google.com/search/docs/essentials/spam-policies)).
- 🔴 **Site reputation abuse, aggiornamento del 28/08/2026** ([spam-policies](https://developers.google.com/search/docs/essentials/spam-policies), [blog agosto 2026](https://developers.google.com/search/blog)): contenuti di terzi pubblicati su un sito autorevole per sfruttarne i segnali. **Nello SEE (Italia inclusa) le pagine in violazione non ricevono azione manuale ma vengono "categorizzate come separate dal dominio principale"** e si posizionano da sole; fuori dallo SEE resta l'azione manuale. Conseguenza per chi affitta sezioni del sito a coupon, casinò o guest post: in Italia non arriva l'avviso in Search Console, arriva il calo della sezione senza spiegazione.

---

## 13. AI Overviews e AI Mode: cosa è documentato e cosa no

Fonti: [ai-features](https://developers.google.com/search/docs/appearance/ai-features), [guida all'ottimizzazione per l'IA generativa (15/05/2026)](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide), [rapporto IA generativa in Search Console (16984139)](https://support.google.com/webmasters/answer/16984139), [controllo IA generativa (16908024)](https://support.google.com/webmasters/answer/16908024).

- **"Non ci sono requisiti aggiuntivi né ottimizzazioni speciali"** per comparire in AI Overviews o AI Mode: contano indicizzazione, eleggibilità allo snippet e le stesse regole di qualità. Google dichiara esplicitamente che **`llms.txt`, file "per l'IA", Markdown o markup dedicati "vengono ignorati"** e "non aiutano né danneggiano"; niente "chunking", niente stile di scrittura per l'IA, niente caccia a menzioni inautentiche. **AEO/GEO come servizio separato non ha fonte Google**. Per prodotti e negozi: **feed Merchant Center** e **Profilo dell'attività**.
- **Reporting** (cambiato nel 2026): dal 03/06/2026 (UK) e per tutti dal 31/08/2026 esiste in Search Console il **rapporto Rendimento per l'IA generativa** (Search e Discover): **solo impressioni**, per pagina, paese, data e dispositivo; **niente clic, CTR o query**. Non compare sulle proprietà con poche impressioni IA. I clic da pagine con AI Overviews restano dentro il rapporto Rendimento "Web" senza filtro separato. Anomalia nota: impressioni sottostimate 13–17/08/2026, ripristinate il 21/08 ([data anomalies](https://support.google.com/webmasters/answer/6211453)). Conseguenza: **il traffico da AI Overviews non è misurabile in modo isolato**; chi lo riporta con un numero lo sta stimando con strumenti terzi.
- **Opt-out**: interruttore a livello di proprietà in Search Console per escludere il sito da AI Overviews, AI Mode e IA in Discover; "non è usato come segnale di ranking" altrove. Per limitare l'uso nei sistemi di addestramento: Google-Extended nel robots.txt. Controlli fini: `nosnippet`, `max-snippet`, `data-nosnippet`, `noindex`.
- **Non documentato da Google**: la percentuale di query con AI Overview per settore, l'effetto sul CTR, il peso di citazioni e menzioni, il funzionamento degli agenti (UCP citato come "emergente", senza istruzioni operative). Su queste cose si dice "non c'è fonte" e si misura con i propri dati.

---

## 14. Core update: come si legge un calo

Fonte: [core-updates](https://developers.google.com/search/docs/appearance/core-updates), [Search Status Dashboard](https://status.search.google.com/summary).

1. Si prende la data del calo e si confronta con la **dashboard**: ranking update recenti: **December 2025 core** (11/12/2025, 18 giorni), **February 2026 Discover update** (05/02/2026, 21 giorni), **March 2026 spam** (24/03), **March 2026 core** (27/03–08/04/2026), **May 2026 core** (21/05–02/06/2026), **June 2026 spam** (24/06, 2 giorni), **August 2026 spam** (18/08, 2 giorni e 16 ore). Nessun core update fra il 02/06 e il 20/09/2026: un calo di luglio–settembre 2026 **non è un core update** e va cercato altrove (migrazione, noindex, server, stagionalità, spam update se il sito ha contenuti a rischio).
2. Si analizza **almeno una settimana intera dopo la fine del rollout**, confrontando "questa settimana con una settimana prima dell'inizio del rollout" (Rendimento → confronto di periodo; query e pagine, non solo totale).
3. Non esiste un fix: si rilegge il sito con le domande di [creating-helpful-content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content). "Alcune modifiche hanno effetto in pochi giorni, ma possono servire diversi mesi", e il recupero può richiedere **il core update successivo**. Un piccolo calo di posizione non richiede "azioni drastiche".
4. Prima di dire "core update" si escludono i cali tecnici: si guarda Indicizzazione delle pagine e Statistiche di scansione nello stesso periodo. Un calo che parte il giorno di un deploy è un deploy.

---

## 15. Igiene di un sito ereditato: ordine di controllo

1. **robots.txt** in produzione: risponde 200? blocca risorse CSS/JS o intere sezioni? contiene regole di staging? (sez. 1)
2. **noindex**: quali URL lo hanno (Indicizzazione delle pagine → "Esclusa dal tag noindex"); ci sono categorie o prodotti dentro? Staging o dominio di test indicizzati (`site:`)?
3. **Canonical**: self-canonical presente, non a URL con redirect/404, non tutti alla home; "Google ha scelto un canonical diverso" quante righe?
4. **Redirect**: catene http/https/www, vecchi URL del sito precedente ancora richiesti (Statistiche di scansione, log), redirect alla home.
5. **Sitemap**: inviata, 200, solo URL canonici e indicizzabili, lastmod credibile.
6. **Indicizzazione delle pagine**: rapporto fra pagine indicizzate e pagine attese; volume di "Rilevata/Scansionata, non indicizzata" e "Duplicato".
7. **Filtri, ordinamenti, parametri e paginazione**: quanti URL generano, come sono gestiti (sez. 2).
8. **Rendering**: HTML iniziale vs renderizzato su una scheda prodotto e una categoria (sez. 8).
9. **Hreflang** se ci sono più lingue o paesi: reciprocità, codici, x-default (sez. 5).
10. **Dati strutturati**: rapporti Miglioramenti; Product/Merchant listing sulle schede, Organization in home, FAQPage inutile da togliere (sez. 6).
11. **Segnali web essenziali** e HTTPS (sez. 7); certificato, mixed content.
12. **Title e meta description** duplicati o boilerplate; alt vuoti sulle immagini prodotto (sez. 9).
13. **Rendimento**: confronto 12 mesi, cali sovrapposti a date di deploy o di update (sez. 14).
14. **Azioni manuali, Problemi di sicurezza**, e sezioni "affittate" a terzi (sez. 12).
15. **Chi ha accesso** a Search Console e chi ha verificato la proprietà: agenzie passate con accesso da proprietario si rimuovono.

---

## 16. Consegna di un sito nuovo da agenzia: cosa pretendere prima del go-live

Si chiede per iscritto e si verifica, non si chiede "avete fatto la SEO?".

- **Ambiente di staging protetto da password** (non da robots.txt) e **piano di rimozione di noindex/Disallow al go-live**, con chi lo fa e chi lo controlla entro un'ora dalla messa online (Controllo URL sulla home e su una scheda prodotto).
- **Mappa dei redirect** completa: ogni URL indicizzato o con traffico/backlink (export da Search Console Rendimento 16 mesi + sitemap vecchia + crawl) → destinazione equivalente, **301/308 lato server, un solo salto**, 404/410 per ciò che non ha equivalente, niente "tutto alla home". Testata su staging con un crawler prima e sul sito vivo dopo.
- **Parità on-page**: title, meta description, canonical, hreflang, dati strutturati (Rich Results Test), breadcrumb, testi di categoria, alt: confronto pagina per pagina su un campione, e HTML iniziale per un sito headless (sez. 8).
- **Sitemap nuova** pronta al go-live; proprietà Search Console già verificate (verifica DNS a livello di dominio, che sopravvive al cambio tema/hosting); **Cambio di indirizzo** solo se cambia il dominio (sez. 3).
- **Continuità di misurazione**: stesso container **GTM** e stesso ID di misurazione **GA4** (o nuovo stream documentato), dataLayer e-commerce con gli stessi nomi evento, consenso e Consent Mode invariati, chiavi di GA4 e collegamenti Google Ads/Search Console verificati sul nuovo sito il giorno stesso. Un go-live che azzera lo storico GA4 non è un restyling, è una perdita di dati.
- **Capacità server e monitoraggio**: 5xx/429 e tempo di risposta nelle Statistiche di scansione per le prime 4 settimane; CWV di campo dopo 28 giorni, lab prima del go-live.
- **Cosa ci si aspetta e per quanto**: fluttuazioni per "alcune settimane o più", redirect mantenuti almeno un anno, nessuna promessa scritta di "zero perdita" (sez. 3).

---

## 17. Meccanica del pannello (da verificare a mano)

- Il rapporto **Rendimento per l'IA generativa** in Search Console: dove sta nel menu in italiano e con quale nome esatto? Compare su una proprietà italiana con poche impressioni IA o resta nascosto?
- L'interruttore di **opt-out dall'IA generativa**: dove sta nelle impostazioni della proprietà e chi (proprietario o utente completo) può cambiarlo?
- Dopo un **Cambio di indirizzo**, i dati del rapporto Rendimento della vecchia proprietà restano leggibili per tutti i 180 giorni o si interrompono prima?
- Nel rapporto **Indicizzazione delle pagine**, dopo quanto tempo una rimozione di noindex + "Richiedi indicizzazione" si riflette nella riga "Esclusa dal tag noindex"?
- Il **Rich Results Test** su una pagina protetta da password o su staging: accetta l'HTML incollato per Merchant listing con lo stesso esito del test da URL?
- **Statistiche di scansione** su una proprietà a livello di dominio: mostra i sottodomini (staging, CDN) separati o aggregati?

---

## 18. Cosa non fare mai

- Bloccare in robots.txt una pagina che si vuole de-indicizzare, o lasciare il robots.txt dello staging in produzione.
- Promettere a un cliente che una migrazione "non perde niente": Google scrive fluttuazioni per settimane e redirect per almeno un anno.
- Redirect di massa alla home, o redirect 302 "per sicurezza" su un cambio definitivo.
- Usare il Cambio di indirizzo per http→https o per un cambio di path.
- Canonical della paginazione alla pagina 1; `rel="prev/next"` come soluzione; ordinamenti e filtri lasciati indicizzabili senza intento di ricerca.
- Vendere FAQPage, HowTo, "ottimizzazione E-E-A-T", `llms.txt` o "GEO" come interventi con effetto documentato da Google.
- Contare l'indice con `site:` o giudicare i CWV dal punteggio Lighthouse.
- Attribuire a un core update un calo che non coincide con una data della Search Status Dashboard.
- Andare in produzione con un sito headless senza aver visto l'HTML renderizzato in Controllo URL.
- Cambiare tema, hosting o dominio senza aver prima esportato 16 mesi di Rendimento e la lista degli URL indicizzati: dopo, quei dati non si ricostruiscono.

---

## Fonti (verificate 20/09/2026)

**Ufficiali Google, lette:** [robots.txt: introduzione](https://developers.google.com/search/docs/crawling-indexing/robots/intro) · [robots.txt: specifica (500 KiB, 4xx/5xx, cache)](https://developers.google.com/search/docs/crawling-indexing/robots/robots_txt) · [noindex](https://developers.google.com/search/docs/crawling-indexing/block-indexing) · [Canonicalizzazione](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls) · [Codici HTTP, 10 hop, 404=410, 5xx](https://developers.google.com/search/docs/crawling-indexing/http-network-errors) · [Redirect](https://developers.google.com/search/docs/crawling-indexing/301-redirects) · [Trasferimento con cambio URL](https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes) · [Cambio di indirizzo (9370220)](https://support.google.com/webmasters/answer/9370220) · [Rapporto Indicizzazione delle pagine (7440203)](https://support.google.com/webmasters/answer/7440203) · [Navigazione a faccette](https://developers.google.com/search/docs/crawling-indexing/crawling-managing-faceted-navigation) · [Paginazione e-commerce](https://developers.google.com/search/docs/specialty/ecommerce/pagination-and-incremental-page-loading) · [Struttura URL e-commerce](https://developers.google.com/search/docs/specialty/ecommerce/designing-a-url-structure-for-ecommerce-sites) · [Crawl budget](https://developers.google.com/search/docs/crawling-indexing/large-site-managing-crawl-budget) · [Sitemap](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap) · [Sitemap immagini](https://developers.google.com/search/docs/crawling-indexing/sitemaps/image-sitemaps) · [hreflang](https://developers.google.com/search/docs/specialty/international/localized-versions) · [Galleria dati strutturati](https://developers.google.com/search/docs/appearance/structured-data/search-gallery) · [Intro dati strutturati](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data) · [Product](https://developers.google.com/search/docs/appearance/structured-data/product) · [Merchant listing](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing) · [Organization](https://developers.google.com/search/docs/appearance/structured-data/organization) · [Breadcrumb](https://developers.google.com/search/docs/appearance/structured-data/breadcrumb) · [Article](https://developers.google.com/search/docs/appearance/structured-data/article) · [FAQPage (eleggibilità e rimozioni)](https://developers.google.com/search/docs/appearance/structured-data/faqpage) · [Core Web Vitals](https://developers.google.com/search/docs/appearance/core-web-vitals) · [Page experience](https://developers.google.com/search/docs/appearance/page-experience) · [Rapporto CWV (9205520)](https://support.google.com/webmasters/answer/9205520) · [web.dev: Web Vitals](https://web.dev/articles/vitals) · [JavaScript SEO basics](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics) · [Rendering dinamico](https://developers.google.com/search/docs/crawling-indexing/javascript/dynamic-rendering) · [Title link](https://developers.google.com/search/docs/appearance/title-link) · [Snippet e meta description](https://developers.google.com/search/docs/appearance/snippet) · [SEO starter guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide) · [Google Immagini](https://developers.google.com/search/docs/appearance/google-images) · [Operatore site:](https://developers.google.com/search/docs/monitor-debug/search-operators/all-search-site) · [Contenuti utili ed E-E-A-T](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) · [Guida ai sistemi di ranking](https://developers.google.com/search/docs/appearance/ranking-systems-guide) · [Policy spam (site reputation 28/08/2026)](https://developers.google.com/search/docs/essentials/spam-policies) · [AI features](https://developers.google.com/search/docs/appearance/ai-features) · [Guida all'ottimizzazione per l'IA generativa](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) · [Core update](https://developers.google.com/search/docs/appearance/core-updates) · [Search Status Dashboard](https://status.search.google.com/summary) · [Aggiornamenti documentazione](https://developers.google.com/search/updates) · [Indice Search Central Blog](https://developers.google.com/search/blog) · [blog.google: controlli e rapporti IA per i siti (03/06 e 31/08/2026)](https://blog.google/products-and-platforms/products/search/new-controls-website-owners/).

**Terze parti (solo per confermare date e contenuti di pagine non lette):** [Search Engine Journal: rapporti IA in Search Console per tutti (31/08/2026)](https://www.searchenginejournal.com/google-search-console-ai-reports-rolled-out-worldwide/587836/) · [Search Engine Land: March 2026 core completato](https://searchengineland.com/google-march-2026-core-update-rollout-is-now-complete-473883) · [Search Engine Land: May 2026 core completato](https://searchengineland.com/google-may-2026-core-update-rollout-is-now-complete-479119).

**Non leggibili via fetch il 20/09/2026, da ricontrollare a mano:** [Search Central Blog 06/2026: rapporti IA generativa](https://developers.google.com/search/blog/2026/06/gen-ai-performance-reports) (solo titolo, corpo non recuperato; contenuto preso da SEJ e dalla guida 16984139) · [Blog 08/2023: modifiche HowTo e FAQ](https://developers.google.com/search/blog/2023/08/howto-faq-changes) (solo titolo; contenuto preso dalle note nella pagina FAQPage) · [Guida Search Console: rapporto IA generativa (16984139)](https://support.google.com/webmasters/answer/16984139) e [controllo IA generativa (16908024)](https://support.google.com/webmasters/answer/16908024) (viste solo tramite risultati di ricerca) · storico completo della [Search Status Dashboard](https://status.search.google.com/products/rGHU1uWEsY7kf7WB79q7/history) (404; usata la pagina summary).
