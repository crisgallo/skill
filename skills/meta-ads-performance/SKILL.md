---
name: "meta-ads-performance"
description: "Regole operative verificate per montare, ottimizzare e diagnosticare campagne Meta Ads (Facebook e Instagram). Usare ogni volta che si lavora su Gestione inserzioni: struttura campagne, fase di apprendimento, budget, pubblici, attribuzione, Conversions API, formati e aree di sicurezza. Serve anche per leggere un pannello altrui e capire cosa è rotto."
---

# Meta Ads: regole operative

**Ultima verifica delle fonti: 12 agosto 2026.**

🔄 **Cosa è cambiato il 12/08/2026, e invalida una regola che era scritta qui:** la **misurazione aggregata degli eventi (AEM) per il web non si configura più**. Fonte ufficiale Meta, articolo *Informazioni sulla misurazione aggregata degli eventi*: non serve più dare priorità a 8 eventi di conversione per dominio, la tab *Misurazione aggregata degli eventi* **è stata rimossa** da Gestione eventi, non serve più selezionare un dominio di conversione creando una campagna, e **la verifica del dominio non è più richiesta per la configurazione degli eventi** (resta utile per altri motivi). Verificato anche sul pannello: le tab di Gestione eventi sono Panoramica, Testa gli eventi, Diagnostica, Cronologia, Impostazioni, e di AEM non c'è traccia né lì né nel pannello del dominio.

---

## 0. Manutenzione di questa skill (leggere per primo)

Meta cambia le regole più volte l'anno, e nel 2026 ne ha già cambiate tre che invalidavano pratiche consolidate. Quindi:

1. **Prima di applicare una soglia numerica su un account che spende, ricontrollala.** Se la verifica ha più di **due o tre mesi**, si rifà una ricerca sulle fonti prima di toccare il pannello.
2. **Quando una fonte smentisce una regola scritta qui, si aggiorna la skill nello stesso momento**, non "poi". Una skill che invecchia in silenzio è peggio di nessuna skill, perché dà sicurezza falsa.
3. Aggiornando, si **riscrive la data** in cima e si annota **cosa è cambiato e da quando**: serve a capire quali dati storici sono confrontabili e quali no.
4. Segnali che è ora di ricontrollare: il pannello mostra etichette o opzioni che qui non sono descritte; **un'impostazione che dovrebbe esserci non si trova** (è il segnale che ha smascherato la rimozione di AEM); i numeri di un report cambiano senza che nessuno abbia toccato niente.
5. ⚠️ **Il Centro assistenza di Meta si contraddice.** Diverse pagine descrivono ancora gli otto slot AEM come se esistessero. La pagina autorevole è quella sulle *modifiche alle campagne per le conversioni sul sito web*. In caso di conflitto fra due pagine ufficiali, vince **quello che si vede nel pannello**.

---

## 1. La fase di apprendimento è il centro di tutto

**Soglia: 50 eventi di ottimizzazione a settimana per gruppo di inserzioni.** Non per campagna, per gruppo. Sotto quella soglia il gruppo resta in *Apprendimento limitato* e la consegna è instabile.

Non è un numero magico: è il volume minimo perché l'algoritmo prenda decisioni statisticamente sensate. Conta anche la **costanza** del segnale, non solo il totale.

### Cosa RESETTA l'apprendimento (verificato 08/2026)

- modificare il **budget di oltre il 20-25%**
- cambiare l'**evento di ottimizzazione**
- toccare il **targeting**
- **aggiungere o togliere inserzioni** dal gruppo
- cambiare **strategia di offerta**
- mettere in **pausa il gruppo per 7 giorni o più**

### Regole di condotta che ne derivano

1. **Quattordici giorni senza toccare niente** dopo il lancio. Le decisioni su struttura, creatività e targeting si prendono *prima*, con una lista di controllo, non aggiustando in corsa.
2. Se una modifica è inevitabile, **falle tutte insieme**: un reset solo invece di tre.
3. Le variazioni di budget si fanno **a scaglioni sotto il 20%**, distanziate.
4. *Apprendimento limitato* non si cura aggiungendo budget a pioggia: si cura **consolidando**. Unire i gruppi che si sovrappongono fa confluire gli eventi in un posto solo.

---

## 2. Struttura: nel 2026 si consolida, non si segmenta

La direzione è **pochi gruppi grandi con molte creatività dentro**, non venti gruppi per venti interessi.

