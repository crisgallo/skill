---
name: "viaggi-treno-italia"
description: "Regole operative verificate per organizzare gli spostamenti di lavoro in Italia senza auto, per un professionista con partita IVA: corriera extraurbana fino alla stazione, treni Trenitalia (Frecce, Intercity, regionali) e Italo, metro e taxi. Tariffe e cosa permette ognuna per cambio e rimborso (Base, Economy, Super Economy; Low Cost, Economy, Flex), CartaFRECCIA e Italo Più, regionale digitale e convalida, PNR, fattura dei biglietti e entro quando, indennizzi per ritardo e cancellazione (regolamento UE 2021/782, 60 e 120 minuti, 25 e 50 per cento), coincidenze perse con biglietti separati, corriere regionali (orari festivi, biglietti in app), scioperi (fasce garantite, dove si controllano), taxi a tariffa fissa, margini porta a porta, spese di viaggio da dedurre o riaddebitare. Usala quando si cerca una soluzione di viaggio, si compra un biglietto, si mette un viaggio a calendario, si controlla la sera prima, un treno è in ritardo, si chiede fattura o indennizzo, anche se si dice solo «il treno di domani»."
---

# Viaggi di lavoro in treno e corriera in Italia: regole operative

**Ultima verifica delle fonti: 28 ottobre 2026.**

## 0. Manutenzione di questa skill (leggere per primo)

1. **Finestra di freschezza: due mesi.** Tariffe, penali, orari e programmi fedeltà cambiano senza preavviso; le condizioni di trasporto di Italo in vigore sono del 01/10/2026 e CartaFRECCIA chiude il 31/12/2026. Se la data in cima ha più di due mesi, si rileggono le pagine tariffe e cambi dei due vettori prima di citare un numero.
2. Quando una fonte smentisce una regola scritta qui, si aggiorna la skill **nello stesso turno**, si riscrive la data in cima e si annota cosa è cambiato e da quando.
3. Due metà da tenere distinte: **regole dei vettori e della legge** (verificate sulle pagine ufficiali e sui testi) e **meccanica dei siti e delle app** (sez. 14: si impara sbagliando e si scrive qui la prima volta). In questa prima stesura nessun punto della sez. 14 è stato confermato sullo schermo.
4. ⚠️ **URL che non funzionano più su trenitalia.com** (404 il 28/10/2026): `condizioni_generali_di_trasporto`, `offerte_e_servizi/base|economy|super_economy`, `indennita_e_rimborsi`, `treni_garantiti_in_caso_di_sciopero`. Le pagine vive stanno sotto `/it/html/trenitalia/Info_*.html` e `/it/informazioni/...` (elenco in Fonti). **EUR-Lex non si legge via fetch**: il regolamento 2021/782 si legge dal PDF ospitato da Italo. **scioperi.mit.gov.it e cgsse.it rispondono 503** a letture automatiche: si aprono nel browser. **atac.roma.it** sta dietro un muro anti-bot.
5. 🔴 Nessun numero qui sotto è inventato. Quello che non si è potuto leggere è marcato **[DA VERIFICARE]** e non si cita all'utente come certo.
6. Il calendario, le ore e le regole di pianificazione dello spazio (minimo 30 minuti, inizio all'ora o alla mezz'ora) stanno in `trello` sez. 9; qui sta solo come si traducono i viaggi in voci di calendario (sez. 11).

---

## 1. Chi usa questa skill e come lavora

La chat organizza gli spostamenti di un professionista con partita IVA che non ha l'auto: parte da un paese servito solo da una **corriera extraurbana**, raggiunge la stazione, prende **treni Trenitalia o Italo**, in città usa **metropolitana e taxi**. Quattro regole di lavoro:

1. **Si cerca, si propone, si compra solo dopo il sì esplicito** dell'utente, nei suoi account; mai un acquisto «per fare prima». Prima di proporre si dice **quale tariffa** e **cosa permette** (sez. 2 e 5), non solo il prezzo.
2. **Ogni viaggio va a calendario** con la soluzione completa porta a porta e i margini (sez. 11), così lo spazio è bloccato anche per chi guarda solo l'agenda.
3. **La sera prima** si rifà il controllo: scioperi proclamati (sez. 9), orari della corriera per il giorno giusto (sez. 8), eventuali variazioni del treno sul PNR.
4. **I biglietti dei viaggi di lavoro si conservano** con la fattura o la ricevuta (sez. 7 e 12), con il nome del cliente o del progetto a cui si riaddebitano.

Niente dati personali nella skill: nomi, indirizzi, numeri di tessera e account restano nelle chat e negli strumenti dell'utente.

---

