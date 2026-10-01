# Changelog wordpress-woocommerce

## 01/10/2026
- 🔴 Sez. 7: regola di Cristiano (chat di manutenzione, `wordpress.md`, 01/10/2026): procedura per modificare uno snippet WPCode da Chrome senza rischiare il sito (controllo anti cache, copia in localStorage con somma di controllo, replaceRange su marcatore, CRLF, cache x-ac, form agganciati). Non verificata su editor diversi da CodeMirror.
- 🟡 Sez. 0: calendario WordPress 7.2 (Beta 1 20–22/10, RC1 17–19/11, code freeze 7–9/12, rilascio 8–10/12/2026) dalla pagina ufficiale; Gutenberg 24.1 del 30/09 (strumenti di design uniformi fra blocchi, nessuna regola cambia). Doc Google for WooCommerce riletta: invariata (3.8.1 per la Merchant API già scritto). Data di verifica al 01/10.
## 29/09/2026
- 🔴 Sez. 3: regola di Cristiano dalle chat Cowork del Blog (05-07/08/2026), promossa a sapere globale il 28/09/2026 (`feedback_wp_ereditare_stile_blocchi.md`): un blocco o un campo nuovo non eredita lo stile dei vicini, si copiano attributi e classi da un elemento fratello e si verifica lo stile calcolato. Fonti web e data di verifica invariate.
## 28/09/2026
- 🔴 Sez. 2: WordPress 7.1.2 del 22/09/2026, release di sicurezza di gravità critica (inclusione di file PHP locale nella risoluzione dei template, CVE-2026-87902), backport fino alla 4.7, auto-update in background: su ogni sito cliente si controlla la versione 7.1.2 o successiva. Trovata il 28/09 tramite la pagina del plugin Two-Factor (0.17.0, «tested up to 7.1.2») e confermata sul post ufficiale wordpress.org/news.
- 🟡 Fonti: pagina GTM 14842164 ora letta (un container per sito, nome = URL principale). Rilette senza cambi la doc Google Analytics for WooCommerce, il post di WordPress 7.1 e la pagina del plugin Two-Factor. Data di verifica al 28/09.
## 23/09/2026
- Sez. 1: WooCommerce 11.1.2 del 22/09/2026 (changelog ufficiale).
- Sez. 8: Google for WooCommerce almeno 3.8.1 per la Merchant API; Google Analytics for WooCommerce non dismesso (doc ufficiali).

## 22/09/2026
- Sez. 1: WooCommerce 11.2.0 in beta dal 21/09/2026 (email di recesso configurabili, CSV per GTIN); solo staging (changelog ufficiale). Data in cima riscritta.

## 20/09/2026

- Prima stesura da fonti ufficiali: wordpress.org (requisiti, Settings Reading, permalink, releases 2026 con 7.0 del 20/05, 7.1 del 19/08 e 7.1.1 di sicurezza del 17/09), make.wordpress.org (tabella PHP/WordPress del core handbook aggiornata 19/08/2026 con ritiro dell'etichetta "beta support" a maggio 2026, tabella del team hosting, sitemap 5.5, Site Health cache checks 6.1, schedule 7.2), developer.wordpress.org (upgrading e auto-update, hardening, migrating, wp search-replace, filtro xmlrpc_enabled, optimization), developer.woocommerce.com (changelog, release calendar, note di 11.0, 11.1 e 11.1.1, politica L-1, configurazione cache), woocommerce.com/document (server requirements, HPOS, Cart/Checkout blocks, Google for WooCommerce e setup, Google Analytics for WooCommerce, Meta for WooCommerce, WooPayments paesi, tasse), wordpress.com/support e blog (plan features, plugins su tutti i piani a pagamento dal 02/04/2026, changelog 08/05/2026, Google Analytics, sitemaps, feeds, staging, Blaze e crediti), php.net supported versions, Google (GA4 ecommerce, WooCommerce Google tag 12973528, Site Kit Tag Manager), iubenda, Complianz, Cookiebot su wordpress.org, issue GitHub #4047 di Meta for WooCommerce.
- Non verificato: pagina support.cookiebot.com sull'installazione WordPress (403); pagina Site Kit "managing Tag Manager" (404, usata la pagina supported-services); corpo della guida GTM "install web container" (14842164); guida "Update PHP" su developer.wordpress.org (404); pagina budget Blaze (404, dati da promote-a-post e blaze-credits); guida sync staging WordPress.com; doc WooCommerce sulle aliquote IVA UE digitali; elenco eventi standard di Meta for WooCommerce (assente dalla doc); deduplicazione GA4 su transaction_id nella stessa sessione; installabilità di Site Kit su piano Personal WordPress.com; plugin di fatturazione elettronica citati solo come fatti di prodotto dalle pagine dei produttori.
