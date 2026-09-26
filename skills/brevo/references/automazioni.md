# Brevo, automazioni: regole operative sull'editor nuovo

Approfondimento della sezione 5 di SKILL.md. Fonti: articoli di help.brevo.com letti via API Zendesk il 25/09/2026 (data di aggiornamento tra parentesi). Vale per l'**editor nuovo**; l'editor classico è in dismissione (SKILL.md sez. 5).

## 1. Come è fatta un'automazione

- Tre tipi di passo: **trigger** (chi entra e quando), **azioni** (cosa succede), **regole** (attese e biforcazioni). Serve almeno un trigger, e i trigger stanno solo nella prima riga. Più trigger nella stessa automazione = **OR**: basta soddisfarne uno ([15445989568402](https://help.brevo.com/hc/en-us/articles/15445989568402), 21/09/2026; [21203352470034](https://help.brevo.com/hc/en-us/articles/21203352470034), 25/07/2026).
- Ogni trigger si affina con **event filters** (dati dell'evento: prodotto, importo, nome del form, nome del meeting) e **contact filters** (attributi, attività email, stato di iscrizione, DOI): il contatto deve soddisfare entrambi.
- **Stati** ([15445936637330](https://help.brevo.com/hc/en-us/articles/15445936637330), 20/09/2026): *Active*; *Paused* = non entra nessuno di nuovo, chi è dentro continua; 🔴 ***Inactive* = non entra nessuno e chi è dentro viene buttato fuori**. Per fermare gli ingressi senza perdere chi è in coda si mette in pausa, non si disattiva.
- **Disattivare un singolo passo** (solo azioni, non trigger né regole): i nuovi lo saltano, chi ci sta dentro esce subito e passa al successivo. Serve per spegnere un'email senza toccare il resto.
- Salvataggio automatico; un passo modificato ma non salvato ha un pallino arancione; undo e redo nella barra.
- **Un contatto può stare in più automazioni insieme**, ognuna corre per conto suo ([208775609](https://help.brevo.com/hc/en-us/articles/208775609), 10/09/2026).

## 2. Quote e limiti che bloccano in silenzio

Fonte: [9168632514066](https://help.brevo.com/hc/en-us/articles/9168632514066) (10/09/2026); [209465385](https://help.brevo.com/hc/en-us/articles/209465385) (21/09/2026).

| Limite | Free e Starter | Standard | Professional ed Enterprise |
|---|---|---|---|
| Contatti unici che possono entrare nelle automazioni attive | **2.000** | illimitati | illimitati |
| Contatti aggiunti a mano per volta | 500 | 500 | 500 |
| Eventi trigger processati al minuto | 6.000 | 6.000 | 10.000 |
| Passi eseguiti al minuto | 3.000 | 3.000 | 6.000 |
| Log di workflow conservati (entro 24 mesi) | 100.000 / 300.000 | 600.000 | 1 miliardo |
| Webhook in uscita / in entrata per account | 40 / 20 | 40 / 20 | 40 / 20 |

- Il tetto dei 2.000 conta **un contatto una volta sola** anche se sta in due automazioni. Brevo avvisa per email **all'80% e al 100%**. Raggiunto il tetto le automazioni restano attive e chi è dentro finisce il percorso; **i nuovi non entrano**. Dopo l'upgrade i bloccati entrano da soli **tranne con il trigger "Contact added to list"**: quelli vanno tolti dalla lista e rimessi (209465385).
- I **crediti prepagati** email ereditano lo stesso limite dei 2.000 contatti ([4409354969746](https://help.brevo.com/hc/en-us/articles/4409354969746), 24/09/2026).
- ⚠️ **Un import massiccio non fa scattare "Contact added to list"**: l'ingresso via import è limitato, Brevo lo dice esplicitamente (209465385). Per far entrare un blocco di contatti si usa **Contact added manually** (500 alla volta, [21969731734546](https://help.brevo.com/hc/en-us/articles/21969731734546), 10/09/2026) oppure un trigger a segmento.
- **Perché un contatto non entra** (209465385): non soddisfa il trigger; non ha fatto l'azione; import massiccio; **non identificato dal tracker** (identificazione solo con account creato sul sito, form Brevo inviato o clic su un'email Brevo, e poi solo dopo il login; email al checkout senza account non basta senza `identify`); evento custom con nome diverso da quello nell'automazione; automazione in pausa; tetto dei 2.000.

## 3. Trigger disponibili

Fonte: 15445989568402 (21/09/2026). Fra parentesi il piano o il pacchetto richiesto.

- **Contatti**: *Contact added to list* (⚠️ **non scatta se il contatto viene spostato da una lista all'altra**), *Contact removed from list* (idem), *Contact matches custom filters* e *Contact is in a segment* (⚠️ **non sono in tempo reale: l'automazione controlla a una frequenza e a un'ora scelte**, ed entra chi corrisponde in quel momento), *Anniversary* (data in un attributo data, prima/dopo/il giorno stesso, **ignora l'anno**: rientra ogni anno), *Contact added manually*.
- **Form**: *Form submitted*, **solo form creati in Brevo**, per nome o per tipo (iscrizione, disiscrizione, aggiornamento profilo).
- **Email**: *Email opened* (⚠️ **gli utenti Apple MPP sono esclusi**: non scatta mai per loro), *Link clicked in an email* (filtri per tipo, nome, URL), *Unsubscribed from email list* (serve a sincronizzare la blocklist fra transazionali e campagne).
- **E-commerce** (richiedono il tracker o un plugin, SKILL.md sez. 5): *Cart updated*, *Cart deleted*, *Order created*, con filtri su prodotti, prezzi, totale ordine.
- **Sito**: *Webpage visited* (tracker), *Custom event* (evento creato via JS o REST; il nome nel sito e nell'automazione devono coincidere).
- **Conversations, Deals, Meetings, Phone** (solo con **Sales Essentials o Sales Advanced**): *Sales email opened/clicked*, *Conversation started/ended* (una conversazione email finisce **5 minuti dopo** l'ultima email; chat non assegnata o senza risposta 5 minuti, assegnata quando gli agenti escono o dopo **30 minuti** di inattività), *Message received* (non scatta per messaggi non mostrati in Conversations o "rimbalzati" da una casella collegata), *Deal created*, *Deal stage updated*, *Task completed*, *Meeting booked/started/canceled*, *Call finished*.
- **Payment**: *Payment request created*, *reminder sent*, *Payment done*.
- **Push, Web Push, WhatsApp reply received** (Professional ed Enterprise); **Loyalty e Wallet** (solo Enterprise).
- **Oggetti personalizzati** (Professional: 1 oggetto; Enterprise: illimitati): trigger su data, creazione, aggiornamento, evento custom; ⚠️ un record entra **solo se associato a un contatto**; associare un oggetto non conta come aggiornamento.

## 4. Azioni disponibili

Fonte: 15445989568402.

- **Contatti**: aggiungi/togli da lista; **Update contact attribute** (sostituisci, **aggiungi** un valore numerico, cancella: è la base del lead scoring); **Blocklist contact** (dalle transazionali di uno o più mittenti, o da tutte le campagne); **Assign a user to a contact** (uno fisso o **round-robin** fra più utenti); **Delete a contact** (⛔ dopo non si possono aggiungere passi); **Update company attribute** (⚠️ si applica a **tutte** le aziende associate al contatto).
- **Messaggi**: *Send an email* (template esistente o creato lì); *Send an SMS* (transazionale o promozionale, **solo testo, niente MMS**); *Send a push notification* (Professional ed Enterprise); *Send a one-to-one email from a mailbox* (Sales Essentials/Advanced, risponde dalla stessa casella, programmabile per giorni e ore); *Send a WhatsApp message* (Professional ed Enterprise, **solo template approvati da Meta**, addebitati come WhatsApp marketing; finestra di invio per giorni e fasce orarie; ⚠️ **senza crediti l'automazione parte lo stesso ma il messaggio non viene inviato**, [9722708011026](https://help.brevo.com/hc/en-us/articles/9722708011026), 28/07/2026); *Notify by email* (notifica interna a indirizzi fissi o presi da un attributo).
- **Webhook**: *Call a webhook* verso un'app esterna con i dati dell'evento e, a scelta, del contatto.
- **Deals** (Sales Essentials/Advanced): *Create a task* (tipo, titolo, scadenza, proprietario, nota); *Update deal attribute* (sul deal più recente, su tutti gli aperti, i persi, i vinti o tutti); *Duplicate a deal* (ricrea il più recente con note e associazioni, prefisso nel nome: serve a riaprire i persi); *Create a deal* (pipeline, fase, prefisso, proprietario o round-robin, task di follow-up; **il proprietario di default è il proprietario del contatto**, per cambiarlo si mette prima "Assign a user").
- **Automazioni**: *Start another automation* (fa entrare il contatto in un'altra automazione **a un passo preciso**, per non duplicare sequenze); *Redirect contact to another step* (salto dentro la stessa automazione). Entrambe si usano dopo uno split.
- **Wallet** (Enterprise): notifiche e spostamenti di campagna wallet.

## 5. Regole: attese e biforcazioni

- **Time delay**: attesa fissa da **1 minuto** (minimo) a **60 mesi** (massimo) ([27438224109074](https://help.brevo.com/hc/en-us/articles/27438224109074), 10/09/2026).
- **Wait until an event happens**: attende un'azione entro un tempo massimo (fino a 60 mesi); fatta in tempo → ramo Sì, altrimenti → ramo No. È la regola del DOI per form esterni e del winback.
- **Conditional split** ([19725335370002](https://help.brevo.com/hc/en-us/articles/19725335370002), 27/08/2026): rami con condizioni più un **ramo di default senza condizioni** per chi non ne soddisfa nessuna; **oltre due rami solo Professional ed Enterprise, fino a 10**; inserendolo fra passi esistenti i passi sotto finiscono nel ramo A. ⚠️ **Il ritardo va prima dello split**: "ha comprato entro una settimana?" si costruisce con Time delay 7 giorni e poi lo split, non il contrario.
- **Percentage split** ([25155893623314](https://help.brevo.com/hc/en-us/articles/25155893623314), 07/08/2026): assegnazione casuale per percentuali (A/B, 80/20 per testare un'offerta, distribuzione del carico, test di cadenza); più di due rami e **report del confronto solo Professional ed Enterprise**; **mettere in pausa un ramo lo porta a 0%** e i nuovi vanno sugli altri; spostando un passo di ramo la sua storia si sposta con lui.

## 6. Ingresso, uscita, rientro

Fonte: [19649907878546](https://help.brevo.com/hc/en-us/articles/19649907878546) (12/09/2026), tab Settings dell'editor.

- **Re-entry after exit**: spento per default (welcome: una volta sola); acceso per carrello abbandonato, rinnovi, cambi di fase; con **Set up wait time** si evita di rimandare gli stessi messaggi a distanza di giorni.
- **Exit conditions**: usciti subito da qualunque passo quando succede X (acquisto o carrello svuotato nel carrello abbandonato; risposta del contatto in una sequenza di vendita). Più condizioni = basta una.
- **Restart conditions**: ripartono dal primo passo quando succede X (nuovo prodotto nel carrello).
- ⚠️ Chi è già dentro, o è uscito senza permesso di rientro, **non viene riaggiunto nemmeno a mano** (21969731734546).

## 7. Test prima di attivare

Fonte: [25318176966290](https://help.brevo.com/hc/en-us/articles/25318176966290) (24/09/2026).

- Il pulsante **Test** fa passare un **contatto reale** dell'account (se stessi) per tutti i passi messaggio, rami compresi; **consuma crediti**; i risultati **non si riaprono** dopo aver chiuso la finestra (si rifà il test o si leggono i log transazionali).
- Esito per passo: *Processed* (inviato) o *Skipped* (passo non salvato o contatto senza canale).
- ⚠️ **Le variabili evento si sostituiscono solo se il contatto di test ha già generato quell'evento** (un acquisto passato); altrimenti restano vuote.
- Alternativa per un'automazione già attiva: aggiungere a mano un campione di contatti e leggere i log (21969731734546).

## 8. Statistiche e log

Fonti: [22724507709714](https://help.brevo.com/hc/en-us/articles/22724507709714) (riscritto il 25/09/2026 in tre viste: *Quick statistics* sulla pagina Workflows, *Overview* nel tab Activity, *Full report* per una automazione su un periodo scelto), [115000263710](https://help.brevo.com/hc/en-us/articles/115000263710) (25/08/2026).

- **Pagina Workflows**, per ogni automazione: *Active now*, *Started*, *Finished*, *Suspended* (cancellati o rimossi a mano mentre erano dentro), **Revenue** (solo Starter e superiori, con Shopify, WooCommerce, Shopware 6, PrestaShop o API **e** una conversione configurata; il filtro "Select a conversion" restringe la lista).
- **Tab Activity** dentro l'automazione: periodo selezionabile (e pulsante di refresh), *Started* distinto in *Through displayed triggers* e *Through deleted triggers*, poi *Finished*, *Removed* e *Active* (fino al 24/09/2026 l'ultima si chiamava *Contacts in progress*); sul canvas il **numero di contatti per passo**, cliccabile verso i log.
- **Per ogni passo messaggio**: email (aperture, clic unici, disiscrizioni, più il **report completo** con le stesse schede di una campagna; **il tasso di apertura include MPP per default**); SMS (inviati, consegnati, disiscrizioni, clic totali, CSV scaricabile dal centro notifiche); WhatsApp (inviati, consegnati, disiscrizioni; ⚠️ nei log il numero di inviati WhatsApp non compare per limiti Meta, si legge nelle statistiche); push (consegnate, cliccate); **Conversion metrics** per passo (conteggio, percentuale, ricavo) se una conversione è configurata.
- **Workflow logs** (Automations > Logs): ogni evento con data, contatto, automazione, passo, messaggio; i campi tecnici (`scenario_id`, `type`, `step_id`, `workflow_points`, `new editor`). Conservazione: **24 mesi** e in più il tetto di volume per piano (sez. 2): oltre il tetto spariscono i più vecchi anche se recenti.
- **Contacts in workflows**: chi è attivo e chi è "on hold" in un'attesa, con passo e data d'ingresso; da qui si **rimuovono fino a 30 contatti per volta** (diventano *Suspended* e generano il log "manually removed"). Anche dalla scheda contatto, sezione Active automations.
- **Event logs** (pagina dal 23/06/2026): tutti gli eventi arrivati da tracker, API e plugin. È il posto dove si verifica che `cart_updated` e `order_completed` arrivino davvero prima di dare la colpa all'automazione.
- **MPP e bot** ([4406537065618](https://help.brevo.com/hc/en-us/articles/4406537065618), 22/09/2026): per gli utenti Apple MPP non scattano *Email opened*, i filtri e i segmenti basati sulle aperture, gli split e le attese basate sulle aperture; le aperture e i clic dei bot **non contano e non fanno avanzare** l'automazione. Trigger affidabili: clic, risposte, form, pagine visitate, acquisti.

## 9. Ricette verificate sulle pagine Brevo

Ogni ricetta rimanda alla pagina da cui è presa; i numeri (ritardi, punteggi) sono gli esempi di Brevo, non soglie.

1. **Benvenuto**: trigger *Contact added to list* o *Form submitted* → Time delay breve → email; rientro spento. Per un **form esterno a Brevo** si costruisce il DOI con *Wait until* clic sul link di conferma entro X, ramo No → niente iscrizione (27438224109074; 15445989568402).
2. **Carrello abbandonato**: SKILL.md sez. 5, più exit condition su *Order created* / *Cart deleted* e restart su *Cart updated* (19649907878546).
3. **Evento sul sito** ([360021575279](https://help.brevo.com/hc/en-us/articles/360021575279), 10/09/2026): evento custom (es. "Added to wishlist") con event filter (valore > 10) e contact filter (nessun ordine nell'ultima settimana) → delay → email con blocco prodotti; poi eventualmente *Create a deal* per il follow-up personale e *Start another automation* verso il benvenuto se non l'ha mai ricevuto.
4. **Lead scoring** ([25723707326738](https://help.brevo.com/hc/en-us/articles/25723707326738), 10/09/2026): attributo numerico `SCORE`; trigger multipli (*Email opened* filtrato sulle campagne, *Webpush clicked*, pagine visitate) → *Update contact attribute* con **Add +5** → *Conditional split* `SCORE ≥ 20` → ramo Sì: *Assign a user* (o *Create a deal*, [10443056273554](https://help.brevo.com/hc/en-us/articles/10443056273554), 17/08/2026); rientro **acceso**, altrimenti conta una volta sola. ⚠️ *Email opened* non vale per gli utenti Apple: si pesano di più clic e visite.
5. **Winback**: trigger *Contact is in a segment* (Unengaged, controllo programmato) → sequenza di 2-3 email → *Wait until* clic entro N giorni → No: *Blocklist contact* ([5981839739538](https://help.brevo.com/hc/en-us/articles/5981839739538), 24/09/2026; 27438224109074).
6. **Compleanno o anniversario**: *Anniversary* su un attributo data, "prima di", "il giorno", "dopo" (15445989568402).
7. **Sincronizzare le disiscrizioni**: *Unsubscribed from email list* (transazionali) → *Blocklist contact* dalle campagne, e viceversa (15445989568402).
8. **Cambio di fase del deal** ([14048831051282](https://help.brevo.com/hc/en-us/articles/14048831051282), 04/08/2026): *Deal stage updated* con filtro *Stage name is exactly X* → delay → email o task. ⚠️ **Il deal deve essere associato ad almeno un contatto**; con **due contatti scatta due volte**; rientro acceso se deve ripartire a ogni passaggio per quella fase.
9. **Creare un task** ([360005695200](https://help.brevo.com/hc/en-us/articles/360005695200), 17/08/2026): *Meeting booked* filtrato sul nome del meeting, o *Form submitted* → *Create a task* con tipo (To do, Email, Call, Meeting, Lunch, Deadline, LinkedIn), scadenza relativa, assegnazione (default proprietario del contatto).
10. **Rinnovi**: *Anniversary* sulla data di scadenza del contratto salvata come attributo → *Create a deal* con prefisso "Rinnovo" e task (10443056273554).

## 10. Ordine di controllo di un'automazione ereditata

Sintesi operativa, non una pagina Brevo.

1. Stato: attiva, in pausa o inattiva; se inattiva, chi c'era dentro è già stato espulso.
2. Trigger: tipo, filtri, e se è a segmento la frequenza del controllo.
3. Tetto dei 2.000 (Usage and plan) e avvisi all'80%.
4. Rientro e uscite: un carrello senza exit su *Order created* manda promemoria a chi ha già comprato.
5. Passi disattivati e rami in pausa a 0%.
6. Trigger basati sulle aperture: quanti utenti Apple ci sono nel segmento.
7. Email del passo: mittente, filtro "Subscribed" sulle promozionali, blocco dinamico con limite di elementi giusto.
8. Log: ultimi ingressi, contatti "on hold" da settimane, eventi custom che non arrivano.
9. Statistiche: conversioni per passo e Revenue sulla pagina Workflows, con MPP e bot esclusi nei report.
