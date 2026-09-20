---
name: creditsafe-monitoraggio-credito
description: "Regole operative verificate per usare Creditsafe (app.creditsafe.com e live-monitoring.creditsafe.com): ricerca società senza bruciare crediti, lettura del Report Società, monitoraggio del portafoglio, regole di notifica, esportazioni, scala di score e rating. Include le trappole già costate crediti. Usala ogni volta che si parla di Creditsafe, di affidabilità o solvibilità di un'azienda, di fido, di score o rating creditizio, di bilanci depositati, di monitoraggio clienti o fornitori, anche senza che venga nominato Creditsafe."
---

# Creditsafe, monitoraggio del credito

**Verificato in piattaforma il 18 e il 19 agosto 2026.** Ogni cosa scritta qui è stata vista sullo schermo, non dedotta. Dove una cosa non è stata verificata, è detto esplicitamente.

## 0. Manutenzione di questa skill

Questa skill invecchia. Va rivista quando cambia una di queste cose:

- Il piano viene rinnovato o modificato (oggi il rinnovo è al **14/01/2027**), perché cambiano i crediti disponibili.
- Compare l'API Connect, che oggi **non c'è**.
- Cambia la struttura dei portafogli o l'interfaccia del monitoraggio.

Chi la aggiorna scrive la data nuova in cima e segna cosa ha verificato di persona.

---

## 1. Che cosa è, e la regola di prudenza che governa tutto

Creditsafe è una fonte di dati economico-finanziari su aziende italiane ed estere. Si accede da `https://app.creditsafe.com/` con la sessione del browser già autenticata.

⚠️ **Non si inseriscono MAI credenziali.** Se la sessione è scaduta, il login lo fa l'utente. Questa non è una preferenza, è una regola dura.

Il piano è a canone annuale e i crediti si dividono in due categorie, e la differenza governa il comportamento.

**Abbondanti, si usano senza chiedere:**

- **Report Società**, il rapporto aziendale completo. Circa 455 residui.
- **Slot di monitoraggio**, circa 475 liberi su 500.
- **Alert** e **PAYGO Estero**, di fatto illimitati.
- **Export del monitoraggio**, 500.

**Scarsi, solo su richiesta esplicita dell'utente:**

- **Informazioni aggiuntive**, 14 pezzi per un anno.
- **Report Dirigente**, 14 pezzi per un anno.

Prima di consumarne uno dei due scarsi si dice quanti ne restano. Il bottone che li brucia si chiama **Approfondisci Report** ed è l'unico che sblocca dirigenti, soci e unità locali, che nel report base non ci sono.

Il consumo residuo si legge da **Il mio account** poi **Prodotti & Servizi** (`/account/productsAndService`). Aprire quella pagina non costa niente ed è il primo posto dove guardare quando si vuole sapere se qualcuno ha speso qualcosa.

---

## 2. ⚠️ Le due applicazioni hanno sessioni separate, e il sintomo inganna

Il monitoraggio **non sta dentro l'app principale**: è un'applicazione separata su `live-monitoring.creditsafe.com`, con login condiviso ma **sessione indipendente**, che scade in un momento diverso.

**Quando la sessione del monitoraggio è caduta non compare una pagina di login.** Andare all'URL diretto rimbalza sul **sito pubblico** `www.creditsafe.com`, che è un terzo dominio con i bottoni "Login" e "Prova gratuita". Sembra di essere finiti sul sito commerciale per sbaglio.

**Perché è grave per un agente:** i permessi degli strumenti browser sono per dominio. Una sessione che stava lavorando su `live-monitoring` viene sbattuta su un dominio per cui non ha il permesso e si ferma ad aspettare un'autorizzazione che nessuno le dà. Dall'esterno sembra bloccata senza motivo. È successo davvero.

**Il rimedio, verificato, è un click:** dall'app principale ancora autenticata, cliccare **"Monitoraggio"** nel menu a sinistra. Rigenera la sessione e apre il monitoraggio in una scheda nuova.

**Come accorgersene prima di piantarsi:** dopo ogni navigazione, controllare che l'URL sia ancora `live-monitoring.creditsafe.com`.

---

## 3. ⚠️ La barra di ricerca in alto APRE il report e brucia un credito

