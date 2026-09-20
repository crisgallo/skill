---
name: "google-ads-performance"
description: "Regole operative verificate per montare, ottimizzare e diagnosticare campagne Google Ads: Search, Demand Gen, Performance Max. Usare ogni volta che si lavora sul pannello Google Ads: tipi di corrispondenza, strategie di offerta, struttura campagne, conversioni, esclusioni, specifiche degli asset. Serve anche per fare l'igiene di un account ereditato."
---

# Google Ads: regole operative

**Ultima verifica delle fonti: 11 agosto 2026.**

---

## 0. Manutenzione di questa skill (leggere per primo)

Google cambia soglie, nomi delle strategie di offerta e specifiche degli asset più volte l'anno. Quindi:

1. **Prima di applicare una soglia numerica su un account che spende, ricontrollala.** Se la verifica in cima ha più di **due o tre mesi**, si rifà una ricerca sulle fonti ufficiali prima di toccare il pannello.
2. **Quando una fonte smentisce una regola scritta qui, si aggiorna la skill nello stesso momento.** Una skill che invecchia in silenzio è peggio di nessuna skill: dà sicurezza falsa.
3. Aggiornando, si **riscrive la data** in cima e si annota **cosa è cambiato e da quando**, così si sa quali dati storici restano confrontabili.
4. Segnali che è ora di ricontrollare: il pannello mostra voci che qui non sono descritte; un'impostazione non si trova più dove dovrebbe; un tipo di campagna viene sostituito da uno nuovo.

---

## 1. La regola che salva più budget: corrispondenza generica solo con i dati

**La corrispondenza generica (broad match) funziona solo accoppiata a Smart Bidding e a un tracciamento delle conversioni solido.** Richiede volume:

- **30-50 conversioni al mese per campagna** come minimo di funzionamento
- **50-100 al mese** perché abbia dati sufficienti a guidare davvero

⚠️ **Su un account nuovo o con budget limitato la generica è la scelta sbagliata:** massimizza la copertura e brucia il budget prima di aver imparato qualcosa. Si parte con **frase ed esatta**, si guardano i termini di ricerca reali, e si allarga solo quando il volume di conversioni lo sostiene.

**Le esclusioni contano più della scelta delle keyword.** Con la generica servono liste di **parole chiave escluse a livello di account**, non solo di campagna, per bloccare interi temi in un colpo.

---

## 2. Strategie di offerta: la sequenza per un account senza storico

1. **Massimizza le conversioni senza target**, per **due-quattro settimane**. Serve a raccogliere dati, non a performare.
2. Poi si aggiunge un **CPA target** ricavato dal costo per conversione **reale osservato**, non desiderato.
3. Il CPA target deciso a tavolino su un account senza storico è il modo più veloce per non avere consegna: se è troppo basso, la campagna semplicemente non gira.

⚠️ Con budget molto piccoli e conversioni rare (poche al mese) nessuna strategia automatica ha dati sufficienti. In quel caso l'obiettivo della campagna **non è convertire, è imparare quali query esistono**: si accetta di ottimizzare su clic e si legge il rapporto sui termini di ricerca.

---

## 3. Struttura: temi ampi, non keyword singole

- Campagne organizzate per **tema o linea di servizio**, con gruppi di annunci **consolidati**.
- Poche campagne larghe battono molte campagne strette: Smart Bidding ha bisogno che le conversioni si accumulino in un posto solo.
- La segmentazione fine per keyword era la pratica di dieci anni fa e oggi spezza i dati.

---

## 4. Conversioni: la parte che decide tutto il resto

- **Una sola azione primaria.** Se sono primarie anche le visualizzazioni di pagina o i clic sul telefono, l'algoritmo ottimizza sul segnale debole, che è più frequente e più facile.
- Tutto il resto va impostato come **secondario**: si misura ma non guida le offerte.
- **Conversioni avanzate** (Enhanced Conversions): alzano il tasso di corrispondenza e recuperano attribuzione persa.
- **Conversioni avanzate per i lead**: rimandano a Google il lead che si è chiuso *offline*. Su cicli di vendita lunghi, dove il modulo compilato non è la vendita, sono il pezzo che pesa di più: insegnano all'algoritmo **quale modulo vale davvero**.
- Verificare il **modello di attribuzione** in uso prima di leggere qualsiasi report.

---

## 5. Tagging e misurazione

