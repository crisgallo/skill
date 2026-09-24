# Changelog google-ads-performance

## 24/09/2026
- Data di verifica in cima a 24 settembre 2026; sez. 0 punto 6 con i cambi del 23/09/2026.
- Sez. 1: blocco "Dal 23/09/2026, come si legge e si testa AI Max": vista "Termini di ricerca e combinazioni di annunci", righe di totale AI Max nel rapporto keyword, filtro AI Max che sottostima (16470459); AI Brief in beta chiusa anche in italiano (blog.google 23/09/2026); esperimenti AI Max contro DSA, limiti 100% DSA e campagne miste (2471185).
- Sez. 7: punto 12 su Ask Advisor (beta, non MCC) che su approvazione mette in pausa campagne e cambia budget (16574983, ppcnewsfeed 22/09/2026), con la regola di leggere la cronologia modifiche su un account ereditato.
## 23/09/2026
- Sez. 5: aggiunta la regola di Cristiano dalla chat Cowork del 19/09/2026 (Sceglinatura, `feedback_numeri_dal_pannello_non_da_ga4.md`): i numeri della campagna si leggono in Google Ads, GA4 solo per tendenze; niente tabelle miste.
- Sez. 8: aggiunta la voce sul classificare termini di ricerca dal nome (`feedback_verifica_catalogo_prima_di_classificare.md`, 19/09/2026): si verifica sul sito del cliente o si chiede, con il caso lenivox/ansiwit. Data di verifica delle fonti invariata: non sono fonti web.

## 20/09/2026

