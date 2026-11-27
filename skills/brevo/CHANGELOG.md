# Changelog brevo

## 27/11/2026
- 🟡 Sez. 3: import con EXT_ID nuovo su un'email già presente senza EXT_ID sostituisce il contatto (storico perso, blocklist che può azzerarsi), dal changelog API. 🟡 Sez. 5b: priorità dei task None/Low/Medium/High, solo High per gli account creati prima del 03/11/2026 (pagina aggiornata il 26/11).

## 25/11/2026
- 🟡 Sez. 5: quote dell'account e delle automazioni del nuovo editor (pagina del 25/11/2026: 2.000 contatti unici su Free e Starter, 500 aggiunti a mano, 6.000 eventi e 3.000 passi al minuto, 150 campagne programmate, 20 webhook in entrata); trigger e regole aggiornati il 24/11 (Best channel e WhatsApp reply solo Professional ed Enterprise, ritardo minimo un minuto, trigger web push e wallet).

## 24/11/2026
- 🟡 Sez. 2: sapere via Mother (24/11): i rapporti DMARC con rua solo verso Brevo non si leggono nel pannello; prima di p=quarantine serve un secondo rua leggibile.
- 🟡 Sez. 11: changelog del 23/11/2026, sezione «Brevo MCP» (connettore nel marketplace di Claude e plugin ChatGPT per i casi comuni, connessione diretta con chiave MCP per tutti gli strumenti).

## 22/11/2026
- 🟡 Sez. 1: pagina prezzi riletta il 22/11/2026 (volumi dichiarati per Starter e Professional, 10 postazioni, MCP per ChatGPT e Claude fra le funzioni), prezzi invariati.

## 19/11/2026
- 🟡 Sez. 3: provvedimento del Garante n. 622 del 03/09/2026 (doc. web 10310279): e-mail promozionale a un professionista sul legittimo interesse con indirizzo preso dal sito dell'Ordine dichiarata illecita, ammonimento; consenso obbligatorio ex art. 130.