- **1-3 gruppi di inserzioni per campagna.**
- Con budget totale **sotto i 50 $ al giorno: non più di 3-4 gruppi in tutto l'account.** Con 20 €/giorno significa **uno o due gruppi, punto.**
- Meglio più creatività dentro lo stesso gruppo che più gruppi con poche creatività.
- Il budget a livello di campagna (CBO) è il default dal 2024 ed è la scelta pratica sugli account piccoli: evita di spostare soldi a mano.

**L'errore classico su budget piccoli:** dieci pubblici da 5 € al giorno. Ogni gruppo resta sotto la soglia, nessuno esce dall'apprendimento, e si paga il prezzo dell'instabilità su tutti.

---

## 3. Attribuzione: cosa è cambiato nel 2026

- **Standard oggi: 7 giorni dal clic + 1 giorno dalla visualizzazione.**
- **Gennaio 2026:** le finestre *7 giorni dalla visualizzazione* e *28 giorni* sono state **rimosse**. Chi le usava ha visto crollare le conversioni attribuite dal 15-30% (7d view) al 30-40% (28d).
- **Marzo 2026:** ridefinito cosa conta come clic. Le interazioni social sono state spostate in una categoria a parte, *engage-through*, con finestra di **1 giorno**.

**Conseguenza pratica:** confrontare periodi a cavallo di quelle date senza saperlo produce cali che sembrano performance e sono contabilità. Prima di dire "è calato", verificare che la finestra sia la stessa.

⚠️ Su un account vecchio le finestre sono spesso **disomogenee fra campagne** (1 giorno contro 7). Uniformarle prima di confrontare qualsiasi cosa.

---

## 4. Pixel e Conversions API

**Pixel da solo non basta più.** Lo standard è **Pixel + CAPI insieme**: gli eventi lato server aggirano i limiti del browser, e alzano l'**Event Match Quality**.