- **Tagging automatico attivo** (Amministrazione → Impostazioni account). Con quello acceso, il `gclid` porta in GA4 campagna, gruppo e parola chiave.
- ⚠️ **Con l'auto-tagging attivo non si mettono UTM manuali**: li sovrascrivono e rompono l'importazione delle conversioni. Basta **nominare bene la campagna**.
- **Applicazione automatica dei consigli: disattivata.** Con quella accesa Google modifica keyword, budget e asset da solo, e ci si ritrova con modifiche che nessuno ha deciso.
- Collegamento con **GA4** attivo: serve per importare i pubblici e per leggere i **percorsi di conversione** invece del solo ultimo clic.

---

## 6. Demand Gen

- Copre YouTube (feed e Shorts), Discover e Gmail.
- **Caricare tutti i rapporti d'aspetto**: 16:9, 1:1 e 9:16. Senza il 9:16 si perde l'inventory Shorts, e un asset verticale in Demand Gen porta oltre il **35% di conversioni in più su Shorts**.
- **Le misure delle immagini non coincidono con quelle dei video.** Per le immagini: orizzontale **1200x628 (1,91:1)**, quadrata **1200x1200**, verticale **960x1200 (4:5)**, verticale **1080x1920 (9:16)**. Massimo **5 MB** per asset, fino a 20 immagini per annuncio.
- **Aree di sicurezza:** testo e loghi dentro il **centro 90% orizzontale e 80% verticale**, così i controlli di riproduzione non li tagliano.
- Budget: sotto una certa soglia giornaliera la campagna non entra in asta in modo utile. **5 € al giorno su Demand Gen è sotto la soglia pratica**: meglio meno giorni con più budget che due mesi di consegna inutile.
- I video possono durare fino a 3 minuti, ma **nel feed Shorts si vedono solo i primi 60 secondi**, con un rimando alla pagina di visione a 50 secondi.

---

## 7. Igiene di un account ereditato

Ordine di controllo che fa emergere i problemi:

1. **Tagging automatico** e **applicazione automatica dei consigli**.
2. **Quale conversione è primaria** e quali secondarie.
3. **Conversioni avanzate**, e in particolare quelle **per i lead**, spesso mai configurate.
4. **Collegamento GA4**.
5. **Elenco delle parole chiave escluse a livello di account**: se è vuoto, si stanno pagando clic sbagliati.
6. **Contatto per la protezione dei dati** (il pannello lo segnala con avviso).
7. **Campagne vecchie in pausa**: non si riaccendono mai a scatola chiusa, ma il loro **rapporto sui termini di ricerca** è oro. Sono anni di query già pagate, ed è la base migliore per costruire keyword ed esclusioni di una campagna nuova, molto meglio di una lista immaginata.
8. **Segmenti di pubblico per il remarketing**: esistono? Superano la soglia minima di membri attivi?
9. **Modello di attribuzione** e coerenza fra campagne.

---

## 8. Search: cosa non fare

- Accendere la generica su un account senza conversioni.
- Impostare un CPA target prima di avere dati.
- Riattivare una campagna vecchia perché "c'è già": geografia, keyword e pagina di destinazione sono quasi sempre di un altro progetto.
- Giudicare una campagna Search di agosto con i criteri di settembre: **la domanda è stagionale, l'asta anche**.
- Aspettarsi che Search porti volume su una nicchia dove le ricerche non esistono: se il volume non c'è, la campagna che intercetta il **problema** (e non il prodotto) diventa la principale.

---

## Fonti (verificate 11/08/2026)

[Tipi di corrispondenza 2026](https://www.stackmatix.com/blog/google-ads-keyword-match-types-guide) · [Generica e Smart Bidding, guida ufficiale](https://support.google.com/google-ads/answer/10195720?hl=en) · [Controllo della spesa e corrispondenze](https://infrontmarketing.ca/blog/google-ads/google-ads-match-types-in-2026-how-to-control-spend-without-killing-scale/) · [Regole che contano nel 2026](https://www.groas.com/post/google-ads-best-practices-2026-rules-that-actually-matter) · [Demand Gen, specifiche asset](https://support.google.com/google-ads/answer/13704860) · [YouTube Shorts, specifiche](https://support.google.com/google-ads/answer/16041697?hl=en) · [Formati e dimensioni Google Ads](https://support.google.com/google-ads/answer/13676244?hl=en)

