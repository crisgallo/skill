# Changelog prestashop

## 25/11/2026
- 🟡 Sez. 10: checklist di igiene di sicurezza del progetto (post del 24/11/2026): 12 delle 18 falle della 9.2.1 richiedono un account back office o una chiave webservice; WAF e rate limiting, cartella admin con IP o Basic Auth, 2FA via modulo e nativa prevista nella 9.3, niente rotazione password a 90 giorni, prefisso tabelle non `ps_`.

## 22/11/2026
- 🟡 Sez. 15: sapere via Mother (22/11): modulo ricaricato da zip con versione non aggiornata in ps_module, «Aggiorna comunque» per allinearla.

## 21/11/2026
- 🔴 Sez. 10 e 15: 3 saperi via Mother (21/11): Slider Revolution, la 6.2.22.5 offerta come aggiornamento è vulnerabile e il blocco lato server rende 403 l'editor; Creative Popup con «Targets pages» su All che si apre in cassa; SMTP Microsoft 365 bloccato dai security defaults, errore 535 nel Log.

## 20/11/2026
- 🔴 Sez. 1: PHP 8.6.0 del 19/11/2026 non supportato da nessuna versione di PrestaShop secondo la tabella dei requisiti: versione PHP dell'hosting da bloccare a 8.5.

## 18/11/2026
- 🔴 Sez. 10 e 15: 3 saperi via Mother #28 (18/11): linguette AxonCreator da categoria solo con i primi 10 prodotti, notifiche «New order» perse col server di posta giù, versione di ps_facetedsearch e revsliderprestashop leggibile nel config.xml pubblico; Mother ha riletto l'advisory Friends of Presta su CVE-2026-117360 (nota sulla fonte aggiornata).
- 🟡 Sez. 1: tabella dei requisiti PHP di devdocs aggiornata il 17/11/2026 con la riga 9.1~9.2 (PHP 8.1-8.5, raccomandato 8.5); nessun requisito cambiato.

