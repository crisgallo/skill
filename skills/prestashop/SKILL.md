---
name: prestashop
description: "Regole operative verificate per fare audit, brief agli sviluppatori e tracciamento su un negozio PrestaShop (1.7, 8, 9) senza svilupparlo: versioni e PHP supportati, fine vita, aggiornamento, prestazioni e debug mode, SEO (URL, canonical, contenuti duplicati, redirect prodotti, sitemap, hreflang), GA4/GTM, Merchant Center, Meta Pixel e CAPI, multinegozio, sicurezza, licenze Addons, migrazione a 9. Usala ogni volta che un cliente o un'agenzia ha un e-commerce PrestaShop, anche se dice solo 'il negozio', 'il sito' o 'il modulo': prima di installare un tag, prima di attivare un feed, prima di accettare un preventivo di aggiornamento."
---

# PrestaShop: regole operative

**Ultima verifica delle fonti: 20 settembre 2026.**

## 0. Manutenzione di questa skill (leggere per primo)

1. **Finestra di freschezza: tre mesi.** PrestaShop pubblica una minor l'anno e patch di sicurezza ogni 4-8 settimane; la matrice PHP e lo stato dei rami cambiano a ogni rilascio. Se la data in cima ha più di tre mesi, si rileggono le release notes prima di dire a un cliente "sei aggiornato".
2. **Quando una fonte smentisce una regola scritta qui, si aggiorna la skill nello stesso turno**, si riscrive la data in cima e si annota cosa è cambiato e da quando.
3. Due metà da tenere distinte: **conoscenza di dominio** (verificata su devdocs, docs, build blog, Addons, Google) e **meccanica del pannello** (sez. 15: domande, si imparano sul back office e si scrivono qui la prima volta).
4. Dove si guardano i cambiamenti: [build.prestashop-project.org](https://build.prestashop-project.org/) (release, "Core Monthly", tag security), [devdocs core-updates](https://devdocs.prestashop-project.org/9/modules/core-updates/9.0/), [advisories Friends of Presta](https://security.friendsofpresta.org/), [ps_googleanalytics releases](https://github.com/PrestaShop/ps_googleanalytics/releases).

---

## 1. Versioni, PHP e fine vita: la regola che decide se il negozio è difendibile

**Il ramo mantenuto è uno solo per major: quando esce una minor nuova, la precedente è fuori manutenzione subito.** Le patch escono entro 6 settimane da un bug bloccante o da una falla ([devdocs, patch release lifecycle](https://devdocs.prestashop-project.org/9/project/release/patch-release-lifecycle/)).

Stato al 20/09/2026:

| Ramo | Stato | Fonte |
|---|---|---|
| **1.6.x** | fuori manutenzione da anni | – |
| **1.7.8.x** | solo sicurezza dal 05/01/2023, **finito il 10/06/2025** con l'uscita di 9.0.0 | [build 1.7.8 extended](https://build.prestashop-project.org/news/2023/178-in-extended-support-phase/), [build 9.0](https://build.prestashop-project.org/news/2025/prestashop-9-0-available/) |
| **8.0 / 8.1** | fuori manutenzione (solo 8.2.x mantenuto) | [build 8.2 extended](https://build.prestashop-project.org/news/2025/82x-extended-support-phase/) |
| **8.2.x** | supporto esteso dal 04/07/2025: solo falle, bug critici, nuovi hook. Ultima 8.2.8 del 18/08/2026. **Finisce con l'uscita di 10.0.0** | [build 8.2.8](https://build.prestashop-project.org/news/2026/prestashop-8-2-8-security-release/) |
| **9.0.x** | fuori manutenzione dal 23/03/2026 (uscita di 9.1.0) | [build 9.1](https://build.prestashop-project.org/news/2026/prestashop-9-1-0-available/) |
| **9.1.x** | **ramo stabile corrente**: 9.1.5 del 18/08/2026, dichiarata ultima della linea prima di 9.2; ramo cancellato dai repository | [build 9.1.5](https://build.prestashop-project.org/news/2026/prestashop-9-1-5-security-release/), [Core Monthly 08/2026](https://build.prestashop-project.org/news/2026/core-monthly-2026-08-01-2026-08-31/) |
| **9.2** | feature freeze 09/07/2026, Beta 1 22/07/2026, **stabile non ancora uscita**: One Page Checkout nativo, Extra Properties, "Ask AI". Mai in produzione una beta | [build 9.2 beta](https://build.prestashop-project.org/news/2026/prestashop-9-2-beta1/) |

**Matrice PHP ufficiale** ([devdocs 9](https://devdocs.prestashop-project.org/9/basics/installation/system-requirements/), [devdocs 8](https://devdocs.prestashop-project.org/8/basics/installation/system-requirements/), [devdocs 1.7](https://devdocs.prestashop-project.org/1.7/basics/installation/system-requirements/)):

- **9.1**: PHP 8.1–8.5 (raccomandato 8.5). **9.0**: 8.1–8.4 (raccomandato 8.4). MySQL 5.7+ o MariaDB 10.2+, `memory_limit` **512M**, Apache 2.4+ o Nginx, `allow_url_fopen` attivo.
- **8.0–8.2**: PHP 7.2–8.1 (raccomandato 8.1; 7.2–8.0 "non raccomandate" perché fuori supporto PHP). `memory_limit` 256M.
- **1.7.8**: PHP 7.1–8.0 (raccomandato 7.4). **1.7.0–1.7.3**: 5.3–7.3. Sotto 1.7.4 non esiste PHP 7.4.

🔴 **Perché i negozi restano fermi:** un 1.7.8 non regge PHP 8.1, un 8.2 non regge PHP 8.2. Chi resta su 1.7/8 sta girando su una PHP a fine vita, e l'hosting che aggiorna PHP d'ufficio rompe il negozio. L'alternativa (cambiare versione) rompe tema e moduli (sez. 12). Non esiste la terza via: il preventivo di aggiornamento va accettato o si mette in conto un negozio senza patch di sicurezza.

⚠️ La pagina ufficiale non pubblica un calendario di fine vita con date: le scadenze sono "quando esce la major successiva". Nessuna data per 10.0 al 20/09/2026.

---

## 2. Aggiornamento: Update Assistant, non FTP

- Lo strumento ufficiale è il modulo **Update Assistant** (`autoupgrade`, v7.x; 7.6.6 ad agosto 2026): parte da **1.7 o superiore**, richiede PHP 7.1+, fa backup e ripristino, ha una CLI, canali "online / online_recommended / local" ([GitHub autoupgrade](https://github.com/PrestaShop/autoupgrade)). Per 9.1 serve la **7.6.0+**, che rileva i moduli incompatibili prima di partire ([build 9.1](https://build.prestashop-project.org/news/2026/prestashop-9-1-0-available/)).
- **Da 1.6 si passa in due tappe**: prima 1.6 → 1.7 con autoupgrade 4.14.3, poi 1.7 → 8/9 con la versione corrente ([GitHub autoupgrade](https://github.com/PrestaShop/autoupgrade)).
- 🔴 **Il modulo disinstalla da solo i moduli che giudica incompatibili**, anche senza consenso esplicito (segnalazione [#1773](https://github.com/PrestaShop/autoupgrade/issues/1773), 9.0.3 → 9.1.0). Prima di lanciare: esporto della lista moduli con versioni, e verifica di quali hanno una versione per la major di arrivo.
- Sempre su **staging** con copia del database; mai sul negozio vivo la prima volta. Backup completo file + DB anche se il modulo lo fa da sé ([build 9.1.5](https://build.prestashop-project.org/news/2026/prestashop-9-1-5-security-release/)).

---

## 3. Prestazioni e debug: le tre impostazioni che si controllano prima di misurare

Pannello: **Parametri avanzati > Prestazioni** (Advanced Parameters > Performance) ([docs 8, Performance](https://docs.prestashop-project.org/v.8-documentation/user-guide/configuring-shop/advanced-parameters/performance)).

1. 🔴 **Modalità debug (Debug mode) = No in produzione.** Con Sì il negozio mostra stack trace con percorsi e query a chiunque e rallenta. Corrisponde a `_PS_MODE_DEV_ = false` in `config/defines.inc.php`; anche il profiler `_PS_DEBUG_PROFILING_ = false` ([devdocs, optimizations](https://devdocs.prestashop-project.org/9/scale/optimizations/)).
2. **Smarty: "Non ricompilare mai i file template"** (Never recompile) e cache **File System**, non MySQL. "Forza compilazione" è per chi sviluppa il tema e dimezza le prestazioni se lasciata.
3. **CCC** (Combina, comprimi e memorizza nella cache): smart cache CSS e JS attive. Se dopo l'attivazione il tema si rompe, è un modulo che inietta asset male: si segnala allo sviluppatore, non si spegne CCC per sempre.
4. Cache applicativa: **APCu** su un solo front, **memcached** centralizzato su più front; su un solo front con MySQL locale la sezione Cache si può lasciare vuota ([devdocs, optimizations](https://devdocs.prestashop-project.org/9/scale/optimizations/)). Redis non compare fra le opzioni native al 20/09/2026.
5. Hosting: `memory_limit` 512M, `max_execution_time` 300, opcache attivo (numeri devdocs, stessa pagina). Immagini WebP/AVIF e CDN sono scelte del tema e dell'hosting: da chiedere in brief, non impostazioni del pannello.

---

## 4. SEO: URL e canonical

Pannello: **Parametri negozio > Traffico e SEO > SEO e URL** ([docs 8, SEO and URLs](https://docs.prestashop-project.org/v.8-documentation/user-guide/configuring-shop/shop-parameters/traffic/seo-and-urls)).

- **URL semplificato (Friendly URL) = Sì**, richiede mod_rewrite. Senza, le URL sono `index.php?id_product=8`.
- 🔴 **Reindirizza all'URL canonico = 301 (Move Permanently).** Le tre opzioni sono nessuno / 301 / 302: con "nessuno" lo stesso prodotto risponde su più URL (con e senza id categoria, con id combinazione, con parametri) e il duplicato è certo. 302 solo se la URL principale deve cambiare a breve.
- **URL accentati**: disattivare su negozi italiani con nomi prodotto accentati, altrimenti si generano URL con caratteri non ASCII che poi vengono codificati diversamente da feed, GTM e Search Console.
- **Disabilita MultiViews di Apache = Sì** se le URL semplificate rispondono a caso.
- **Schema degli URL**: le route sono configurabili (8 campi). Chi toglie `{id}` dalle URL prodotto o categoria cambia tutte le URL del negozio: si fa solo con piano di redirect e mai dopo che il catalogo è indicizzato.
- ⚠️ **"Genera file robots.txt" sovrascrive il file esistente**: le regole aggiunte a mano spariscono. Si rigenera e poi si riaggiungono le righe custom (stessa pagina docs). Il file generato blocca `?order=` e, dalla 9.0, `?q=` (sez. 5).
- Meta title e description per pagina statica (indice, contatti, 404, ecc.) e per lingua stanno in fondo alla stessa pagina; per prodotti e categorie stanno nella **scheda SEO** dell'entità ([docs 8, Managing products](https://docs.prestashop-project.org/v.8-documentation/user-guide/selling/managing-catalog/managing-products)).

---

## 5. SEO: le trappole di contenuto duplicato che PrestaShop crea da solo

1. **Combinazioni.** La URL prodotto porta l'id della combinazione (`1-1-nome.html`) e ogni variante è una URL. Il canonical nativo punta alla URL senza id combinazione, che a sua volta reindirizza alla combinazione di default; la storia di questa scelta è nelle issue [#9508](https://github.com/PrestaShop/PrestaShop/issues/9508) e [#26676](https://github.com/PrestaShop/PrestaShop/issues/26676). Da verificare su ogni tema: i temi custom spesso sovrascrivono `head.tpl` e perdono il canonical.
2. **Navigazione a faccette (`ps_facetedsearch`).** I filtri producono URL con `?q=Colore-Blu` e simili. **Dalla 9.0.0** le pagine filtrate (`q`) e ordinate (`order`) escono con meta **noindex** e `robots.txt` blocca `q=` ([PR #37066](https://github.com/PrestaShop/PrestaShop/pull/37066), merge 11/10/2024). **Su 8.x e 1.7** c'è solo il blocco robots.txt e il canonical alla categoria, nessun noindex ([discussione #40335](https://github.com/PrestaShop/PrestaShop/discussions/40335), 15/12/2025): Google può indicizzare comunque le URL filtrate linkate. Su 8.x serve uno sviluppatore o un modulo SEO per il noindex. Nel modulo esistono opzioni "consenti ai robot di usare i filtri condizione/disponibilità/produttore": si mettono a No salvo strategia esplicita.
3. **Paginazione.** `?page=2` è una URL distinta. [DA VERIFICARE] il comportamento del canonical sulle pagine successive alla prima per versione: si controlla sul sorgente della pagina 2 di una categoria prima di parlarne al cliente.
4. **Lingue.** Ogni lingua ha il prefisso `/it/`, `/en/`. Il tema Classic emette `<link rel="alternate" hreflang>` per ogni lingua attiva da `$urls.alternative_langs` e il canonical da `$page.canonical` ([classic-theme head.tpl](https://github.com/PrestaShop/classic-theme/blob/develop/templates/_partials/head.tpl)). Non emette `x-default` [DA VERIFICARE su 9.1]; su multinegozio con domini diversi per lingua gli hreflang incrociati fra negozi non sono nativi: serve un modulo o il tema.
5. **Valute.** Il cambio valuta non cambia URL nei temi nativi 1.7+, quindi non duplica [DA VERIFICARE su temi custom che mettono la valuta in query string].
6. **Robots meta.** Classic stampa `<meta name="robots">` solo se diverso da `index`: un noindex ereditato da un modulo si vede solo nel sorgente, non nel pannello.

**Sitemap.** Modulo nativo gratuito **Google Sitemap** (`gsitemap`): un file per lingua, compatibile multinegozio, richiede PS 8.2+ nella versione corrente ([GitHub gsitemap](https://github.com/PrestaShop/gsitemap)). Le sitemap **non si aggiornano da sole**: va programmato il cron indicato nella configurazione del modulo [DA VERIFICARE la stringa cron sul pannello]. Prodotti disattivati e categorie vuote non devono comparire: si controlla il file, non la spunta.

---

## 6. SEO: prodotti disattivati, cancellati, 404

- **Scheda SEO del prodotto → "Pagina di reindirizzamento" (Redirection when disabled)**: *Nessun redirect (404)*, *Nessun redirect (410)*, *Redirect permanente (301)* verso prodotto o categoria, *Redirect temporaneo (302)* ([docs 8, Managing products](https://docs.prestashop-project.org/v.8-documentation/user-guide/selling/managing-catalog/managing-products); il 410 è presente nel pannello ma la docs 8 non lo descrive, e su una versione della pagina prodotto non si salvava: [#29945](https://github.com/PrestaShop/PrestaShop/issues/29945)).
- 🔴 **Il default è 404.** Un catalogo stagionale che disattiva prodotti senza impostare 301 perde ogni posizionamento e ogni annuncio Shopping che punta lì. Regola: 301 verso la categoria per i prodotti che non tornano, 302 o 404 per quelli che tornano a breve, 410 per ciò che deve sparire dall'indice.
- ⚠️ **301 senza destinazione = errore 500**, non 404 ([#42288](https://github.com/PrestaShop/PrestaShop/issues/42288)). Si controlla che ogni 301 abbia un target.
- **Prodotto cancellato = 404 secco**, nessuna opzione nativa. Il redirect si fa prima di cancellare, o via modulo/`.htaccess`.
- **Categorie disattivate: nessun redirect nativo** (richiesta aperta [#35500](https://github.com/PrestaShop/PrestaShop/issues/35500)). Serve regola server o modulo.
- I 404 reali si leggono in **Statistiche > Pagine non trovate** (modulo `ps_pagesnotfound`, v4.0.0 per 9.2): è la lista da cui partono i redirect dopo una migrazione.

---

## 7. Tracciamento: GA4, GTM, consenso

- **PrestaShop Metrics (`ps_metrics`) è stato dismesso il 01/01/2026** e non è più sul Marketplace (help center [FAQ Metrics](https://help-center.prestashop.com/hc/en-us/articles/27960692458002--Frequently-Asked-Questions-about-PrestaShop-Metrics): non leggibile via fetch il 20/09/2026, data presa dallo snippet di ricerca; da ricontrollare a mano). Se è ancora installato, si disinstalla.
- **Modulo ufficiale GA4: `ps_googleanalytics` v6.0.0 (22/06/2024)**, richiede PS **8.2+**; su 1.7 resta la 5.x (min 1.7.7). Si aggancia a header, pagina prodotto, carrello (quantità e rimozione), corriere, conferma ordine, cambio stato/annullo ordine per i rimborsi ([GitHub ps_googleanalytics](https://github.com/PrestaShop/ps_googleanalytics), [releases](https://github.com/PrestaShop/ps_googleanalytics/releases)). [DA VERIFICARE] la lista esatta dei nomi evento GA4 emessi e i parametri `items`: si legge in DebugView, non nella pagina del modulo. **Non fa GTM, non fa Consent Mode** [DA VERIFICARE sulla 6.0.0]: è un gtag diretto.
- **GTM: nessun modulo nativo.** Le strade sono due: modulo terzo dal Marketplace che espone un `dataLayer` e-commerce (esistono con i 18 eventi GA4 e Consent Mode v2, prezzo e qualità variabili) oppure sviluppatore che inietta il container su `displayHeader` e i push sugli hook di carrello/ordine. **Regola: un solo sistema di tracciamento.** ps_googleanalytics + GTM con tag GA4 = acquisti doppi.
- **Cosa si ottiene senza sviluppatore**: page view, view_item, add_to_cart, purchase (dal modulo ufficiale o da un modulo GTM). **Cosa richiede sviluppo o modulo maturo**: `view_item_list` con posizione, `select_item`, `add_shipping_info`/`add_payment_info` distinti, `refund`, `user_id`, purchase server-side, deduplica, e-commerce sul One Page Checkout di 9.2.
- **Consenso.** `psgdpr` gestisce accesso e cancellazione dati e le caselle di consenso nei form, **non il banner cookie** ([GitHub psgdpr](https://github.com/PrestaShop/psgdpr)). Nessun banner nativo: serve un modulo cookie con **Consent Mode v2** dal Marketplace, che blocchi i tag prima del consenso. Contesto italiano: [Linee guida cookie del Garante, 10/06/2021](https://www.garanteprivacy.it/web/guest/home/docweb/-/docweb-display/docweb/9677876): rifiuto con la stessa evidenza dell'accetta, nessun pre-flag, nessun cookie wall.
- **Multinegozio**: ogni negozio è un contesto di configurazione a sé ([devdocs multistore](https://devdocs.prestashop-project.org/9/modules/concepts/multistore/)): ID GA4, container GTM e pixel vanno impostati per negozio, non "per tutti i negozi" a scatola chiusa.

---

## 8. Google Merchant Center e Google Ads

- **Modulo ufficiale: "PrestaShop Marketing with Google"** (`psxmarketingwithgoogle`, PrestaShop SA, gratuito, sul Marketplace [85751](https://addons.prestashop.com/en/promotions-marketing/85751-prestashop-marketing-with-google-.html)): sincronizza il catalogo con Merchant Center con aggiornamento quotidiano di prezzo e disponibilità, schede gratuite, Performance Max dal back office, tracciamento conversioni (aggiunta al carrello e acquisto), conversioni avanzate, tag remarketing, verifica sito e Google tag ([GitHub psxmarketingwithgoogle](https://github.com/PrestaShopCorp/psxmarketingwithgoogle); lato Google: [Google Ads 10431635](https://support.google.com/google-ads/answer/10431635?hl=en)). Richiede un PrestaShop Account. Compatibilità 1.7/8/9 dichiarata da fonte terza (care-center), non verificata sul Marketplace (pagina 403).
- 🔴 **Se il modulo installa il Google tag e c'è già GA4/GTM, si sceglie chi traccia**: con entrambi si contano conversioni doppie in Google Ads.
- **Esportatori terzi** (feed XML/CSV programmato) restano la scelta quando servono: regole per combinazione, lingue e valute multiple, campi custom (`custom_label`, `gtin` da attributo), più negozi. Il feed va aggiornato **almeno ogni 24 ore** (regola Google).
- **Errori di feed tipici su PrestaShop** (fonti Google): **prezzo non corrispondente** ([12159029](https://support.google.com/merchants/answer/12159029?hl=en)) per prezzi specifici per gruppo cliente, IVA mostrata diversa dal feed, prezzo della combinazione cambiato via JavaScript dopo il caricamento (Google legge l'HTML iniziale); **pagina prodotto non disponibile** ([12158123](https://support.google.com/merchants/answer/12158123?hl=en)) per prodotti disattivati a 404 o catene di più di 2 redirect (sez. 6); **combinazioni**: ogni variante con `id` proprio, `item_group_id` = prodotto padre e `link` alla URL della combinazione, non del padre; **lingua/valuta**: un feed per ogni combinazione paese-lingua-valuta.
- **Meta.** Modulo ufficiale **"PrestaShop Social with Facebook & Instagram"** (`ps_facebook`, PrestaShop SA): Pixel con gestione del consenso, hook per la Conversions API, sincronizzazione catalogo; dichiarato PS 1.7+, **compatibilità con 9.x non dichiarata** nel README ([GitHub ps_facebook](https://github.com/PrestaShopCorp/ps_facebook)) [DA VERIFICARE sul Marketplace]. Alternativa: modulo terzo Pixel + CAPI con deduplica `event_id`. Anche qui: un solo pixel, o gli acquisti raddoppiano.

---

## 9. Multinegozio

- Si attiva in **Parametri negozio > Generale > Abilita multinegozio**, poi compare **Parametri avanzati > Multinegozio** ([docs 8, Multistore](https://docs.prestashop-project.org/v.8-documentation/user-guide/configuring-shop/advanced-parameters/multistore)). Gruppi di negozi e negozi; ogni negozio ha una URL principale e può averne altre che reindirizzano; "Condividi quantità" **azzera le quantità** quando viene attivato.
- Effetti su tracciamento e feed: configurazione **per contesto** (sez. 7), un feed per negozio, sitemap per negozio, hreflang incrociati non nativi (sez. 5), `robots.txt` unico per installazione. Prima di ogni verifica si guarda **quale contesto** è selezionato in alto nel back office.
- Licenze: **una licenza Addons vale per un negozio/dominio** (sez. 11): il multinegozio moltiplica le licenze.

---

## 10. Sicurezza: quello che un PM controlla senza toccare codice

1. **Cartella `admin` rinominata e cartella `install` cancellata**: PrestaShop non apre il back office finché non è fatto ([devdocs, file structure](https://devdocs.prestashop-project.org/9/development/architecture/file-structure/); help center "Best practices for securing your store" non leggibile via fetch il 20/09/2026, da ricontrollare a mano).
2. **Patch applicate**: 9.1.5 e 8.2.8 (18/08/2026) chiudono 5 falle, 3 High (formula injection CSV, SSRF import, spoofing `X-Forwarded-For`); lo spoofing IP richiede **anche** la configurazione corretta del proxy/CDN, non basta aggiornare ([build 8.2.8](https://build.prestashop-project.org/news/2026/prestashop-8-2-8-security-release/)). 9.1.3 del 20/05/2026 chiudeva una XSS Critical nel servizio clienti.
3. **Security Charter**: CVE pubblicata per ogni falla ≥ 7.5, mai fix silenziosi ([prestashop.com/security-charter](https://prestashop.com/security-charter/)). Le advisory dei moduli (anche di Addons) escono su [security.friendsofpresta.org](https://security.friendsofpresta.org/): si controlla lì la lista moduli del negozio.
4. **Moduli solo dal Marketplace o dal sito ufficiale dell'autore**, mai zip "nulled": la maggior parte delle compromissioni passa da moduli.
5. **Backup** file + DB automatici e testati con un ripristino, prima di ogni aggiornamento.
6. **Debug mode a No** (sez. 3): espone percorsi e query.

---

## 11. Marketplace Addons e licenze

- **Una licenza = un negozio (dominio)**; per altri negozi o per un multinegozio si comprano altre licenze; per il supporto si richiede la prova d'acquisto per ogni negozio ([Addons FAQ](https://addons.prestashop.com/en/content/1-faq) e [T&C](https://addons.prestashop.com/en/content/12-terms-and-conditions-of-use), entrambe non leggibili via fetch il 20/09/2026, regola presa dagli snippet: da ricontrollare a mano).
- Supporto post-vendita: dal 01/07/2021 la "Zen Option" è sostituita da **Business Care**, abbonamento nel conto Marketplace ([helpcenter partners, Zen Option](https://helpcenter-partners.prestashop.com/hc/en-us/articles/18371101719314-Zen-Option)). Durata degli aggiornamenti inclusi con l'acquisto: [DA VERIFICARE] sulla pagina del modulo.
- Prima di un aggiornamento major si verifica **modulo per modulo** la compatibilità dichiarata sulla scheda Addons; se la scheda non elenca la major di arrivo, il modulo va considerato incompatibile finché l'autore non risponde.
- I moduli "PrestaShop SA / PrestaShop Corp" (Marketing with Google, Social, Account, Checkout) richiedono un **PrestaShop Account** collegato: senza, non si configurano.

---

## 12. Migrazione 1.6/1.7 → 8/9: cosa si rompe

- **9.0** (10/06/2025): PHP 8.1 minimo, Symfony 6.4 LTS, Admin API; rimossi Guzzle e Swift Mailer dal core, gestione avanzata dello stock, consegna multi-indirizzo, oltre 30 hook della vecchia pagina prodotto, classe `PrestaShopAutoload`; i template di categoria, produttore, fornitore e negozi usano Presenter con strutture dati diverse ([devdocs core-updates 9.0](https://devdocs.prestashop-project.org/9/modules/core-updates/9.0/)). Tradotto: ogni modulo che tocca la pagina prodotto o le mail, e ogni tema con override di categoria, va riscritto o sostituito.
- **9.1** (23/03/2026): Bootstrap 5.3 e **Hummingbird 2.0 tema di default per le installazioni nuove** (chi aggiorna tiene il suo tema; Classic resta mantenuto, 3.1.1); **jQuery deprecato, sarà rimosso in PrestaShop 10**; hook `displaySearch` rimosso ([devdocs core-updates 9.1](https://devdocs.prestashop-project.org/9/modules/core-updates/9.1/)). Un tema costruito su jQuery ha una scadenza.
- **9.2**: One Page Checkout nativo: i moduli di pagamento e corriere vanno ritestati nel flusso a pagina singola; i moduli one-page-checkout terzi diventano ridondanti ([build 9.2 beta](https://build.prestashop-project.org/news/2026/prestashop-9-2-beta1/)).
- **URL**: il formato delle URL semplificate non cambia se non si toccano le route (sez. 4), quindi una migrazione fatta bene non richiede redirect di massa; cambiano invece se si cambia tema con struttura categorie diversa, se si migra da 1.6 con `id_product_attribute` diverso, o se si sposta il dominio. Si esporta la lista URL prima (sitemap + Search Console) e si confronta dopo.
- **Tema e Core Web Vitals**: Classic carica jQuery e CSS in blocco; Hummingbird 2.x (2.1.0 per 9.2, 2.0.0 per 9.1) è Bootstrap 5, SCSS, TypeScript e senza jQuery interno ([GitHub hummingbird](https://github.com/PrestaShop/hummingbird)). I numeri "+40% velocità, Lighthouse mobile da 40 a 75" sono **regole empiriche di agenzie terze, non numeri PrestaShop**. Le CWV reali si leggono in Search Console, non nel Lighthouse del tema demo.

---

## 13. Igiene di un PrestaShop ereditato: ordine di controllo

1. **Versione core e PHP** (Parametri avanzati > Informazioni): se il ramo è fuori manutenzione (sez. 1) tutto il resto è provvisorio.
2. **Debug mode, Smarty, CCC** (sez. 3).
3. **Cartella admin rinominata, install assente, backup esistenti** (sez. 10).
4. **SEO e URL**: friendly URL, canonical 301, robots.txt (sez. 4).
5. **Sorgente di una pagina prodotto con combinazioni e di una categoria filtrata**: canonical, hreflang, robots meta (sez. 5).
6. **Prodotti disattivati con redirect 404 di default** ed elenco Pagine non trovate (sez. 6).
7. **Moduli di tracciamento installati**: quanti gtag e pixel ci sono nel sorgente (sez. 7-8). Uno per piattaforma.
8. **Banner cookie e Consent Mode v2** (sez. 7).
9. **Feed Merchant Center**: chi lo genera, ogni quanto, quanti prodotti disapprovati e per quale motivo (sez. 8).
10. **Lista moduli con versione, autore, licenza e compatibilità con la major successiva** (sez. 11): è il preventivo di aggiornamento in nuce.
11. **Multinegozio attivo?** Se sì, si rifà la lista per ogni contesto (sez. 9).
12. **Sitemap aggiornata e cron attivi** (sez. 5).

---

## 14. Cosa deve consegnare lo sviluppatore prima del go-live

- Debug mode No, Smarty "mai ricompilare", CCC attivo, cache configurata, `memory_limit` 512M (sez. 3).
- Admin rinominata, install cancellata, backup schedulato e un ripristino provato (sez. 10).
- Canonical 301, robots.txt rigenerato con le regole custom, sitemap con cron, `?q=` e `?order=` non indicizzabili (sez. 4-5).
- Mappa redirect delle vecchie URL caricata e testata su un campione (sez. 6, 12).
- Un solo sistema di tracciamento con `dataLayer` documentato: nome evento, parametri, hook che lo genera; DebugView di un acquisto di prova con `transaction_id`, `value`, `tax`, `shipping`, `items` (sez. 7).
- Banner cookie con Consent Mode v2 e tag bloccati prima del consenso (sez. 7).
- Feed Merchant Center con 0 disapprovazioni per prezzo o pagina non disponibile su un campione di combinazioni (sez. 8).
- Elenco moduli con versione e licenza, per ogni negozio (sez. 11).

---

## 15. Meccanica del pannello (da verificare a mano)

- Sulla pagina prodotto 9.1, dove sta esattamente l'opzione **410** e si salva? (issue #29945 la descrive non salvata su una versione della pagina.)
- Il **robots.txt generato da 9.1** contiene già `Disallow: /*?q=` oltre a `order=`? E dopo la rigenerazione le regole custom spariscono davvero?
- **gsitemap**: la stringa cron è mostrata nella configurazione del modulo? Con quale frequenza il negozio la esegue?
- **ps_googleanalytics 6.0.0**: `purchase` parte sulla pagina di conferma ordine (client) o alla validazione dell'ordine? Cosa succede con pagamenti a redirect (PayPal, bonifico)?
- **Update Assistant 7.6**: la schermata dei moduli incompatibili chiede conferma prima di disinstallarli?
- **ps_facebook**: si installa su 9.1 senza errori? Il Marketplace dichiara la 9?

---

## 16. Cosa non fare mai

- Lasciare debug mode attivo su un negozio in produzione, anche "per un'ora".
- Aggiornare PHP sull'hosting prima di aver letto la matrice della versione installata (sez. 1).
- Lanciare l'Update Assistant sul negozio vivo senza staging e senza esportare la lista moduli.
- Installare un secondo modulo GA4/pixel "per confronto": raddoppia le conversioni.
- Cliccare "Genera robots.txt" senza copia del file corrente.
- Cambiare lo schema delle URL o il tema su un catalogo indicizzato senza mappa redirect.
- Disattivare prodotti in massa lasciando il default 404.
- Usare un feed Merchant Center che espone prezzi diversi da quelli della pagina per il gruppo "Visitatore".
- Comprare un modulo Addons senza leggere la compatibilità con la major di destinazione e il numero di negozi coperti.
- Fidarsi di un canonical o di un hreflang "perché il tema lo fa": si legge il sorgente.

---

## Fonti (verificate 20/09/2026)

**Ufficiali PrestaShop:** [devdocs 9, system requirements](https://devdocs.prestashop-project.org/9/basics/installation/system-requirements/) · [devdocs 8, system requirements](https://devdocs.prestashop-project.org/8/basics/installation/system-requirements/) · [devdocs 1.7, system requirements](https://devdocs.prestashop-project.org/1.7/basics/installation/system-requirements/) · [devdocs, patch release lifecycle](https://devdocs.prestashop-project.org/9/project/release/patch-release-lifecycle/) · [devdocs, optimizations](https://devdocs.prestashop-project.org/9/scale/optimizations/) · [devdocs, core updates 9.0](https://devdocs.prestashop-project.org/9/modules/core-updates/9.0/) · [devdocs, core updates 9.1](https://devdocs.prestashop-project.org/9/modules/core-updates/9.1/) · [devdocs, multistore](https://devdocs.prestashop-project.org/9/modules/concepts/multistore/) · [devdocs, file structure](https://devdocs.prestashop-project.org/9/development/architecture/file-structure/) · [docs 8, SEO and URLs](https://docs.prestashop-project.org/v.8-documentation/user-guide/configuring-shop/shop-parameters/traffic/seo-and-urls) · [docs 8, Performance](https://docs.prestashop-project.org/v.8-documentation/user-guide/configuring-shop/advanced-parameters/performance) · [docs 8, Managing products](https://docs.prestashop-project.org/v.8-documentation/user-guide/selling/managing-catalog/managing-products) · [docs 8, Multistore](https://docs.prestashop-project.org/v.8-documentation/user-guide/configuring-shop/advanced-parameters/multistore) · [docs 9, user guide](https://docs.prestashop-project.org/v.9-documentation/user-guide) · [build: 1.7.8 extended support (05/01/2023)](https://build.prestashop-project.org/news/2023/178-in-extended-support-phase/) · [build: 9.0 available (10/06/2025)](https://build.prestashop-project.org/news/2025/prestashop-9-0-available/) · [build: 8.2.x extended support (04/07/2025)](https://build.prestashop-project.org/news/2025/82x-extended-support-phase/) · [build: 9.1 available (23/03/2026)](https://build.prestashop-project.org/news/2026/prestashop-9-1-0-available/) · [build: 9.2 feature freeze (09/07/2026)](https://build.prestashop-project.org/news/2026/prestashop-9-2-feature-freeze/) · [build: 9.2 Beta 1 (22/07/2026)](https://build.prestashop-project.org/news/2026/prestashop-9-2-beta1/) · [build: 9.1.5 (18/08/2026)](https://build.prestashop-project.org/news/2026/prestashop-9-1-5-security-release/) · [build: 8.2.8 (18/08/2026)](https://build.prestashop-project.org/news/2026/prestashop-8-2-8-security-release/) · [build: Core Monthly luglio 2026](https://build.prestashop-project.org/news/2026/core-monthly-2026-07-01-2026-07-31/) · [build: Core Monthly agosto 2026 (03/09/2026)](https://build.prestashop-project.org/news/2026/core-monthly-2026-08-01-2026-08-31/) · [Security Charter](https://prestashop.com/security-charter/) · [GitHub autoupgrade](https://github.com/PrestaShop/autoupgrade) · [GitHub ps_googleanalytics](https://github.com/PrestaShop/ps_googleanalytics) e [releases](https://github.com/PrestaShop/ps_googleanalytics/releases) · [GitHub gsitemap](https://github.com/PrestaShop/gsitemap) · [GitHub ps_facetedsearch](https://github.com/PrestaShop/ps_facetedsearch) · [GitHub psgdpr](https://github.com/PrestaShop/psgdpr) · [GitHub hummingbird](https://github.com/PrestaShop/hummingbird) · [GitHub classic-theme head.tpl](https://github.com/PrestaShop/classic-theme/blob/develop/templates/_partials/head.tpl) · [GitHub psxmarketingwithgoogle](https://github.com/PrestaShopCorp/psxmarketingwithgoogle) · [GitHub ps_facebook](https://github.com/PrestaShopCorp/ps_facebook) · [PR #37066 noindex faccette](https://github.com/PrestaShop/PrestaShop/pull/37066) · [Discussione #40335](https://github.com/PrestaShop/PrestaShop/discussions/40335) · Issue [#9508](https://github.com/PrestaShop/PrestaShop/issues/9508), [#26676](https://github.com/PrestaShop/PrestaShop/issues/26676), [#29945](https://github.com/PrestaShop/PrestaShop/issues/29945), [#35500](https://github.com/PrestaShop/PrestaShop/issues/35500), [#42288](https://github.com/PrestaShop/PrestaShop/issues/42288), [autoupgrade #1773](https://github.com/PrestaShop/autoupgrade/issues/1773) · [helpcenter partners, Zen Option](https://helpcenter-partners.prestashop.com/hc/en-us/articles/18371101719314-Zen-Option).

**Ufficiali Google e Garante:** [Google Ads 10431635, Performance Max con PrestaShop](https://support.google.com/google-ads/answer/10431635?hl=en) · [Merchant Center 12159029, prezzo non corrispondente](https://support.google.com/merchants/answer/12159029?hl=en) · [Merchant Center 12158123, pagina prodotto non disponibile](https://support.google.com/merchants/answer/12158123?hl=en) · [Garante, Linee guida cookie 9677876](https://www.garanteprivacy.it/web/guest/home/docweb/-/docweb-display/docweb/9677876).

**Terze parti (pratica, non numeri PrestaShop):** [Friends of Presta, advisories](https://security.friendsofpresta.org/) · [care-center, Marketing with Google (compatibilità 1.7/8/9)](https://care-center.prestashop.com/gb/free-tutorials/650-marketing-google.html) · [prestasoo, Hummingbird e CWV](https://www.prestasoo.com/blog/prestashop-hummingbird-theme) · [axelweb, Hummingbird (numeri Lighthouse)](https://axelweb.fr/blog/prestashop/theme-hummingbird-prestashop-guide-complet).

**Non leggibili via fetch il 20/09/2026, da ricontrollare a mano:** help center [PrestaShop Marketing with Google (28399806197138)](https://help-center.prestashop.com/hc/en-us/articles/28399806197138--PrestaShop-Marketing-with-Google), [FAQ PrestaShop Metrics (27960692458002)](https://help-center.prestashop.com/hc/en-us/articles/27960692458002--Frequently-Asked-Questions-about-PrestaShop-Metrics), [Best practices for securing your store (10799637660946)](https://help-center.prestashop.com/hc/en-us/articles/10799637660946--Best-practices-for-securing-your-store), [The debug mode (9242063447698)](https://help-center.prestashop.com/hc/en-us/articles/9242063447698-The-debug-mode) (tutte 403); [Addons FAQ](https://addons.prestashop.com/en/content/1-faq), [Addons T&C](https://addons.prestashop.com/en/content/12-terms-and-conditions-of-use), [scheda Marketing with Google 85751](https://addons.prestashop.com/en/promotions-marketing/85751-prestashop-marketing-with-google-.html) (403); [devdocs, prestashop-versions](https://devdocs.prestashop-project.org/9/basics/introduction/prestashop-versions/) (404); README di ps_googleanalytics senza lista eventi.
