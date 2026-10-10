# Routine giornaliera di aggiornamento delle skill

Questo file è il compito che la sessione automatica esegue ogni mattina alle 10:00 ora italiana.
Si modifica qui, non nel trigger: il trigger dice solo "leggi ROUTINE.md ed eseguilo".

## Regole fisse

1. Il repository `crisgallo/skill` è la fonte di verità. Si lavora sul ramo predefinito, si committa e si spinge.
2. Le righe marcate **✅ VERIFICATO** con una data sono osservazioni fatte di persona sul pannello. **Non si toccano mai.** Se una fonte le smentisce, si aggiunge sotto una riga "⚠️ Nota del GG/MM/AAAA: la fonte X dice Y (URL). Da ricontrollare sul pannello." e basta.
3. Ogni regola nuova o modificata porta **data del cambio** (quella della piattaforma, non quella in cui ce ne siamo accorti) e **URL della fonte ufficiale** inline. Niente soglie da blog presentate come ufficiali: si etichettano "regola empirica di terzi".
4. Quando si modifica una skill: si riscrive la riga "Ultima verifica delle fonti" in cima, si aggiorna il blocco "Cosa è cambiato" se esiste, si aggiunge una voce datata in `skills/<nome>/CHANGELOG.md` **con il livello in testa alla voce** (🔴 sostanziale o 🟡 minore, definizione in regola 7), si valida con `quick_validate.py` (deve stampare "Skill is valid!"), si rigenera lo zip con `scripts/package.sh`.
5. Una skill sotto le 120 righe o sopra le 400 righe è un segnale di errore: si controlla prima di committare.
7. **Livello di ogni modifica** (decisione di Cristiano del 25/09/2026). Ogni voce di CHANGELOG comincia con 🔴 o 🟡.
   - **🔴 Sostanziale**: cambia un numero, una soglia, un default, una procedura o un nome di menu che si usa; una scadenza entro 60 giorni; una funzione nuova che cambia cosa si fa sul pannello; una patch di sicurezza di una piattaforma che i clienti usano; una regola nata dalle chat di Cristiano (passo B); una skill nuova o una richiesta esplicita di Cristiano.
   - **🟡 Minore**: listino o pagina riletti con gli stessi numeri; nota di terzi aggiunta; fonte aggiunta o sostituita senza cambio di regola; data di verifica spostata; precisazione di testo; dettaglio in un file `references/`; novità che non cambia una decisione operativa.
   - Nel dubbio si sceglie 🟡 e si scrive nel report perché. **Le modifiche minori non vanno mai per mail** (decisione di Cristiano del 28/09/2026): restano nel repository e in `dist/`, e vengono spedite solo insieme alla prossima modifica sostanziale della stessa skill.
