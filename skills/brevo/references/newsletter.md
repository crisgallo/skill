# Brevo, newsletter e campagne email: regole operative

Approfondimento della sezione 4 di SKILL.md. Fonti: articoli di help.brevo.com letti via API Zendesk il 25/09/2026 (data di aggiornamento di ogni articolo tra parentesi). Nulla qui è stato osservato sul pannello: le righe ✅ VERIFICATO stanno solo in SKILL.md.

## 1. Liste, segmenti, destinatari

- **Una lista è statica, un segmento è dinamico.** Nella lista un contatto entra per import, form, API o automazione e ci resta finché qualcuno lo toglie; nel segmento entra ed esce da solo in base alle condizioni. Le liste servono per organizzare (canale di acquisizione, categoria di iscrizione, form di origine), i segmenti per mirare. Le **liste dinamiche sono diventate statiche il 01/01/2025** ([29012455073938](https://help.brevo.com/hc/en-us/articles/29012455073938), 23/09/2026; [360021703959](https://help.brevo.com/hc/en-us/articles/360021703959), 23/09/2026).
- **Quote**: 300 liste e 300 cartelle (600 liste su Enterprise), **200 attributi contatto** per account, un segmento combina **fino a 100 condizioni** ([9168632514066](https://help.brevo.com/hc/en-us/articles/9168632514066), 10/09/2026; [14902945335954](https://help.brevo.com/hc/en-us/articles/14902945335954), 16/09/2026).
- **Condizioni disponibili nei segmenti** (14902945335954): attributi (email, nome, telefono, EXT_ID, fuso, lista, segmento, stato di verifica, data di creazione e modifica, proprietario, prossima attività, **Engagement status**, attributi personalizzati di tutti e sette i tipi); email (iscrizione/blocklist con motivo, inviata/ricevuta/aperta/cliccata/disiscritta e i negativi, per tipo, nome, tag, lingua, periodo; **su "aperta" e "non aperta" si sceglie se includere le aperture Apple MPP**); form (**solo eventi dopo il 23/08/2024 e solo form del nuovo editor**); SMS, WhatsApp, push; Conversations (**solo conversazioni dopo il 01/06/2023**); Meetings; Phone; web tracking; e-commerce. Alcune condizioni compaiono solo dopo che l'evento è accaduto almeno una volta.
- **Destinatari di una campagna** ([4413566705298](https://help.brevo.com/hc/en-us/articles/4413566705298), 24/09/2026): più liste e segmenti insieme, più **al massimo 10 contatti singoli**; i contatti in blocklist vengono esclusi da soli e **non consumano crediti**; "Don't send to unengaged contacts" applica il segmento Unengaged definito in Settings > Contacts; **Advanced options** esclude liste o segmenti e aggiunge condizioni; **Consent groups** solo Professional ed Enterprise; **frequency cap** ("Include this email in the frequency cap") solo Enterprise.
- ⚠️ **Inviare a tutta la lista costa deliverability** quando molti non interagiscono: Brevo stesso consiglia segmenti mirati (29012455073938). Per un e-commerce la newsletter settimanale va a un segmento "engaged o cliente recente", non alla lista intera.

## 2. Mittente, oggetto, contenuto, impostazioni

- **Mittente**: default = Campaign sender dell'account; se la lista ha un mittente personalizzato valgono le regole di priorità di lista (o si spunta "Ignore list custom settings"); il **nome mittente si personalizza con attributi** (es. l'account manager del contatto); Reply-To e campo "To" si sovrascrivono nelle impostazioni aggiuntive (4413566705298).
- **Oggetto e anteprima**: variabili contatto e data feed, emoji, generazione con Aura. Il preview text è quello che decide il tasso di apertura insieme all'oggetto: si compila sempre, altrimenti il client mostra la prima riga del corpo.
- **Design**: editor drag&drop, editor semplice, HTML incollato. ⚠️ Partendo da "Your emails" si eredita **solo il design**: mittente, oggetto e impostazioni vanno rifatti (4413566705298). Campagne multilingua solo Professional ed Enterprise.
- ⛔ **Vietato** inserire password leggibili o link di auto-login nelle campagne (regola Brevo, 4413566705298).
- **Impostazioni aggiuntive**: UTM (regole in SKILL.md sez. 4), immagini incorporate (Starter/Standard/Professional fino a 5.000 contatti, Enterprise 50.000; sconsigliato con più immagini, limite 5 MB), **un solo allegato sotto i 4 MB** (ics, xlsx, docx, csv, pdf, txt, immagini, ppt e altri), **tag** della campagna (poi filtrabile nei contatti: "ha ricevuto una campagna con tag Sconto"), data di scadenza (feature "green", oggi nessun client la applica), pagina di disiscrizione personalizzata, form di aggiornamento profilo, header e footer di default con mirror e unsubscribe.
- **Requisiti Gmail e Yahoo** in vigore da febbraio 2024: dominio autenticato, disiscrizione in un clic, complaint sotto soglia (SKILL.md sez. 2).

## 3. Personalizzazione: Brevo Template Language

Fonte: [360000946299](https://help.brevo.com/hc/en-us/articles/360000946299) (12/09/2026).

| Variabile | Campagne | Automazioni | Transazionali | Note |
|---|---|---|---|---|
| Attributi contatto `{{ contact.FIRSTNAME }}` | sì | sì | sì | con testo di riserva se vuoto |
| `{{mirror}}` `{{update_profile}}` `{{unsubscribe}}` | sì | sì | sì | solo email |
| `{{time_now}}` e `{{time_now\|date:"..."}}` | sì | sì | sì | **senza fuso impostato nell'account restituisce UTC** |
| Dati evento (parametri transazionali) | ⛔ no | sì | sì | solo messaggi scatenati da un'azione |
| Data feed | sì | sì | sì | dati esterni letti al momento dell'invio |
| Product feed | sì | sì | sì | raccomandazioni dal catalogo |
| Codici coupon unici | sì | sì | no | un codice per destinatario, usabile una volta |
| Attributi di oggetti personalizzati | no | sì | no | solo automazioni scatenate da un oggetto |

- ⚠️ **Gli attributi a scelta multipla non si possono usare nella personalizzazione** (né email, né SMS, né WhatsApp): servono solo per segmentare e per i form ([10617359589906](https://help.brevo.com/hc/en-us/articles/10617359589906), 24/09/2026).
- **Filtri** sulle variabili: valore di default se vuoto, maiuscole, formati data e numero, codifica.
- **Content visibility** ([360000591660](https://help.brevo.com/hc/en-us/articles/360000591660), 10/09/2026): mostra o nasconde un blocco o una sezione per dispositivo (tutti, solo desktop, solo mobile), attributi contatto, dati evento, data feed, attributi oggetto; condizioni combinabili con **and/or**; chi non soddisfa la condizione **o ha il dato mancante non vede il blocco**. Tecnica: due blocchi con condizioni opposte, così ogni destinatario vede qualcosa.
- **Blocco Dynamic content** ([20932599276690](https://help.brevo.com/hc/en-us/articles/20932599276690), 21/04/2026; [9854758414098](https://help.brevo.com/hc/en-us/articles/9854758414098), 22/06/2026; [22933728350482](https://help.brevo.com/hc/en-us/articles/22933728350482), 07/09/2026): ripete una sezione per ogni elemento di un array (prodotti nel carrello, righe ordine, eventi); **il blocco compare nell'editor solo se l'account ha almeno un evento registrato da automazione o un data feed attivo**; **limite di default 3 elementi**, modificabile, con indice di partenza (0 = primo); i dati non ripetibili (totale ordine, link carrello) si inseriscono in un blocco normale; griglie solo inserendo a mano gli indici.
- ⚠️ **Anteprima delle email con dati evento**: "View in inbox" e il test email **non sostituiscono le variabili evento**. Si usa "Preview as recipient" con un JSON incollato oppure "Preview event" scegliendo un evento passato (che deve essere accaduto almeno una volta) (22933728350482).
- Data feed: usabili in campagne, automazioni e transazionali; nel test la mail parte con i dati vivi del feed (9854758414098).

## 4. Programmazione, reinvio, archivio

- **Quattro modi di inviare** (4413566705298): subito; a data e ora; **Send at best time** (Standard e superiori, consegna entro 24 ore, regole in SKILL.md sez. 4); **Send in batches** (Professional ed Enterprise): massimo **10 lotti**, intervallo massimo **24 ore** fra lotti, ⚠️ **impostazioni congelate** dopo la programmazione (solo sospendere o rimettere in coda) e **ricevono solo i contatti presenti nelle liste prima del primo lotto**.
- **Quote** (9168632514066): 10.000 campagne create compresi i bozza (50.000 Enterprise), **150 campagne programmate contemporaneamente** (300 Enterprise), 300 campagne SMS (600 Enterprise). Raggiunto il limite compare "Archive all campaigns exceeding the limit": archivia le più vecchie per data di modifica ([4411394977810](https://help.brevo.com/hc/en-us/articles/4411394977810), 02/09/2026).
- **Send to new contacts** (ex "Requeue" sulle campagne inviate): rimanda la campagna **solo a chi è entrato nelle liste o nei segmenti dopo il primo invio**. ⛔ **Non si duplica una campagna per rimandarla**: la copia è una campagna nuova e riparte a tutti, anche a chi l'ha già ricevuta (4411394977810).
- **Resume campaign** (ex "Requeue" sulle sospese): riprende dopo una sospensione manuale o per crediti finiti; sul Free si riprende a mano **ogni 24 ore** per i 300 successivi.
- **Reinvio dopo soft bounce o con modifiche** ([4526670078610](https://help.brevo.com/hc/en-us/articles/4526670078610), 16/09/2026): si duplica, si sceglie la stessa lista e in Advanced options si aggiunge la condizione **Email > Email not received > Over all time > nome della campagna originale**. Così ricevono solo i mancanti.
- **Duplicazione**: si scelgono le parti da copiare (mittente, destinatari, oggetto, regole A/B, design, impostazioni). Una campagna **rifiutata** si duplica, si corregge secondo la pagina Compliance e si rimanda.
- **Archiviare** si può solo con stato Sent, Suspended o Canceled.
- A/B test e reinvio ai non-aperti: SKILL.md sez. 4 (vincitore per clic, non per aperture; soggetto diverso nel reinvio).

## 5. Report: cosa misura davvero ogni numero

Fonti: [19764406559506](https://help.brevo.com/hc/en-us/articles/19764406559506) (10/09/2026), [208828089](https://help.brevo.com/hc/en-us/articles/208828089) (09/09/2026), [4406537065618](https://help.brevo.com/hc/en-us/articles/4406537065618) (22/09/2026).

- 🔴 **Dal 06/02/2025 le aperture includono Apple MPP e dal 08/07/2025 anche i bot, per default.** L'esclusione si accende in **Settings > Campaigns > Default settings > Default report settings** ("Exclude Apple MPP opens", "Exclude bot activity"). Finché è spenta, ogni tasso di apertura letto a un cliente è gonfiato. Nei **segmenti** invece le aperture MPP sono **escluse per default** (Settings > Contacts > Apple MPP opens in segments).
- **Formule** (4406537065618): con MPP incluso, open rate = (aperture + aperture MPP) / consegnate; escluso, open rate = aperture / (consegnate − aperture MPP). CTOR = clic unici / aperture (con o senza MPP secondo l'impostazione). **MPP tocca solo le aperture; i bot toccano aperture e clic**; bounce e disiscrizioni non sono toccati.
- **Untrackable contacts** nel report = destinatari con MPP: di loro non si sa né se né quando né dove hanno aperto.
- **Definizioni**: *Opens* = destinatari unici che hanno aperto almeno una volta; *Total opens* = aperture totali; *Clicks* = clic unici; *Total clicks* = tutti i clic; *CTR* = destinatari con almeno un clic / consegnate; *CTOR* = clic / aperture. ⚠️ **Unsubscribe, mirror, update profile e mailto sono esclusi dai clic** ma compaiono nella heatmap (tranne mailto).
- **Deliverability**: *Sent to*, *Delivered* (in inbox **o in spam**: consegnato non vuol dire letto), *Delivery rate*, *In processing* (differite, in coda, in analisi), *Skipped* (solo con feed esterni), soft e hard bounce con motivi. Soglie scritte da Brevo: **delivery sotto il 90% = agire subito**; **disiscrizioni sopre l'1%** e **complaint sopra lo 0,2%** possono sospendere account o campagna; **hard bounce sopra il 2%** idem (dal report delle automazioni, [22724507709714](https://help.brevo.com/hc/en-us/articles/22724507709714), 06/09/2026).
- **Solo Standard, Professional ed Enterprise**: breakdown per dominio e per lista (deliverability, aperture, clic, disiscrizioni), aperture e clic per ora, distribuzione geografica, **heatmap dei clic**, export CSV per dominio, elenco prodotti ordinati nella scheda Revenue. Sul Free e sullo Starter si leggono solo i totali.
- **Scheda Conversions** (visibile solo con una conversione configurata, motore in SKILL.md sez. 6): conversioni totali, tasso, ricavo totale, contatti unici, ricavo medio, **valore per email consegnata** (= ricavo / consegnate: è la metrica da mettere nel report mensile), prodotti ordinati.
- **Scheda Revenue** (solo con eCommerce dashboard): ricavo, carrello medio, ordini e tasso d'ordine, **first-time buyers**, prodotti ordinati da un link della campagna. Finestra a 48 ore dalla ricezione: ordine di grandezza, non attribuzione (SKILL.md sez. 6).
- **Condividere ed esportare**: link di sola lettura via email; PDF; CSV per contatto, lista o dominio; export di singole sezioni (motivi dei soft bounce, paesi).
- **Statistics** (Marketing > Statistics) aggrega per periodo email e SMS ed esporta in CSV; per trend nel tempo e dashboard serve **Brevo Analytics** (Professional ed Enterprise).
- 🔴 **Retention**: dal 01/01/2025, sugli account con **più di 10 milioni di eventi email**, gli eventi più vecchi di **24 mesi vengono cancellati**; chi vuole lo storico esporta i report ogni mese (9168632514066).
- **Benchmark**: l'articolo di Brevo indica come "standard di settore" un **open rate 20-30%** e un **CTR 2-5%** ([19764406559506](https://help.brevo.com/hc/en-us/articles/19764406559506)); il Benchmark Brevo 2025 ([213406845](https://help.brevo.com/hc/en-us/articles/213406845), 16/08/2026) è su 44 miliardi di email e 80.000 aziende, con SMS "open rate stimato 55%" e WhatsApp "98%". Sono **indicazioni di Brevo, non soglie**: i numeri per settore stanno nel PDF, non nella pagina.

## 6. Igiene della lista

Fonte: [5981839739538](https://help.brevo.com/hc/en-us/articles/5981839739538) (24/09/2026).

- Pulizia **almeno una volta l'anno**; prima se calano aperture e clic, salgono bounce, disiscrizioni o complaint, o entrano molti contatti nuovi ogni trimestre.
- Chi togliere: **Unengaged** (segmento predefinito, criteri modificabili in Settings > Contacts; i contatti MPP ne sono esclusi), **vecchi** (creazione > 24 mesi, meglio se anche senza ordini negli ultimi 24 mesi), **indirizzi generici** (contact@, info@, sales@, noreply@: cercati dalla barra), **non validi**, ⛔ **liste comprate o affittate: vietate su Brevo, si mettono tutte in blocklist**.
- ⚠️ **Si mette in blocklist, non si cancella**: la blocklist impedisce di reimportarli per sbaglio e conserva storico e attributi.
- Prima della blocklist: una sequenza di **winback** (chi non risponde si toglie con la coscienza a posto), poi automazione che mette in blocklist gli Unengaged.
- **"Don't send to unengaged contacts"** sulla campagna serve solo finché non sono in blocklist.

## 7. Ordine di controllo prima di programmare una newsletter

Sintesi operativa di questo file, non una pagina Brevo.

1. Destinatari: segmento, non lista intera; esclusi Unengaged; verificato che il segmento non includa contatti senza consenso (SKILL.md sez. 3).
2. Mittente su dominio autenticato, Reply-To presidiato.
3. Oggetto e preview text compilati; variabili con valore di riserva.
4. Content visibility e blocchi dinamici provati con "Preview as recipient" su almeno due contatti diversi.
5. UTM attivi, nome campagna parlante (SKILL.md sez. 4), nessun accorciatore di link.
6. Test alla test list, controllo su mobile e in modalità scura.
7. Programmazione: se serve "Send in batches", ricordare che dopo non si modifica nulla.
8. Dopo l'invio: report letto con MPP e bot esclusi; unsubscribe < 1%, complaint < 0,2%, delivery > 90%; valore per email consegnata annotato per il confronto mensile.
