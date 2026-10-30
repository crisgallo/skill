# Changelog gtm (fino al 30/10/2026 «gtm-server-side»)

## 30/10/2026
- 🔴 Skill rinominata da «gtm-server-side» a «gtm» su richiesta di Cristiano (chat Gruppo NEM, 30/10/2026): copre il container web e quello server, e il nome vecchio faceva pensare al solo server. Descrizione e titolo aggiornati, nota in sez. 0. Nuova sez. 15 «Siti editoriali» con i soli quattro temi (video, paywall e abbonati, più testate su container separati, articoli in webview nelle app), tutti [DA VERIFICARE]: le regole arrivano dal lavoro sul pannello dal 09/11/2026. Su claude.ai va eliminata la skill gtm-server-side e caricata gtm.
## 27/10/2026
- 🟡 Sez. 11: pagina Cookie Keeper di Stape aggiornata il 26/10/2026: 39 cookie standard con le durate per famiglia (13 mesi GA, 400 giorni affiliazioni, 90 giorni cookie pubblicitari, 1 mese ttclid), master cookie dai plugin, test con Safari 16.4+.

## 23/10/2026
- 🟡 Sez. 11: annuncio WebKit del 19/10/2026 (iOS, iPadOS, macOS, visionOS 27): blocco a livello di dominio dei servizi terzi di risoluzione delle identità via email; secondo Stape (22/10) il server-to-server non è toccato; controllo della quota Apple in GA4 e dei cali dopo l'aggiornamento. Fonti aggiunte.

## 17/10/2026
- 🟡 Sez. 9: dettaglio dell'ottimizzazione dei container dalle note Stape del 16/10/2026 (terza parte): tag Destination per GA, Google Ads e Floodlight, impostazioni condivise, procedura guidata, accessi in lettura al container, «Manage data transmission settings» per il consenso, Anteprima con richieste trattenute.
## 13/10/2026
- 🟡 Sez. 9: nota di rilascio GTM del 12/10/2026 «Optimizing Google Tag Manager containers»: i container mandano i dati direttamente ai prodotti Google senza un gtag.js separato, destinazioni e tag collegati; disponibilità generale del flusso opt-in del 20/08.

## 12/10/2026
- 🟡 Sez. 7: prezzi Stape riletti sulla pagina pricing: Pro 20 $/mese a pagamento mensile (17 con l'annuale), Business 100 (83), Enterprise 200 (167); prima la skill riportava solo le cifre dell'annuale come prezzo mensile.

## 09/10/2026
- 🔴 Sez. 9: nota di rilascio GTM dell'08/10/2026: i container si inizializzano al caricamento con o senza gtag('config') e i comandi config compaiono nel dataLayer come eventi gtag.config; controllo degli attivatori evento personalizzato con jolly e snippet gtag.js su ogni pagina per chi usa ancora il codice config. 🟡 17/09/2026: riepilogo di versione suggerito dall'AI.
## 02/10/2026
- 🟡 Sez. 11: documentazione Cookie Keeper riscritta il 02/10/2026 (oltre 40 cookie, attivazione per piattaforma, snippet del Custom Loader da aggiornare); piani invariati. Data di verifica al 02/10.
## 01/10/2026
- 🔴 Sez. 4: regola di Cristiano sull'Anteprima corretta (chat di manutenzione, `gtm_e_consenso.md`, 01/10/2026): la pagina del sito si apre in una finestra nuova fuori dal gruppo di schede della chat, quindi clicca e compila sempre Cristiano anche se l'Anteprima l'ha aperta la chat; seconda sessione rompe il collegamento; dialogo «Arresta debug» si annulla; la scheda Tag Assistant non si chiude da Chrome. Finestra nuova confermata su 6107056.
## 29/09/2026
- 🔴 Sez. 3 e 4: due regole di Cristiano dalle chat Cowork del Blog (12-16/08/2026), promosse a sapere globale il 28/09/2026: le tendine del pannello GTM non si impostano via JavaScript su righe esistenti, riga nuova nasce con «contiene», si ricarica la pagina dopo ogni salvataggio, Page Path uguale a /slug/ (`feedback_gtm_select_via_js.md`); nei test in Anteprima i clic li fa Cristiano e Claude legge il Tag Assistant, scheda Variabili per chiudere la verifica, un secondo Tag Assistant rompe la sessione (`feedback_anteprima_gtm_divisione_lavoro.md`). Fonti web e data di verifica invariate.
## 28/09/2026
- 🟡 Sez. 1: la regola «un solo tag Google» ora cita la frase esatta di Google (13543899, un solo tag Google per tutto il sito) e i 30 minuti prima che la raccolta dati parta (15756616). Rilette senza cambi 6107056 (Anteprima), 10718549 (consenso), 13034206, 7201382 (DebugView), annunci GTM. Data di verifica al 28/09.
## 20/09/2026

- Prima stesura da fonti ufficiali: release notes GTM (4620708) con le voci 01/05, 22/06, 01/07, 09/07/2026; pagina "Updates to Google tag and Google Tag Manager" del 20/08/2026 (17079602); prefisso dell'ID e restrizioni (17070049); tag Google in GTM (15756616) e annuncio (13543899); eventi GA4 in GTM (13034206); tipi di attivatore (7679319); consenso in GTM (10718549) e consent mode (9976101); Anteprima (6107056), Tag Assistant (10039345), Tag Diagnostics (14681508); aree di lavoro (7059647), versioni e approvazioni (6107163), permessi (6107011); Google tag gateway (16816376 e developers); dataLayer e e-commerce GA4 (developers); server-side: intro, dominio personalizzato, invio dati, SST fundamentals lezione 5, consent mode server, debug, Cloud Run, App Engine, setup manuale; GA4 DebugView (7201382) e Tempo reale (9271392); Meta: deduplica Pixel/CAPI, CAPI Tag per GTM server, Using the API (Test Events); Stape: pricing (/price), plan tiers, billing, custom domain, Custom Loader, Cookie Keeper, zone server, Global vs EU, Meta CAPI setup, Unique Event ID, news 21/08/2026, blog costi 04/09/2025; Garante, Linee guida cookie 10/06/2021 (9677876).
- Non verificato: pagine ufficiali del client GA4, dei cookie server-side (FPID) e di "how it works" su developers.google.com (404; il dettaglio FPID viene da Simo Ahava, fonte terza); pagina dependency-serving (rimanda al gateway); stape.io/pricing (404, letta /price) e valuta/IVA mostrate a un account italiano; documentazione Stape del tag Facebook Conversions API (404); pagina Meta payload-helper senza sezione Test Events; pagina ufficiale della policy Google sul consenso in EEA; grace period e soglia del 10% sulle quote Stape (solo fonte terza); possibilità di cambiare zona server Stape dopo la creazione; regola "5-10 richieste per pagina vista" (empirica di terzi); percentuale di recupero segnali del gateway (11%, fonte terza che cita Google).
