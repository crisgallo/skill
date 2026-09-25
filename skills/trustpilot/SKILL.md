---
name: "trustpilot"
description: "Regole operative verificate per gestire Trustpilot su un e-commerce italiano: cosa sbloccano i piani e quanto costano, come si calcola il TrustScore, come si invitano i clienti senza violare le linee guida (AFS, integrazioni, API, niente gating né incentivi), come si risponde e si segnala una recensione, Consumer Warning, TrustBox e rich snippet, Google Seller Ratings, direttiva Omnibus e sanzione AGCM, cosa mettere nel report mensile. Usala ogni volta che si parla di recensioni, punteggio, stelline, inviti, widget, valutazioni del venditore su Google Ads o di come rispondere a una recensione negativa, anche se Trustpilot non viene nominato."
---

# Trustpilot: regole operative

**Ultima verifica delle fonti: 25 settembre 2026.**

## 0. Manutenzione di questa skill (leggere per primo)

1. **Finestra di freschezza: tre mesi** per le regole (linee guida, piani, prezzi), **un mese** per i prezzi se c'è un rinnovo in vista. Trustpilot ha cambiato linee guida (v7.2, giugno 2026), termini (v9.0, 23/06/2026), piani (Starter, 2026) e app Shopify (giugno-luglio 2026) nello stesso anno.
2. **Quando una fonte smentisce una regola scritta qui si aggiorna la skill nello stesso turno**, si riscrive la data in cima e si annota cosa è cambiato e da quando.
3. Due metà da tenere distinte: **conoscenza di dominio** (verificata sulle fonti ufficiali, con link inline) e **meccanica del pannello** (sez. 15: si impara sbagliando e si scrive qui la prima volta, con data).
4. Dove si guardano i cambiamenti: [Releases and updates](https://business.trustpilot.com/blog/releases-and-updates) · [Product updates](https://business.trustpilot.com/blog/releases-and-updates/product-updates) · [Guidelines for Businesses (versione corrente)](https://corporate.trustpilot.com/legal/for-businesses/guidelines-for-businesses) · [Action we take](https://corporate.trustpilot.com/legal/for-everyone/action-we-take/mar-2026) · [Newsroom](https://corporate.trustpilot.com/press/news) · [Store ratings Google Ads (2375474)](https://support.google.com/google-ads/answer/2375474?hl=it).
5. ⚠️ **Il centro assistenza è migrato da support.trustpilot.com a help.trustpilot.com** (Salesforce): le pagine si rendono solo con JavaScript e **non si leggono via fetch**. Le regole tratte da lì in questa skill vengono dagli estratti dei motori di ricerca e vanno **ricontrollate a mano nel browser** prima di essere usate contro un cliente.

---

## 1. Cosa si paga e cosa sblocca (la regola che costa di più)

**Senza piano a pagamento non si può mostrare TrustScore né stelline sul sito o nelle inserzioni.** Le Legal Brand Guidelines **v3.0 (settembre 2026)** dicono che sul Free si può citare Trustpilot solo "in testo semplice, con un link alla propria pagina profilo Trustpilot" (esempio ufficiale: "See our reviews on Trustpilot") e usare il Review Collector Widget per raccogliere recensioni; **vietati "loghi, Star Rating o grafiche a stelle, TrustScore, Star Label, Category Ranking o qualsiasi widget che mostri recensioni o valutazioni"** ([Legal Brand Guidelines v3.0, set 2026](https://corporate.trustpilot.com/legal/for-businesses/legal-brand-guidelines/sept-2026); sostituisce la v2.0 del feb 2023). Un e-commerce Free che mette "4,6 su Trustpilot" nell'annuncio Meta è in violazione.

Piani come esposti il 24/09/2026 (prezzo per dominio, al mese, fatturazione annuale; ogni dominio si paga a parte; contratti a 12 mesi prepagati) ([plans USD](https://business.trustpilot.com/plans), [plans IT in EUR](https://it.business.trustpilot.com/plans)):

| Piano | Prezzo | Inviti/mese | TrustBox | Utenti | Domini |
|---|---|---|---|---|---|
| Free | 0 | 50 | nessuno | 1 | 1 |
| Starter | 79 €/mese (99 $) | 100 | 2 | 1 | 1 |
| Plus | 189 €/mese (319 $) | 300 | 10 | 3 | fino a 3 |
| Premium | 479 €/mese (799 $) | 1.000 | 21 | 10 | illimitati |
| Enterprise | su preventivo | illimitati | 23 | 1.000 | illimitati |

- **Starter è solo per clienti nuovi con ricavi fino a 5 milioni di dollari** e include solo le integrazioni e-commerce; da Plus in su tutte le integrazioni. **Recensioni di prodotto, recensioni per sede e accesso API sono add-on**, non inclusi nel listino ([pricing](https://business.trustpilot.com/pricing)). Il prezzo dell'add-on non è pubblicato: [DA VERIFICARE] con il commerciale prima di promettere rich snippet di prodotto.
- Plus ha una **prova gratuita di 14 giorni** (pagina plans USD, 24/09/2026); Starter no.
- ⚠️ Prezzo EUR e USD non sono una conversione: sono due listini. Si cita quello della pagina italiana e si allega lo screenshot con data.
- 🔴 **Rinnovo automatico di altri 12 mesi; disdetta almeno 30 giorni prima della scadenza**, via cancellation@trustpilot.com o dal pannello ([Terms of Use and Sale for Businesses v9.0, 23/06/2026](https://corporate.trustpilot.com/legal/for-businesses/terms-of-use-and-sale-for-businesses/jun-2026)). Si mette la scadenza in calendario il giorno della firma.
- Alla fine del piano il profilo resta sul Free e **le recensioni restano pubbliche per sempre**, anche se si chiude l'account (stessi Termini). Non esiste "togliamo Trustpilot".
- **Gli inviti oltre la quota**: i Termini non dicono cosa succede. [DA VERIFICARE] sul pannello se vengono bloccati o messi in coda.

---

## 2. TrustScore: come si calcola e cosa serve per un 4,x

**Il TrustScore non è la media delle stelle.** Tre fattori, dichiarati da Trustpilot ([TrustScore and star rating explained](https://help.trustpilot.com/s/article/TrustScore-and-star-rating-explained?language=en_US), non leggibile via fetch; contenuto confermato da estratti di ricerca e dal mirror [trustratings.com](https://trustratings.com/help/trustscore-explained)):

1. **Media bayesiana**: nel calcolo entrano sempre **7 recensioni fittizie da 3,5 stelle**. Un profilo con una sola recensione da 1 stella mostra 3,2, non 1,0; con una sola da 5 stelle mostra circa 3,65, non 5,0.
2. **Recenza**: le recensioni recenti pesano di più. Il mirror riporta "una recensione di 6 mesi fa pesa la metà di una di oggi": **regola riportata da terzi, non verificata sulla pagina ufficiale**.
3. **Frequenza**: il punteggio si ricalcola a ogni recensione; con un flusso regolare è più stabile, con raffiche e vuoti oscilla.

**Arrotondamento delle stelle**: il TrustScore (1,0–5,0, un decimale) si mostra arrotondato alla mezza stella più vicina con regola matematica standard: **4,3–4,7 → 4,5 stelle; da 4,8 → 5 stelle; 3,8–4,2 → 4 stelle** (stessa fonte). Le etichette verbali (Eccellente, Ottimo, Nella media, Scarso, Pessimo) seguono le fasce di stelle: [DA VERIFICARE] le soglie esatte sul pannello.

**Ordine di grandezza per un 4,x** (calcolo dalla formula dichiarata, senza pesi temporali: **stima, non numero Trustpilot**): con sole recensioni a 5 stelle servono **circa 3** per mostrare 4,0, **circa 7** per 4,3 (4,5 stelle), **circa 46** per 4,8 (5 stelle). Con il 10% di recensioni a 1 stella la media reale si ferma a 4,6; con il 20% a 4,2. **La quota di recensioni a 1-2 stelle decide il punteggio più del numero di recensioni a 5.**

**TrustScore e numero di recensioni sono due cose diverse e vanno riportate separate**: 4,7 con 30 recensioni e 4,7 con 3.000 non valgono uguale né per il consumatore né per Google (sez. 9). Le recensioni rimosse per violazione escono dal conteggio; le aziende "non possono mai pagare per rimuovere recensioni" ([corporate.trustpilot.com/trust](https://corporate.trustpilot.com/trust)).

---

## 3. Chi si invita: le regole che fanno scattare le sanzioni

Fonte unica: [Guidelines for Businesses v7.2, giugno 2026](https://corporate.trustpilot.com/legal/for-businesses/guidelines-for-businesses/jun-2026).

- **Si invita chi ha avuto un'esperienza reale, un invito per esperienza.** Non i lead, non chi ha solo chiesto un preventivo.
- ⛔ **Niente review gating / cherry-picking**: vietato "invitare solo chi si sa che ha avuto un'esperienza positiva" e vietato "impostare gli inviti a uno stadio del percorso cliente raggiunto solo da chi ha avuto una buona esperienza". Si invita **tutti allo stesso modo e nello stesso punto del percorso**, ordini con reso e reclami compresi. L'invito che parte "solo dopo la consegna confermata senza ticket" è gating.
- ⛔ **Niente incentivi**: sconti, codici promo, estrazioni, rimborsi, omaggi "o qualsiasi altro beneficio" collegati a scrivere o modificare una recensione. Vale anche per "lascia una recensione e ti rimborsiamo la spedizione".
- ⛔ **Niente recensioni false**, né scritte in casa né commissionate, né richieste a dipendenti e amici.
- ⛔ **Niente uso distorto della segnalazione**: "si segnalano le recensioni a 5 stelle per gli stessi motivi per cui si segnalano quelle a 1 stella" (sez. 6).
- **Consenso**: i Termini v9.0 mettono in capo all'azienda la conformità legale del contenuto degli inviti e i consensi privacy, e avvertono che in alcune giurisdizioni l'invito può essere marketing con consenso preventivo. In Italia l'invito post-acquisto va coperto da informativa privacy che nomini Trustpilot come destinatario e dalla base giuridica scelta con il DPO o il legale: [DA VERIFICARE] la posizione del Garante sugli inviti a recensire, non trovata su fonte ufficiale in questa revisione.

---

## 4. Come si invita: AFS, integrazioni, API, ritardo, mittente

- **Automatic Feedback Service (AFS)** è il metodo base: si mette l'indirizzo Trustpilot univoco in **BCC sull'email transazionale** (conferma d'ordine o spedizione); Trustpilot legge nome ed email del destinatario e programma l'invito secondo il ritardo impostato. Le recensioni raccolte così hanno l'etichetta **Verified**. **È incluso nel Free** (50 inviti/mese) ([AFS](https://help.trustpilot.com/s/article/How-to-use-Automatic-Feedback-Service-AFS?language=en_US), [What is AFS](https://help.trustpilot.com/s/article/What-is-Automatic-Feedback-Service?language=en_US); entrambe non leggibili via fetch, contenuto da estratti). Se il sistema non ha un campo BCC, si manda un'email trigger separata con lo snippet strutturato ([AFS senza BCC](https://help.trustpilot.com/s/article/How-to-use-Automatic-Feedback-Service-without-a-BCC-field?language=en_US)).
- ⚠️ **In BCC va una sola email per ordine**: se si mette l'indirizzo AFS sia sulla conferma sia sulla spedizione si invita due volte la stessa esperienza (violazione sez. 3) e si bruciano inviti a quota.
- **Integrazioni e-commerce** ([WooCommerce](https://help.trustpilot.com/s/article/Trustpilots-WooCommerce-integration?language=en_US), [PrestaShop](https://help.trustpilot.com/s/article/Trustpilots-PrestaShop-integration?language=en_US), [app Shopify](https://help.trustpilot.com/s/article/Trustpilot-Shopify-app?language=en_US)): invitano al cambio di stato dell'ordine, aggiungono TrustBox, sincronizzano il catalogo per le recensioni di prodotto. **Starter le include; il Free ha "integrazioni limitate"** (sez. 1). 🔴 **App Shopify rifatta il 29/06/2026: widget e impostazioni della vecchia app "Trustpilot Reviews" (legacy) non migrano da soli**; si ricollega l'account, si riconfigura l'automazione degli inviti e si rimettono i widget dal Theme Editor ([29/06/2026](https://business.trustpilot.com/blog/releases-and-updates/shopify), [10/07/2026](https://business.trustpilot.com/blog/releases-and-updates/trustpilot-shopify-upgrade)). Data di spegnimento della legacy: non pubblicata, [DA VERIFICARE].
- **Invitation API**: `POST https://invitations-api.trustpilot.com/v1/private/business-units/{businessUnitId}/email-invitations` con `consumerEmail`, `referenceNumber`, `templateId`, `senderEmail`, almeno uno fra `serviceReviewInvitation` e `productReviewInvitation`, `preferredSendTime` in UTC; autenticazione OAuth business user (client credentials con header `x-business-user-id` di un Admin/Manager). Endpoint `invitation-links` per link univoci ([Invitation API](https://developers.trustpilot.com/invitation-api)). L'accesso API è un **add-on** (sez. 1). Se si omettono `senderEmail`, `templateId`, `preferredSendTime` valgono le impostazioni del pannello ([Trigger invitations using APIs](https://help.trustpilot.com/s/article/Trigger-invitations-using-Trustpilot-APIs?language=en_US)).
- **Ritardo**: si imposta in Impostazioni inviti (per-integrazione: "Send delay"); l'AFS mette in coda "qualche giorno dopo". Numero di default non verificato: [DA VERIFICARE] sul pannello. Regola operativa: invito **dopo la consegna prevista**, non alla conferma d'ordine, e uguale per tutti (sez. 3). Dall'aprile 2026 l'**Invitation Optimizer** fa A/B test su ritardo e template ([Product updates aprile 2026](https://business.trustpilot.com/blog/releases-and-updates/product-updates)); piano richiesto non dichiarato.
- **Mittente**: il **sender email personalizzato richiede un piano a pagamento** e un **record SPF** corretto sul dominio, altrimenti l'invito resta in errore ([Invitation status overview](https://help.trustpilot.com/s/article/Invitation-status-overview?language=en_US), estratto). Si controlla SPF/DKIM con chi gestisce il DNS prima di attivarlo.
- **Etichette** ([review labels](https://help.trustpilot.com/s/article/About-Trustpilots-review-labels?language=en_US), estratti): **Verified** = invito automatico legato a una transazione (AFS, integrazione, API email) oppure documentazione fornita dal recensore; **Invited** = invito da file, Business Generated Link, Invitation Link API, in-app collector; **Unprompted** = organica, basic link, link univoco, Review Collector. ⚠️ **Le recensioni da Basic Invitation (link nella propria newsletter) non sono Verified e non contano per Google Seller Ratings** (sez. 9). Su inviti manuali/file le finestre d'accesso sono temporanee e la quota torna a quella del piano quando scadono ([manual invitation access](https://help.trustpilot.com/s/article/I-lost-access-to-manual-invitations?language=en_US), estratto).
- Promemoria: il follow-up è dichiarato portare "in media il 35% di recensioni in più" ([review invitations](https://business.trustpilot.com/features/review-invitations)): numero marketing Trustpilot, non misurato sul cliente.

---

## 5. Rispondere alle recensioni

- Si può rispondere solo con profilo rivendicato; **si può rispondere anche dal Free** ([Can businesses reply](https://help.trustpilot.com/s/article/Can-businesses-reply-to-reviews?language=en_US), estratto).
- **La risposta è pubblica**, sotto la recensione sul profilo, e resta visibile: non è un messaggio privato al cliente.
- ⛔ **Niente dati personali, minacce, linguaggio aggressivo: Trustpilot rimuove la risposta** (Guidelines v7.2). Quindi mai numero d'ordine completo, indirizzo, nome e cognome se il recensore non li ha scritti.
- Regola operativa per il collaboratore social/CRM: rispondere a tutte le 1-3 stelle **entro 48 ore lavorative** (regola interna, non numero Trustpilot), in italiano, senza template identico copiato dieci volte; un fatto, una scusa se dovuta, un canale di contatto generico (email assistenza), niente promessa di rimborso pubblica. Alle 5 stelle si risponde a campione, non è obbligatorio.
- **Non si risponde chiedendo di alzare le stelle** e non si offre nulla in cambio della modifica: è un incentivo (sez. 3). Il recensore può modificare la recensione da solo dopo il chiarimento.
- Se la recensione viola le linee guida per i recensori, **si segnala invece di rispondere** (sez. 6).

---

## 6. Segnalare (flag) una recensione

- Motivi ammessi ([For which reasons can businesses flag reviews](https://help.trustpilot.com/s/article/For-which-reasons-can-businesses-flag-reviews?language=en_US), non leggibile via fetch; [Action we take](https://corporate.trustpilot.com/legal/for-everyone/action-we-take/mar-2026)): contenuto dannoso o illegale (odio, minacce, terrorismo), dati personali, pubblicità/promozione, **"non basata su un'esperienza reale"**, recensione all'azienda sbagliata.
- **Durante l'indagine la recensione resta online**, tranne quelle segnalate come dannose o illegali, che vengono nascoste. Se viola ed è correggibile, al recensore viene chiesto di modificarla (può essere nascosta temporaneamente); se non risolve, resta offline ([misuse of flagging tool](https://help.trustpilot.com/s/article/What-happens-if-businesses-misuse-the-review-flagging-tool?language=en_US), estratto).
- Per "non basata su esperienza reale": il software di rilevazione decide per primo; se l'azienda non è d'accordo, **risponde all'email della decisione con documentazione** (nessun ordine nel periodo, riferimenti a prodotti/sedi inesistenti); se Trustpilot concorda "sposta la recensione offline e avvisa il recensore", che può controbattere con prove ([Changes to reported reviews](https://business.trustpilot.com/blog/build-trusted-brand/changes-to-reported-reviews)). Prima si usa **Find Reviewer** per cercare il cliente nel proprio database.
- ⛔ **Non si segnala per il tono, per "è ingiusta" o per far sparire le 1 stella.** Segnalare troppo in fretta, per motivi sbagliati o in modo sbilanciato sulle negative è misuso e porta a warning, poi a restrizioni della funzione (sez. 7).
- Tempi di risposta: 1-3 giorni sui piani a pagamento, 1-2 settimane sul Free: **regola empirica di terzi, non numero Trustpilot** ([reverbico](https://reverbico.com/blog/remove-trustpilot-reviews/)).

---

## 7. Cosa fa scattare il banner: Consumer Alert e Consumer Warning

Scala di enforcement ([Action we take, marzo 2026](https://corporate.trustpilot.com/legal/for-everyone/action-we-take/mar-2026)): email educativa → **warning** formale → **cease-and-desist** → **restrizioni** (es. blocco della segnalazione o della modifica del profilo) → **Consumer Warning con TrustScore nascosto** → azione legale o segnalazione alle autorità.

- 🔴 **Consumer Warning**: banner pubblico che dice che l'azienda ha abusato della piattaforma; TrustScore nascosto; i piani a pagamento cessano e l'account scende a funzioni minime (rispondere e segnalare); dura **di norma 6 mesi**, con revisione periodica, e non viene tolto finché il misuso non è cessato. Cause: recensioni false (rimosse subito), incentivi, inviti selettivi, uso distorto della segnalazione.
- **Consumer Alert** è un'altra cosa: avviso informativo (settore ad alto rischio, indagine di un'autorità, attenzione mediatica) che **non implica misuso**. Nel report al cliente si distinguono.
- Regola operativa: **se arriva un'email educativa o un warning, si ferma tutto e si avvisa il consulente lo stesso giorno**; non si continua "finché non ci beccano".

---

## 8. TrustBox, dati strutturati, rich snippet

- I TrustBox sono i widget ufficiali; **servono un piano a pagamento** (2 su Starter, sez. 1). Sul sito "si usa un widget così che ciò che il consumatore vede sia live e accurato": ⛔ **vietato sostituire un widget con un'immagine statica**, vietati "widget, plug-in, estensioni o applicazioni non autorizzati" per mostrare contenuti Trustpilot, ⛔ **vietati i widget Product Score in home page, in landing page o accanto a un prodotto non correlato** ([Legal Brand Guidelines v3.0, set 2026](https://corporate.trustpilot.com/legal/for-businesses/legal-brand-guidelines/sept-2026)).
- 🔴 **Le stelline delle recensioni di servizio (azienda) non danno rich snippet sul proprio sito.** Da settembre 2019 Google esclude le "self-serving reviews": se l'entità recensita controlla le recensioni, le pagine con markup `Organization` o `LocalBusiness` non sono idonee, **anche tramite widget di terzi** ([review snippet](https://developers.google.com/search/docs/appearance/structured-data/review-snippet), [Search Central blog 09/2019](https://developers.google.com/search/blog/2019/09/making-review-rich-results-more-helpful)). Chi promette "stelline in SERP con il TrustBox aziendale" promette una cosa che Google non fa dal 2019.
- ✅ **Le stelline in SERP si ottengono solo con le recensioni di prodotto** (`Product` + `AggregateRating` con `ratingValue` e `ratingCount`/`reviewCount`, decimali con il punto). I TrustBox di prodotto "SEO" portano il JSON-LD incorporato; **non si aggiunge markup proprio dello stesso tipo** (duplicato), **non si ritarda il caricamento del widget** e non lo si nasconde in tab o "mostra altro"; **SKU e titolo devono coincidere con il feed Merchant Center** ([Get rich snippets with product review TrustBox](https://help.trustpilot.com/s/article/Get-rich-snippets-with-product-review-TrustBox-widgets?language=en_US), estratti). Recensioni di prodotto = add-on (sez. 1). Google non garantisce la visualizzazione.
- ⛔ Google vieta di aggregare recensioni da altri siti nel proprio markup e le recensioni incentivate non dichiarate (stessa pagina Google).
- Dal 13/08/2026 Trustpilot ospita **Product Review Pages** sul proprio dominio (in beta, "aziende idonee"; dichiara +1.548% citazioni AI nella prima settimana: **numero marketing, non riproducibile**) ([13/08/2026](https://business.trustpilot.com/blog/releases-and-updates/spotlight-product-ai-recommended-search-era)).

---

## 9. Google Seller Ratings (oggi "Valutazioni negozio") via Trustpilot

- **Numero Google**: la maggior parte dei commercianti ottiene la valutazione dopo **100 o più recensioni idonee**, raccolte **negli ultimi 24 mesi**, **per paese**; negli annunci di testo serve **media almeno 3,5 stelle**; Trustpilot è fra gli aggregatori accettati; si mostra su Rete di ricerca e YouTube, e non serve Merchant Center per la Ricerca ([2375474](https://support.google.com/google-ads/answer/2375474?hl=it)).
- ⚠️ **La FAQ Trustpilot dice ancora "100 recensioni verificate per paese negli ultimi 12 mesi"** ([Trustpilot and Google store ratings FAQ](https://help.trustpilot.com/s/article/Trustpilot-and-Googles-store-ratings-FAQ?language=en_US), estratto): la pagina Google fa fede (24 mesi); si pianifica comunque sui 12 per stare sul sicuro. Le recensioni per l'Italia contano solo per la valutazione in Italia.
- **Contano solo le recensioni verificate** (AFS, integrazioni, API email); **le Basic Invitation non contano** (stessa FAQ). Se il collaboratore raccoglie con il link in newsletter, il conteggio per Google non cresce.
- Non c'è un collegamento account da fare: Trustpilot passa i dati a Google; comparsa tipica **2-6 settimane** dopo il raggiungimento dei requisiti, a discrezione di Google, che **non garantisce** la visualizzazione (stessa FAQ). Controllo: `https://www.google.com/shopping/ratings/account/lookup?q=dominio.it`.
- In Google Ads compare come asset automatico (stelle, numero di valutazioni, eventuale qualificatore come tempo di consegna). Non si scrivono stelline né "4,7★" nel testo dell'annuncio: la policy editoriale Google vieta simboli usati in modo "gimmicky" ([6021546](https://support.google.com/adspolicy/answer/6021546)); [DA VERIFICARE] l'applicazione al caso specifico prima di contestare un rifiuto.

---

## 10. Lato legale italiano (solo fonti ufficiali)

- **D.Lgs. 7 marzo 2023 n. 26** (recepimento direttiva Omnibus 2019/2161, in vigore dal **2 aprile 2023**) ha aggiunto al Codice del Consumo: l'obbligo di informare **se e come** si garantisce che le recensioni pubblicate provengano da consumatori che hanno davvero acquistato o usato il prodotto (art. 22, comma aggiunto dal decreto) e la pratica **in ogni caso ingannevole** di dichiarare che le recensioni provengono da consumatori reali **senza misure ragionevoli e proporzionate per verificarlo** (**art. 23, c. 1, lett. bb-ter**); vietato anche inviare o commissionare recensioni false ([Assonime 22/03/2023](https://www.assonime.it/attivita-editoriale/news/Pagine/News-22_03_2023.aspx), [Brocardi art. 23](https://www.brocardi.it/codice-del-consumo/parte-ii/titolo-iii/capo-ii/sezione-i/art23.html)). Sanzioni AGCM fino a 10 milioni di euro.
- 🔴 **AGCM, provvedimento n. 31878 del 17/03/2026 (PS12962, pubblicato 23/03/2026): 4 milioni di euro a Trustpilot Group Plc, Trustpilot A/S e Trustpilot S.r.l.** per pratica ingannevole (artt. 20, 21, 22, 23 c.1 lett. bb-ter): verifiche insufficienti anche sulle recensioni "Verified", strumenti a pagamento che permettono inviti selettivi, informazioni sulla meccanica della piattaforma frammentate (dark pattern) ([comunicato AGCM](https://www.agcm.it/media/comunicati-stampa/2026/3/PS12962), [provvedimento PDF](https://www.agcm.it/dotcmsCustom/tc/2031/3/getDominoAttach?urlStr=81.126.91.44%3A8080%2FC12560D000291394%2F0%2F43CEA3D8214A249AC1258DC30041B0F0%2F%24File%2Fp31878.pdf)). Trustpilot contesta e ha annunciato ricorso ([dichiarazione, terza parte](https://www.agenziagiornalisticaopinione.it/opinionews/trustpilot-replica-ad-agcm-contestiamo-la-decisione-e-presenteremo-il-ricorso-per-proteggere-trasparenza-e-affidabilita/)).
- **Conseguenza per l'e-commerce**: l'etichetta "Verified" di Trustpilot **non basta da sola** come "misura ragionevole e proporzionata" agli occhi dell'AGCM. Si scrive sul sito (pagina recensioni o note legali) **come** si raccolgono le recensioni: "inviti automatici inviati a tutti i clienti dopo ogni ordine tramite Trustpilot (AFS), nessun incentivo, nessuna selezione", e si conserva il log degli inviti. Non si scrive "recensioni verificate" sul sito senza descrivere il metodo.
- Le pagine Trustpilot sulle leggi UE ([New EU laws on reviews](https://help.trustpilot.com/s/article/New-EU-laws-on-reviews-What-they-mean-for-businesses-using-Trustpilot?language=en_US), 2022) non sono leggibili via fetch; le Guidelines v7.2 **non citano** la direttiva Omnibus. Nessuna "dichiarazione di conformità" ufficiale trovata dopo la sanzione: [DA VERIFICARE].

---

## 11. Report mensile: cosa si misura e cosa è vanity

Disponibilità analytics: dashboard base su tutti i piani; **selettore intervallo date da Plus**; **filtri e Analytics explorer su Premium ed Enterprise** ([Service reviews analytics](https://help.trustpilot.com/s/article/Service-reviews-analytics?language=en_US), estratto); Custom Dashboards, AI Search Analytics e In-App Review Collector dall'aprile 2026 (AI Search Analytics da Plus; Collector in-app da Plus, 1.000 clic/mese) ([Product updates](https://business.trustpilot.com/blog/releases-and-updates/product-updates), [plans IT](https://it.business.trustpilot.com/plans)). Sul Free si esporta a mano.

**Va nel report** (con intervallo di date esplicito):
1. TrustScore a fine mese **e** variazione sul mese precedente; numero di recensioni **nel mese**, separato dal totale storico.
2. **Distribuzione stelle del mese** e quota 1-2 stelle: è quello che muove il punteggio (sez. 2).
3. **Inviti inviati → recensioni ricevute** (tasso di conversione) e inviti in errore (SPF, quota esaurita).
4. Quota **Verified vs Unprompted** e avanzamento verso i 100 verified per l'Italia (sez. 9).
5. **Tasso e tempo di risposta** alle 1-3 stelle; recensioni segnalate ed esito.
6. Warning, email educative, Consumer Alert/Warning ricevuti: **sempre**, anche se zero.

**Vanity**: totale storico delle recensioni come se fosse del mese; etichetta "Eccellente" senza il trend; impression del TrustBox; citazioni AI e "+1.548%" da blog Trustpilot; posizione nella categoria Trustpilot; recensioni raccolte con Basic link contate come progresso verso Seller Ratings.

---

## 12. TrustScore e recensioni nelle creatività Meta e Google

Fonte: [Legal Brand Guidelines v3.0, settembre 2026](https://corporate.trustpilot.com/legal/for-businesses/legal-brand-guidelines/sept-2026) (sostituisce la v2.0 del febbraio 2023).
- **Solo con piano a pagamento** (sez. 1). Asset ufficiali (loghi, stelle, badge, template annunci, generatore immagini recensione) dal pannello ([Marketing assets](https://help.trustpilot.com/s/article/Trustpilots-Marketing-assets?language=en_US)).
- **La parola "TrustScore" deve stare accanto al numero** (4,6 da solo si confonde con le stelle) e 🔴 **accanto a TrustScore, stelle o Star Label va sempre il numero totale di recensioni** ([v3.0](https://corporate.trustpilot.com/legal/for-businesses/legal-brand-guidelines/sept-2026)).
- Il dato deve essere **attuale**: su materiale che non si aggiorna da solo (immagini per ads, email, stampa) va il timbro **"Trustpilot rating as of [Mese/Anno]" in corpo almeno 8 pt**, e il dato si **rinfresca almeno ogni 30 giorni, ed entro 5 giorni lavorativi se il TrustScore scende di più di 0,2** ([v3.0](https://corporate.trustpilot.com/legal/for-businesses/legal-brand-guidelines/sept-2026)). Si mette una scadenza a 30 giorni a ogni creatività con il punteggio.
- Citazioni di recensioni: testuali, **con nome e logo Trustpilot, data della recensione e stelle** della singola recensione; per usare il nome del recensore serve il suo **"permesso esplicito e documentato"**, altrimenti si **anonimizza del tutto** la citazione ([v3.0](https://corporate.trustpilot.com/legal/for-businesses/legal-brand-guidelines/sept-2026)).
- **Claim di ranking** ("primi in categoria") "accurati al momento della pubblicazione e verificabili dal consumatore sul sito Trustpilot"; **confronti** solo "come con come" e "accurati per ogni azienda o prodotto citato" ([v3.0](https://corporate.trustpilot.com/legal/for-businesses/legal-brand-guidelines/sept-2026)).
- Non alterare logo e stelle; non presentare Trustpilot come endorsement; non usare i dati di un'altra azienda. ⛔ **Non si passano Brand Asset o contenuti Trustpilot a terzi** (agenzia, marketplace, comparatore) "perché li rendano per conto loro" ([v3.0](https://corporate.trustpilot.com/legal/for-businesses/legal-brand-guidelines/sept-2026)).
- 🔴 **Sparita l'approvazione preventiva del CSM per TV, radio, audio digitale e affissioni** della v2.0: la v3.0 dice che Trustpilot "non approva, firma o pre-autorizza singole campagne" che rientrano nel piano e nelle linee guida; serve permesso solo per usi fuori da piano e linee guida. Enforcement: "se troviamo un misuso, agiamo per correggerlo", da un avviso fino a restrizioni dell'account, nota sul profilo, fine dell'abbonamento e azione legale ([v3.0](https://corporate.trustpilot.com/legal/for-businesses/legal-brand-guidelines/sept-2026)).
- Meta non ha regole specifiche su Trustpilot: valgono le policy generali sulle affermazioni ingannevoli; su Google Ads le stelline vere arrivano solo dalle Valutazioni negozio (sez. 9).

---

## 13. Cosa è cambiato fra giugno e settembre 2026

- **24/09/2026, Product updates September 2026** ([post](https://business.trustpilot.com/blog/releases-and-updates/product-updates-september-2026)): pagine pubbliche di **recensione per prodotto** (Trustpilot dichiara +1.548% di citazioni AI in una settimana su 418 aziende in beta: numero suo, non verificabile); **QR Code Review Collector** (già nei piani, sez. 1); **Location Reviews** con caricamento in blocco e **Location Reviews API** (add-on API); **Review Follow-up Targeting** (sondaggio automatico dopo parole chiave nella recensione); **Search Query Data** (cosa cercano i visitatori del profilo); **AI Search Market Insights** (quante volte ChatGPT, Claude e Perplexity citano il profilo rispetto ai concorrenti); **Multi-Domain Management e Custom Roles** solo Enterprise. Per un e-commerce italiano le due cose che cambiano il report mensile sono le pagine prodotto (rich snippet, sez. 8) e il dato sulle citazioni AI; il resto non si promette al cliente senza sapere su quale piano è.

- **Giugno 2026**: Guidelines for Businesses **v7.2** ([jun-2026](https://corporate.trustpilot.com/legal/for-businesses/guidelines-for-businesses/jun-2026)) e Guidelines for Reviewers aggiornate; **Terms of Use and Sale v9.0 dal 23/06/2026** (rinnovo automatico, disdetta 30 giorni, recensioni permanenti). Diff rispetto alla v7.1: non pubblicato, [DA VERIFICARE].
- **29/06 e 10/07/2026**: **nuova app Shopify** con Theme Editor nativo; configurazioni della legacy non migrano (sez. 4).
- **10/08/2026**: inviti da **workflow HubSpot** ([hubspot-workflows](https://business.trustpilot.com/blog/releases-and-updates/hubspot-workflows)).
- **13/08/2026**: **Product Review Pages** in beta (sez. 8).
- **Settembre 2026**: **Legal Brand Guidelines v3.0** ([sept-2026](https://corporate.trustpilot.com/legal/for-businesses/legal-brand-guidelines/sept-2026)) sostituiscono la v2.0 del febbraio 2023: Free solo testo semplice con link (più Review Collector Widget); numero totale di recensioni sempre accanto al punteggio; timbro data e refresh ogni 30 giorni (5 giorni lavorativi se −0,2); permesso documentato per il nome del recensore; niente asset o contenuti a terzi; niente Product Score in home o landing; **sparita l'approvazione CSM per TV/radio/affissioni** (sez. 1, 8, 12). Giorno esatto di pubblicazione non indicato: [DA VERIFICARE].
- **Marzo 2026** (prima della finestra ma decisivo): policy "Action we take" e sanzione AGCM (sez. 7 e 10). **Aprile 2026**: In-App Review Collector, Invitation Optimizer, AI Search Analytics, Custom Dashboards.
- Google Ads: la pagina Valutazioni negozio parla di **24 mesi** e non più di 12 (sez. 9); data del cambio non trovata.
- **15/09/2026**: risultati H1 2026 (ricavi +19% a cambi costanti; solo contesto, nessun cambio di prodotto annunciato) ([Investing.com](https://www.investing.com/news/transcripts/earnings-call-transcript-trustpilot-h1-2026-profit-growth-fails-to-lift-shares-93CH-4901103)). **16/09/2026**: un'analisi terza rileva Consumer Warning sul 21% di 100 profili di broker ([Finance Magnates](https://www.financemagnates.com/forex/trustpilot-slaps-warning-label-on-20-of-100-top-broker-profiles/)): segnale che l'enforcement è attivo, non una regola.

---

## 14. Igiene di un profilo ereditato: ordine di controllo

1. **Piano attivo, scadenza e data ultima per la disdetta** (30 giorni); chi è admin; quanti domini si pagano.
2. **Email educative, warning, Consumer Alert/Warning** nella casella dell'admin e sul profilo pubblico.
3. **Come partono gli inviti oggi**: AFS su quale email, integrazione, API, file, basic link; **quante email hanno il BCC** (doppi inviti); il ritardo impostato; a chi **non** si invita (gating nascosto in un filtro dell'automazione).
4. **Incentivi in giro**: cartoline nel pacco, email post-vendita, script dell'assistenza con "sconto per una recensione".
5. **Sender email**: personalizzato con SPF a posto o default Trustpilot; inviti in stato di errore.
6. **Quota Verified vs Unprompted** e conteggio per l'Italia negli ultimi 12/24 mesi (sez. 9); esito lookup Google.
7. **Recensioni segnalate negli ultimi 12 mesi** e per quale motivo: se sono quasi tutte 1 stella "non genuine", c'è un rischio misuso.
8. **Risposte pubblicate**: dati personali o toni da rimuovere prima che lo faccia Trustpilot.
9. **TrustBox e stelline sul sito**: widget ufficiali o immagini statiche; plugin o estensioni non autorizzati; widget Product Score in home o landing; markup duplicato; widget in lazy load; piano che li consente ([v3.0](https://corporate.trustpilot.com/legal/for-businesses/legal-brand-guidelines/sept-2026)).
10. **Sito**: pagina che spiega come si raccolgono le recensioni (Omnibus, sez. 10); "recensioni verificate" scritto senza metodo.
11. **Shopify**: app legacy ancora installata (sez. 4).
12. **Creatività e materiali in giro** (ads, email, stampa, cataloghi, marketplace): punteggio senza numero di recensioni o senza timbro "Trustpilot rating as of"; data dell'ultimo refresh oltre 30 giorni; citazioni con nome del recensore senza permesso documentato; asset Trustpilot passati ad agenzie o terzi ([v3.0](https://corporate.trustpilot.com/legal/for-businesses/legal-brand-guidelines/sept-2026)).

---

## 15. Meccanica del pannello (da verificare a mano)

- Dove sta il ritardo di default dell'AFS e se è unico o per template; qual è il numero preimpostato.
- Cosa succede al 51° invito del mese sul Free e al superamento della quota sui piani a pagamento: blocco, coda, upsell.
- Se il pannello mostra le soglie delle etichette verbali (Eccellente ecc.) e dove.
- Dove si vede lo stato "Verified/Invited/Unprompted" per singola recensione e se esiste un filtro per l'export.
- Se l'export CSV delle recensioni e degli inviti esiste sul Free.
- Dove compaiono le email educative e i warning dentro il pannello, oltre che via email.

---

## 16. Cosa non fare mai

- Mostrare TrustScore, stelline, logo o widget sul sito o nelle ads con il piano Free: solo testo semplice con link ([v3.0](https://corporate.trustpilot.com/legal/for-businesses/legal-brand-guidelines/sept-2026)).
- Sostituire un TrustBox con uno screenshot, o usare plugin non ufficiali per le stelline ([v3.0](https://corporate.trustpilot.com/legal/for-businesses/legal-brand-guidelines/sept-2026)).
- Mettere il TrustScore in una creatività senza numero totale di recensioni e senza timbro data, o lasciarla girare oltre 30 giorni ([v3.0](https://corporate.trustpilot.com/legal/for-businesses/legal-brand-guidelines/sept-2026)).
- Citare una recensione con il nome del recensore senza permesso documentato, o passare asset Trustpilot a un'agenzia o a un marketplace perché li renda da sé ([v3.0](https://corporate.trustpilot.com/legal/for-businesses/legal-brand-guidelines/sept-2026)).
- Mettere l'indirizzo AFS in BCC su più di un'email per ordine, o su email di marketing.
- Filtrare gli inviti per "clienti senza ticket" o "ordini senza reso".
- Offrire sconti, rimborsi o buoni per una recensione o per modificarla.
- Segnalare le 1 stella per il tono o senza aver cercato il cliente con Find Reviewer.
- Rispondere in pubblico con numero d'ordine, indirizzo o nome completo del cliente.
- Promettere rich snippet con le stelline aziendali (servono recensioni di prodotto, add-on).
- Contare le recensioni da Basic link verso i 100 per Google.
- Scrivere "recensioni verificate" sul sito senza descrivere il metodo.
- Lasciare passare la finestra di disdetta di 30 giorni.
- Copiare nel report un numero preso da un blog Trustpilot ("+35%", "+1.548%") come se fosse del cliente.

---

## Fonti (verificate 20-21/09/2026)

**Ufficiali Trustpilot, lette:** [Guidelines for Businesses v7.2 (giugno 2026)](https://corporate.trustpilot.com/legal/for-businesses/guidelines-for-businesses/jun-2026) · [Terms of Use and Sale for Businesses v9.0 (23/06/2026)](https://corporate.trustpilot.com/legal/for-businesses/terms-of-use-and-sale-for-businesses/jun-2026) · [Action we take (marzo 2026)](https://corporate.trustpilot.com/legal/for-everyone/action-we-take/mar-2026) · [Legal Brand Guidelines v3.0 (settembre 2026)](https://corporate.trustpilot.com/legal/for-businesses/legal-brand-guidelines/sept-2026) · [Legal Brand Guidelines v2.0 (feb 2023, superata)](https://corporate.trustpilot.com/legal/for-businesses/legal-brand-guidelines/feb-2023) · [Plans USD](https://business.trustpilot.com/plans) · [Pricing USD](https://business.trustpilot.com/pricing) · [Plans IT (EUR)](https://it.business.trustpilot.com/plans) · [Invitation API](https://developers.trustpilot.com/invitation-api) · [Developers home](https://developers.trustpilot.com/) · [Review invitations (feature)](https://business.trustpilot.com/features/review-invitations) · [Dashboard and analytics (feature)](https://business.trustpilot.com/features/dashboard-analytics) · [corporate.trustpilot.com/trust](https://corporate.trustpilot.com/trust) · [Product updates aprile 2026](https://business.trustpilot.com/blog/releases-and-updates/product-updates) · [Releases and updates](https://business.trustpilot.com/blog/releases-and-updates) · [Shopify 29/06/2026](https://business.trustpilot.com/blog/releases-and-updates/shopify) · [Shopify 10/07/2026](https://business.trustpilot.com/blog/releases-and-updates/trustpilot-shopify-upgrade) · [Product Review Pages 13/08/2026](https://business.trustpilot.com/blog/releases-and-updates/spotlight-product-ai-recommended-search-era) · [Changes to reported reviews](https://business.trustpilot.com/blog/build-trusted-brand/changes-to-reported-reviews) · [Rich snippets (blog, 09/02/2022)](https://business.trustpilot.com/blog/get-seen-in-search/rich-snippets-stars-for-product-reviews-can-boost-seo).

**Ufficiali Google:** [Valutazioni negozio (2375474, IT)](https://support.google.com/google-ads/answer/2375474?hl=it) · [Review snippet structured data](https://developers.google.com/search/docs/appearance/structured-data/review-snippet) · [Search Central blog 09/2019, self-serving reviews](https://developers.google.com/search/blog/2019/09/making-review-rich-results-more-helpful) · [Policy editoriale Google Ads (6021546)](https://support.google.com/adspolicy/answer/6021546).

**Ufficiali Italia:** [AGCM comunicato PS12962 (23/03/2026)](https://www.agcm.it/media/comunicati-stampa/2026/3/PS12962) · [AGCM provvedimento 31878 (PDF)](https://www.agcm.it/dotcmsCustom/tc/2031/3/getDominoAttach?urlStr=81.126.91.44%3A8080%2FC12560D000291394%2F0%2F43CEA3D8214A249AC1258DC30041B0F0%2F%24File%2Fp31878.pdf) (non aperto in questa revisione, citato dal comunicato).

**Terze parti (pratica, non numeri Trustpilot):** [trustratings.com, mirror dell'articolo TrustScore](https://trustratings.com/help/trustscore-explained) · [Studio Stefanelli, decisione AGCM](https://www.studiolegalestefanelli.it/it/approfondimenti/trustpilot-recensioni-ingannevoli-agcm-2026) · [Assonime 22/03/2023](https://www.assonime.it/attivita-editoriale/news/Pagine/News-22_03_2023.aspx) · [Brocardi art. 23 Cod. Cons.](https://www.brocardi.it/codice-del-consumo/parte-ii/titolo-iii/capo-ii/sezione-i/art23.html) · [Agenzia Opinione, replica Trustpilot](https://www.agenziagiornalisticaopinione.it/opinionews/trustpilot-replica-ad-agcm-contestiamo-la-decisione-e-presenteremo-il-ricorso-per-proteggere-trasparenza-e-affidabilita/) · [StackTome 25/03/2025, basic link](https://www.stacktome.com/blog/how-will-trustpilots-upcoming-basic-link-invitation-updates-impact-ecommerce-brands) · [reverbico, tempi di flag](https://reverbico.com/blog/remove-trustpilot-reviews/) · [Finance Magnates 16/09/2026](https://www.financemagnates.com/forex/trustpilot-slaps-warning-label-on-20-of-100-top-broker-profiles/) · [Investing.com H1 2026](https://www.investing.com/news/transcripts/earnings-call-transcript-trustpilot-h1-2026-profit-growth-fails-to-lift-shares-93CH-4901103).

**Non leggibili via fetch il 20/09/2026, da ricontrollare a mano** (help.trustpilot.com rende solo con JavaScript; contenuto usato solo dagli estratti dei motori di ricerca): [TrustScore and star rating explained](https://help.trustpilot.com/s/article/TrustScore-and-star-rating-explained?language=en_US) · [AFS](https://help.trustpilot.com/s/article/How-to-use-Automatic-Feedback-Service-AFS?language=en_US) · [What is AFS](https://help.trustpilot.com/s/article/What-is-Automatic-Feedback-Service?language=en_US) · [AFS senza BCC](https://help.trustpilot.com/s/article/How-to-use-Automatic-Feedback-Service-without-a-BCC-field?language=en_US) · [Trigger invitations using APIs](https://help.trustpilot.com/s/article/Trigger-invitations-using-Trustpilot-APIs?language=en_US) · [Invitation status overview](https://help.trustpilot.com/s/article/Invitation-status-overview?language=en_US) · [Review labels](https://help.trustpilot.com/s/article/About-Trustpilots-review-labels?language=en_US) · [Why Verified](https://help.trustpilot.com/s/article/Why-are-some-reviews-marked-Verified?language=en_US) · [Flag reasons](https://help.trustpilot.com/s/article/For-which-reasons-can-businesses-flag-reviews?language=en_US) · [Misuse of flagging tool](https://help.trustpilot.com/s/article/What-happens-if-businesses-misuse-the-review-flagging-tool?language=en_US) · [Consumer Warnings and Alerts](https://help.trustpilot.com/s/article/Trustpilot-Consumer-Warnings-and-Alerts?language=en_US) · [Google store ratings FAQ](https://help.trustpilot.com/s/article/Trustpilot-and-Googles-store-ratings-FAQ?language=en_US) · [Rich snippets con TrustBox prodotto](https://help.trustpilot.com/s/article/Get-rich-snippets-with-product-review-TrustBox-widgets?language=en_US) · [Service reviews analytics](https://help.trustpilot.com/s/article/Service-reviews-analytics?language=en_US) · [WooCommerce](https://help.trustpilot.com/s/article/Trustpilots-WooCommerce-integration?language=en_US) · [PrestaShop](https://help.trustpilot.com/s/article/Trustpilots-PrestaShop-integration?language=en_US) · [Shopify app](https://help.trustpilot.com/s/article/Trustpilot-Shopify-app?language=en_US) · [Can businesses reply](https://help.trustpilot.com/s/article/Can-businesses-reply-to-reviews?language=en_US) · [New EU laws on reviews](https://help.trustpilot.com/s/article/New-EU-laws-on-reviews-What-they-mean-for-businesses-using-Trustpilot?language=en_US) · [Marketing assets](https://help.trustpilot.com/s/article/Trustpilots-Marketing-assets?language=en_US) · [Manual invitation access](https://help.trustpilot.com/s/article/I-lost-access-to-manual-invitations?language=en_US). Anche [business.trustpilot.com/integrations](https://business.trustpilot.com/integrations) e [trustpilot.com/trust/how-trustscore-works](https://www.trustpilot.com/trust/how-trustscore-works) rispondono 404; web.archive.org non raggiungibile.