**Verificato sul campo, ed è costato un credito.** Digitando un termine nella barra di ricerca in cima alla pagina, se il termine fa **match secco** su una sola azienda la piattaforma **non mostra la lista**: va dritta sul Report Società e consuma. Nessuna conferma, nessun avviso. È già capitato di aprire il rapporto di un barbiere cancellato nel 2017 cercando un cognome.

**Il metodo sicuro, da usare sempre: costruire l'URL di ricerca a mano.**

```
https://app.creditsafe.com/search?countries=IT&limit=24&name=<TERMINE URL ENCODED>&page=1
```

Questo apre sempre la **lista** e non può aprire un report.

**Controllo dopo ogni ricerca:** l'URL deve essere ancora `/search?...`. Se è diventato `/companies/IT-...`, è stato aperto un report ed è stato speso un credito.

⚠️ **La ricerca per ragione sociale è fuzzy e larghissima.** Cercare `ALMAPHYTO` in Italia restituisce oltre settemila aziende, perché matcha su `ALMA`. Quindi **"non compare in cima" non vuol dire "non esiste"**: per una prova negativa serve il codice fiscale.

⚠️ **San Marino è nella tendina dei paesi ma NON è interrogabile.** Qualunque ricerca torna un errore generico, mentre le altre sezioni della stessa pagina rispondono. Non è la query, è il paese. E gli slot del piano si chiamano "Monitoraggio, società italiane", quindi anche trovando la scheda il monitoraggio di una sammarinese va verificato con l'Account Manager.

---

## 4. ⚠️ Il monitoraggio automatico è acceso: aprire un report ha un effetto collaterale

Nel pannello del monitoraggio c'è un interruttore **Monitoraggio automatico**, ed è **acceso**. Secondo la guida ufficiale, con quell'interruttore attivo **ogni azienda di cui si apre un Rapporto di Credito entra automaticamente nel portafoglio monitorato**.

Quindi aprire un report non consuma solo un credito: **consuma uno slot e cambia le notifiche che arrivano all'utente**.

**Regola operativa: prima di aprire il report di un'azienda si guarda se è già in `Portfolio`.** Se c'è, si apre liberamente. Se non c'è, si chiede. Il controllo è gratis.

⚠️ **Un test involontario NON lo ha confermato**, e va detto: aprendo per sbaglio il rapporto di una società cancellata e non monitorata, il contatore dei report è salito ma il contatore degli slot è rimasto fermo e l'azienda non è entrata. Un caso solo, e su una società cessata: **non basta a dichiarare falsa la guida ufficiale**. La cautela resta, il rischio è meno probabile di quanto temuto.

---

## 5. Come si aggiunge un'azienda a un portafoglio

⚠️ **Il pulsante verde `Aggiungi` NON aggiunge un'azienda: crea un PORTAFOGLIO NUOVO.** Se si apre un dialog che chiede nome del portfolio, oggetto email e destinatari, si è nel posto sbagliato. **Si annulla.**

La strada giusta, che non consuma crediti report:

1. `Monitoraggio` poi `Portfolio`, **selezionando prima il portafoglio di destinazione** dal menu in alto a destra.
2. Pulsante arancione **`Importa da file`**.
3. Dentro il dialog, aprire **`+ Importazione Manuale`**: nazione, tipo **Safe Number** (in alternativa il numero REA), e una textarea in cui si incollano gli identificativi **uno per riga**.
4. Pulsante verde **`Importa`**.

⚠️ **L'import funziona ma è asincrono, e la conferma inganna.** Il messaggio dice *"L'import delle società è stato avviato"*, non completato. Le aziende possono metterci **minuti** a comparire, mentre il pulsante di aggiornamento risponde *"I dati del portfolio sono stati aggiornati con successo"* mostrando i dati vecchi.

**La regola che ne esce: si aspetta e si ricontrolla più tardi. NON si ripete l'import perché "non si vede".** Una volta è stato ripetuto quattro volte sulla stessa azienda e per fortuna la piattaforma deduplica per Safe Number. È una fortuna, non un metodo.

---

## 6. Il campo Riferimento, e l'errore che fa fare