## 2. Trenitalia, Frecce e Intercity: tariffe e cosa permette ognuna

Le pagine lette il 28/10/2026 ([tariffe](https://www.trenitalia.com/it/html/trenitalia/Info_Tariffe_it_LeFrecce.html), [cambi e rimborsi](https://www.trenitalia.com/it/html/trenitalia/Info_cambi_rimborsi.html)):

- **Base.** Cambio di prenotazione (data e ora) e cambio biglietto **illimitati fino alla partenza**, e **una sola volta fino a un'ora dopo** la partenza del treno prenotato. **Rimborso fino alla partenza con trattenuta del 20%**; i biglietti fino a 10 € non sono rimborsabili. Si può salire su **un altro treno della stessa categoria da un'ora prima a un'ora dopo** quello prenotato pagando **10 €** di differenza (a bordo o in biglietteria). Cambio nome gratis. È la tariffa da comprare quando l'orario di ritorno è incerto.
- **Economy.** Si compra **fino alle 24 del terzo giorno prima** della partenza. **Un solo cambio** di data o ora **fino alla partenza**, pagando la **differenza verso la tariffa Base** dello stesso treno (stessa origine e destinazione, stesso livello di servizio). **Non rimborsabile**, salvo chi ha pagato l'opzione **tiRimborso (1 €)** che rimborsa con trattenuta del 10%. Non si può salire su un altro treno.
- **Super Economy.** Si compra **fino alle 24 del nono giorno prima** (Frecce e FrecciaLink) e del **sesto giorno prima** (Intercity e Intercity Notte). **Nessun cambio di data e ora, nessun rimborso** (salvo tiRimborso a **3 €**); il cambio nome è ammesso. Va presa solo per viaggi certi.
- **Offerte a condizioni proprie** (lette sulla pagina tariffe): Young e Senior (età), FrecciaYoung e FrecciaSenior, FrecciaDays, Bimbi Gratis. Ognuna ha i propri limiti di cambio e rimborso, da rileggere al momento: non si dà per scontato che valgano le regole Base.
- **Biglietto con codice PNR.** Il biglietto delle Frecce e degli Intercity è nominativo con posto assegnato, identificato dal **PNR**; a bordo si mostra il PDF o l'app, non serve timbrare. In caso di cambio il PNR resta, cambia il biglietto: si rilegge sempre l'ultima versione in app prima di salire.
- **Rimborso per sciopero o soppressione**: per Frecce e Intercity la rinuncia al viaggio si chiede **dall'annuncio dello sciopero fino alla partenza** del treno; per i regionali **fino alle 24 del giorno prima** (fonte terza, [DA VERIFICARE] sulla pagina Trenitalia).

---

## 3. CartaFRECCIA: chiude il 31/12/2026

Dalla [pagina CartaFRECCIA](https://www.trenitalia.com/it/cartafreccia.html) letta il 28/10/2026: **il programma termina il 31/12/2026; i punti restano spendibili fino al 31/03/2027.** Fino ad allora i livelli sono Argento (+10% punti, FrecciaClub, 2 upgrade), Oro (+25%, 3 upgrade, FrecciaLounge con un ospite, cambio a bordo, canale WhatsApp), Platino (+50%, 4 upgrade, un biglietto omaggio, SuperFlex) e Platino Infinito. **Le soglie di punti per livello non sono pubblicate** nella pagina letta **[DA VERIFICARE]**. Regola pratica: chi ha punti li usa prima della scadenza; non si pianifica una strategia di accumulo su un programma che chiude; se Trenitalia annuncia il programma sostitutivo si riscrive questa sezione.

---

## 4. Trenitalia, treni regionali: biglietto digitale, convalida, validità, indennizzo

Pagine lette il 28/10/2026: [nuovo biglietto digitale regionale](https://www.trenitalia.com/it/regionale/nuovo-biglietto-digitale-regionale.html), [indennizzo automatico](https://www.trenitalia.com/it/servizi/indennizzo-automatico-biglietto-digitale-regionale.html).

- **Il biglietto digitale regionale è nominativo e legato a un treno preciso.** Si compra **fino a 5 minuti prima** della partenza. **Cambi di data e ora illimitati fino alle 23:59 del giorno prima**; il giorno stesso si cambia **solo l'ora**, fino alla partenza. Si viaggia con il documento d'identità.
- **La convalida è automatica**: alla partenza programmata il biglietto in app mostra la **barra verde**; il check-in non è più obbligatorio (dal 21/09/2024 anche per biglietti comprati da terzi). È valido **fino all'arrivo programmato, solo sul treno scelto**. **Il PDF stampato non vale per viaggiare**: si mostra l'app o il sito.
- **Treno perso**: con il biglietto convalidato si sale sul **primo treno utile della stessa tratta** senza rifare il biglietto, per il giorno stesso.
- **Rimborso**: **100% in self-service fino alle 23:59 del giorno prima** (esclusi carnet, Piemonte/Torino, Lombardia, Emilia-Romagna e i vettori diversi da Trenitalia); dal giorno stesso non si rimborsa, si cambia l'ora.
- **Indennizzo automatico per ritardo (dal 01/01/2025)**, accreditato sulla carta usata senza richiesta: **25% dai 60 minuti se il biglietto costa almeno 16 €**, **50% dai 120 minuti se costa almeno 8 €**, niente sotto i 4 € di indennizzo, esclusi i pagamenti in contanti e i biglietti di altri vettori.
- **Biglietto cartaceo** (biglietteria o self-service): va **convalidato prima di salire**; la durata di validità (4 ore dalla convalida secondo la prassi) e l'importo delle **sanzioni** a bordo **[DA VERIFICARE]** sulle Condizioni regionali, che il 28/10 non si sono potute leggere. Regola di sicurezza: il regionale si compra in app, scelto sul treno giusto, e si guarda la barra verde prima di salire. **Un regionale cartaceo non convalidato è una multa**, anche se pagato.

---

## 5. Italo: tariffe, opzioni, Italo Più, Italobus, contratto dal 01/10/2026

Fonti: [tariffe](https://www.italotreno.com/it/il-treno/tariffe), [termini e condizioni](https://www.italotreno.com/it/termini-condizioni), [Contratto di trasporto in vigore dal 01/10/2026](https://www.italotreno.com/~/media/Images/content/pdf/contratto_di_trasporto/Contrattoditrasportorel610) (letto per intero), [Italo Più](https://www.italotreno.com/it/programma-fedelta-italo-piu/livelli-benefici).

- **Low Cost**: cambio **fino a 72 ore prima** della partenza con **sovrapprezzo del 60%** più l'eventuale differenza di prezzo; **nessun rimborso**; niente cambio nome.
- **Economy**: **cambi illimitati fino a 3 minuti prima** con **sovrapprezzo del 20%** più differenza; **rimborso del 40%** del prezzo (trattenuta 60%).
- **Flex**: cambi illimitati, **anche di nome**, senza sovrapprezzo (si paga solo la differenza); **rimborso dell'80%**.
- **Opzioni a pagamento**: **Opzione Rimborso** (rimborso dell'80% chiesto **fino a 72 ore prima**, su tariffe che non lo prevedono), **Extra Tempo** (10 €, salire su un altro treno vicino [DA VERIFICARE] le finestre esatte), **Parti Ora** (15 €, fino a 2 ore prima, servono almeno due treni utili; il suo prezzo non concorre all'indennizzo).
- **Dal contratto 01/10/2026**: la rinuncia al viaggio si chiede **fino a 3 minuti prima**; il **riaccredito arriva entro 30 giorni**, mai in contanti; il cambio si fa con **Codice Biglietto e nominativo** sul sito, in app o al 060708 (Pronto Italo), non via email. A bordo senza biglietto valido si paga **penale del 20% sulla tariffa Bordo**; il viaggio irregolare costa **200 €, ridotti a 130 € se pagati entro 30 giorni**.
- **Italo Più** (promozione dei livelli fino al 30/11/2026): 1 punto per euro, doppi su Flex; livelli **Member, Premium (800 punti), Privilege (3.000), Privilege Plus (6.000)**; benefici crescenti (Fast Track, upgrade 2/4/6, accessi lounge 1/20/illimitati); i punti valgono **fino al 30/05/2027**, il biglietto premio si usa entro 180 giorni, il livello si ricalcola ogni 12 mesi. Date e soglie sono promozionali: si rileggono dopo il 30/11/2026.
- **Italobus e Itabus**: dal giugno 2023 il biglietto treno più bus è **unico**, i punti maturano solo sulla tratta treno; cambio e rimborso della tratta bus seguono la tariffa del biglietto, ma le condizioni specifiche del bus **[DA VERIFICARE]** sulla pagina dedicata, non letta.

---

## 6. Ritardi, cancellazioni, coincidenze perse: regolamento UE 2021/782 e regole dei vettori

Il regolamento 2021/782 (in vigore dal 07/06/2023, testo letto il 28/10/2026 dal [PDF ospitato da Italo](https://www.italotreno.com/~/media/Images/content/pdf/contratto_di_trasporto/regolamento-europeo/Regeuropeo782-2021)) vale per Frecce, Intercity e Italo; **i regionali e i servizi urbani godono di deroghe nazionali** (art. 2), per cui si applicano le regole del vettore (sez. 4).

- **Dai 60 minuti di ritardo previsto all'arrivo (art. 18)** il passeggero sceglie: **rimborso integrale** del biglietto (per la parte non fatta, e anche per quella fatta se il viaggio non ha più senso, con ritorno al punto di partenza); **prosecuzione o itinerario alternativo** appena possibile; **itinerario alternativo in data successiva**. Se il vettore **non propone un'alternativa entro 100 minuti**, il passeggero può organizzarsi con altri vettori e **farsi rimborsare i costi**. Italo scrive la stessa regola nell'art. 16 del contratto.
- **Indennizzo (art. 19)**: **25% del prezzo per ritardi da 60 a 119 minuti, 50% da 120 minuti** in su, pagato **entro un mese** dalla richiesta, in buoni o, **su richiesta, in denaro**; il vettore può non pagare importi **sotto i 4 €**. **Nessun indennizzo se il ritardo era noto prima dell'acquisto** o se con l'alternativa si arriva con meno di 60 minuti di ritardo. Il vettore si esonera solo per circostanze straordinarie esterne, colpa del viaggiatore o fatto di terzi non evitabile: **lo sciopero del proprio personale non esonera** (Italo lo scrive espressamente, art. 16.3).
- **Assistenza (art. 20)**: pasti e bevande in proporzione all'attesa; **albergo fino a 3 notti** se serve pernottare (il tetto vale quando il ritardo dipende da cause esterne).
- **Trenitalia, Frecce e Intercity** ([indennità per ritardo](https://www.trenitalia.com/it/informazioni/la-guida-del-viaggiatore/indennita-per-ritardo.html), [indennizzo](https://www.trenitalia.com/it/html/trenitalia/Indennizzo_per_ritardo.html)): oltre al regolamento, **bonus del 25% non monetizzabile per ritardi da 30 a 59 minuti**; 25% da 60 a 119 e 50% da 120 **a scelta in bonus o denaro**; la richiesta si fa **da 24 ore dopo l'arrivo fino a 12 mesi** via web, app, Smart Refund, call center o biglietteria; sotto i 4 € non si paga.
- **Italo**: **25% da 60 a 119 minuti, 50% da 120**, su richiesta, riconosciuto **entro 30 giorni** come **Voucher da indennizzo** (o sul Borsellino Italo per gli iscritti): il voucher scade **365 giorni dopo l'arrivo**, si usa anche per biglietti di prezzo diverso e **si monetizza con bonifico entro 30 giorni** chiedendolo sul sito o al 060708, tranne importi fino a 4 € (art. 16.4 e 17 del contratto). Al reclamo Italo risponde entro un mese (massimo tre); se tarda oltre i 90 giorni paga un indennizzo del 10% (20% oltre i 120) per delibera ART 28/2021.
- **Coincidenze perse.** Con **biglietto unico** (una sola transazione, un solo PNR o «soluzione di viaggio» del vettore) il vettore risponde della coincidenza: si prosegue con il primo treno utile e valgono rimborso, alternativa e indennizzo sul percorso intero (art. 12). Con **biglietti separati** (due PNR, due vettori, o un regionale più una Freccia comprati a parte) **nessuna tutela**: il secondo treno è perso e il biglietto va rifatto a prezzo del giorno. Il regolamento impone di dirlo prima dell'acquisto; questa skill lo ripete a ogni proposta con più biglietti (sez. 11).
- **Treno cancellato in anticipo** (lo si vede sul PNR o nelle notifiche): si sceglie subito fra rimborso e nuova soluzione, prima che i posti sulle alternative finiscano.

---

## 7. Fattura elettronica dei biglietti

- **Trenitalia** ([emissione fattura](https://www.trenitalia.com/it/informazioni/emissione-fatturaonline.html)): sul sito e in app si attiva **«Richiedi la fattura» prima del pagamento**, inserendo partita IVA e, per la fattura elettronica, **PEC o codice destinatario** (altrimenti la fattura va nel cassetto fiscale). Dimenticata? Si recupera **entro le 24 del giorno dell'acquisto** da «Emissione Fattura/Ristampa documento fiscale». In biglietteria si chiede **prima** di pagare; alle self-service contestualmente all'acquisto; a bordo entro le 24 del giorno dopo. **Dopo un cambio, se la fattura non era stata chiesta, non si può più chiedere.** Split payment (enti pubblici): numero dedicato 800 18 60 19. Le fatture emesse si rivedono in Area Riservata > Crediti e Fatture.
- **Italo** ([fattura](https://www.italotreno.com/it/contatti-supporto/fattura)): si chiede **durante l'acquisto** oppure **entro le 24 del giorno dell'acquisto** da «Cambia Prenotazione > Richiedi Fattura» con il Codice Biglietto, o al 060708; lo split payment si chiede solo per telefono; i clienti **Italo Impresa** ricevono una fattura mensile unica.
- Regola per la chat: **la fattura si chiede nel flusso di acquisto, mai dopo**; la finestra è di poche ore e dopo un cambio si perde. Per il riaddebito al cliente basta anche il biglietto con ricevuta di pagamento (sez. 12), ma la fattura semplifica la registrazione.

---

## 8. Corriere extraurbane: regole valide per le aziende regionali, con Adriabus come esempio

Letto il 28/10/2026 su [adriabus.eu](https://www.adriabus.eu/) e [orari](https://www.adriabus.eu/orari/):

- **Gli orari ufficiali sono PDF per linea**, divisi per periodo: **invernale (per Adriabus dal 14/09/2026 al 05/06/2027), estivo, scolastico e non scolastico, feriale e festivo**. Il PDF della linea è l'unica fonte; gli aggregatori (Google Maps, app terze) spesso tengono l'orario del periodo sbagliato. Si legge la colonna del giorno giusto: **nei giorni festivi e nel periodo non scolastico molte corse saltano**; a ogni cambio di periodo si riscarica il PDF.
- **Biglietti**: in **app dell'azienda** (Adriabus ha la propria e MooneyGo), nelle **rivendite** autorizzate e alle **emettitrici**. Con i sistemi di bigliettazione nuovi **non si vende più nulla a bordo** (Adriabus dal sistema MARTA): si sale già con il biglietto. Il biglietto in app si **attiva prima di salire**; parte un **timer di 60 secondi** e il titolo è controllabile dal verificatore; chi non lo attiva è sanzionato secondo la legge regionale (per le Marche L.R. 12/2009), importi **[DA VERIFICARE]**. Dove la vendita a bordo esiste ancora, c'è un sovrapprezzo: si legge sul sito dell'azienda.
- **Variazioni e scioperi** dell'azienda stanno in **home page** del sito (Adriabus pubblica avviso con orari delle fasce: esempio reale, sciopero del 30/10/2026 dalle 08:30 alle 16:59 e dalle 20 a fine servizio) e nelle fermate soppresse (dal 14/09/2026 la linea 131 non ferma più a Cattolica FS). Si legge la sera prima e la mattina stessa.
- **Se la corsa salta**: le corriere regionali **non prevedono indennizzo**; si chiama il numero dell'azienda (Adriabus 800 664 332), si cerca la corsa successiva o il taxi e si **avvisa il cliente**. Per questo la corriera non si incastra mai con l'ultimo treno possibile (sez. 11).

---

## 9. Scioperi: fasce garantite, treni garantiti, dove si controllano

- **Treni regionali Trenitalia** ([treni garantiti in caso di sciopero](https://www.trenitalia.com/it/informazioni/treni_garantiti_incasodisciopero.app.html)): nei giorni **feriali** sono garantite le fasce **6-9 e 18-21**; nei **festivi 7-10 e 18-21** (per alcune regioni elenchi propri, Alto Adige a parte). I treni in corsa al momento dello sciopero arrivano a destinazione se entro un'ora di percorso; **lunga percorrenza**: elenco dei treni garantiti nelle **Tabelle A e B** (PDF sulla stessa pagina). **Italo** pubblica i treni «garantiti» e «non garantiti» sul sito: un treno non garantito **non è soppresso**, può partire, ma non ci si conta.
- **Corriere**: ogni azienda pubblica le proprie fasce garantite nell'avviso di sciopero (Adriabus, sez. 8); di norma coprono le ore di pendolarismo, ma **le fasce cambiano da azienda ad azienda** e si leggono sull'avviso, non si presumono.
- **Dove si controllano**: calendario del Ministero dei trasporti ([scioperi.mit.gov.it](https://scioperi.mit.gov.it/mit2/public/scioperi)) e Commissione di garanzia ([cgsse.it](https://www.cgsse.it/)), poi i siti dei vettori. Entrambi i siti pubblici **non si leggono via fetch** (503): la chat li apre nel browser dell'utente o chiede all'utente di aprirli.
- **Preavviso**: la legge 146/1990 impone un preavviso minimo di **10 giorni** per i servizi pubblici essenziali, con rarefazione fra scioperi dello stesso bacino **[DA VERIFICARE sul testo di legge]**: il 28/10 normattiva mostrava solo l'art. 1. Regola pratica: uno sciopero nazionale è noto almeno dieci giorni prima, quindi **si controlla il calendario quando si compra** e di nuovo la sera prima; quello che compare dopo è di norma una revoca o un'adesione locale.
- **Rimborso per sciopero** (sez. 2 e 4): Frecce e Intercity dall'annuncio fino alla partenza; regionali fino alle 24 del giorno prima [DA VERIFICARE].

---

## 10. Metro e taxi nelle città principali

- **Roma**: ATAC **Tap&Go** sulla metro con carta contactless o telefono, **1,50 € per 100 minuti** con tetto giornaliero (fonti terze indicano 7 € o 8,50 €: **[DA VERIFICARE]** sul sito ATAC, non leggibile). Taxi da e per **Fiumicino, tariffe fisse ADR** ([pagina ADR](https://www.adr.it/it/pax-fco-taxi), letta il 28/10/2026): **Roma centro entro le Mura Aureliane 55 €**, stazione Tiburtina 60 €, stazione Ostiense 50 €, Ciampino 55 €, Civitavecchia 130 €; corsa minima 35 € e tetto di 80 € per destinazioni entro il GRA; la tariffa fissa comprende bagagli e supplementi. Taxi ufficiali bianchi con tassametro; la tariffa fissa va **concordata prima** di partire.
- **Milano**: ATM metro con **tap in e tap out** su carta contactless ([pagina ATM](https://atm.it/EN/VIAGGIACONNOI/Pages/contactless_cards_metro.aspx)): **2,20 € per 90 minuti**, dopo la quarta corsa nel giorno il tetto del giornaliero; dal 01/01/2026 i biglietti cartacei sono aboliti (fonte terza [DA VERIFICARE]). Taxi **Malpensa**: tariffa fissa comunale, le fonti lette discordano fra 95 e 110 € **[DA VERIFICARE]** sul sito del Comune; **Linate a tassametro**.
- **Altre città**: la regola generale è controllare se la metropolitana accetta la carta contactless (Roma, Milano, Napoli, Torino e Brescia lo fanno con regole proprie **[DA VERIFICARE]** per ogni città prima di citare un prezzo) e se il Comune ha **tariffe fisse** da stazioni e aeroporti; dove non ci sono, si chiede prima al tassista la stima e si pretende la ricevuta.
- **App dei taxi**: le app di prenotazione (radiotaxi cittadini, FreeNow, itTaxi, Uber dove opera con taxi) rilasciano **ricevuta elettronica con il percorso**, utile per la deduzione (sez. 12); quando la corsa è tracciata dall'app non serve lo scontrino cartaceo.

---

## 11. Pianificazione porta a porta: margini, biglietto unico o separato, cosa comprare quando

1. **Margine corriera → treno**: almeno **una corsa di corriera prima** di quella «giusta», o un margine **di 30 minuti** se la corsa precedente non esiste. La corriera non ha tutele (sez. 8); se salta, il treno non aspetta e il biglietto Super Economy è perso.
2. **Margine treno → treno con biglietti separati**: **mai sotto i 30 minuti**, e sui nodi grandi (Bologna, Roma, Milano) **45**. Con biglietto unico dello stesso vettore valgono le coincidenze garantite (sez. 6) e si può scendere a quello che propone il sito.
3. **Biglietto unico o separato**: unico quando la stessa compagnia copre tutto il percorso (una «soluzione di viaggio» Trenitalia con cambio, o Italo più Italobus); separato quando si mescolano regionale e Freccia comprati a parte, o Trenitalia e Italo. Prima del sì si scrive all'utente: «biglietti separati, nessuna tutela sulla coincidenza, margine X minuti».
4. **Cosa comprare prima**: il tratto a prezzo dinamico (Frecce, Italo) **appena il giorno è certo**, scegliendo Economy o Super Economy solo se l'orario non cambierà, altrimenti Base o Flex; il regionale **in app il giorno prima o la mattina stessa** (prezzo fisso, cambi fino alle 23:59 del giorno prima, rimborso 100% fino allo stesso termine); la corriera **in app prima di salire**; metro e taxi al momento.
5. **Viaggio incerto** (riunione da confermare): Base o Flex, oppure si aspetta la conferma e si paga di più; un Super Economy per un viaggio incerto è denaro perso con probabilità alta, e si dice.
6. **Voce di calendario**: una sola voce per tratta con «partenza casa» e «arrivo destinazione» reali (corriera inclusa), più la riunione; descrizione con i PNR, la tariffa e cosa permette, i numeri utili. Regole di spazio e durata minima come in `trello` sez. 9.
7. **La sera prima**: calendario MIT e vettori per scioperi (sez. 9), PDF della corriera per il giorno giusto (sez. 8), notifiche sul PNR, meteo se il percorso è di montagna; la mattina si guarda il treno in tempo reale prima di uscire.
8. **Ritorno**: si tiene aperto con Base o Flex, oppure si compra la sera prima del ritorno; quando il cliente allunga la riunione, il cambio senza penale vale più del risparmio.

---

## 12. Spese di viaggio per una partita IVA: cosa conservare

Dalla [circolare 15/E del 22/12/2025 dell'Agenzia delle Entrate](https://www.agenziaentrate.gov.it/portale/documents/20143/8410837/Circolare+n.+15+del+22_12_2025.pdf/ea6aa7af-f133-2381-8750-6c3b871b7bc6?t=1766416605375) (letta il 28/10/2026):

- **Tracciabilità obbligatoria** (dal 2025) solo per **vitto, alloggio, viaggio e trasporto con taxi o NCC**, anche se prenotati via app o piattaforma: si pagano con carta, bonifico o altro mezzo tracciato e si conserva la prova (ricevuta della carta, estratto conto). **I biglietti di treno, bus, aereo e nave sono esclusi dall'obbligo** di tracciabilità, ma vanno comunque documentati. Il decreto-legge 84/2025 limita l'obbligo alle trasferte **in Italia**.
- **Riaddebito analitico al committente**: le spese di viaggio **riaddebitate analiticamente** in fattura al cliente **non concorrono al reddito del professionista** e non sono deducibili come costo (art. 54 TUIR dopo il decreto 192/2024); l'art. 54-ter regola le spese non rimborsate dal cliente. Per questo ogni biglietto va associato al cliente o al progetto nel momento in cui si archivia.
- **Cosa conservare per ogni viaggio**: il **biglietto** (PDF con PNR o Codice Biglietto), la **fattura** se chiesta (sez. 7) o la **ricevuta di pagamento**, la ricevuta del taxi con il percorso, la ricevuta della corriera (l'app la rilascia) e, se il viaggio ha avuto un ritardo indennizzato, la nota dell'indennizzo (riduce il costo). Si archiviano **nello stesso giorno** con data, tratta e cliente.
- Spese di rappresentanza (pasti offerti al cliente) deducibili all'1% dei compensi e solo se tracciate. **Per le soglie e le aliquote di deducibilità si rimanda al commercialista**: questa skill si ferma a cosa conservare.

---

## 13. Trappole che costano soldi

- **Super Economy o Low Cost per un viaggio incerto**: non si cambiano e non si rimborsano; si dice prima del sì.
- **Regionale cartaceo non convalidato, o digitale senza barra verde**: multa anche con biglietto pagato; il PDF non vale.
- **Biglietti separati con coincidenza stretta**: nessuna tutela, secondo biglietto da ricomprare.
- **Corriera festiva o non scolastica**: la corsa delle 7 che si prende tutti i giorni può non esistere il sabato o ad agosto; si legge la colonna giusta del PDF.
- **Sciopero controllato solo all'acquisto**: si ricontrolla la sera prima; una revoca o un'adesione locale compare dopo.
- **Fattura chiesta dopo**: oltre le 24 del giorno dell'acquisto, o dopo un cambio, non si ottiene più.
- **Indennizzo non chiesto**: per Frecce, Intercity e Italo l'indennizzo va **richiesto** (solo il regionale Trenitalia è automatico); si fa entro i termini e si preferisce il denaro al bonus quando il viaggio si riaddebita al cliente.
- **Tariffa fissa del taxi non concordata**: a Roma e Milano si cita la tariffa fissa prima di salire e si chiede la ricevuta.
- **Punti CartaFRECCIA lasciati scadere**: il programma chiude il 31/12/2026, i punti si spendono entro il 31/03/2027.

---

## 14. Meccanica dei siti e delle app (da verificare a mano)

Nessun punto confermato sullo schermo in questa prima stesura. Da scrivere qui alla prima volta che si fanno: dove sta la casella «Richiedi la fattura» nel checkout Trenitalia e in quello Italo; come si legge il PNR e il Codice Biglietto nelle app; dove si attiva il biglietto della corriera in app e come appare il timer; come si chiede l'indennizzo Trenitalia da Area Riservata e Italo da «Cambia Prenotazione»; come si collega la carta a Tap&Go e al tap in e out ATM per avere la ricevuta.

---

## 15. Cosa non fare mai

- Comprare un biglietto senza il sì esplicito dell'utente, o su un account diverso dal suo.
- Proporre un prezzo senza dire la tariffa e cosa permette per cambio e rimborso.
- Incastrare la corriera con l'ultimo treno possibile, o due biglietti separati con meno di 30 minuti.
- Dare per scontato l'orario della corriera senza aprire il PDF del periodo in corso e del giorno giusto.
- Lasciar passare le 24 del giorno dell'acquisto senza chiedere la fattura, se serve.
- Salire su un regionale senza la barra verde o la convalida.
- Citare come certa una cifra marcata [DA VERIFICARE], o un orario letto da un aggregatore.
- Scrivere nella skill nomi, indirizzi, numeri di tessera o account dell'utente.

---

## Fonti (verificate 28/10/2026)

**Trenitalia, lette:** [Tariffe Frecce e Intercity](https://www.trenitalia.com/it/html/trenitalia/Info_Tariffe_it_LeFrecce.html) · [Cambi e rimborsi](https://www.trenitalia.com/it/html/trenitalia/Info_cambi_rimborsi.html) · [Indennizzo per ritardo](https://www.trenitalia.com/it/html/trenitalia/Indennizzo_per_ritardo.html) · [Indennità per ritardo, guida del viaggiatore](https://www.trenitalia.com/it/informazioni/la-guida-del-viaggiatore/indennita-per-ritardo.html) · [Emissione fattura online](https://www.trenitalia.com/it/informazioni/emissione-fatturaonline.html) · [Nuovo biglietto digitale regionale](https://www.trenitalia.com/it/regionale/nuovo-biglietto-digitale-regionale.html) · [Indennizzo automatico regionale](https://www.trenitalia.com/it/servizi/indennizzo-automatico-biglietto-digitale-regionale.html) · [Treni garantiti in caso di sciopero](https://www.trenitalia.com/it/informazioni/treni_garantiti_incasodisciopero.app.html) · [CartaFRECCIA](https://www.trenitalia.com/it/cartafreccia.html).

**Italo, lette:** [Tariffe](https://www.italotreno.com/it/il-treno/tariffe) · [Termini e condizioni](https://www.italotreno.com/it/termini-condizioni) · [Contratto di trasporto dal 01/10/2026 (PDF)](https://www.italotreno.com/~/media/Images/content/pdf/contratto_di_trasporto/Contrattoditrasportorel610) · [Italo Più, livelli e benefici](https://www.italotreno.com/it/programma-fedelta-italo-piu/livelli-benefici) · [Italo Più, assistenza](https://www.italotreno.com/it/programma-fedelta-italo-piu/assistenza-programma-fedelta) · [Fattura](https://www.italotreno.com/it/contatti-supporto/fattura).

**Norme, lette:** [Regolamento UE 2021/782, testo italiano (PDF ospitato da Italo)](https://www.italotreno.com/~/media/Images/content/pdf/contratto_di_trasporto/regolamento-europeo/Regeuropeo782-2021) · [Agenzia delle Entrate, circolare 15/E del 22/12/2025 (PDF)](https://www.agenziaentrate.gov.it/portale/documents/20143/8410837/Circolare+n.+15+del+22_12_2025.pdf/ea6aa7af-f133-2381-8750-6c3b871b7bc6?t=1766416605375).

**Trasporto locale, lette:** [Adriabus, home](https://www.adriabus.eu/) · [Adriabus, orari](https://www.adriabus.eu/orari/) · [ADR, taxi da Fiumicino](https://www.adr.it/it/pax-fco-taxi) · [ATM Milano, carte contactless in metro](https://atm.it/EN/VIAGGIACONNOI/Pages/contactless_cards_metro.aspx).

**Terze parti, lette (usate solo dove la fonte ufficiale non era leggibile, marcate [DA VERIFICARE]):** sicurauto.it (treni garantiti, taxi Roma e Milano, rimborso per sciopero), lentepubblica.it (indennizzo automatico regionale), aziendabanca.it (Tap&Go ATAC).

**Non lette in questa stesura, da verificare prima di citarle:** Condizioni generali di trasporto Trenitalia e Condizioni regionali (validità del cartaceo, sanzioni) · [EUR-Lex 2021/782](https://eur-lex.europa.eu/legal-content/IT/TXT/?uri=CELEX:32021R0782) (vuoto via fetch) · [legge 146/1990 su normattiva](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:1990-06-12;146) (solo art. 1) · [calendario scioperi MIT](https://scioperi.mit.gov.it/mit2/public/scioperi) e [CGSSE](https://www.cgsse.it/) (503) · [ATAC Tap&Go](https://www.atac.roma.it/tapandgo) (muro anti-bot) · pagina Italobus · tariffe fisse taxi del Comune di Milano · regole contactless di Napoli, Torino, Brescia.