- **EMQ sotto 6: la finestra di attribuzione che scegli conta poco**, perché una quota alta di conversioni è modellata e non osservata.
- In Gestione eventi, la colonna **Metodo di collegamento** dice la verità: se su tutti gli eventi c'è scritto solo **Browser**, la CAPI non esiste. Quando è a posto, dice *Browser e server*.
- Vie possibili: container server-side (Stape e simili hanno piani d'ingresso) oppure integrazione diretta lato CMS.
- 🔴 **Browser e server devono mandare lo stesso nome evento e lo stesso `event_id`**, altrimenti Meta conta due volte invece di deduplicare. Se un container server-side riscrive il nome evento con una trasformazione, quella trasformazione va cambiata **nello stesso giro** in cui si cambia il nome lato browser: due pubblicazioni distanti lasciano una finestra in cui gli eventi non deduplicano.
- ✅ **AEM: non c'è più niente da configurare (12/08/2026).** Otto slot per dominio, priorità degli eventi, insiemi di valori e dominio di conversione in campagna: tutto rimosso. Gli eventi vengono elaborati da Meta senza intervento. Quindi la vecchia raccomandazione "verifica il dominio e imposta la priorità prima di spendere" **non vale più**: aggiungere un nome evento nuovo non consuma nessuno slot e non richiede riordini.
- ⚠️ **Se in un pannello la tab AEM c'è ancora**, quell'account non è stato migrato: lì la priorità conta e le vecchie regole valgono. Si guarda, non si presume.

---

## 5. Pubblici

- **Soglia minima di utilizzo: circa 1000 persone.** Sotto, il pubblico non è pubblicabile e non genera lookalike. Un lookalike "non disponibile" quasi sempre significa **fonte troppo magra**, non un errore.
- Le fonti **non sono equivalenti**: su un profilo con poco traffico web, le **interazioni con il profilo Instagram a 365 giorni** possono valere decine di migliaia di persone mentre i visitatori del sito a 180 giorni restano sotto mille. **Guardare i numeri prima di decidere su cosa poggiare il retargeting.**
- Le interazioni sono un bacino **largo ma tiepido**: chi ha guardato un profilo non è chi vuole comprare. Il lookalike all'1% serve a stringere.
- Un pubblico da sito appena creato **si popola con lo storico già raccolto dal pixel**: crearlo oggi con finestra 180 giorni vale come averlo avuto sei mesi fa. **Crearli presto costa zero e vale molto.**
- Finestre: 180 giorni per i visitatori, 365 per interazioni e lead. Le finestre corte (30 giorni) si svuotano nei periodi di silenzio editoriale.
- Nei pubblici da URL mettere **anche i vecchi indirizzi** delle pagine che hanno cambiato slug: chi è passato prima del redirect ha il vecchio URL nel pixel.

### Trappole del pannello

- Creando un pubblico da profilo Instagram o pagina Facebook, **l'origine preselezionata può essere di un altro cliente** collegato al Business Manager. Va sempre controllata.
- **Non si elimina un pubblico se qualcuno ci ha costruito sopra un lookalike:** prima i simili, poi le fonti.
- **I pubblici salvati non si eliminano insieme ai personalizzati:** due operazioni separate.
- Eliminando un pubblico usato da una campagna, Meta chiede se mettere in pausa la campagna. **Rispondere consapevolmente**: quel messaggio è anche un modo per scoprire campagne attive che i filtri non mostravano.

---

## 6. Formati e aree di sicurezza

- **Marzo 2026: Meta ha unificato Facebook Stories, Facebook Reels, Instagram Stories e Instagram Reels in un'unica area di sicurezza 9:16.** Un solo verticale corretto vale per tutti e quattro.
- **Verticale 1080x1920:** coperti il **14% in alto**, il **35% in basso** (670 px) e il **6% per lato**. L'area utile è poco più di metà schermo.
- Nella zona coperta ci va **solo estensione di sfondo**: mai testo, logo o richiamo all'azione.
- Feed: **4:5 (1080x1350)** è il formato che occupa più schermo; l'1:1 come secondo asset.
- I video vanno pensati **muti**: in feed l'audio parte spento.
- Se un elemento di firma (nome del prodotto, dominio, richiamo) sta ai bordi del fotogramma, nel verticale finisce **sotto l'interfaccia**. Va ancorato all'area sicura, non al bordo.

---

## 7. Come si legge un pannello che non si conosce

Ordine di lettura che fa emergere i problemi veri:

1. **Campagne con l'interruttore acceso**, anche se in bozza: sono spese pronte a partire. ⚠️ Spegnere una campagna **non spegne i suoi gruppi di inserzioni**: si controllano anche quelli.
2. **Filtro sulle inserzioni attive** per vedere cosa sta davvero spendendo. Non è esaustivo: una campagna può risultare attiva altrove e non comparire lì.
3. **Modifiche non pubblicate** in sospeso, spesso con errori dentro.
4. **Gestione eventi**: quali eventi arrivano, da quale metodo, con quale EMQ, e **quali sono fermi da settimane** (di solito rotti da un restyling del sito e mai riparati).
5. **Pubblici**: dimensioni, non nomi.
6. **Verifica del dominio**: utile per l'autorità sul dominio, **non più necessaria per la configurazione degli eventi** (vedi sezione 4).
7. **Nomi e finestre di attribuzione**: se sono disomogenei, nessun confronto storico regge.

---

## 8. Cosa non fare mai

- Ottimizzare per **copertura** quando lo scopo è costruire un bacino di retargeting: la copertura non lascia un pubblico su cui tornare, il traffico sì.
- Spendere su **pubblico freddo B2B** senza aver prima verificato come si comporta il traffico freddo già acquistato: spesso ha tassi di coinvolgimento ridicoli rispetto ad altre fonti.
- Confrontare periodi con finestre di attribuzione diverse.
- Toccare una campagna durante l'apprendimento perché "non sta andando".
- Giudicare una campagna di costruzione bacino sui lead: misura la cosa sbagliata.
- **Dichiarare un prerequisito che non hai verificato sul pannello corrente.** Il 12/08/2026 la priorità AEM è stata data per necessaria basandosi su questa skill: non esisteva più.

---

## Fonti (verificate 11/08/2026, più l'aggiornamento AEM del 12/08/2026)

[AEM, fonte ufficiale Meta: niente più priorità a 8 eventi, tab rimossa, verifica del dominio non più richiesta](https://www.facebook.com/business/help/721422165168355) · [Learning phase, cosa la resetta](https://withblip.com/blog/meta-ads-learning-phase-bulk-editing/) · [La regola delle 50 conversioni](https://www.pigeondigital.com/insight/facebook-ads-learning-phase-50-conversions-rule-2026) · [Struttura account 2026, CBO e consolidamento](https://creative-brackets.com/blog/meta-ads-account-structure-in-2026/) · [Advantage+ e budget piccoli](https://bir.ch/blog/advantage-plus-sales-campaigns-guide) · [Attribuzione 2026](https://jetfuel.agency/meta-ads-attribution-settings-2026/) · [Rimozione finestre gennaio 2026](https://www.dataslayer.ai/blog/meta-ads-attribution-window-removed-january-2026) · [CAPI ed EMQ](https://www.conversios.io/blog/meta-attribution-window-changes-2026-fix-your-tracking/) · [Aree di sicurezza](https://billo.app/blog/meta-ads-safe-zones/)