Ogni azienda in portafoglio ha un campo **Riferimento**, che traduce la ragione sociale nel nome con cui l'utente chiama davvero quell'azienda. Sono spesso molto diversi: un cliente conosciuto come "Euroricambi" sta in piattaforma come "FA.TA. RICAMBI", uno conosciuto come "Gruppo NEM" sta come "NORD EST MULTIMEDIA".

⚠️ **Prima di dire che un cliente non è monitorato, si controlla il campo Riferimento e il codice fiscale, mai il nome che usa l'utente.** È già successo di compilare una lista di "clienti scoperti" sulla sola ragione sociale e di sbagliarne due su undici.

**Dove si compila:** dalla lista del `Portfolio`, **icona matita** a inizio riga, dialog *"Modifica i dettagli dell'azienda"* con i campi Riferimento, Limite e Note, poi `Conferma`. Compare il messaggio "I dettagli dell'azienda sono stati aggiornati con successo".

⚠️ **NON si compila dal dialog "Opzioni di monitoraggio" del report**, dove il campo `Referenza` esiste ma **non salva**. Verificato: il testo digitato lì si perde.

⚠️ **Il numero REA è per provincia, il codice fiscale no.** Una società con sedi in province diverse ha più REA e quindi più schede Creditsafe con Safe Number diversi. **Il codice fiscale è la vera chiave di identità.** È così che si riconosce un doppione in portafoglio.

---

## 7. Il monitoraggio: portafogli, regole, eventi

Il monitoraggio ha cinque sezioni: **Home** (contatori eventi e feed), **Portfolio**, **Regole di notifica**, **Esportazioni**, **Analisi**.

**Le regole di notifica sono PER PORTAFOGLIO.** Due portafogli possono avere configurazioni diverse, e questo è il posto dove si sbaglia più facilmente.

⚠️ **Il selettore di portafoglio si resetta su `Default` a ogni ricarica e a ogni cambio di scheda.** Se si ricarica e si va su `Regole di notifica` senza riselezionare, si sta leggendo `Default` credendo di leggere un altro portafoglio. **La controprova sono i contatori eventi in cima**, che cambiano col portafoglio: se non si muovono, il filtro non ha agito.

⚠️ **Se il portafoglio predefinito è stato svuotato, la Home su `Default` non mostra più niente.** Gli eventi vanno letti selezionando **`Tutti i portfolio`**. È un errore facile e silenzioso: si guarda una Home a zero e si conclude che non è successo niente, mentre gli eventi ci sono.

**Un'azienda in due portafogli genera lo stesso evento due volte**, una per portafoglio. Non sono due eventi, è lo stesso contato due volte.

**Che cosa genera un evento, visto sul campo:** Limite (il fido consigliato), Score Internazionale, Ultima annualità di bilancio, Ultimo anno di bilancio consolidato, Indirizzo, Comportamento sui pagamenti, Payment Expectation. Ogni evento riporta valore vecchio e valore nuovo, che è la parte utile.

**L'avviso email parte il giorno dopo l'evento, non in tempo reale.**

**Le regole che contano di più** sono `Comportamento sui pagamenti` e `Payment Expectation`, perché sono le uniche che anticipano il cliente che sta per smettere di pagare. Tutte le altre fotografano una cosa già successa.

⚠️ **Il dato sui pagamenti in Italia esiste**, anche se il campo *Trend di pagamento* del report appare spesso vuoto. Verificato il 19/08/2026: una società italiana in portafoglio ha generato eventi reali su entrambe quelle regole. Che il campo vuoto del report e questi eventi siano lo stesso dato sottostante è **probabile ma non provato**.

**La finestra dei bilanci è maggio-agosto.** I depositi al 31/12 arrivano lì, e producono a grappolo bilancio nuovo, punteggio ricalcolato, fido rivisto. È il periodo in cui il monitoraggio va guardato più spesso.

⚠️ **Osservazione da verificare, non ancora spiegata:** si è visto un punteggio scendere di tre punti nello stesso giorno del deposito di un bilancio **senza** che venisse generato l'evento `Score Internazionale`, con la regola accesa e la soglia a un punto. Se si conferma, i cali di score legati a un bilancio nuovo sfuggono alla notifica, che è proprio il caso più interessante. Da ricontrollare al prossimo deposito.