## 17/11/2026
- 🔴 Sez. 10: CVE-2026-54159 di ps_facetedsearch (3.0.0-4.0.3, RCE senza autenticazione, CVSS 10, corretta nella 4.0.4, GHSA del 10/07/2026): controllo della versione in Moduli e aggiornamento immediato. Nota sulla fonte dell'avviso Slider Revolution (sola advisory Friends of Presta, non su NVD).
- 🔴 Sez. 2, 3, 4, 6, 7, 8 e 15: 14 saperi verificati in pratica dalle chat di un e-commerce (via Mother #28): limite di spazio del Theme Customizer, CSS e redirect da moduli minimi, JSON-LD da modulo con tabella propria, aggiornamento di moduli con dati per prodotto, mail del tema, pagine CMS noindex, token non valido, regole carrello cumulabili, Cross Selling On Cart, foto principale eager, select_promotion, Smart Blog, Creative Popup.

## 16/11/2026
- 🔴 Sez. 10: avviso critico del 14/11/2026 sul modulo Slider Revolution for PrestaShop (CVE-2026-117360, CVSS 9.8, RCE senza autenticazione, sfruttato in rete, nessuna patch): sostituire il modulo e cancellarne i file, disattivarlo non basta; blocco dei percorsi dal web server nell'attesa; controllo file e credenziali.

## 11/11/2026
- 🔴 Sez. 17 nuova (caso verificato sul back office di un negozio 8.0.4 il 10/11/2026, via chat [Manutenzione] Sistema #25): l'import CSV con sole colonne ID e Accessori crea un prodotto vuoto attivo con «Forza tutti gli ID» = No e riduce le categorie a una cambiando categoria principale e canonical con = Sì; gli accessori si salvano dalla scheda prodotto (campo related_products), confronto di tutti i campi prima e dopo, poi Pulisci la cache; prova su un prodotto con controllo di categorie e numero prodotti. Bullet in sez. 16.

## 10/11/2026
- 🔴 Sez. 1: release di sicurezza PrestaShop 9.2.1 e 8.2.9 del 09/11/2026 (18 e 15 falle, in gran parte High, diverse senza account: installer, codici sconto, ordini doppi, reset password; chiavi webservice in multinegozio; SVG e import dal back office; Admin API solo su 9); moduli ps_emailsubscription 3.0.1 e GDPR; cosa fare oggi. Tabella versioni aggiornata; data in cima al 10/11/2026.

## 05/11/2026
- 🟡 Sez. 1: Core Monthly di ottobre 2026 (03/11): consolidamento 9.2, Admin API con scope obbligatorio, 170 PR; nessuna release nuova.
## 24/10/2026
- 🟡 Sez. 1: avviso informativo php.net del 23/10/2026 su session upload progress (CVE-2026-115560): nessuna release nuova, la mitigazione `session.upload_progress.enabled=0` del 21/10 resta al suo posto; riguarda solo chi cambia il serialize handler a runtime. Fonte aggiunta.

## 22/10/2026
- 🔴 Sez. 1: avviso di sicurezza php.net del 21/10/2026 (due RCE critiche nel runtime PHP, CVSS 9.2) e avviso PrestaShop dello stesso giorno: la patch è dell'hosting, non di PrestaShop; versioni corrette 8.2.35, 8.3.36, 8.4.27, 8.5.12; controllo in Parametri avanzati > Informazioni, conferma scritta dell'hosting con riavvio dei processi, mitigazioni temporanee.
## 09/10/2026
- 🟡 Sez. versioni: Core Monthly di settembre (08/10/2026): Hummingbird 2.1.2 con 9.2, moduli nativi aggiornati, nessuna 9.2.1 annunciata, PS Summit 4-5/11 con anteprima di PrestaShop 10.
## 01/10/2026
- 🔴 Sez. 1, 13: PrestaShop 9.2.0 stabile del 30/09/2026 (PHP 8.1-8.5, Update Assistant 7.6.6 da 9.0.x/9.1.x, Hummingbird 2.1.2, interruttore one-page/quattro pagine, Extra Properties, Ask AI). 9.1.x superato, fine manutenzione [DA VERIFICARE]. Data di verifica al 01/10.
## 29/09/2026
- 🟡 Sez. 1: PrestaShop 9.2 RC1 del 21/09/2026 (PHP 8.1-8.5, nessun upgrade da beta o RC, stabile non ancora uscita). Rilette senza cambi le pagine su 1.7.8 e 8.2.x in supporto esteso e la 8.2.8. Data di verifica al 29/09.
## 20/09/2026
- Prima stesura da fonti ufficiali: devdocs (system requirements 1.7/8/9, patch release lifecycle, optimizations, core updates 9.0 e 9.1, multistore, file structure), docs 8 (SEO and URLs, Performance, Managing products, Multistore), build.prestashop-project.org (1.7.8 extended support 05/01/2023, 9.0 del 10/06/2025, 8.2.x extended support 04/07/2025, 9.1 del 23/03/2026, 9.2 feature freeze e Beta 1 di luglio 2026, 9.1.5 e 8.2.8 del 18/08/2026, Core Monthly luglio e agosto 2026), Security Charter, GitHub dei moduli nativi (autoupgrade, ps_googleanalytics, gsitemap, ps_facetedsearch, psgdpr, hummingbird, classic-theme head.tpl, psxmarketingwithgoogle, ps_facebook), PR #37066 e discussione #40335 sul noindex delle faccette, issue su canonical combinazioni e redirect prodotti, Google Ads 10431635, Merchant Center 12159029 e 12158123, Linee guida cookie del Garante.
- Non verificato: help center PrestaShop (Marketing with Google, FAQ PrestaShop Metrics con la data di dismissione 01/01/2026, best practices di sicurezza, debug mode) e pagine Addons (FAQ, T&C, scheda 85751) rispondono 403; lista esatta degli eventi GA4 di ps_googleanalytics 6.0.0 e presenza di Consent Mode; x-default hreflang e canonical della paginazione sul tema Classic 9.1; cron di gsitemap; compatibilità di ps_facebook con 9.x; durata degli aggiornamenti inclusi nelle licenze Addons; presenza dell'opzione 410 sulla pagina prodotto 9.1.