- Aggiornata la data di verifica in cima a 20 settembre 2026 e aggiunto il blocco "Cosa è cambiato" con date (sez. 0, regola 3 dell'autore).
- Aggiunto in sez. 0 il punto 5: la pagina annunci ufficiale 9048695 è ferma al 20/05/2026, i cambi si intercettano dagli avvisi in cima alle pagine Help e dal Developer Blog.
- Sez. 1: separato il numero Google (almeno 30 conversioni, 50 per ROAS target; 7065882, 6268632) dalle soglie 30-50 e 50-100 conversioni/mese, ora etichettate "regola empirica, non numero Google" con attribuzione ai blog (stackmatix, infrontmarketing).
- Sez. 1: aggiunta la fascia 10-30 conversioni/mese come scelta caso per caso, senza regola inventata.
- Sez. 1: aggiunta la regola AI Max: creazione della generica di campagna bloccata dal 03/08/2026, conversione automatica 1–30/09/2026, controlli post-conversione (search term matching, text customization, espansione URL finale, rapporto termini separato keyword/AI Max), DSA da febbraio 2027 (13389795, blog.google, Developer Blog 12/08/2026, ppc.land).
- Sez. 1: aggiunto il test AI Mode con keyword esatte e a frase confermato il 04/09/2026 (ppc.land; nessuna pagina Help trovata).
- Sez. 1: precisato che l'elenco esclusioni a livello di account ha limite di 1.000 parole chiave, vale per Search, PMax, App, Shopping, Smart, Local e non cita Demand Gen (11396330).
- Sez. 2: "due-quattro settimane senza target" etichettato come regola empirica (groas 23/04/2026), affiancato dal numero Google sul volume.
- Sez. 2: aggiunto il cambio del 17/08/2026 (rollout 27/08): CPA/ROAS/CPC target consegnano al target sulle campagne limitate dal budget; Bid Target Adjustment Tool dal 06/07/2026; elenco campagne interessate ed escluse (17061251, 17125145).
- Sez. 3: sostituita la frase vaga "pratica di dieci anni fa" con il legame alla soglia delle 30 conversioni; aggiunta la rimozione del targeting per lingua da Search e dalla parte Search di PMax da fine settembre 2026 (1722078, Developer Blog 13/08/2026).
- Sez. 4: aggiunta la conversione "Ricerche di brand" (primaria solo di nome, reporting, finestra 7 giorni, brand mapping) (16212033).
- Sez. 4: corrette le conversioni avanzate: web e lead unificate da giugno 2026 con unico interruttore, caricamenti offline e lead solo via Data Manager API dal 15/06/2026 (16884284); aggiunti i limiti 90/63 giorni (15081888) e la regola dei 7 giorni per l'attribuzione basata sui dati, segnalata come fonte terza non verificata (ppc.land 22/08/2026).
- Sez. 4: modello di attribuzione riscritto come "basato sui dati o ultimo clic", gli altri modelli non più supportati; data della rimozione dichiarata non verificata (6259715).
- Sez. 5: corretta la frase su UTM e gclid: il tagging automatico ha la priorità sul manuale, gli UTM non rompono l'importazione delle conversioni; il consiglio di non stratificare UTM resta con la motivazione giusta (3095550). Aggiunto il percorso completo dell'auto-tagging.
- Sez. 5: aggiunta la fonte per l'applicazione automatica dei consigli (10279006) e il controllo sugli esperimenti, che da aprile 2026 applicano i risultati in automatico di default (ppcnewsfeed; Search Engine Land 473266 in 403).
- Sez. 6: reti Demand Gen corrette: YouTube, Discover, Gmail, Maps, Rete Display, video partner (13695777); aggiunta la migrazione delle campagne Display standalone dentro Demand Gen con Rete Display non deselezionabile (17051545, blog.google).
- Sez. 6: aggiunta la fonte ufficiale del +35% conversioni su Shorts (9128498); aggiunto il 4:5 fra i rapporti video ammessi.
- Sez. 6: aggiunte le pagine specifiche separate per immagini (17140672) e video (17141078: 1-5 video per annuncio, minimo 5 s, sotto 10 s non serve su In-stream, consigliati oltre 15 s); "20 immagini per annuncio" ora citato da 15701616.
- Sez. 6: aree di sicurezza riscritte con le zone Google per Shorts (10% alto, 25% basso, 10% destra; 9128498, business.google.com); il vecchio 90%/80% dichiarato regola di blog per il 16:9.
- Sez. 6: budget Demand Gen: aggiunto il minimo 5 USD/giorno via API dal 01/04/2026 e la raccomandazione di almeno 10× il CPA target (prima 15-20×, abbassato a settembre 2026) (13695777, Developer Blog 27/02/2026, ppc.land, twooctobers 01/09/2026); aggiunta la fonte per i 60 secondi nel feed Shorts (16041697).
- Sez. 6: aggiunti i lookalike come suggerimenti e non vincoli da marzo 2026 (13541369).
- Sez. 7: aggiunto il controllo sugli esperimenti (punto 1), la nota su "Ricerche di brand" (punto 2), la voce unica delle conversioni avanzate e il canale Data Manager (punto 3), il percorso e la fonte del contatto per la protezione dei dati (punto 6, 7687725).
- Sez. 7: soglia remarketing esplicitata a 100 utenti attivi negli ultimi 30 giorni su tutte le reti da dicembre 2025 (2472738); aggiunta l'etichettatura automatica del tipo cliente su Customer Match dal 18/08/2026 (12080169, digitalapplied).
- Sez. 7: aggiunti i punti 10 (ricontrollo target impostati prima del 17/08/2026) e 11 (impostazione video PMax).
- Sez. 8: aggiunti "lasciare un CPA target largo dopo il 17/08/2026" e la rilettura del rapporto termini di ricerca dopo la conversione ad AI Max.
- Nuova sez. 9 Performance Max: gruppi di asset, esclusioni di campagna e di account (11396330), rapporto per canale, esclusione clienti esistenti, ridimensionamento video con IA generativa con opt-out entro il 04/09/2026 (Search Engine Land 485252), rimandi a lingua e target. Nessuna soglia numerica aggiunta.
- Fonti riscritte: URL confermate divise fra ufficiali e terze parti; corrette le etichette fuorvianti (10195720 non contiene soglie né regole sulle esclusioni; 13676244 ha i numeri dentro immagini; stackmatix aggiornato il 13/09/2026, dopo la verifica dell'11/08); aggiunte tutte le pagine ufficiali nuove; elencate le pagine non leggibili.
- Non verificato al 20/09/2026: corpo dei post del Google Ads Developer Blog del 27/02, 12/08 e 13/08/2026 (solo titolo e data); Search Engine Land 473266 e 433352 (403); data esatta della rimozione dei modelli di attribuzione (fonte con le date in 403); pagina ufficiale sui rapporti di attribuzione per la regola dei 7 giorni sulle conversioni offline; pagina Help sui gruppi di asset PMax; data della migrazione automatica finale Display → Demand Gen (gennaio 2027 solo da fonti terze); nessuna pagina Help per il test AI Mode con esatta e frase.