**Analisi** dà la distribuzione del portafoglio per fascia di rischio, con l'elenco cliccabile per lettera. È il cruscotto da aprire per primo quando serve la fotografia d'insieme invece del singolo cliente.

**Esportazioni** permette esportazioni **pianificate** ricorrenti via email. È il sostituto dell'API quando l'API non c'è nel piano: invece di ricontrollare il pannello a mano, si programma un export del portafoglio e si lavora sul file.

---

## 8. Dentro un Report Società

**Un credito copre l'azienda intera, tutte le schede.** Navigare fra Sintesi, Bilanci, KPI, Score, ESG, Gruppo, Possibili collegamenti e Documenti **non costa niente in più**. Si entra una volta e si guarda tutto. Uscire e rientrare invece rischia di ricontare.

URL diretto: `app.creditsafe.com/companies/IT-0-<NumeroREA>`.

**Sintesi.** Anagrafica completa con PEC, capitale sociale, numero medio dipendenti, codici ateco, descrizione dell'attività, capogruppo. Poi tre blocchi che valgono da soli il report:

- **Dati finanziari chiave** su tre anni con variazione percentuale.
- **Commenti**: una decina di frasi in italiano che spiegano lo score a parole, incluso **quanto sono vecchi i bilanci depositati**. È la parte più sottovalutata del report.
- **Sintesi richieste**: quante volte il report è stato richiesto negli ultimi 3, 6, 9 e 12 mesi. È un termometro di quanta gente sta controllando quell'azienda, e una impennata è un segnale in sé.

**Bilanci.** Cinque esercizi affiancati, due viste, e **servono entrambe**:

- `Riclassificato`: stato patrimoniale attivo e indici (ROS, ROI, ROE, Current Ratio, Acid test, **tempi medi di incasso e di pagamento**, PFN, EBITDA e EBIT margin).
- `IFRS`: **qui c'è il resto**, cioè il conto economico completo e il **passivo** (debiti verso fornitori, verso banche, **debiti infragruppo**, patrimonio netto).

⚠️ **Chi guarda solo `Riclassificato` non vede il conto economico né i debiti.** Il passivo sta sotto `IFRS`. Esportabile in Excel.

**KPI.** Il confronto con il settore: per ogni indicatore, su cinque anni, valore dell'azienda contro **media e mediana del macro settore ateco**. È la scheda più utile quando serve un giudizio e non un numero.

**Score.** Score di oggi, score precedente, data dell'ultimo cambiamento, storico dello score e storico del fido.

**Gruppo.** Compare solo se l'azienda è in un gruppo. Organigramma navigabile con le percentuali di controllo.

**Possibili collegamenti.** ⚠️ La parte **internazionale è rumorosa** e va ignorata quasi sempre: su una società può dare migliaia di corrispondenze matchate sulla sola stringa "S.R.L.". La sezione nazionale invece è pulita e utile.

**Documenti.** ⚠️ **Non si scarica niente senza il via dell'utente**: visure e bilanci ottici sono prodotti a sé nel listino, quindi il download quasi certamente consuma.

---

## 9. La scala ufficiale di score e rating

| Punteggio | Rischio | Lettera | Giudizio |
|---|---|:--:|---|
| 71-100 | molto basso | **A** | Affidabilità molto alta |
| 51-70 | basso | **B** | Affidabilità alta |
| 30-50 | moderato | **C** | Affidabile |
| 21-29 | alto | **D** | Attenzione, affidabilità bassa |
| 1-20 | molto alto | **D** | Attenzione, affidabilità bassa |
| non disponibile | | **E** | Non disponibile |

⚠️ **A e D sono asimmetriche.** La lettera D copre tutto da 1 a 29, quindi **due aziende entrambe "D" possono essere lontanissime**. Il numero conta più della lettera. Un'azienda senza bilancio recente non ha punteggio e riporta *"Bilancio d'esercizio troppo vecchio"*.

---

## 10. ⚠️ Le tre trappole di lettura dei numeri

Queste sono le cose che fanno dire sciocchezze con la faccia sicura.