6. Non si inventa. Se una pagina non si legge (403, corpo vuoto), si scrive nel report che non si è potuta leggere e si passa oltre. Le pagine che rispondono 403 di solito sono: facebook.com/business/help, help.openai.com, help.trustpilot.com (usare l'API Zendesk), support.getharvest.com, help.ads.microsoft.com (usare lo specchio learn.microsoft.com), jonloomer.com, searchengineland.com. Le pagine di **help.brevo.com** rispondono 403 al fetch ma si leggono dall'API Zendesk `https://help.brevo.com/api/v2/help_center/en-us/articles/<id>.json` (campo `body`, data in `updated_at`); `scripts/snapshot.py` lo fa da solo, e per leggere un articolo a mano si usa lo stesso URL.

## Passi

### A. Preparazione
- `git pull` sul ramo predefinito.
- Leggere `snapshots/state.json` (URL → hash del contenuto → data ultimo controllo). Se non esiste, questo è il primo giro: si crea la base e non si segnala nulla come "cambiato".

### B. Raccolta di quello che arriva da Cristiano: copie locali, chat Cowork, snapshot Drive
Tre fonti, in quest'ordine. Tutte hanno la precedenza su qualsiasi fonte web: sono osservazioni dal pannello o decisioni di Cristiano.

**B1. Copie locali salvate a mano.** Su Google Drive cercare la cartella `skill_modificate_in_locale` (parentId noto: `1AEkZiDqkeA2Ydf96vWorV_9KKeGm7cvx`, ricercabile per titolo). Per ogni file `<skill>_SKILL_locale_<data>.md` più recente dell'ultima data registrata in `snapshots/state.json` sotto `locali`:
  - scaricarlo, confrontarlo con `skills/<skill>/SKILL.md`;
  - integrare le differenze nella skill del repository (le righe ✅ VERIFICATO nuove entrano così come sono);
  - registrare in `snapshots/state.json` la data del file trattato.

**B2. Regole nate nelle chat Cowork.** Le chat di progetto salvano le decisioni di Cristiano come file `feedback_<tema>.md` nelle cartelle memoria dei progetti su Drive (`_claude_memory`, `memory`, `_regole`). Non stanno dentro nessuna skill, quindi senza questo passo si perdono.
  - Cercare con il connettore Drive: `title contains 'feedback_' and modifiedTime > '<chat.ultima_lettura>T00:00:00Z'` (la data sta in `snapshots/state.json`, chiave `chat`). Scorrere tutte le pagine dei risultati.
  - ⚠️ Lo stesso file compare più volte (copie negli snapshot giornalieri, stesso titolo e stessa dimensione) e ogni tanto una sincronizzazione ritocca la `modifiedTime` di decine di file vecchi (successo il 19/09/2026 alle 13:52). Si tiene una copia per titolo e si scartano i titoli già presenti in `chat.feedback_visti` con la stessa data di modifica.
  - Il contenuto si legge con `get_file_metadata` e `snippetVerbosity: MAX_ALLOWED` (il connettore non legge i `.md` con `read_file_content`; `download_file_content` restituisce base64 e va usato solo se il file supera i 10 KB).
  - Per ogni file nuovo si decide:
    - **riguarda una skill del repository** (una regola operativa su una piattaforma coperta, tipicamente marcata "CANDIDATA A REGOLA GLOBALE"): si integra nella sezione giusta come `📌 **Regola di Cristiano (chat Cowork del GG/MM/AAAA, progetto X):** ...`, con il caso che l'ha generata in una o due righe e i numeri se ci sono. Non si scrive ✅ VERIFICATO e **non si tocca la riga "Ultima verifica delle fonti"**: non è una fonte web. Voce nel CHANGELOG con il nome del file di feedback.
    - **regola di progetto** (nomenclature, perimetri di prodotto, claim di un cliente, regole di processo): non entra nelle skill di piattaforma. ⚠️ Dal 30/09/2026 esiste la skill `trello`: le regole di Cristiano su card, checklist, date e commenti Trello (`feedback_trello_*.md`, `workflow_trello_*.md`, `feedback_card_apertura_e_rotazione.md`) si integrano lì come 📌, non sono più «regole di processo». Si elenca nel report sotto "Regole di progetto viste, non integrate" con una riga di sintesi.
    - **abrogata** (lo dice il file stesso): si ignora.
  - Registrare in `snapshots/state.json` sotto `chat`: `ultima_lettura` = data di oggi e, in `feedback_visti`, titolo, data di modifica ed esito di ogni file trattato.

**B3. Skill modificate direttamente dalle chat Cowork.** Ogni giorno verso le 12:00 una copia della cache Cowork finisce su Drive in una cartella `skills` (percorso: `<id account>/939cbb1e-876a-47f2-95b8-2b2a78a1ba55/skills/<nome skill>/SKILL.md`). Se una chat ha modificato una skill sul posto, la modifica sta lì e da nessun'altra parte; quando Cristiano cancella la skill per caricare lo zip nuovo, sparisce.
  - Cercare: `title = 'SKILL.md' and createdTime > '<data di ieri>T00:00:00Z'` con `excludeContentSnippets: true`, e prendere per ogni file `parentId` e `fileSize`. I `parentId` si risolvono con `parentId = '<id cartella skills>'` (id della cartella `skills` più recente: `title = 'skills' and mimeType = 'application/vnd.google-apps.folder'`, prima riga). Le cartelle che non corrispondono a una skill del repository (`built-in-browser`, `chrome-browser`, `deep-research`, `docx`, `pptx`, `xlsx`, `skill-creator`, `morning`, `docs`, `substack-articoli-settimanale`, e simili) si ignorano.
  - Scrivere un file `<nome> <fileSize>` per riga ed eseguire `python3 scripts/drive_check.py <file> --save AAAA-MM-GG`. Confronta la dimensione con tutte le versioni di `skills/<nome>/SKILL.md` nella storia git, senza scaricare nulla.
    - `IDENTICO`: la copia Cowork è una versione del repository (quella caricata dall'ultimo zip, o una precedente). Nulla da fare.
    - `DA_SCARICARE`: nessuna versione ha quella dimensione, quindi una chat ha modificato la skill. Scaricare con `download_file_content`, decodificare, fare `diff` con la versione del repository più vicina (`git log -p -- skills/<nome>/SKILL.md`) e portare nel repository le righe aggiunte o cambiate dalla chat, con le regole di sempre (le ✅ VERIFICATO nuove entrano così come sono; nulla si cancella). Voce nel CHANGELOG "dalla copia Cowork del GG/MM/AAAA".
  - ⚠️ La `modifiedTime` dei SKILL.md su Drive è l'ora della sincronizzazione, non della modifica: non serve a niente. Conta solo la dimensione.
  - Lo stato del confronto finisce in `snapshots/state.json` sotto `drive` (data dello snapshot, dimensione e commit corrispondente per skill).

**B4. Newsletter di prodotto delle piattaforme nella Gmail di Cristiano** (aggiunto il 01/10/2026 su sua richiesta: la newsletter OpenAI del 30/09 conteneva quattro novità che il confronto delle pagine non aveva fatto emergere). Le piattaforme mandano i riepiloghi delle novità per mail, già riassunti: si leggono ogni giorno e si trattano come una fonte ufficiale (il mittente è la piattaforma stessa).
  - ⚠️ **Cristiano archivia queste mail appena arrivano: la ricerca NON si limita alla inbox.** Si usa `search_threads` con `in:anywhere -in:trash -in:spam newer_than:2d` e un filtro sui mittenti noti: `{from:email.openai.com from:openai.com from:google.com from:facebookmail.com from:meta.com from:microsoft.com from:brevo.com from:trustpilot.com from:linkedin.com from:atlassian.com from:woocommerce.com from:prestashop.com from:getharvest.com from:redmine.org from:creditsafe.com from:substack.com}`, **meno il rumore già visto il 01/10/2026** (prova fatta su quattro giorni: 38 thread, uno solo di prodotto): `-from:jobalerts-noreply@linkedin.com -from:jobs-noreply@linkedin.com -from:messaging-digest-noreply@linkedin.com -from:notifications-noreply@linkedin.com -from:googlecloud@google.com -from:noreply-accounts@google.com -from:drive-shares-dm-noreply@google.com -from:comments-noreply@docs.google.com -from:gemini-notes@google.com -from:google-maps-noreply@google.com -from:workspace-noreply@google.com -from:looker-studio-noreply@google.com -from:googlebase-noreply@google.com -from:maccount@microsoft.com -from:noreply@tm.openai.com -from:payments-noreply@google.com -from:Monitoring@creditsafe.com -from:contact@t.brevo.com -from:notify-noreply@google.com -from:sc-noreply@google.com -from:reaction@mg1.substack.com -from:businessprofile-noreply@google.com -from:*@xwf.google.com` (gli ultimi cinque, aggiunti fra il 04 e il 10/10/2026, sono le notifiche di pubblicazione dei container GTM, i rendimenti mensili di Search Console dei siti dei clienti, le reazioni ai commenti Substack, i rendimenti mensili dei Profili dell'attività su Google e le mail commerciali dei rappresentanti Google Ads). Le newsletter Substack di altri autori (mittente `<autore>@substack.com`) non sono mail di prodotto: contano solo quelle di `substack.com` sul prodotto Substack; le notifiche di `no-reply@substack.com` (nuovo abbonato, nuovo follower, statistiche mensili) non sono di prodotto e si saltano (04/10/2026). Se i mittenti cambiano si aggiorna questa riga. Le anteprime della ricerca non bastano: ogni mail candidata si legge per intero con `get_message` in `PLAIN_TEXT`.
  - Si contano solo le **mail di prodotto** (novità, release, policy, scadenze). Promozioni, fatture, avvisi di sicurezza dell'account, inviti a webinar e notifiche di campagne (budget, approvazioni) si ignorano e non si leggono.
  - Ogni novità si verifica sulla pagina ufficiale linkata nella mail prima di scriverla; se la pagina non è leggibile (403) si scrive la regola con la mail come fonte e `[DA VERIFICARE]`. Il livello 🔴/🟡 segue la regola fissa 7, e la mail segue il passo D: una newsletter non è mai da sola un'urgenza.
  - Registro in `snapshots/state.json` sotto `newsletter`: `ultima_lettura` e `viste` con, per ogni mail letta, id Gmail, data, mittente, oggetto ed esito (quali skill, o «niente da integrare»). Una mail già in `viste` non si rilegge.
  - ⚠️ Mai rispondere, inoltrare, etichettare, archiviare o cancellare queste mail: si leggono soltanto.

### C. Verifica delle fonti, una skill per volta
Per ogni cartella in `skills/`:
1. Leggere `SKILL.md`, la riga "Ultima verifica delle fonti" e la finestra di freschezza dichiarata in sezione 0.
2. Eseguire `python3 scripts/snapshot.py --check`: estrae tutti gli URL di tutte le skill, li scarica, calcola l'hash del testo e stampa la lista `CAMBIATO <url> <skill>`. Solo quelli si leggono (WebFetch). Alla fine del giro `python3 scripts/snapshot.py --update` salva lo stato nuovo. Per ogni URL cambiato:
   - hash uguale: nulla da fare;
   - hash diverso: leggere la pagina e stabilire se la modifica tocca una regola scritta nella skill. Se sì, correggere la skill (regola 3 e 4). Se no, aggiornare solo l'hash.
3. Cercare sul web le novità delle ultime 24 ore sulla piattaforma (release notes, annunci ufficiali, changelog). Se una novità cambia una regola o ne aggiunge una operativa, integrarla con data e URL.
4. Se la data di ultima verifica supera la finestra di freschezza: fare una verifica completa delle regole numeriche della skill sulle fonti ufficiali, anche senza cambi di hash, e riscrivere la data.
5. Skill senza fonti web (`creditsafe-monitoraggio-credito`, `substack-intelligence`, `cristiano-gallinelli-persona`): solo passo B. Per la persona, ogni lunedì leggere `https://cristianogallinelli.blog/feed/` e, se c'è un articolo nuovo, aggiungere titolo, data, temi e lessico alla skill come fatto il 20/09/2026.

### D. Chiusura
- Rigenerare `dist/` con `scripts/package.sh`.
- Scrivere `reports/AAAA-MM-GG.md` con: skill controllate, URL cambiati, modifiche fatte (per skill, in una riga ciascuna), pagine non leggibili, modifiche locali integrate (B1), feedback dalle chat integrati e regole di progetto viste ma non integrate (B2), esito del confronto con lo snapshot Cowork (B3).
- Commit con messaggio "Giro del AAAA-MM-GG: <n> skill aggiornate" e push.
- **Registro degli zip in attesa** (`snapshots/state.json`, chiave `pendenti`): per ogni skill modificata oggi si scrive `{"dal": "<prima data non ancora spedita>", "livello": "sostanziale"|"minore", "voci": [<righe del changelog>]}`; se la skill era già in attesa si tengono la data più vecchia e il livello più alto e si aggiungono le voci. Quando una skill viene spedita in una mail, la sua voce si cancella e si scrive `ultima_mail[<skill>] = <data>`. Una skill con sole modifiche minori resta in `pendenti` a tempo indeterminato: serve solo a elencare, nella mail futura, tutto quello che lo zip contiene.
- **Mail solo il lunedì, e solo per le modifiche sostanziali** (decisione di Cristiano del 01/10/2026, che aggiorna quella del 28/09: il controllo resta quotidiano, la mail diventa settimanale perché il costo per Cristiano è cancellare e ricaricare gli zip). Dal martedì alla domenica le skill modificate si accumulano in `pendenti` e **non si manda nessuna mail**. **Il lunedì**, se almeno una skill ha `livello = sostanziale` in `pendenti`, si manda a gallinelli@gmail.com una mail con **oggetto fisso, sempre identico: `Skill aggiornate`** (senza data, senza nomi, mai un oggetto diverso). Nel corpo entrano **solo le skill con livello sostanziale**: per ognuna cosa è cambiato e perché (tutte le voci del changelog accumulate in `pendenti`, comprese le minori della stessa skill, perché stanno nello stesso zip), il link allo zip su GitHub (`https://github.com/crisgallo/skill/raw/<ramo>/dist/<nome>.zip`) e il promemoria "Nel tuo account Claude, Personalizza > Skill: elimina la skill vecchia e carica questo zip". Le skill con sole modifiche minori **non compaiono mai nella mail**, nemmeno il lunedì, nemmeno dopo settimane.
- **Eccezione, stesso giorno anche se non è lunedì:** una patch di sicurezza di una piattaforma che Cristiano o i suoi clienti fanno girare (Redmine, PrestaShop, WordPress, WooCommerce) o una scadenza entro 14 giorni che richiede un'azione sul pannello (fine di una versione API, obbligo di policy, opt-out). In quel caso la mail parte subito con le sole skill urgenti; le altre aspettano il lunedì. Nel report si scrive perché era urgente.
- Se il lunedì nessuna skill ha una modifica sostanziale: nessuna mail. Il repository resta comunque aggiornato ogni giorno: chi vuole lo zip prima della mail lo trova in `dist/`.
- Se Cristiano scrive «manda la mail» in chat, la mail parte quel giorno con tutte le sostanziali in attesa, qualunque giorno sia.
- **Se il connettore Gmail non è disponibile nella sessione**, il passo B4 si salta e lo si scrive nel report; per la mail del lunedì: (succede quando la routine è stata creata senza connettori) stesso contenuto, ma si apre una **issue su GitHub** nel repository `crisgallo/skill` con gli strumenti `mcp__github__*` (titolo = oggetto della mail, corpo = corpo della mail). GitHub la recapita per email al proprietario del repository. Anche in questo caso: nessuna issue se nulla è cambiato.
- **Se il connettore Google Drive non è disponibile**, il passo B (B1, B2 e B3) si salta e lo si scrive nel report, così Cristiano sa che le modifiche locali e quelle delle chat di quel giorno non sono state raccolte.

## E. Prova di completamento (obbligatoria)
Il giro NON è finito finché non sono vere tutte e tre queste cose, verificate con comandi e non a memoria:
1. `git log origin/<ramo> -1` mostra il commit di oggi ("Giro del AAAA-MM-GG"): il push è avvenuto davvero.
2. `reports/AAAA-MM-GG.md` esiste sul remoto (`git show origin/<ramo>:reports/AAAA-MM-GG.md`).
3. `snapshots/state.json` esiste sul remoto.
Se una delle tre è falsa, si ripete commit e push finché non è vera. Chiudere la sessione con file solo in staging, o con un "fatto" non provato, è un giro fallito. Il giro del 21/09/2026 è finito così: cinque minuti di lavoro, nulla su GitHub.

## Cosa non fare mai
- Chiudere la sessione senza aver eseguito il passo E.
- Modificare o cancellare una riga ✅ VERIFICATO.
- Committare una skill che non passa `quick_validate.py`.
- Mandare una mail quando non è cambiato nulla, o per modifiche solo minori (non vanno mai per mail), o con un oggetto diverso da `Skill aggiornate`, o in un giorno diverso dal lunedì senza un'urgenza (patch di sicurezza, scadenza entro 14 giorni) o una richiesta esplicita di Cristiano.
- Scrivere "VERIFICATO" su qualcosa letto da una pagina web.
- Accorciare una skill per farla stare: se serve spazio, si sposta materiale in un file `references/` nella stessa cartella e si linka.

## Dove gira la routine, e come si sposta

La routine è legata a una sessione claude.ai code che ha il repository collegato (permessi di push), Gmail e Google Drive: ogni mattina si sveglia lì. Le sessioni create da zero dalle routine non hanno i permessi di push, e il giro fallisce in silenzio (successo il 21/09/2026, due volte).

Per spostarla su una chat nuova:
1. Aprire una chat nuova su claude.ai code collegata a `crisgallo/skill`, con Gmail e Google Drive attivi.
2. Dirle: "Leggi ROUTINE.md e crea la routine giornaliera delle 10:00 ora italiana legata a questa sessione (create_trigger senza sessione nuova, cron `0 8 * * *` in UTC), con il prompt di ROUTINE-prompt.md adattato a una sessione che ha già il repository".
3. Cancellare la routine vecchia dalla pagina delle routine di claude.ai.

Nulla di indispensabile vive nella chat: istruzioni, script, stato e report stanno nel repository.
