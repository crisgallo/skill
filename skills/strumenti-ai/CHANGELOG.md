# Changelog strumenti-ai

## 25/11/2026
- 🟡 Sez. 1: Claude Opus 4.5 deprecato, ritiro dall'API il 22/01/2027 (release notes del 23/11/2026); script con il vecchio ID da migrare a Opus 5.5.

## 24/11/2026
- 🟡 Sez. 2: Claude Sheets, modifiche evidenziate cella per cella e sole funzioni di base, export .xlsx o CSV o Claude for Excel; Claude Data per i cruscotti, Sheets per i fogli da compilare (articolo riletto il 24/11/2026 via Mother).

## 23/11/2026
- 🔴 Sez. 2: crediti di utilizzo a consumo dopo i limiti (Impostazioni > Utilizzo, limite di spesa mensile, tariffe API, separati dai crediti API mensili) e pacchetti prepagati scontati (50/250/1.000 $ con 10/20/30%, tetto 2.000 $ al mese, 3.000 per i Team), articoli support.claude.com letti il 23/11/2026.

## 22/11/2026
- 🔴 Sez. 2: Claude Whiteboards e Sheets in beta e Claude Data (ex Dashboards) disponibile a tutti dal 10/11/2026 su tutti i piani a pagamento (articolo ufficiale letto il 22/11/2026): query certificate, condivisione live, cache, connettore dati necessario, default per Team ed Enterprise, connettori interattivi come app.

## 21/11/2026
- 🟡 Sez. 4: quando Claude Code legge AGENTS.md (quali CLAUDE.md contano, riga di avvio, sottocartelle, differenze sugli hook e sugli import), pagina memory riletta il 21/11/2026.

## 19/11/2026
- 🟡 Sez. 1: moltiplicatore 1,1x per l'inferenza solo negli Stati Uniti (inference_geo) dai modelli 4.6 in poi, prezzi di lettura dalla cache per modello (pagina prezzi riletta il 19/11/2026).

## 17/11/2026
- 🔴 Sez. 7: Competenze dell'app desktop solo da plugin o da Personalizza > Competenze > Carica una competenza, `~/.claude/skills` ignorata, percorsi assoluti, valide solo nelle chat nuove (verificato il 16/11). Sez. 8: regole di Cristiano del 10-16/11 (spiegare il task prima di eseguirlo salvo compiti da Mother; domanda con consiglio; pagine pubbliche nel browser integrato e login su Chrome; Cristiano parla con Mother).

## 14/11/2026
- 🟡 Sez. 0, 1, 2: Claude Code 2.1.325; raccomandazione ufficiale «start with Opus 5.5 for most workloads»; `/usage` con la ripartizione del consumo per skill, subagenti, plugin e MCP, `/insights`. Pagine di Claude Code aggiornate il 12/11 sera: regole riscontrate invariate. Data in cima al 14/11/2026.

## 13/11/2026
- 🔴 Sez. 8: due regole globali di Cristiano, «la chat fa dopo il permesso» (12/11/2026) e «la skill apposita si carica prima di ogni attività» (01/10, aggiornata il 12/11/2026: ricarica dopo la compattazione, skill sopra 20 KB a un sottoagente, Competenze su Cowork, controlli locali dal 01/11 e dal 12/11). 🟡 Sez. 6: caso Atlassian MCP v2 (v1 fino al 01/03/2027, connettori v1 su Claude da rifare, Trello escluso). Data in cima al 13/11/2026.

## 12/11/2026
- 🔴 Skill nuova, richiesta da Cristiano il 12/11/2026 dopo l'ingresso delle newsletter AI Builders Club fra le fonti. Nove sezioni: modelli e prezzi API (Fable 5.2 dal 09/11/2026 a 8/40 $, Opus 5.5 4/20, Sonnet 5.5 2/10, Haiku 5.5 0,10/0,50; contesto 1M, output 128K, batch a metà, fast mode doppio, date di ritiro); piani e limiti (Free, Pro 17/20 $, Max 100 $ 5x con 100 $ di crediti API, Ultra 200 $ 10x senza finestra di 5 ore, Team, Enterprise; due finestre di limite, cosa consuma, costi medi di Claude Code; dichiarazioni della newsletter su inclusione e reset marcate [DA VERIFICARE]); skill (specifica: nome 1-64 minuscolo uguale alla cartella senza «anthropic» né «claude», descrizione 1-1.024, corpo sotto 500 righe, tre livelli di caricamento; caricamento in Personalizza > Skill con zip a radice cartella, errori tipici, sincronizzazione in Claude Code 2.1.273+, campi solo Claude Code, 1.536 caratteri e 5.000/25.000 token dopo la compattazione; discrepanza del centro assistenza sui 200 caratteri); Claude Code (CLAUDE.md a quattro livelli concatenati sotto 200 righe, regole, import, memoria automatica, settings e precedenza, modalità dei permessi, resume, compact, osservazione di Cristiano sulla compattazione sopra 200.000 token e rotazione dalla quinta, riferimenti @ a 25.000 token, subagenti, worktree, lista per spendere meno); sessioni cloud e attività pianificate (piani, ambienti Default Limited, GitHub App, --cloud e teleport, routine che non fanno domande, scadenza, condivisione, Remote Control); connettori MCP (percorso, un solo connettore sul Free, autenticazione, infrastruttura Anthropic, avvertenze di sicurezza, modalità Ricerca); Cowork («now just Claude», solo desktop per le cartelle locali, computer use in anteprima); pratiche d'uso ufficiali e le sei regole della newsletter come segnale; cosa non fare mai. Fonti: 21 pagine ufficiali lette il 12/11/2026 (platform.claude.com, claude.com, support.claude.com, code.claude.com, agentskills.io, modelcontextprotocol.io, GitHub).