**1. Il ROE con patrimonio netto negativo è un artefatto.** Se il patrimonio netto è negativo, il ROE si ribalta di segno e mostra un numero splendido. Un ROE del 108% su un patrimonio netto di meno un milione **non è un buon risultato**, è una divisione per un numero negativo. **Prima di citare un ROE si guarda il segno del patrimonio netto.**

**2. Le percentuali di crescita mentono se un esercizio è breve.** Quando una società cambia la data di chiusura del bilancio produce un esercizio di transizione che dura pochi mesi, e il pannello confronta allegramente dodici mesi con tre. Si è vista una crescita mostrata come **+508%** che sugli esercizi pieni era **+54%**. **Prima di citare una variazione percentuale si guarda la lunghezza dei due esercizi confrontati.** Vale anche al contrario sulle perdite.

**3. Una D non è una storia, è una probabilità.** Davanti a un rating basso si guardano sempre tre cose prima di parlare:

- **Il patrimonio netto è negativo?**
- **C'è una capogruppo, e da dove arriva il debito?**
- **Quanto è vecchio l'ultimo bilancio depositato?**

Due aziende con la stessa D possono essere opposte. Una con fatturato in calo del 68%, cassa a settemila euro e bilancio fermo a diciannove mesi prima è un'azienda che si sta spegnendo. Una filiale italiana che cresce, ha tre milioni in cassa e perde perché la casa madre estera la finanzia con debito a lungo termine ha lo stesso rating ma un rischio di natura completamente diversa: non è insolvenza operativa, è la **decisione strategica del gruppo**.

⚠️ **E su quella decisione non si risponde.** Alla domanda "quanto durerà il sostegno della capogruppo" non risponde nessun dato disponibile. **Si presidiano i segnali** che la anticiperebbero, e sono tutti coperti dalle regole di notifica: variazione del **Capitale Sociale** (una ricapitalizzazione dice che il gruppo resta), **uscita da un gruppo**, cambio di **Stato società**, nuova **annualità di bilancio**, **protesti**. Un ritardo nel deposito del prossimo bilancio è di per sé un segnale.

⚠️ **E non si dà per scontato che una capogruppo estera sia quotata.** È già stato affermato senza verificarlo, ed era falso. Una capogruppo **non quotata non ha obblighi di informativa periodica**, quindi la sua salute **non è monitorabile dall'esterno**. Cambia completamente cosa si può dire.

---

## 11. Cosa NON fare

1. **Non inserire mai credenziali.** Sessione scaduta significa che il login lo fa l'utente.
2. **Non usare la barra di ricerca in alto.** Si costruisce l'URL `/search?` a mano.
3. **Non consumare Informazioni aggiuntive e Report Dirigente** senza richiesta esplicita. Non cliccare **Approfondisci Report**.
4. **Non modificare i portafogli di iniziativa.** Aggiungere, spostare o cancellare aziende **cambia le notifiche che l'utente riceve**. Si propone, non si fa. Lo stesso vale per i destinatari degli alert.
5. **Non aprire il report di un'azienda che non è già in `Portfolio`** senza chiedere. Il controllo è gratis.
6. **Non ripetere un import perché "non si vede".** È asincrono, si aspetta.
7. **Non scaricare visure e bilanci ottici** senza il via dell'utente.
8. **Non dare un numero a memoria.** I punteggi cambiano: prima di riferire un dato lo si rilegge dalla fonte.
9. **Non dare consigli di investimento.** Questa non è consulenza finanziaria: si riportano i dati e si spiega come leggerli, la decisione è di chi legge.
10. **Non far uscire questi dati.** Sono informazioni economiche riservate su aziende terze: restano nelle risposte all'utente, non finiscono in materiali per clienti.

---

## Fonti

- FAQ dentro il pannello: `app.creditsafe.com/account/faq`, molto più dense di quanto il nome suggerisca.
- White paper **ScoreCard** sul modello di valutazione italiano.
- Guide della **Creditsafe Academy**: Monitoraggio, Rapporto di credito società italiane, Informazioni aggiuntive e Report Dirigente, Prospetti.
- Verifiche dirette in piattaforma del 18 e 19 agosto 2026, da cui vengono tutte le trappole descritte qui.
