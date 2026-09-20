---
name: "sviluppo-web"
description: "Regole operative verificate per coordinare sviluppatori e agenzie su siti ed e-commerce dei clienti (WordPress, WooCommerce, PrestaShop, PHP custom) senza scrivere codice: staging e ambienti, repository e deploy, rollback, DNS e migrazioni, SSL, hosting e versioni PHP, Core Web Vitals come metrica di accettazione, sicurezza e data breach, accessibilità (EAA), continuità del tracciamento GTM/GA4/Search Console, checklist di go-live, contratto di manutenzione, preventivi e brief. Usala ogni volta che si commissiona, si collauda o si accetta un intervento su un sito, si cambia hosting o dominio, si firma una manutenzione o si giudica un preventivo, anche se nessuno ha nominato lo sviluppatore."
---

# Sviluppo web (lato PM e marketing): regole operative

**Ultima verifica delle fonti: 20 settembre 2026.**

**Cosa cambia fra il 2026 e il 2028 (per chi ha ancora la checklist del 2024):**

- **Certificati TLS:** massimo di settore 200 giorni dal 15/03/2026, 100 dal 15/03/2027, 47 dal 15/03/2029; Let's Encrypt passa a 64 giorni dal 10/02/2027 e a 45 dal 16/02/2028, e **dal 04/06/2025 non manda più email di scadenza** (sez. 4).
- **PHP 8.2 esce dal supporto di sicurezza il 31/12/2026; 8.4 esce dal supporto attivo lo stesso giorno.** PHP 8.6 è in beta (RC 1 prevista il 24/09/2026) (sez. 5).
- **WordPress 7.0 (20/05/2026)** ha tolto PHP 7.2 e 7.3; **WooCommerce 10.8+** richiede PHP 8.3 e propone PHP 8.1 minimo dalla 11.5 (gennaio 2027) (sez. 5).
- **Accessibilità:** EAA applicabile dal 28/06/2025 anche all'e-commerce; **Linee guida AgID sull'accessibilità dei servizi pubblicate a marzo 2026**, vigilanza AgID (sez. 8).

## 0. Manutenzione di questa skill (leggere per primo)

⛔ **Questa skill è scritta da chi coordina, non da chi programma e non da un avvocato.** Decide cosa chiedere, cosa controllare e cosa non accettare da uno sviluppatore. Il "come" tecnico resta allo sviluppatore; il parere legale (GDPR, accessibilità, contratti) resta al legale.

