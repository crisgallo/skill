---
name: "strumenti-ai"
description: "Regole operative verificate per usare gli strumenti Anthropic da consulente, senza fare lo sviluppatore: modelli e prezzi API (Fable 5.2, Opus 5.5, Sonnet 5.5, Haiku 5.5), piani Free, Pro, Max, Ultra, Team ed Enterprise con i limiti d'uso a finestre di 5 ore e settimanali, skill personalizzate (formato SKILL.md, limiti di nome e descrizione, zip, caricamento dalla pagina Personalizza, voce Skill, sincronizzazione con Claude Code), Claude Code (CLAUDE.md, impostazioni, modalità dei permessi, compattazione, subagenti, costi), sessioni cloud e attività pianificate, connettori MCP personalizzati, Cowork e app desktop. Usala ogni volta che si sceglie un modello o un piano, si scrive o si carica una skill, si monta una routine, si collega un connettore, si legge una fattura o un limite d'uso, o una newsletter racconta una novità di Claude da verificare."
---

# Strumenti AI di Anthropic: regole operative

**Ultima verifica delle fonti: 13 novembre 2026.**

## 0. Manutenzione di questa skill (leggere per primo)

1. **Finestra di freschezza: un mese** per modelli, prezzi e piani, **due settimane** per Claude Code, che esce quasi ogni giorno (versione 2.1.322 al 12/11/2026). Se la data qui sopra è più vecchia, prima di consigliare un piano o un modello si rileggono le pagine in Fonti.
2. **Quando una fonte smentisce una regola scritta qui si aggiorna la skill nello stesso turno**, si riscrive la data in cima e si annota cosa è cambiato e da quando.
3. Dove si guardano i cambiamenti: [release notes della piattaforma](https://platform.claude.com/docs/en/release-notes/overview) · [release notes delle app Claude](https://support.claude.com/en/articles/12138966-release-notes) · [CHANGELOG di Claude Code](https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md) · [newsroom](https://www.anthropic.com/news). ⚠️ `docs.anthropic.com` reindirizza a `platform.claude.com` (301, 12/11/2026): i link vecchi funzionano ancora, quelli nuovi si scrivono sul dominio nuovo.
4. Due metà da tenere distinte: **conoscenza di dominio** (verificata sulle pagine ufficiali, con link inline) e **meccanica del pannello** (quello che si vede su claude.ai, nell'app desktop e nel terminale, con la data della prova). Le newsletter di terzi (AI Builders Club e simili) sono **segnali**: entrano qui solo dopo la verifica sulla pagina ufficiale, altrimenti restano marcate [DA VERIFICARE].
5. Il nome di una skill non può contenere le parole «anthropic» né «claude» (sez. 3): per questo questa skill si chiama `strumenti-ai`.

---

## 1. Modelli e prezzi API (verificati il 12/11/2026)

Quattro modelli correnti, tutti con **finestra di contesto da 1 milione di token, 128.000 token di output massimo e conoscenza affidabile fino a giugno 2026** ([panoramica modelli](https://platform.claude.com/docs/en/about-claude/models/overview), [prezzi](https://platform.claude.com/docs/en/about-claude/pricing)). Prezzi in dollari per milione di token, input / output:

| Modello | ID API | Prezzo | Sforzo di default | Ritiro non prima del |
|---|---|---|---|---|
| Fable 5.2 (dal 09/11/2026) | `claude-fable-5-2` | 8 / 40 | alto | 09/11/2027 |
| Opus 5.5 | `claude-opus-5-5` | 4 / 20 | medio | 22/09/2027 |
| Sonnet 5.5 | `claude-sonnet-5-5` | 2 / 10 | alto | 28/09/2027 |
| Haiku 5.5 (dal 07/10/2026) | `claude-haiku-5-5` | 0,10 / 0,50 fino a 100.000 token di prompt; 0,50 / 2,50 oltre | medio | 07/10/2027 |

- **Fable 5.2 costa il doppio di Opus 5.5** su input e output; la lettura dalla cache costa 0,20 per entrambi. **Batch API: metà prezzo** su tutti i modelli (Fable 4 / 20, Opus 2 / 10, Sonnet 1 / 5). **Fast mode** raddoppia il prezzo (Fable 16 / 80, Opus 8 / 40). Solo Haiku 5.5 ha la tariffa lunga oltre i 100.000 token di prompt.
- Fable 5.2 è «costruito per il ragionamento esigente e il lavoro agentico lungo»; Mythos 5.2 ha le stesse capacità ma solo per organizzazioni verificate ([release notes 09/11/2026](https://platform.claude.com/docs/en/release-notes/overview)). Opus 4.1, Opus 4 e Sonnet 4 sono ritirati salvo su Google Cloud e Bedrock.
- **Come si sceglie, con i numeri davanti:** per il lavoro di tutti i giorni (analisi, testi, dati) Sonnet 5.5 o Opus 5.5; Fable 5.2 per i compiti lunghi e difficili dove il costo doppio si ripaga. Il confronto a sei lavori della newsletter AI Builders Club dell'11/11/2026 (Fable più forte su grafica e cose nuove, Opus pari sui conti e sul foglio di calcolo spendendo circa la metà, 189 contro 123 dollari a consumo) è **una prova di terzi**, non un benchmark Anthropic: si cita come esperienza, non come regola.
- Per le fatture a consumo: nella Console l'area di lavoro «Claude Code» nasce da sola al primo accesso e **i tetti di spesa si impostano per area di lavoro** ([costi](https://code.claude.com/docs/en/costs)).

---

## 2. Piani e limiti d'uso (pagina prezzi letta il 12/11/2026, solo dollari)

| Piano | Prezzo | Cosa porta |
|---|---|---|
| Free | 0 | uso limitato; un solo connettore personalizzato |
| Pro | 17 $/mese annuale (200 $ anticipati) o 20 $ mensile | uso 1x, Claude Code incluso |
| Max | 100 $/mese | uso 5x del Pro, 100 $/mese di crediti API |
| Ultra | 200 $/mese | uso settimanale 10x, **senza il limite delle 5 ore** per gli account verificati |
| Team | Standard 20 $/posto annuale o 25 $ mensile; Premium 100 $ annuale o 125 $ mensile (5x) | Claude Code e Cowork, connettore Slack |
| Enterprise | 20 $/posto/mese annuale, minimo 20 posti | uso a tariffe API |

Fonte: [claude.com/pricing](https://claude.com/pricing). Prezzi in euro non mostrati: la fattura italiana si legge sull'account, non si deduce.

- **Due finestre di limite, non una** ([best practice sui limiti](https://support.claude.com/en/articles/9797557-usage-limit-best-practices)): una **sessione di 5 ore** e un **limite settimanale**. Le barre si leggono in **Impostazioni > Utilizzo**. Nessun numero pubblico di messaggi o token: il limite dipende da lunghezza dei messaggi e degli allegati, lunghezza della conversazione, strumenti, modello, livello di sforzo, artefatti e compiti a più passi. Le sessioni cloud di Claude Code, i subagenti e le attività pianificate **consumano lo stesso limite** del piano ([sessioni cloud](https://code.claude.com/docs/en/claude-code-on-the-web)).
- **Cosa fa salire il consumo** ([costi di Claude Code](https://code.claude.com/docs/en/costs)): una conversazione lunga rimanda tutto il contesto a ogni richiesta; una pausa più lunga della vita della cache fa perdere la cache; `/compact` legge la conversazione che riassume, `/clear` non costa nulla. Prima di una conversazione nuova su un tema diverso si fa `/clear`.
- Numeri Anthropic sui costi di Claude Code in azienda: **circa 13 $ per sviluppatore per giorno attivo, 150-250 $ al mese**, sotto i 30 $ al giorno per il 90% degli utenti. Chi ha un abbonamento vede in `/usage` le barre del piano e il valore in dollari della sessione «non è rilevante per la fatturazione».
- [DA VERIFICARE] Dichiarazioni della newsletter AI Builders Club dell'11/11/2026, non trovate su pagine ufficiali: Fable 5.2 incluso nel Pro fino al 16/11/2026 con metà dei limiti settimanali; reset gratuiti dei limiti regalati agli abbonati Max al lancio (validi fino all'08/03/2027) e a tutti i paganti il 10/11 (valido fino al 10/12/2026), da attivare a mano nelle impostazioni. Si controlla su **Impostazioni > Utilizzo** prima di contarci.

---

## 3. Skill personalizzate: formato, limiti, caricamento

**Che cosa è una skill.** Una cartella con un file `SKILL.md` (frontmatter YAML più testo Markdown) e, se servono, `scripts/`, `references/`, `assets/`. Claude carica a tre livelli: all'avvio solo nome e descrizione (**circa 100 token per skill**), il corpo quando la skill scatta (**sotto i 5.000 token consigliati**), i file collegati solo quando li apre ([panoramica Agent Skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview), [specifica](https://agentskills.io/specification)). La descrizione decide se la skill scatta: deve dire **cosa fa e quando si usa**, con le parole che l'utente userebbe.

**Limiti del frontmatter (specifica, 12/11/2026):**
- `name`: da 1 a 64 caratteri, **solo minuscole, cifre e trattini**, non inizia né finisce con un trattino, niente `--`, **uguale al nome della cartella**; **non può contenere «anthropic» né «claude»**.
- `description`: da 1 a 1.024 caratteri, niente tag XML. ⚠️ L'articolo del centro assistenza [Creating custom skills](https://support.claude.com/en/articles/12512198-creating-custom-skills) dice ancora «200 caratteri» e scrive `skill.md` minuscolo: valgono la specifica e la piattaforma (1.024 e `SKILL.md`), ma una descrizione sopra i 200 caratteri si prova prima di darla per buona su claude.ai [DA VERIFICARE].
- Facoltativi: `license`, `compatibility` (1-500 caratteri, quasi mai necessario), `metadata`, `allowed-tools` (sperimentale).
- **Corpo sotto le 500 righe**; i file di riferimento a un livello solo da `SKILL.md`. Validazione: `skills-ref validate ./cartella`, oppure lo script `quick_validate.py` della skill `skill-creator` (deve dire «Skill is valid!»).

**Su claude.ai** ([Using skills in Claude](https://support.claude.com/en/articles/12512180-using-skills-in-claude)): serve **Impostazioni > Funzionalità > Esecuzione del codice e creazione di file** acceso; le skill si gestiscono in **Personalizza > Skill** (`claude.ai/customize/skills`): «+», «Crea skill», «Carica una skill», **zip con la cartella della skill come radice** (non i file sciolti, non una cartella dentro un'altra); il nome della cartella deve coincidere con `name`. Errori tipici: «Skill folder name doesn't match the skill name», «Missing required skill.md file», «Invalid characters in skill name or description», «ZIP file exceeds size limits» (limite numerico non pubblicato). Le skill Anthropic (Excel, Word, PowerPoint, PDF) scattano da sole. Su Team ed Enterprise si abilitano da Impostazioni dell'organizzazione > Plugin e skill; le skill condivise sono in sola lettura per chi le riceve. Piani: la pagina del centro assistenza dice anche Free; la pagina della piattaforma elenca il caricamento su Pro, Max, Ultra, Team ed Enterprise [DA VERIFICARE sul Free].

**Sostituire una skill caricata:** si elimina la vecchia dalla sua scheda in Personalizza > Skill e si carica lo zip nuovo; le skill su claude.ai **non si aggiornano da sole** e non si sincronizzano con l'API né con le skill su disco di Claude Code.

**In Claude Code** ([skills](https://code.claude.com/docs/en/skills)): personali in `~/.claude/skills/<nome>/SKILL.md` (**non caricate in Cowork né nelle sessioni cloud**), di progetto in `.claude/skills/<nome>/` (si committa), dei plugin in `<plugin>/skills/`; le skill abilitate su claude.ai arrivano in `~/.claude/skills/synced/` (richiede Claude Code 2.1.273 o successivo, `/skills` le mostra sotto «claude.ai sync», `syncClaudeAiSkills: false` spegne la sincronizzazione; la cartella `synced` è riservata). Si invocano da sole o con `/nome`; `disable-model-invocation: true` toglie l'invocazione automatica, `user-invocable: false` le nasconde dal menu `/`. Campi solo di Claude Code: `context: fork` (gira in un subagente che **non vede la conversazione**), `agent`, `model`, `effort`, `allowed-tools`, `paths`, `hooks`. Numeri: descrizione più `when_to_use` **troncate a 1.536 caratteri** nell'elenco; dopo una compattazione vengono riallegati **i primi 5.000 token** di ogni skill invocata entro un budget di **25.000 token**. Le modifiche a `SKILL.md` si vedono senza riavviare.

**Sicurezza:** «Use Skills only from trusted sources»; mai chiavi API o password dentro una skill; si legge una skill scaricata prima di abilitarla. **Registrare una skill** (dimostrazione dal vivo) esiste solo in Cowork su Mac per Pro, Max, Ultra e Team.

---

## 4. Claude Code: file di memoria, impostazioni, contesto

Claude Code è «uno strumento agentico che legge il codice, modifica file, esegue comandi» e gira nel **terminale**, nelle **estensioni** VS Code e JetBrains, nell'**app desktop** (che include Claude Code) e sul **web** a claude.ai/code, con le app iOS e Android per le sessioni web; serve un abbonamento Claude o un account Console ([panoramica](https://code.claude.com/docs/en/overview)). Per un consulente serve a far girare routine, leggere cartelle e repository, scrivere documenti: non è solo per programmare.

**CLAUDE.md e memoria** ([memory](https://code.claude.com/docs/en/memory)):
- Quattro livelli, letti dal più largo al più stretto e **concatenati, nessuno sovrascrive l'altro**: criteri gestiti dall'azienda, utente (`~/.claude/CLAUDE.md`), progetto (`./CLAUDE.md` o `./.claude/CLAUDE.md`, nel repository), locale (`./CLAUDE.local.md`, da mettere in `.gitignore`). Le regole in `.claude/rules/*.md` con `paths` si caricano solo quando si toccano quei file. Se due istruzioni si contraddicono «Claude può sceglierne una a caso»: si tolgono i doppioni.
- **Sotto le 200 righe per file**; `@percorso` importa un altro file (massimo quattro salti, gli import non riducono il costo di contesto). CLAUDE.md è **contesto, non configurazione imposta**: un divieto vero si mette in `permissions.deny` o in un hook. `/init` crea il file, `/memory` elenca i file caricati, `/context` mostra cosa occupa la finestra, `/doctor prompt-audit` cerca istruzioni vecchie o in conflitto.
- **Memoria automatica** (accesa di default nelle sessioni locali): note su utente, feedback, progetto e riferimenti in `~/.claude/projects/<progetto>/memory/`, indice `MEMORY.md` caricato per le prime 200 righe o 25 KB; è per macchina, **non passa fra computer né nel cloud**. Si spegne in `/memory` (`autoMemoryEnabled`).
- `AGENTS.md` viene letto solo se non c'è nessun CLAUDE.md.

**Impostazioni e permessi** ([settings](https://code.claude.com/docs/en/settings)): `~/.claude/settings.json` (utente), `.claude/settings.json` (progetto, si committa), `.claude/settings.local.json` (solo questa macchina), impostazioni gestite; precedenza dalle gestite in giù, le liste `permissions.allow/deny/ask` **si sommano** fra i file. JSON stretto, senza commenti né virgole finali; `/status` dice da dove arriva ogni impostazione, `claude doctor` elenca le voci rifiutate. Modalità dei permessi: `default` (chiede), `acceptEdits`, `plan` (**Shift+Tab**: propone un piano e non modifica nulla finché non si approva), `auto`, `dontAsk`, `bypassPermissions`; `auto` e `bypassPermissions` valgono solo da impostazioni utente o gestite o da `--permission-mode` per sessione. `/model` salva il modello di default, `/effort` il livello di sforzo. `~/.claude.json` lo scrive Claude Code (account, MCP, decisioni di fiducia): non si modifica a mano.

**Contesto, compattazione, sessioni:**
- Ogni conversazione è salvata in locale: `claude --continue` riprende l'ultima nella cartella, `claude --resume` sceglie dall'elenco, `/resume` dentro la sessione; `/rename` prima di chiudere aiuta a ritrovarla.
- `/compact` riassume la conversazione (si può dare un'istruzione: `/compact Tieni i numeri e i link`) e **costa token perché rilegge tutto**; una sezione «Compact instructions» in CLAUDE.md guida il riassunto. 📌 **Osservazione di Cristiano (10/11/2026, skill trello sez. 10):** l'app compatta da sola ogni chat **sopra i 200.000 token ferma più di un'ora**, quindi la compattazione è un evento quotidiano; dopo ogni compattazione si rileggono le fonti di verità (card, file di stato), non ci si fida del riassunto, e una chat si gira **dalla quinta compattazione**, dicendolo a Cristiano.
- I riferimenti `@file` entrano fino a **25.000 token** per file e i file sopra **256 KB** non entrano; le cartelle danno solo l'elenco. Le immagini si trascinano o si incollano (Ctrl+V, Alt+V su Windows).
- **Subagenti** ([sub-agents](https://code.claude.com/docs/en/sub-agents)): assistenti con la propria finestra di contesto, utili per «isolare le operazioni che producono molto output» (leggere pagine, cercare nei file) senza sporcare la conversazione principale; consumano lo stesso limite. Integrati: **Explore** (sola lettura, veloce), **Plan**, **general-purpose**; Explore e Plan partono senza CLAUDE.md. Si definiscono in `.claude/agents/` (progetto) o `~/.claude/agents/` (utente), con `name` e `description` obbligatori e `model` a scelta (`sonnet`, `opus`, `haiku`, `fable`, `inherit`). I team di agenti in modalità piano consumano **circa 7 volte** più token.
- **Lavoro in parallelo**: `claude --worktree <nome>` apre una copia separata del repository su un ramo proprio (serve almeno un commit).
- **Per spendere meno** (lista Anthropic): `/clear` fra compiti diversi, Sonnet per la maggior parte del lavoro e Opus o Fable per il ragionamento difficile, `/effort` più basso, server MCP inutili spenti con `/mcp`, **istruzioni di procedura spostate da CLAUDE.md alle skill**, lavoro verboso delegato ai subagenti, modalità piano prima dei cambi grandi, Escape per fermare e `/rewind` per tornare indietro.

---

## 5. Sessioni cloud, attività pianificate, Remote Control

- **Chi le ha**: Pro, Max, Ultra, Team ed Enterprise con posti premium o Chat + Claude Code ([sessioni cloud](https://code.claude.com/docs/en/claude-code-on-the-web)). Girano su macchine virtuali di Anthropic, **continuano a chiusura del portatile**, consumano il limite del piano e **non hanno un costo a parte per la macchina**.
- Si aprono da claude.ai/code, dalla scheda Code dell'app mobile, dall'app desktop (selettore «Cloud environment»), da `claude --cloud "..."` nel terminale e dalle attività pianificate. `--cloud` clona il remoto GitHub al ramo corrente: **prima si fa push**; senza remoto o senza GitHub App il repository viene impacchettato (limite 100 MB, i file non tracciati restano fuori).
- **Ambienti**: configurazione salvata con accesso di rete, variabili e script di avvio; il primo si chiama **Default** e parte con rete «Limited». Lo script di avvio è messo in cache solo se finisce in **circa cinque minuti**. GitHub: serve la **Claude GitHub App** (indispensabile per Auto-fix, che segue una PR e corregge CI e commenti), oppure `/web-setup` con il proprio token.
- Da cloud a locale: `claude --teleport` (o `/teleport`) riporta la sessione nel terminale, con git pulito e lo stesso account. Da locale si continua una sessione cloud con `claude -p "messaggio" --cloud <id>`.
- **Attività pianificate** (`/schedule`, pagina claude.ai/code/routines; prima si chiamavano «routines»): girano in autonomia e **non possono fare domande**, quindi il prompt deve bastare da solo e le regole devono stare nel repository, non nella testa della chat (il modello è `ROUTINE.md` di questo repository). Alternative: attività pianificate del desktop, GitHub Actions, `/loop` nella sessione corrente.
- Le sessioni cloud **scadono dopo un periodo di inattività**: la conversazione si recupera, i comandi in corso e i `/loop` no. In cloud funzionano `/compact`, `/context` e `/clear`; `/config` apre il browser. Condivisione: Privata o Pubblica su Pro e Max, Privata o Team su Team ed Enterprise.
- **Remote Control** collega una sessione al proprio computer per leggere cartelle e usare il browser locale ([panoramica](https://code.claude.com/docs/en/overview)); una sessione resta legata al primo computer a cui si attacca.

---

## 6. Connettori e MCP

- **MCP** (Model Context Protocol) è «uno standard open source per collegare le applicazioni AI a sistemi esterni», «come una porta USB-C per le applicazioni AI» ([introduzione](https://modelcontextprotocol.io/docs/getting-started/intro)): file, database, strumenti e flussi di lavoro arrivano a Claude attraverso server MCP, locali o remoti.
- **Connettori personalizzati su claude.ai** ([guida](https://support.claude.com/en/articles/11175166-getting-started-with-custom-connectors-using-remote-mcp)): Pro e Max da **Personalizza > Connettori > «+ Aggiungi» > «Aggiungi connettore personalizzato»**, con nome e URL del server; Team ed Enterprise da Impostazioni dell'organizzazione > Connettori (solo Owner e Primary Owner su Team). **Il Free ha un solo connettore personalizzato.** Autenticazione: accesso subito, quando serve o nessuno; client OAuth «identità pubblicata di Claude» (consigliata), registrazione automatica o proprio client; intestazioni per chiavi API. Si accendono per conversazione dal «+» > Connettori. Per modificare un connettore si rimuove e si ricrea.
- Claude si collega al server **dall'infrastruttura cloud di Anthropic**: un server su rete privata deve ammettere gli IP di Anthropic.
- ⚠️ **Sicurezza, parole di Anthropic**: i connettori personalizzati collegano Claude a «servizi arbitrari non verificati da Anthropic»; si leggono gli scope OAuth richiesti, si tengono d'occhio prompt injection e cambi di comportamento degli strumenti; in modalità Ricerca gli strumenti dei connettori girano **senza ulteriore approvazione**, quindi gli strumenti che scrivono si disabilitano. Su Team ed Enterprise «tutti quelli che usano il connettore raggiungono il servizio con la stessa credenziale».
- In Claude Code i server MCP si gestiscono con `/mcp` e pesano sul contesto (`/context` lo mostra): quelli inutili si spengono.
- 🟡 **Caso Atlassian, 12/11/2026** (mail «More tools, more products: upgrade Atlassian MCP» e [guida ufficiale di aggiornamento](https://support.atlassian.com/atlassian-ai-gateway/docs/how-to-upgrade-from-atlassian-mcp-v1-to-atlassian-mcp-v2/), lette il 13/11/2026): la versione 2 del server MCP Atlassian copre Jira, Confluence, Loom, Bitbucket, Goals, Projects, Teams, Focus e Talent; **la v1 (Rovo MCP) resta fino al 01/03/2027**, poi espone da sola gli strumenti v2. Su Claude, app desktop e web, le connessioni v1 **diventano connettori «Custom Web»**: si rimuovono e si reinstalla il connettore v2 dall'elenco Atlassian; in Claude Code l'URL in `~/.claude.json` passa a `https://mcp.atlassian.com/v2/mcp` e si rifà l'accesso. **Trello non è fra i prodotti elencati**: il connettore Trello usato nelle chat è un server a parte (skill trello sez. 8). Regola generale: quando un fornitore cambia versione del server MCP, il connettore vecchio non si aggiorna da solo e va rifatto.

---

## 7. Cowork e app desktop

- La pagina ufficiale ([claude.com/product/cowork](https://claude.com/product/cowork), letta il 12/11/2026) dice «Claude Cowork is now just Claude. Rolling out to Pro, Max, and Ultra, with more plans to follow»: Cowork è la modalità in cui Claude «porta a termine compiti che si possono guidare da ovunque», lavorando «nelle cartelle e negli strumenti che scegli». Team ed Enterprise lo includono; il Free non è elencato.
- **Solo l'app desktop raggiunge cartelle e applicazioni locali**; web e mobile no. Il pulsante di download è per macOS; Windows non è nominato nella pagina [DA VERIFICARE]. Cancellare qualcosa richiede sempre approvazione; Claude usa prima connettori e integrazioni; le **attività pianificate** girano senza presidio «a qualunque cadenza»; il **browser integrato** c'è su Pro, Max, Ultra e Team desktop; il **computer use è in anteprima di ricerca** sia in Cowork sia in Claude Code.
- I compiti agentici «consumano più capacità della chat normale»: su un piano Pro una giornata di Cowork può esaurire la finestra di 5 ore prima di una giornata di chat.
- Enterprise: gli amministratori possono spegnere Cowork, limitarlo per team e leggere l'attività via OpenTelemetry. Le skill caricate su claude.ai valgono anche in Cowork; quelle personali su disco di Claude Code no (sez. 3).

---

## 8. Come si lavora con Claude: regole ufficiali e segnali di terzi

**Dalle pagine Anthropic (sez. 4 e 5):** obiettivo chiaro e contesto nel prompt, modalità piano prima dei cambi grandi, `/clear` fra compiti diversi, subagenti per il lavoro che produce molto testo, procedure nelle skill e non in CLAUDE.md, CLAUDE.md sotto le 200 righe, un'attività pianificata scritta come se nessuno potesse rispondere.

📌 **Regole di Cristiano su come lavorano le chat (file di regole globali su Drive, lette il 13/11/2026):**
- **La chat fa, dopo il permesso; non chiede a Cristiano di fare** (`feedback_fare_non_far_fare.md`, 12/11/2026, globale). Quello che la chat può fare con gli strumenti che ha (pubblicare un post o una Nota, programmare, premere un tasto su un pannello, salvare, caricare, spostare) non lo passa a Cristiano: scrive cosa sta per fare, **chiede il permesso con una domanda sola a risposta sì o no** che dice cosa, dove e quando, e col sì lo fa lei, poi verifica il risultato dove lo vede chi lo usa. Il permesso vale per quell'azione e non si estende alla successiva né a un testo cambiato dopo. Restano a Cristiano le email e i messaggi di progetto (solo bozza) e quello che le chat non fanno nemmeno col permesso: pagamenti, trasferimenti di denaro, password, codici e passkey, creazione di account, accettazione di termini. Parole sue, 12/11/2026: «smetti di chiedermi di fare le cose, chiedimi il permesso di farle». Le routine seguono il loro prompt.
- **La skill apposita si carica prima di ogni attività** (`feedback_skill_prima_di_ogni_attivita.md`, 01/10/2026, aggiornato il 12/11/2026, globale). Prima del primo passo di qualunque lavoro (documento, email, report, foglio, card, pannello, campagna) si scorre l'elenco delle skill e si carica quella che lo copre, **prima dell'errore e nel dubbio sempre**; fra una generica e una specifica vale la specifica; se il lavoro cambia a metà si ricarica quella nuova; **dopo una compattazione il testo delle skill non è più nel contesto e si ricarica**; le skill **sopra i 20 KB** le legge un sottoagente con la domanda precisa, non la chat principale. Se servirebbe una skill che non esiste, la si propone a Cristiano in una riga e solo col suo sì la si chiede alla chat delle skill. Da sapere: su Cowork le skill si chiamano **Competenze**; con due copie dello stesso nome vale quella in `/mnt/skills/plugins/` e si controlla la data di verifica in cima (il 20/09/2026 una copia vecchia in `/mnt/skills/user/` ha fatto sbagliare una soglia). Dal 01/11/2026 sui Mac di Cristiano un controllo locale rifiuta di aprire un pannello coperto da una skill se la skill non è caricata, e dal 12/11 ferma la scrittura finché la skill dovuta non è letta.

**Dalla newsletter AI Builders Club del 06/11/2026 (Michele Cotti, «sei nuove regole»), opinione di terzi non verificata su pagine Anthropic, [DA VERIFICARE] prima di farne regola:** 1) dare l'obiettivo e non il compito («voglio che mi paghi entro venerdì senza rovinare il rapporto» invece di «scrivi un sollecito»); 2) togliere le frasi magiche («agisci come», «ragiona passo passo»); 3) al posto del piano un brief di tre righe: cosa fare, cosa non toccare, come capisce di aver finito; 4) far ricontrollare il lavoro da una chat nuova con l'elenco dei punti; 5) skill al posto di un agente per ogni lavoro, e ogni tanto rifare il lavoro senza skill per vedere se serve ancora; 6) prima di consegnare, cinque revisori con un motivo diverso per bocciare. Le regole 3, 4 e 5 coincidono con pratiche già scritte nelle pagine ufficiali (piano, subagenti, skill); la 1 e la 2 sono stile di prompt; la 6 è un metodo di revisione. L'affermazione che «il creatore di Claude Code ha scritto che il plan mode non è più utile» non ha fonte citata.

---

## 9. Cosa non fare mai

- Consigliare un modello o un piano senza aver riletto prezzi e limiti nelle ultime quattro settimane.
- Dare per ufficiale un numero letto in una newsletter (crediti, reset, inclusione di un modello in un piano) senza averlo visto su una pagina Anthropic o in Impostazioni > Utilizzo.
- Caricare una skill con uno zip dei file sciolti, con una cartella dal nome diverso da `name`, o con «claude» o «anthropic» nel nome.
- Credere che una skill caricata su claude.ai si aggiorni da sola, o che una skill su disco di Claude Code valga in Cowork o nel cloud.
- Mettere chiavi, password o dati di clienti dentro una skill, un CLAUDE.md o un connettore condiviso con il team.
- Accendere un connettore personalizzato con strumenti di scrittura in modalità Ricerca.
- Scrivere un'attività pianificata che aspetta una risposta: nessuno risponde.
- Fidarsi del riassunto dopo una compattazione: si rileggono card, file di stato e fonti (regola di Cristiano del 10/11/2026).
- Modificare `~/.claude.json` a mano o mettere commenti nei file `settings.json`.

---

## Fonti (lette il 12/11/2026)

**Modelli, prezzi, piani:** [Panoramica modelli](https://platform.claude.com/docs/en/about-claude/models/overview) · [Prezzi API](https://platform.claude.com/docs/en/about-claude/pricing) · [Release notes piattaforma](https://platform.claude.com/docs/en/release-notes/overview) · [Prezzi dei piani](https://claude.com/pricing) · [Best practice sui limiti d'uso](https://support.claude.com/en/articles/9797557-usage-limit-best-practices) · [Release notes app Claude](https://support.claude.com/en/articles/12138966-release-notes) · [Newsroom, Fable 5.2 e Mythos 5.2 (09/11/2026)](https://www.anthropic.com/news).

**Skill:** [Agent Skills, panoramica](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) · [Specifica Agent Skills](https://agentskills.io/specification) · [Skill in Claude Code](https://code.claude.com/docs/en/skills) · [Usare le skill in Claude](https://support.claude.com/en/articles/12512180-using-skills-in-claude) · [Creare skill personalizzate](https://support.claude.com/en/articles/12512198-creating-custom-skills).

**Claude Code:** [Panoramica](https://code.claude.com/docs/en/overview) · [Memoria e CLAUDE.md](https://code.claude.com/docs/en/memory) · [Costi](https://code.claude.com/docs/en/costs) · [Impostazioni](https://code.claude.com/docs/en/settings) · [Flussi di lavoro comuni](https://code.claude.com/docs/en/common-workflows) · [Subagenti](https://code.claude.com/docs/en/sub-agents) · [Sessioni cloud](https://code.claude.com/docs/en/claude-code-on-the-web) · [CHANGELOG](https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md).

**Connettori e Cowork:** [Introduzione a MCP](https://modelcontextprotocol.io/docs/getting-started/intro) · [Connettori personalizzati](https://support.claude.com/en/articles/11175166-getting-started-with-custom-connectors-using-remote-mcp) · [Cowork](https://claude.com/product/cowork).

**Segnali di terzi (cronaca, non fonte):** newsletter AI Builders Club del 06/11 e dell'11/11/2026 (Michele Cotti), via Gmail di Cristiano.
