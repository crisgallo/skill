# Routine giornaliera di aggiornamento delle skill

Questo file è il compito che la sessione automatica esegue ogni mattina alle 10:00 ora italiana.
Si modifica qui, non nel trigger: il trigger dice solo "leggi ROUTINE.md ed eseguilo".

## Regole fisse

1. Il repository `crisgallo/skill` è la fonte di verità. Si lavora sul ramo predefinito, si committa e si spinge.
2. Le righe marcate **✅ VERIFICATO** con una data sono osservazioni fatte di persona sul pannello. **Non si toccano mai.** Se una fonte le smentisce, si aggiunge sotto una riga "⚠️ Nota del GG/MM/AAAA: la fonte X dice Y (URL). Da ricontrollare sul pannello." e basta.
3. Ogni regola nuova o modificata porta **data del cambio** (quella della piattaforma, non quella in cui ce ne siamo accorti) e **URL della fonte ufficiale** inline. Niente soglie da blog presentate come ufficiali: si etichettano "regola empirica di terzi".
4. Quando si modifica una skill: si riscrive la riga "Ultima verifica delle fonti" in cima, si aggiorna il blocco "Cosa è cambiato" se esiste, si aggiunge una voce datata in `skills/<nome>/CHANGELOG.md`, si valida con `quick_validate.py` (deve stampare "Skill is valid!"), si rigenera lo zip con `scripts/package.sh`.
5. Una skill sotto le 120 righe o sopra le 400 righe è un segnale di errore: si controlla prima di committare.
6. Non si inventa. Se una pagina non si legge (403, corpo vuoto), si scrive nel report che non si è potuta leggere e si passa oltre. Le pagine che rispondono 403 di solito sono: facebook.com/business/help, help.openai.com, help.trustpilot.com (usare l'API Zendesk), support.getharvest.com, help.ads.microsoft.com (usare lo specchio learn.microsoft.com), jonloomer.com, searchengineland.com.

## Passi

### A. Preparazione
- `git pull` sul ramo predefinito.
- Leggere `snapshots/state.json` (URL → hash del contenuto → data ultimo controllo). Se non esiste, questo è il primo giro: si crea la base e non si segnala nulla come "cambiato".

### B. Raccolta delle modifiche fatte da Cristiano in locale
- Su Google Drive cercare la cartella `skill_modificate_in_locale` (parentId noto: `1AEkZiDqkeA2Ydf96vWorV_9KKeGm7cvx`, ricercabile per titolo). Per ogni file `<skill>_SKILL_locale_<data>.md` più recente dell'ultima data registrata in `snapshots/state.json` sotto `locali`:
  - scaricarlo, confrontarlo con `skills/<skill>/SKILL.md`;
  - integrare le differenze nella skill del repository (le righe ✅ VERIFICATO nuove entrano così come sono);
  - registrare in `snapshots/state.json` la data del file trattato.
- Queste modifiche hanno la precedenza su qualsiasi fonte web: sono osservazioni dal pannello.

### C. Verifica delle fonti, una skill per volta
Per ogni cartella in `skills/`:
1. Leggere `SKILL.md`, la riga "Ultima verifica delle fonti" e la finestra di freschezza dichiarata in sezione 0.
2. Estrarre gli URL della sezione "Fonti" e quelli inline. Scaricare ogni URL (WebFetch). Calcolare un hash del testo utile. Confrontare con `snapshots/state.json`:
   - hash uguale: nulla da fare;
   - hash diverso: leggere la pagina e stabilire se la modifica tocca una regola scritta nella skill. Se sì, correggere la skill (regola 3 e 4). Se no, aggiornare solo l'hash.
3. Cercare sul web le novità delle ultime 24 ore sulla piattaforma (release notes, annunci ufficiali, changelog). Se una novità cambia una regola o ne aggiunge una operativa, integrarla con data e URL.
4. Se la data di ultima verifica supera la finestra di freschezza: fare una verifica completa delle regole numeriche della skill sulle fonti ufficiali, anche senza cambi di hash, e riscrivere la data.
5. Skill senza fonti web (`creditsafe-monitoraggio-credito`, `substack-intelligence`, `cristiano-gallinelli-persona`): solo passo B. Per la persona, ogni lunedì leggere `https://cristianogallinelli.blog/feed/` e, se c'è un articolo nuovo, aggiungere titolo, data, temi e lessico alla skill come fatto il 20/09/2026.

### D. Chiusura
- Rigenerare `dist/` con `scripts/package.sh`.
- Scrivere `reports/AAAA-MM-GG.md` con: skill controllate, URL cambiati, modifiche fatte (per skill, in una riga ciascuna), pagine non leggibili, modifiche locali integrate.
- Commit con messaggio "Giro del AAAA-MM-GG: <n> skill aggiornate" e push.
- **Solo se almeno una skill è stata modificata**: inviare una mail a gallinelli@gmail.com, oggetto "Skill aggiornate il GG/MM/AAAA: <elenco nomi>", corpo con: per ogni skill modificata, cosa è cambiato e perché (le voci del CHANGELOG di oggi), il link allo zip su GitHub (`https://github.com/crisgallo/skill/raw/<ramo>/dist/<nome>.zip`), e il promemoria: "Nel tuo account Claude, Personalizza > Skill: elimina la skill vecchia e carica questo zip". Se nulla è cambiato: nessuna mail.
- **Se il connettore Gmail non è disponibile nella sessione** (succede quando la routine è stata creata senza connettori): stesso contenuto, ma si apre una **issue su GitHub** nel repository `crisgallo/skill` con gli strumenti `mcp__github__*` (titolo = oggetto della mail, corpo = corpo della mail). GitHub la recapita per email al proprietario del repository. Anche in questo caso: nessuna issue se nulla è cambiato.
- **Se il connettore Google Drive non è disponibile**, il passo B si salta e lo si scrive nel report, così Cristiano sa che le modifiche locali di quel giorno non sono state raccolte.

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
- Mandare una mail quando non è cambiato nulla.
- Scrivere "VERIFICATO" su qualcosa letto da una pagina web.
- Accorciare una skill per farla stare: se serve spazio, si sposta materiale in un file `references/` nella stessa cartella e si linka.