1. **Finestra di freschezza: tre mesi.** Le date di fine supporto PHP, i requisiti WordPress/WooCommerce e i tempi dei certificati cambiano a scadenze annunciate: se la data in cima ha più di tre mesi si rileggono le tabelle di sez. 4 e 5 prima di scriverle in un preventivo o in un contratto.
2. **Quando una fonte smentisce una regola scritta qui, si aggiorna la skill nello stesso turno**, si riscrive la data e si annota cosa è cambiato e da quando.
3. Due metà da tenere distinte: **conoscenza di dominio** (verificata su php.net, MDN, web.dev, Google Search Central, letsencrypt.org, eur-lex, Garante, AgID) e **meccanica dei pannelli** (sez. 14: si impara sbagliando, si scrive qui la prima volta).
4. Dove si guardano i cambiamenti: [php.net/supported-versions](https://www.php.net/supported-versions.php) · [WordPress requirements](https://wordpress.org/about/requirements/) e [Make WordPress Core](https://make.wordpress.org/core/) · [WooCommerce Developer Blog](https://developer.woocommerce.com/blog/) · [PrestaShop devdocs](https://devdocs.prestashop-project.org/) · [Let's Encrypt upcoming features](https://letsencrypt.org/upcoming-features/) · [web.dev/vitals](https://web.dev/articles/vitals) · [Google Search Central](https://developers.google.com/search/docs) · [Garante, tema Cookie](https://www.garanteprivacy.it/temi/cookie) · [AgID accessibilità](https://www.agid.gov.it/it/design-servizi/accessibilita).

## 1. Ambienti: la regola che costa di più è "si prova in produzione"

**Ogni sito con un cliente dietro ha tre ambienti: locale (dello sviluppatore), staging (copia raggiungibile da PM e cliente), produzione. Nessuna modifica arriva in produzione senza essere passata da staging.** Un intervento "veloce" fatto direttamente sul sito live non ha un ambiente in cui riprodurre il guasto e non ha un rollback: quando rompe il checkout, rompe il fatturato.

- 🔴 **Lo staging è noindex E protetto da password. Le due cose insieme, non una.** Google indicizza tutto quello che raggiunge: uno staging aperto diventa un duplicato del sito che compete con l'originale. La protezione con password è il metodo che Google stesso indica per tenere Googlebot fuori ([remove-information](https://developers.google.com/search/docs/crawling-indexing/remove-information)); il `noindex` (meta o header `X-Robots-Tag`) funziona solo se la pagina **non** è bloccata da robots.txt, altrimenti il crawler non lo legge mai ([block-indexing](https://developers.google.com/search/docs/crawling-indexing/block-indexing)). Robots.txt da solo non basta: un URL disallow può comparire in SERP se linkato da fuori ([robots intro](https://developers.google.com/search/docs/crawling-indexing/robots/intro)).
- ⚠️ La password HTTP Basic viaggia in base64, cioè in chiaro: va usata solo sotto HTTPS ([MDN Authentication](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Authentication)). Uno staging in HTTP con password è finto.
- 🔴 **Lo staging con la copia del database di produzione contiene dati personali veri (clienti, ordini, indirizzi).** È un trattamento come gli altri: l'agenzia che lo tiene è responsabile ex art. 28 GDPR e serve un contratto scritto con istruzioni, riservatezza, sub-responsabili autorizzati, cancellazione a fine servizio ([art. 28](https://gdpr-info.eu/art-28-gdpr/)); pseudonimizzazione e cifratura sono fra le misure dell'art. 32 ([art. 32](https://gdpr-info.eu/art-32-gdpr/)). Regola pratica: dati anonimizzati o campione sintetico; se serve la copia vera, accessi nominativi e cancellazione a fine lavoro, per iscritto.
- ⚠️ **Sullo staging i tag di tracciamento puntano a proprietà di test o sono spenti.** Uno staging che spara `purchase` sulla GA4 di produzione sporca i numeri con cui si giudica la campagna (vedi skill `ga4-performance`, traffico interno).
- Nel brief di ogni task si scrive **su quale ambiente** si lavora e **chi** porta in produzione (sez. 12).

## 2. Versionamento e deploy: cosa chiede un PM che non scrive codice

**Il codice del sito sta in un repository (Git) di cui il cliente è proprietario o ha accesso in lettura. Tema, plugin custom, configurazioni: tutto quello che è stato scritto per il cliente.** Senza repository, l'agenzia che sparisce si porta via il sito.

Le quattro domande da fare e da mettere nel contratto:

1. **Dove sta il repository e chi ne ha accesso** (l'account del cliente ha almeno lettura; l'accesso non è sul Gmail personale dello sviluppatore).
2. **Quali branch esistono e cosa rappresentano** (di norma uno per lo sviluppo, uno che rispecchia la produzione). Non serve capire Git: serve sapere che "produzione" corrisponde a un branch preciso.
3. **Chi può fare il deploy e come** (manuale via SFTP, pipeline automatica, pulsante nell'hosting). Un nome, non "chiunque abbia le credenziali".
4. **Ogni rilascio ha un tag** (`v2.3.0` o data). I tag segnano i punti di rilascio nella storia e sono la cosa a cui si torna per il rollback; **vanno pubblicati esplicitamente**, `git push` da solo non li invia ([git-scm, Tagging](https://git-scm.com/book/en/v2/Git-Basics-Tagging)). Se lo sviluppatore non sa dire quale tag è in produzione, non c'è rollback.

🔴 **Segreti fuori dal repository.** Password del database, chiavi API, salt: stanno in file di configurazione non versionati o in variabili d'ambiente. WordPress stesso indica di tenere `wp-config.php` fuori dalla radice raggiungibile e di negarne l'accesso ([Hardening WordPress](https://developer.wordpress.org/advanced-administration/security/hardening/)). Una chiave API in un commit è compromessa anche se il repository è privato.

### Deploy e rollback

- **Backup completo (file + database) immediatamente prima di ogni deploy, con verifica che sia ripristinabile.** "Abbiamo il backup dell'hosting di stanotte" non è un backup pre-deploy: fra stanotte e adesso ci sono ordini.
- **Piano di rollback scritto prima del deploy**: chi lo decide, entro quanti minuti, cosa si ripristina (solo codice, o anche database: gli ordini arrivati nel frattempo si perdono se si ripristina il DB).
- **Finestra di deploy concordata con chi vende:** non durante una campagna in corso, non il venerdì pomeriggio, non nelle ore di picco ordini dell'e-commerce. Lo sviluppatore non conosce il calendario promo: glielo dà il PM.
- **Pagina di manutenzione con codice HTTP 503**, non 200 e non una home "in costruzione": un 503 dice a Google di ripassare, un 200 con "torniamo presto" viene indicizzato.
- ⛔ **Nessuna modifica diretta ai file di produzione fuori dal repository** ("ho sistemato al volo via FTP"). Al deploy successivo la modifica sparisce e nessuno sa perché il sito è tornato rotto.

## 3. DNS e domini: tre fornitori diversi, e l'email che si rompe

**Registrar (chi possiede il dominio), DNS (chi risponde alle query) e hosting (chi serve il sito) sono tre ruoli, spesso tre aziende. Prima di qualunque migrazione si scrive chi è chi, con le credenziali intestate al cliente.** La migrazione che va storta nove volte su dieci non ha rotto il sito: ha rotto la posta.

- **TTL prima della migrazione.** Il TTL è per quanti secondi i resolver tengono in cache un record ([MDN TTL](https://developer.mozilla.org/en-US/docs/Glossary/TTL)). Google raccomanda di abbassarlo a un valore basso (poche ore) **almeno una settimana prima** del cambio di hosting, così il nuovo indirizzo si propaga in fretta ([Changing your hosting](https://developers.google.com/search/docs/crawling-indexing/site-move-no-url-change)). Abbassarlo il giorno stesso non serve: le cache hanno già il vecchio valore con il vecchio TTL.
- **Il vecchio server resta acceso** finché il traffico sul nuovo non è stabile: un utente con la cache vecchia deve trovare ancora il sito.
- **I record che contano, da esportare prima di toccare i nameserver:**
  - `A` / `AAAA`: il sito (IPv4 / IPv6). Sono i soli che cambiano in un cambio hosting.
  - `CNAME`: alias (`www`, sottodomini verso CDN o SaaS).
  - `MX`: dove arriva la posta. **Non c'entrano con il sito e non vanno toccati**: se spariscono dalla nuova zona DNS, la posta rimbalza.
  - `TXT`: SPF, DKIM, DMARC, verifiche di proprietà (`google-site-verification=…`), altri servizi. Se si ricreano i DNS da zero e mancano, si perdono verifiche e autenticazione email.
- **Cosa rompe la posta quando si sposta il sito:** (a) zona DNS ricreata senza MX; (b) SPF che includeva il vecchio hosting da cui il sito manda le email transazionali (ordini, reset password): il nuovo server non è autorizzato e le email finiscono in spam; (c) selettore DKIM non ricreato. Regole Gmail dal 01/02/2024: tutti i mittenti devono avere SPF **o** DKIM, PTR valido, TLS, spam sotto lo 0,3%; chi manda più di 5.000 messaggi/giorno deve avere SPF **e** DKIM **e** DMARC allineato, con unsubscribe a un clic ([Email sender guidelines](https://support.google.com/a/answer/81126?hl=en)). Un solo record SPF per dominio, che inizia con `v=spf1`, con al massimo 10 `include` ([Set up SPF](https://knowledge.workspace.google.com/admin/security/set-up-spf)).
- **Search Console:** la verifica dura finché il token (file, meta tag, record DNS) resta al suo posto; rimuoverlo fa perdere la proprietà ([9008080](https://support.google.com/webmasters/answer/9008080?hl=en)). La proprietà di tipo Dominio si verifica solo via DNS.
- **Cambio di dominio**: mappa 301 vecchio→nuovo per ogni URL, sitemap nuova, strumento *Cambio di indirizzo* in Search Console. Lo strumento serve **solo** per cambio di dominio o sottodominio, non per http→https né per www/non-www ([Site move with URL changes](https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes)). Redirect da tenere "il più a lungo possibile, in genere almeno 1 anno".

## 4. SSL/TLS: il certificato scade e nessuno avvisa più

**Dal 04/06/2025 Let's Encrypt non manda più le email di scadenza** ([annuncio](https://letsencrypt.org/2025/01/22/ending-expiration-emails/)). Se il rinnovo automatico si rompe, il primo a saperlo è il cliente che vede il sito "non sicuro". Serve un monitoraggio esterno della scadenza, e va scritto nel contratto di manutenzione (sez. 12).

- I certificati Let's Encrypt durano **90 giorni**, rinnovo consigliato ogni 60 (o quando resta un terzo di vita; meglio ARI, controllato due volte al giorno) ([FAQ](https://letsencrypt.org/docs/faq/), [Integration guide](https://letsencrypt.org/docs/integration-guide/)). Esistono certificati opzionali da **6 giorni**.
- **Calendario:** Let's Encrypt scende a **64 giorni dal 10/02/2027** e a **45 giorni dal 16/02/2028**; i rinnovi non contano nei limiti di emissione ([post 02/12/2025](https://letsencrypt.org/2025/12/02/from-90-to-45), [post 24/02/2026](https://letsencrypt.org/2026/02/24/rate-limits-45-day-certs), [cert-lifetimes](https://letsencrypt.org/docs/cert-lifetimes/)). Per tutte le CA il massimo di settore scende a **200 giorni dal 15/03/2026, 100 dal 15/03/2027, 47 dal 15/03/2029** ([CA/B Forum SC-081v3](https://cabforum.org/2025/04/11/ballot-sc081v3-introduce-schedule-of-reducing-validity-and-data-reuse-periods/)). Conseguenza: **il rinnovo manuale non è più un'opzione**; chi propone "lo rinnoviamo noi a mano ogni anno" propone un sito che si spegne.
- Limiti Let's Encrypt: 50 certificati per dominio registrato ogni 7 giorni, 5 duplicati identici ogni 7 giorni, 5 validazioni fallite per ora ([rate limits](https://letsencrypt.org/docs/rate-limits/)). Uno sviluppatore che "riprova" in loop si blocca da solo.
- **HSTS** (`Strict-Transport-Security`): dice al browser di usare solo HTTPS per `max-age` secondi; `includeSubDomains` estende ai sottodomini, `preload` iscrive alle liste dei browser ed è **difficile da annullare**. Si attiva **dopo** aver verificato che tutto, sottodomini compresi, risponde in HTTPS; si spegne solo servendo `max-age=0` via HTTPS ([MDN HSTS](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Strict-Transport-Security)). Uno staging o un sottodominio in HTTP sotto `includeSubDomains` diventa irraggiungibile.
- **Mixed content dopo una migrazione a HTTPS:** immagini, audio e video in `http://` vengono aggiornati in automatico dal browser; **script, CSS, iframe, font e fetch in `http://` vengono bloccati** e la pagina si rompe in silenzio ([MDN Mixed content](https://developer.mozilla.org/en-US/docs/Web/Security/Mixed_content)). Si chiede: search-and-replace degli URL assoluti nel database, controllo della console del browser sulle pagine chiave, eventualmente `Content-Security-Policy: upgrade-insecure-requests`.

## 5. Hosting e versioni: cosa chiedere prima di firmare

**Un hosting si giudica su nove risposte scritte:** versione PHP disponibile e chi la aggiorna; CPU/RAM/PHP workers dedicati o condivisi; backup automatici con **retention** (quanti giorni) e **dove** (stesso server = non è un backup); **test di ripristino** fatto e datato; CDN; WAF; monitoraggio uptime con avviso a chi; log di accesso conservati quanto; sede dei dati e contratto ex art. 28 GDPR. "Backup giornaliero" senza retention e senza test di ripristino è una parola.

### PHP: versioni supportate al 20/09/2026 ([php.net](https://www.php.net/supported-versions.php))

| branch | rilascio | fine supporto attivo | fine supporto sicurezza |
|---|---|---|---|
| 8.2 | 08/12/2022 | 31/12/2024 | **31/12/2026** |
| 8.3 | 23/11/2023 | 31/12/2025 | 31/12/2027 |
| 8.4 | 21/11/2024 | 31/12/2026 | 31/12/2028 |
| 8.5 | 20/11/2025 | 31/12/2027 | 31/12/2029 |

PHP 8.1 e precedenti sono **end of life**: nessuna patch di sicurezza. PHP 8.6 è in beta 3 dal 10/09/2026, RC 1 prevista il 24/09/2026 ([news 2026](https://www.php.net/archive/2026.php)); GA prevista il 19/11/2026 (data da fonte terza, php.watch, non su php.net alla data di verifica).

🔴 **Regola:** in produzione solo un branch in supporto attivo o di sicurezza; **chi propone un nuovo sito su un PHP che esce dal supporto entro 12 mesi (oggi: 8.2) propone un debito tecnico con la data sopra.** Il cambio di versione PHP si prova in staging, mai in produzione: un plugin incompatibile produce un errore 500 su tutto il sito.

### Requisiti CMS (ufficiali)

- **WordPress:** raccomandati PHP 8.3+ e MySQL 8.0+ / MariaDB 10.11+, HTTPS ([requirements](https://wordpress.org/about/requirements/)). WordPress 7.0 (rilascio 20/05/2026) e 7.1 supportano PHP da 7.4 a 8.5; 7.2 e 7.3 sono stati tolti ([PHP compatibility](https://make.wordpress.org/core/handbook/references/php-compatibility-and-wordpress-versions/), [Dropping PHP 7.2/7.3](https://make.wordpress.org/core/2026/01/09/dropping-support-for-php-7-2-and-7-3/)).
- **WooCommerce 10.8+:** PHP 8.3+ (testato fino a 8.4), WordPress 6.9+, MySQL 8.0+ / MariaDB 10.6+, memoria 256 MB+, HTTPS ([server requirements](https://woocommerce.com/document/server-requirements/)). Proposta dell'08/09/2026: **PHP 8.1 minimo dalla 11.5 (gennaio 2027)**, fine di 7.4 e 8.0 ([Developer Blog](https://developer.woocommerce.com/2026/09/08/from-php-7-4-to-8-1/)).
- **PrestaShop 9:** PHP da 8.2 a 8.5 (raccomandato 8.5), MySQL 5.7+ / MariaDB 10.2+, `memory_limit` almeno 512M, Apache 2.4 o Nginx ([system requirements](https://devdocs.prestashop-project.org/9/basics/installation/system-requirements/)).

⚠️ "Funziona su PHP 7.4" (minimo legacy di WordPress) non è un requisito soddisfatto: è un sito su un runtime senza patch dal 2022.

## 6. Performance: i Core Web Vitals sono la metrica di accettazione, non "mi sembra veloce"

**Un intervento sul sito si accetta sui tre Core Web Vitals misurati sul campo al 75° percentile, mobile e desktop separati** ([web.dev/vitals](https://web.dev/articles/vitals)):

| metrica | buono | da migliorare | scarso | fonte |
|---|---|---|---|---|
| LCP (caricamento) | ≤ 2,5 s | ≤ 4,0 s | > 4,0 s | [web.dev/lcp](https://web.dev/articles/lcp) |
| INP (reattività) | ≤ 200 ms | ≤ 500 ms | > 500 ms | [web.dev/inp](https://web.dev/articles/inp) |
| CLS (stabilità) | ≤ 0,1 | ≤ 0,25 | > 0,25 | [web.dev/cls](https://web.dev/articles/cls) |

- **Dove si leggono.** PageSpeed Insights mostra due cose diverse: i **dati sul campo** (CrUX, utenti reali degli ultimi 28 giorni, 75° percentile) e i **dati di laboratorio** (Lighthouse, una simulazione su un dispositivo). Il verdetto "Superato" riguarda solo il campo: tutte e tre le metriche in "buono" (LCP e CLS se INP non ha dati) ([PSI about](https://developers.google.com/speed/docs/insights/v5/about)). Se l'URL non ha dati, PSI ripiega sull'origine intera. Search Console, rapporto *Core Web Vitals*, raggruppa gli URL e classifica per la metrica peggiore ([9205520](https://support.google.com/webmasters/answer/9205520?hl=en)).
- 🔴 **Conseguenze:** (1) lo staging non ha CrUX, quindi in collaudo si guarda solo il laboratorio e **il collaudo vero si chiude 28 giorni dopo il go-live**, sul campo; (2) il punteggio 0-100 di Lighthouse **non** è un CWV e non si scrive nel contratto; (3) Lighthouse non misura INP (serve interazione): un tema "100/100" può avere INP scarso.
- **Cosa chiedere in ordine di resa:** immagini con dimensioni dichiarate e formato moderno (immagini senza dimensioni, embed che si ridimensionano e font che cambiano metrica sono le cause di CLS elencate da web.dev); caching HTTP corretto: asset con versione nell'URL e `Cache-Control: public, max-age=31536000, immutable`, HTML con `no-cache` ([MDN Caching](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Caching)); **script di terze parti** caricati `async`/`defer`, embed pesanti caricati a scroll, `preconnect` sui domini terzi ([web.dev third-party JS](https://web.dev/articles/optimizing-content-efficiency-loading-third-party-javascript)).
- ⚠️ **I "terzi" li mette il marketing**, non lo sviluppatore: GTM con venti tag, chat, heatmap, pixel. Prima di chiedere allo sviluppatore di "velocizzare", si conta cosa c'è nel container.
- ⚠️ Al 20/09/2026 web.dev elenca **solo** LCP, INP e CLS; i blog che annunciano "nuove metriche 2026" o "valutazione per dominio" non trovano riscontro sulla pagina ufficiale. Non si citano.

## 7. Sicurezza minima e incidenti

**Il minimo non negoziabile:** core, tema e plugin aggiornati con cadenza scritta; account amministratore nominativi (niente `admin` condiviso), 2FA su admin, hosting, registrar e DNS; privilegi minimi (l'editor non è amministratore; l'utente MySQL ha solo SELECT/INSERT/UPDATE/DELETE); segreti fuori dal repository; SFTP, mai FTP in chiaro; editor di file dal pannello disabilitato (`DISALLOW_FILE_EDIT`); WAF davanti al sito; **backup cifrati, verificati e conservati fuori dal server** ([Hardening WordPress](https://developer.wordpress.org/advanced-administration/security/hardening/)).

- L'art. 32 GDPR chiede la capacità di **ripristinare tempestivamente** disponibilità e accesso ai dati dopo un incidente e un **processo di test periodico** delle misure ([art. 32](https://gdpr-info.eu/art-32-gdpr/)): il test di ripristino del backup non è pignoleria, è un obbligo.
- 🔴 **Data breach: il titolare notifica al Garante senza ingiustificato ritardo e, ove possibile, entro 72 ore da quando ne ha avuto conoscenza**, salvo che sia improbabile un rischio per gli interessati; **il responsabile (agenzia, hosting) informa il titolare senza ingiustificato ritardo** ([art. 33](https://gdpr-info.eu/art-33-gdpr/)). La notifica si fa solo via procedura telematica su [servizi.gpdp.it/databreach](https://servizi.gpdp.it/databreach/s/), una notifica oltre le 72 ore va motivata, ogni violazione va documentata in un registro anche se non notificata; se il rischio è elevato si informano anche gli interessati (art. 34) ([Garante, Data breach](https://www.garanteprivacy.it/data-breach)).
- **Processo scritto nel contratto:** chi rileva, chi avvisa il cliente **entro quante ore** (il conto delle 72 parte dal titolare, non dall'agenzia: se l'agenzia avvisa dopo tre giorni ha bruciato la finestra), chi isola, chi conserva i log, chi ripristina, chi scrive al legale.
- ⚠️ Password inviate via email o chat, condivise fra fornitori, mai ruotate a fine collaborazione: sono la prima causa di accesso non autorizzato che si vede sui siti PMI. Si usa un password manager con condivisione e si ruota tutto quando un fornitore esce.

## 8. Accessibilità in Italia: cosa è obbligatorio e per chi

- **European Accessibility Act, direttiva (UE) 2019/882:** si applica ai prodotti e servizi immessi/forniti **dal 28/06/2025**; i **servizi di commercio elettronico** rientrano espressamente (art. 3, punto 30); le **microimprese** che forniscono servizi sono esenti (meno di 10 persone **e** fatturato o bilancio ≤ 2 milioni €, art. 3 punto 23); periodo transitorio fino al 28/06/2030 per prodotti già in uso e contratti in essere ([EUR-Lex 2019/882](https://eur-lex.europa.eu/eli/dir/2019/882/oj)).
- **Recepimento: D.Lgs. 27/05/2022 n. 82**, obblighi dal 28/06/2025 (art. 1), e-commerce incluso (art. 1, c. 3, lett. f) ([Normattiva](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2022-05-27;82)). AgID è autorità di vigilanza per i servizi e ha pubblicato le **Linee guida sull'accessibilità dei servizi** (marzo 2026, dopo notifica alla Commissione), con una piattaforma per le segnalazioni degli utenti ([AgID, EAA guidelines](https://www.agid.gov.it/en/news/european-accessibility-act-eaa-agid-publishes-guidelines-digital-accessibility)). Sanzioni art. 24: 5.000-40.000 € (importi da fonte terza, [Accessiway](https://www.accessiway.com/it/blog/dlgs-82-2022-eaa); `[DA VERIFICARE]` sul testo del decreto).
- **Legge 4/2004 (Stanca):** obbliga le PA e i privati con fatturato medio triennale **oltre 500 milioni €** a pubblicare la *Dichiarazione di accessibilità* entro il **23 settembre di ogni anno** su form.agid.gov.it, con meccanismo di feedback e ricorso al Difensore civico digitale se non si risponde entro 30 giorni; riferimento tecnico la norma **UNI CEI EN 301 549** ([AgID](https://www.agid.gov.it/it/design-servizi/accessibilita)). EN 301 549 recepisce le WCAG 2.1 livello AA: è il riferimento da scrivere nel capitolato.
- **Regola operativa per un e-commerce PMI sopra la soglia di microimpresa:** il capitolato cita "conformità WCAG 2.1 AA / EN 301 549", il collaudo include tastiera sola, contrasto, testi alternativi, form con etichette ed errori leggibili, e una **pagina di accessibilità con contatto per le segnalazioni**. Un overlay a pagamento "che rende accessibile il sito" non sostituisce il codice: non risulta in nessuna fonte ufficiale come strumento di conformità.

## 9. Cookie e privacy: cosa si consegna allo sviluppatore

Il dettaglio sta nella skill `consent-mode-privacy`. Qui il minimo che va nel brief di sviluppo, con la fonte:

- **Nessuno script non tecnico parte prima del consenso**; lo scroll non è consenso; la **X** di chiusura equivale a rifiuto e deve avere la stessa evidenza di *Accetta*; il banner non si ripropone a chi ha rifiutato **prima di 6 mesi**; gli analytics sono esenti solo se anonimizzati (IP mascherato, solo statistiche aggregate, un solo dominio) ([Linee guida Garante 10/06/2021, docweb 9677876](https://www.garanteprivacy.it/home/docweb/-/docweb-display/docweb/9677876)).
- **Consent Mode**: default `denied` inizializzato prima di ogni tag, `update` al consenso, tag GA4/Ads/Meta **dentro GTM** e non nel tema o nei plugin "che mettono il pixel da soli" (prima causa di cookie prima del consenso).
- **Link a privacy policy e cookie policy nel footer di ogni pagina** e nei form; checkbox del consenso marketing non preselezionata; testo del form allineato all'informativa.
- Si consegna allo sviluppatore **la lista dei tag e dei cookie reali** (fatta guardando il sito in DevTools), non "metti il banner".

## 10. Continuità del tracciamento: in ogni intervento, non solo al go-live

**Ogni intervento sul sito (tema nuovo, plugin, migrazione, redesign del checkout) può azzerare il tracciamento senza che nessuno se ne accorga finché il report non crolla.** Il PM porta in ogni brief l'inventario:

- **Container GTM**: ID `GTM-XXXXXXXX`, snippet **il più in alto possibile in `<head>`** e `<noscript>` **subito dopo `<body>`** ([GTM install](https://support.google.com/tagmanager/answer/14847097?hl=en)); un solo container per sito ([6103696](https://support.google.com/tagmanager/answer/6103696?hl=en)).
- **Stream GA4**: ID misurazione `G-XXXXXXX`, in Amministrazione › Stream di dati ([12270356](https://support.google.com/analytics/answer/12270356?hl=en)). Se il tag GA4 è nel container, il tema non deve caricarne un secondo.
- **Search Console**: metodo di verifica in uso (file, meta tag, GA, GTM, record DNS) e dove sta il token: se sparisce con il tema nuovo, sparisce la proprietà ([9008080](https://support.google.com/webmasters/answer/9008080?hl=en)).
- **Eventi dataLayer**: elenco `evento → parametri → pagina` da mantenere identico. Per l'e-commerce, `purchase` con `transaction_id`, `value`, `currency`, `items`, preceduto da `dataLayer.push({ ecommerce: null })`; sequenza `view_item`, `add_to_cart`, `begin_checkout`, `purchase` ([GA4 ecommerce, GTM](https://developers.google.com/analytics/devguides/collection/ga4/ecommerce?client_type=gtm)). Un `purchase` senza `transaction_id` conta doppio a ogni refresh della thank-you page.
- **Mappa dei redirect** vecchio→nuovo per ogni URL che cambia, in **301 o 308** (permanenti; 302/307 non passano la canonicità), lato server e non via JavaScript ([Redirects](https://developers.google.com/search/docs/crawling-indexing/301-redirects), [MDN 301](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/301)).

**I numeri da fotografare prima e confrontare dopo (stesso giorno della settimana, 7 giorni):** sessioni/giorno per canale; `purchase` in GA4 contro ordini nel backend (lo scarto atteso è quello pre-intervento); eventi chiave per pagina; tag che scattano in Tag Assistant sulle 5 pagine tipo (home, categoria, prodotto, checkout, thank-you); pagine indicizzate e errori in Search Console; CWV per gruppo di URL; posizione media delle 20 query principali. Un intervento senza il "prima" non si può collaudare.

## 11. Checklist di go-live (si spunta per iscritto, con chi ha verificato)

1. `noindex` e password rimossi da produzione; robots.txt di produzione (non quello dello staging); `Disallow: /` assente.
2. Sitemap XML raggiungibile e inviata in Search Console; proprietà verificata **prima** del go-live.
3. Redirect testati su un campione della mappa + le 20 pagine più trafficate: un salto solo, niente catene, codice 301/308.
4. Monitoraggio 404 attivo (Search Console › Pagine, log del server) per 4 settimane; canonical assoluti e autoreferenziali, in HTTPS ([canonical](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls)); hreflang bidirezionale e autoreferenziale con `x-default` se multilingua ([hreflang](https://developers.google.com/search/docs/specialty/international/localized-versions)).
5. Form testati **end to end**: invio, email di notifica ricevuta (non solo "inviato"), record nel CRM, thank-you page con evento GA4.
6. Email transazionali (ordine, spedizione, reset password) recapitate in inbox su Gmail e Outlook, con SPF/DKIM/DMARC passati (sez. 3).
7. E-commerce: **ordine di test reale** con pagamento vero e rimborso, per ogni metodo di pagamento; evento `purchase` verificato in GA4 tempo reale con `transaction_id` e `value` corretti; stato ordine, fattura, email cliente.
8. Tag Assistant sulle 5 pagine tipo: container giusto, GA4 giusto, nessun tag doppio, consent mode attivo.
9. HTTPS su tutto, nessun mixed content nella console, certificato con rinnovo automatico e monitoraggio esterno; HSTS solo se tutto è pronto (sez. 4).
10. Favicon, `og:title`, `og:type`, `og:image`, `og:url` (i quattro obbligatori del protocollo, [ogp.me](https://ogp.me/)) e `og:description`; anteprima controllata su WhatsApp/LinkedIn.
11. Banner cookie attivo, policy linkate, nessun cookie prima del consenso (sez. 9).
12. PageSpeed Insights sulle pagine tipo: laboratorio senza errori bloccanti; appuntamento a **+28 giorni** per il campo (sez. 6).
13. Backup post go-live, tag di rilascio nel repository, credenziali ruotate e consegnate al cliente in password manager.

## 12. Manutenzione, preventivi, brief

### Contratto di manutenzione: cosa contiene

Cadenza aggiornamenti (core/plugin/tema) con test in staging prima; backup: frequenza, retention, sede esterna, **test di ripristino con cadenza**; monitoraggio uptime e scadenza certificato **con avviso a chi**; tempi di presa in carico e di risoluzione per gravità (sito giù ≠ typo); **monte ore** e tariffa dell'extra; cosa è **escluso** (sviluppo nuovo, contenuti, terze parti, ripristino da compromissione se il cliente ha ignorato gli aggiornamenti); accesso del cliente a repository, hosting e backup; processo incidenti (sez. 7); clausola art. 28 GDPR; cosa succede a fine contratto (consegna di codice, credenziali, DNS).

### Come si legge un preventivo

Si accetta solo se ha: **perimetro** (pagine, funzioni, integrazioni, lingue) scritto; **assunzioni** (contenuti e immagini forniti dal cliente entro quando; tema acquistato o custom; hosting esistente); **esclusioni** esplicite; **ore per voce** o prezzo a corpo con cosa comprende; **gestione delle change request** (come si stima, chi approva, a quale tariffa); ambienti e deploy (sez. 1-2); **cosa è consegnato** (repository, accessi, documentazione); garanzia post go-live (quanti giorni per i bug). Un preventivo a una riga "sito web 4.500 €" si rimanda indietro con questa lista.

### Come si scrive un task che non torna sbagliato

Titolo con il risultato atteso; **criteri di accettazione** verificabili ("il form X invia a Y e mostra Z", non "sistema il form"); **screenshot o registrazione** del problema con URL, browser, dispositivo; **ambiente** (staging/produzione) e dati di prova; **impatto sul tracciamento** (eventi da mantenere, sez. 10); **scadenza** e priorità motivata; chi collauda. Un task senza criterio di accettazione torna "fatto" e non lo è.

## 13. Igiene di un sito ereditato: ordine di controllo

1. **Chi possiede cosa**: dominio (registrar), DNS, hosting, repository, account Google (GTM, GA4, Search Console, Ads), CMP. Intestazione al cliente, accesso del PM. Senza questo tutto il resto è ostaggio.
2. **Backup**: esiste, dov'è, ultimo ripristino provato.
3. **Versione PHP e CMS** contro le tabelle di sez. 5; plugin abbandonati.
4. **Certificato**: chi lo rinnova, monitoraggio scadenza.
5. **Ambienti**: esiste uno staging? È indicizzato? (`site:staging.dominio.it`, `site:dev.dominio.it`).
6. **Account admin**: quanti, di chi, ultimo accesso, 2FA; ex fornitori ancora dentro.
7. **Tracciamento**: container e stream in uso, tag doppi, `purchase` contro ordini reali negli ultimi 30 giorni.
8. **Email**: SPF/DKIM/DMARC del dominio, mittente delle transazionali.
9. **Cookie**: cosa parte prima del consenso.
10. **CWV** sul campo per gruppo di URL; **404** e redirect rotti in Search Console.
11. **Accessibilità**: soglia microimpresa, presenza della pagina di accessibilità.
12. **Contratti**: manutenzione in essere, cosa copre, scadenza.

## 14. Meccanica dei pannelli (da verificare a mano)

- Nell'hosting del cliente, cambiare la versione PHP dal pannello agisce **subito su produzione** o si può provare prima sullo staging dello stesso pannello?
- Il backup "giornaliero" dell'hosting: quanti giorni di retention mostra davvero il pannello, e il ripristino è di tutto il sito o si può scegliere solo il database?
- Con Basic Auth sullo staging: il cron di WordPress e i webhook dei pagamenti (Stripe, PayPal) passano, o vanno esclusi dalla protezione per far funzionare gli ordini di test?
- Dopo un cambio di nameserver: il pannello del vecchio provider mostra ancora i record TXT/MX da copiare, o li cancella al trasferimento?
- Search Console, dopo un cambio tema: la proprietà verificata via meta tag cade **subito** o al successivo controllo periodico? Quanto tempo passa?
- Rapporto Core Web Vitals di Search Console: quanti giorni dopo il go-live compare il primo gruppo di URL per un sito piccolo?

## 15. Cosa non fare mai

- **Accettare un flusso di lavoro solo FTP** (niente repository, niente staging, modifiche a mano sui file live).
- **Accettare "non serve lo staging, è una modifica piccola".**
- **Ricevere o inviare credenziali via email o chat.** Password manager, accessi nominativi, rotazione all'uscita di un fornitore.
- **Accettare "sul mio computer funziona"** come chiusura di un bug: il bug si riproduce sullo staging con lo screenshot del cliente.
- **Lasciare modifiche di produzione non versionate**: al deploy successivo spariscono.
- **Fare il deploy senza backup di quel momento e senza piano di rollback scritto.**
- **Cambiare hosting senza aver esportato la zona DNS e senza aver abbassato il TTL una settimana prima.**
- **Mettere online uno staging senza password**, o rimuovere il `noindex` "dopo".
- **Copiare il database di produzione in staging senza contratto ex art. 28 e senza anonimizzazione.**
- **Mettere in produzione un PHP fuori supporto** o un CMS sotto i requisiti ufficiali.
- **Scrivere nel contratto il punteggio Lighthouse** come metrica di accettazione: si scrivono LCP, INP, CLS sul campo.
- **Attivare HSTS con `preload`** prima che ogni sottodominio risponda in HTTPS.
- **Rinnovare i certificati a mano.**
- **Far partire tag prima del consenso** perché "il plugin lo fa da solo".
- **Andare live senza l'ordine di test reale e il `purchase` verificato.**
- **Firmare un preventivo senza esclusioni e senza gestione delle change request.**

## Fonti (verificate 20/09/2026)

**Ufficiali**
- PHP: [Supported versions](https://www.php.net/supported-versions.php) · [News 2026 (8.6 alpha/beta/RC)](https://www.php.net/archive/2026.php)
- WordPress: [Requirements](https://wordpress.org/about/requirements/) · [PHP compatibility and WordPress versions](https://make.wordpress.org/core/handbook/references/php-compatibility-and-wordpress-versions/) · [Dropping PHP 7.2/7.3, 09/01/2026](https://make.wordpress.org/core/2026/01/09/dropping-support-for-php-7-2-and-7-3/) · [Hardening WordPress](https://developer.wordpress.org/advanced-administration/security/hardening/)
- WooCommerce: [Server requirements](https://woocommerce.com/document/server-requirements/) · [From PHP 7.4 to 8.1, 08/09/2026](https://developer.woocommerce.com/2026/09/08/from-php-7-4-to-8-1/)
- PrestaShop: [System requirements v9](https://devdocs.prestashop-project.org/9/basics/installation/system-requirements/)
- Let's Encrypt: [FAQ](https://letsencrypt.org/docs/faq/) · [Integration guide](https://letsencrypt.org/docs/integration-guide/) · [Rate limits](https://letsencrypt.org/docs/rate-limits/) · [Certificate lifetimes](https://letsencrypt.org/docs/cert-lifetimes/) · [Ending expiration emails, 22/01/2025](https://letsencrypt.org/2025/01/22/ending-expiration-emails/) · [Rate limits and 45-day certs, 24/02/2026](https://letsencrypt.org/2026/02/24/rate-limits-45-day-certs) · CA/B Forum [Ballot SC-081v3](https://cabforum.org/2025/04/11/ballot-sc081v3-introduce-schedule-of-reducing-validity-and-data-reuse-periods/)
- MDN: [HSTS](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Strict-Transport-Security) · [Mixed content](https://developer.mozilla.org/en-US/docs/Web/Security/Mixed_content) · [301](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/301) · [TTL](https://developer.mozilla.org/en-US/docs/Glossary/TTL) · [HTTP caching](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Caching) · [HTTP authentication](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Authentication)
- Google Search Central: [Site move with URL changes](https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes) · [Changing your hosting (no URL change)](https://developers.google.com/search/docs/crawling-indexing/site-move-no-url-change) · [Block indexing (noindex)](https://developers.google.com/search/docs/crawling-indexing/block-indexing) · [Remove information](https://developers.google.com/search/docs/crawling-indexing/remove-information) · [robots.txt intro](https://developers.google.com/search/docs/crawling-indexing/robots/intro) · [Redirects](https://developers.google.com/search/docs/crawling-indexing/301-redirects) · [Canonical](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls) · [hreflang](https://developers.google.com/search/docs/specialty/international/localized-versions)
- Google, web.dev e PSI: [Web Vitals](https://web.dev/articles/vitals) · [LCP](https://web.dev/articles/lcp) · [INP](https://web.dev/articles/inp) · [CLS](https://web.dev/articles/cls) · [Third-party JavaScript](https://web.dev/articles/optimizing-content-efficiency-loading-third-party-javascript) · [PageSpeed Insights, about](https://developers.google.com/speed/docs/insights/v5/about) · Search Console [Core Web Vitals report 9205520](https://support.google.com/webmasters/answer/9205520?hl=en) · [Verifica proprietà 9008080](https://support.google.com/webmasters/answer/9008080?hl=en)
- Google tag e GA4: [GTM install 14847097](https://support.google.com/tagmanager/answer/14847097?hl=en) · [GTM container 6103696](https://support.google.com/tagmanager/answer/6103696?hl=en) · [GA4 Measurement ID 12270356](https://support.google.com/analytics/answer/12270356?hl=en) · [GA4 ecommerce dev guide](https://developers.google.com/analytics/devguides/collection/ga4/ecommerce?client_type=gtm)
- Email: [Gmail sender guidelines 81126](https://support.google.com/a/answer/81126?hl=en) · [Set up SPF](https://knowledge.workspace.google.com/admin/security/set-up-spf)
- GDPR: [art. 28](https://gdpr-info.eu/art-28-gdpr/) · [art. 32](https://gdpr-info.eu/art-32-gdpr/) · [art. 33](https://gdpr-info.eu/art-33-gdpr/) · Garante [Data breach](https://www.garanteprivacy.it/data-breach) · [Linee guida cookie 10/06/2021, docweb 9677876](https://www.garanteprivacy.it/home/docweb/-/docweb-display/docweb/9677876)
- Accessibilità: [Direttiva (UE) 2019/882](https://eur-lex.europa.eu/eli/dir/2019/882/oj) · [D.Lgs. 82/2022 su Normattiva](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2022-05-27;82) (letto solo l'art. 1) · [AgID accessibilità](https://www.agid.gov.it/it/design-servizi/accessibilita) · [AgID, EAA guidelines published](https://www.agid.gov.it/en/news/european-accessibility-act-eaa-agid-publishes-guidelines-digital-accessibility) · [AgID, consultazione 15/05/2025](https://www.agid.gov.it/it/notizie/eaa-consultazione-linee-guida-agid-accessibilita-dei-servizi)
- Altro: [git-scm, Tagging](https://git-scm.com/book/en/v2/Git-Basics-Tagging) · [Open Graph protocol](https://ogp.me/)

**Terze parti (etichettate nel testo)**
- [Accessiway su D.Lgs. 82/2022](https://www.accessiway.com/it/blog/dlgs-82-2022-eaa) (art. 21 vigilanza AgID, art. 24 sanzioni 5.000-40.000 €) · [tuteladigitale.it, regolamento vigilanza AgID 11/08/2026](https://www.tuteladigitale.it/journal/cybersicurezza/regolamento-vigilanza-accessibilita-digitale-agid-2026/) · php.watch e laravel-news per la GA di PHP 8.6 al 19/11/2026 · community.letsencrypt.org per il profilo `tlsserver` a 45 giorni opt-in dal 13/05/2026.

**Non leggibili via fetch il 20/09/2026, da ricontrollare a mano:** developer.woocommerce.com/docs/woocommerce-server-requirements (404, usata woocommerce.com/document); garanteprivacy.it/temi/databreach (404, usata /data-breach); support.google.com/analytics/answer/9964640 (contenuto non pertinente); testo integrale del D.Lgs. 82/2022 oltre l'art. 1 (microimprese, art. 21, art. 24) e determinazione AgID delle Linee guida di marzo 2026 (numero e data da fonti terze: det. 38 del 04/03/2026); post Let's Encrypt del 02/12/2025 (date 64/45 giorni riprese da riassunto e da cert-lifetimes).