## 18/11/2026
- 🔴 Sez. 3, 4 e 5: 4 saperi verificati in pratica dalle chat di un e-commerce di integratori (via Mother #28, 18/11): frase per prodotto con blocco {% if item.id %} generato dal foglio, campi degli eventi del modulo PrestaShop, MPP esclusi nei segmenti e attribuzione a 7 giorni, email HTML leggibili su Gmail per iPhone.
- 🟡 Sez. 12: release del 27 e 29/10/2026 (SMS in altri paesi, segmento per posizione rilevata, passaggi Wallet usati, pop-up per lista e attributi) e articolo del 17/11 sui modelli collegati nei passi email del nuovo editor automazioni. Titolo della sezione esteso a novembre.

## 17/11/2026
- 🔴 Sez. 3, 4, 5, 9 e 14: 13 saperi verificati in pratica dalle chat di un e-commerce (via Mother #28): filtro replace assente nei modelli, mail di benvenuto dell'integrazione PrestaShop, indirizzo di risposta che si perde, condizione di riavvio sugli ordini, attributo del consenso al pixel, uscite e filtri non retroattivi, eventi d'ordine del modulo PrestaShop, attivazione delle automazioni, UTM dei passi email, colonna Predefinito dei mittenti, editor drag and drop, modulo d'iscrizione con reCAPTCHA.
- 🔴 Sez. 2: stati di invio dell'account nel Deliverability center (Validated, Pending validation, Under review, Paused, No longer available, Sending restricted), seconda pausa potenzialmente definitiva, abbonamento che continua. Sez. 5: Brevo PushOwl unico collegamento Shopify supportato, procedura e import che sovrascrive attributi e iscrizioni.

## 14/11/2026
- 🟡 Sez. 10: release di prodotto riletta (Content Hub al posto della Content Library dal 12/10, pagina di report per automazione dal 14/10, quattro priorità dei task CRM dal 04/11). Data in cima al 14/11/2026.

## 13/11/2026
- 🔴 Sez. 10: changelog API del 10/11/2026 su ordini ed eventi (date UTC con Z, aggiornamenti che si accodano, endpoint singolo vivo e batch con historical: true per lo storico, eventi via API salvati come personalizzati e quindi senza automazioni e-commerce, tracker o trackEvent per il carrello); webhook con api_key_name e campi di automazione. 🟡 Sez. 1: prezzi annuali della pagina prezzi. Data in cima al 13/11/2026.

## 04/11/2026
- 🔴 Sez. 9: procedura sul pannello per il consenso al pixel per contatto (Settings > Contacts > Per-contact pixel tracking consent, «Track contacts whose consent is unknown» su No, attributi creati, casella nei form, link «Revoke pixel tracking consent link» o placeholder `{{ revoke_open_pixel_tracking }}` nel footer, campo API `contactPixelTrackingConsent`, finalità non canale), dall'articolo 37113920427922 aggiornato il 03/11; chiuso il [DA VERIFICARE] di ieri: la revoca del solo pixel con iscrizione mantenuta è coperta. Menu del tracciamento anonimo (11643306229906). Vademecum del Garante del 05/10: tracking pixel fra le ispezioni del secondo semestre 2026. Altri otto articoli Brevo con data 03/11 riletti: nessun numero cambiato.
## 03/11/2026
- 🔴 Sez. 9, 12 e Fonti: Linee guida del Garante sui tracking pixel nelle e-mail (provv. n. 284 del 17/04/2026, GU n. 98 del 29/04/2026, adeguamento entro il 29/10/2026): consenso preventivo per il pixel che misura il singolo destinatario, deroghe (statistica aggregata, sicurezza, comunicazioni dovute), informativa, rifiuto del solo pixel con link o icona; cosa fare su Brevo (consenso per contatto o tracciamento anonimo), revoca granulare [DA VERIFICARE]. Correzione della riga precedente che diceva «per l'Italia nessuna indicazione del Garante» (segnalazione della chat di manutenzione del 03/11).
- 🟡 Sez. 11: changelog API del 30/10 e 02/11: campi `shipping` e SKU sugli ordini, parametro `secondarySortByModifiedAt` su GET /orders. Articoli CRM 360019003659 e 360019089760 riletti il 03/11: coerenti con references/crm.md.
## 31/10/2026
- 🟡 Sez. 11: articolo sulle chiavi API ritoccato il 30/10/2026: email al proprietario a ogni chiave creata o cancellata, stato read-only dopo una compromissione.
## 30/10/2026
- 🟡 Sez. 11: changelog API di ottobre 2026 (letto il 30/10): `removeTrackingPixel` solo Enterprise, OAuth 2.0 machine-to-machine con endpoint spostato il 13/10, filtri `modifiedSince` e `createdSince` sugli export, export vuoto risponde 200. Nessuna regola operativa cambia.
## 28/10/2026
- 🟡 Sez. 9: articoli sul reinvio aggiornati il 27/10/2026: «Requeue» rinominato «Send to new contacts», «Resume campaign» per le sospese, reinvio ai non-aperti una volta sola e non con lotti o warm-up, duplicare per i nuovi contatti sconsigliato.

## 27/10/2026
- 🟡 Sez. 11: articolo 209467485 aggiornato il 26/10/2026: chiavi Restricted per risorsa o Full, validità 7 giorni-1 anno o senza scadenza, disattivazione dopo 90 giorni senza chiamate riuscite con email 7 giorni prima, chiave MCP opzionale.

## 17/10/2026
- 🟡 Sez. 11: changelog API 14-17/10/2026: filtri `modifiedSince`/`createdSince` sull'export contatti, endpoint di scansione wallet pass, export senza risultati che risponde 200 vuoto (prima 202 con processId), app OAuth pubbliche con Brevo CLI 2.5.0.
## 14/10/2026
- 🟡 Sez. 9 e 11: regola di Cristiano del 13/10/2026 (confronti fra campagne solo a parità di giorni dall'invio, `feedback_report_e_numeri.md`); changelog del 13/10/2026: endpoint del token OAuth M2M su api.brevo.com e scope esplicito (senza scope il token riceve tutti gli scope dell'app).

## 09/10/2026
- 🟡 Sez. 1: crediti email prepagati (articolo 4409354969746 aggiornato l'08/10/2026): pacchetti da 5.000 a 1 milione, non scadono, funzioni Starter, add-on non rimborsabili; articolo prezzi 208589409 riletto, stessi numeri.
## 08/10/2026
- 🟡 Sez. 11: dal changelog API (06-07/10/2026): autenticazione OAuth 2.0 machine-to-machine accanto alla chiave API, guide SMTP per Base44, Bolt.new, Lovable, n8n, v0 e Supabase Auth. Nessuna regola cambiata.
## 06/10/2026
- 🔴 Sez. 11: `POST /contacts/batch` viene spento il 30/10/2026, si passa a `POST /v3/contacts/import` (changelog API Brevo, nota del 12/05/2026 letta il 06/10/2026); su un account ereditato si chiede all'integratore quale endpoint usa.
## 02/10/2026
- 🔴 Sez. 13: regola di Cristiano verificata il 02/10/2026 (chat di manutenzione): iscrizioni automatiche da moduli senza captcha (segni, conferme cliccate in 10-70 secondi, «Qualsiasi tipo di email» nei segmenti conta anche le transazionali); sospetti esclusi dal segmento e in blocklist, protezioni da chiedere al sito.
- 🔴 Sez. 9, 13 e 14: regola di Cristiano verificata il 02/10/2026 (chat di manutenzione): le Impostazioni predefinite delle campagne hanno un solo «Salva» e un mittente predefinito non verificato blocca tutto, esclusioni MPP e bot comprese; l'accensione ricalcola subito anche le campagne già inviate (aperture 23,23% → 17,49%, clic 10,73% → 1,6% su un caso); domanda aperta della sez. 14 risolta.
## 01/10/2026
- 🔴 Sez. 3: procedura ufficiale di riconferma del consenso (articolo 360000454424 riscritto il 30/09/2026): campagna con bottone, segmento «Link clicked in an email», lista nuova dal segmento, export CSV per contatto come prova; sostituisce la riga «invio uno-a-uno verso il form». Articolo 360000454204 (form GDPR) riletto: invariato nelle regole. Data di verifica al 01/10.
## 30/09/2026
- 🔴 Sez. 8: l'articolo «Create and manage your API keys» (209467485), riscritto da Brevo il 29/09/2026 alle 12:43 UTC, aggiunge le regole di scadenza: scadenza da 7 giorni a 1 anno oppure nessuna (email 3 giorni prima), e disattivazione automatica di ogni chiave senza chiamate riuscite da 90 giorni anche se non ha scadenza (email 7 giorni prima); riattivazione dalla stessa pagina; opzione «Create MCP server API key». Cambia una soglia che decide se un'integrazione poco usata continua a funzionare. Data di verifica al 30/09.
## 29/09/2026
- 🟡 Sez. 8: la pagina delle chiavi API si chiama «API Keys & MCP» (Settings > SMTP & API), riscritta da Brevo il 28/09/2026: permesso dedicato, codice a 6 cifre, chiave visibile una volta sola, email al proprietario. Nessuna regola cambia. Data di verifica al 29/09.
## 26/09/2026
- 🟡 `references/automazioni.md`, sez. 8: l'articolo «Review your automation statistics» (22724507709714) è stato riscritto da Brevo il 25/09/2026 in tre viste (Quick statistics, Overview, Full report); aggiornati nomi delle voci del pannello laterale (*Finished*, *Removed*, *Active* al posto di *Contacts in progress*) e data della fonte. Numeri e regole invariati. Le altre 74 fonti Brevo rilette senza cambi.

## 25/09/2026
- Richiesta di Cristiano (chat del 25/09): profondità da esperto su newsletter, automazioni e CRM. Letti 62 articoli di help.brevo.com via API Zendesk (date di aggiornamento 02/2026-24/09/2026).
- Nuovi `references/newsletter.md` (liste e segmenti, condizioni, destinatari, mittente e impostazioni, Brevo Template Language, content visibility, blocco dinamico, programmazione e Send in batches, Send to new contacts, report scheda per scheda con formule MPP, igiene lista, ordine di controllo), `references/automazioni.md` (editor nuovo, stati, quote, tutti i trigger/azioni/regole con piani, ingresso/uscita, test, statistiche, log, dieci ricette, ordine di controllo), `references/crm.md` (pacchetti Sales e seat, oggetti e associazioni, attributi, pipeline e pipeline pesata, deal e import, report, punteggi SCORE_ e predittivi, formule, Meetings e Conversations, ordine di controllo).
- SKILL.md: descrizione allargata; sez. 0 con la mappa dei references; sez. 4 e 5 con i rimandi e tre regole nuove (Inactive espelle, added-to-list non scatta su spostamento e import, Email opened mai per MPP); nuova sez. 5b CRM; sez. 13 punti 13-14; fonti aggiunte. Data di verifica in cima a 25 settembre 2026.
- `scripts/snapshot.py`: le pagine help.brevo.com ora vengono lette dall'API Zendesk, quindi le 75 fonti Brevo entrano nel controllo giornaliero (prima erano tutte 403).
## 20/09/2026

- Prima stesura da fonti ufficiali: 70+ articoli di help.brevo.com letti via API Zendesk (piani e limiti del Free, sospensioni e soglie, IP condiviso/dedicato e warm-up, autenticazione dominio e requisiti Gmail/Yahoo/Microsoft, branded subdomain, bounce, blocklist e tipi di disiscrizione, import e merge, lista legittima e form GDPR, DOI, consent groups, A/B test, Send at best time, preview/test, UTM, tracker via GTM e plugin, carrello abbandonato, WooCommerce/PrestaShop/Shopify PushOwl, eCommerce dashboard e nuovo motore conversioni, SMTP/porte/log/retention, Sender ID e regole SMS Italia, WhatsApp consenso e tier, Apple MPP e bot, pulizia lista, score, pixel/CNIL, migrazione editor automazioni); developers.brevo.com (limiti API, changelog 02-03/09/2026); tracker-doc.brevo.com (identify); 25 pagine release di brevo.com/releases (giugno-settembre 2026); Google 81126; Yahoo Sender Best Practices.
- Non verificato: prezzi in euro dei piani e costo per SMS/WhatsApp in Italia (pagina pricing letta solo nella parte statica); accettazione di un Sender ID alfanumerico "Local" per l'Italia e fasce orarie SMS italiane (assenti dalla tabella per paese); posizione del Garante italiano sul pixel di apertura (Brevo cita solo la CNIL); regola dei 2 giorni per le disiscrizioni confermata solo sulla pagina Yahoo, non estratta dalla pagina Google; help.brevo.com in HTML risponde 403 (contenuto letto via API Zendesk); brevo.com/product-updates è 404 e l'indice /releases è solo shell JS.
