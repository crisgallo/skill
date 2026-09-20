---
name: "redmine-harvest"
description: "Regole operative verificate per lavorare da subappaltatore dentro il Redmine di una web agency e tenere le proprie ore su Harvest: leggere le notifiche email dei ticket, aggiornare le segnalazioni con l'etichetta giusta, registrare il tempo impiegato, tirare giù le ore del mese via REST API, riconciliarle con la fattura all'agenzia, tenere Harvest allineato senza contare le ore due volte, budget e report condivisi con i clienti via API v2, chiusura mensile. Usala ogni volta che arriva una mail di Redmine, che si parla di ore da fatturare, di timesheet, di report ore per un cliente, di budget di progetto o di API Redmine/Harvest, anche se la piattaforma non viene nominata."
---

# Redmine e Harvest: regole operative

**Ultima verifica delle fonti: 20 settembre 2026.**

## 0. Manutenzione di questa skill (leggere per primo)

1. **Finestra di freschezza: tre mesi per Redmine, due per Harvest.** Redmine cambia con release semestrali (7.0.0 il 30/06/2026, patch 7.0.1/6.1.4/6.0.11 il 26/08/2026) e le patch sono quasi sempre di sicurezza. Harvest dal maggio 2026 spinge funzioni "settimana dopo settimana" e ha cambiato interfaccia, permessi e prezzo nello stesso anno: le voci di menu descritte qui possono spostarsi.
2. **Quando una fonte smentisce una regola, si aggiorna la skill nello stesso turno**, si riscrive la data in cima e si annota cosa è cambiato e da quando (sez. 13).
3. **Due metà da tenere distinte.** Conoscenza di dominio (verificata sulle fonti ufficiali: wiki redmine.org, codice Redmine su GitHub, help.getharvest.com/api-v2) e meccanica del pannello (sez. 15: si impara sbagliando sull'istanza dell'agenzia e sul proprio account Harvest, e si scrive qui la prima volta). ⚠️ Il Redmine dell'agenzia è **una loro istanza, con la loro versione, i loro tracker, i loro stati e i loro permessi**: niente di quello che dice il wiki vale finché non lo si è visto sullo schermo di quella istanza.
4. Dove si guardano i cambiamenti: [news redmine.org](https://www.redmine.org/projects/redmine/news), [Changelog_7_0](https://www.redmine.org/projects/redmine/wiki/Changelog_7_0), [Changelog_6_1](https://www.redmine.org/projects/redmine/wiki/Changelog_6_1); Harvest: [blog "In Season"](https://www.getharvest.com/blog/tag/product-news) e [help.getharvest.com/api-v2](https://help.getharvest.com/api-v2/). ⛔ Il changelog API di Harvest all'URL storico risponde 404 e l'help center support.getharvest.com risponde 403 via fetch: si legge a mano dal browser.

---

## 1. Redmine: il modello dati che decide dove finiscono le ore

**Le ore si registrano su una segnalazione (issue), non su un progetto, ogni volta che una segnalazione esiste.** Redmine ammette il tempo a livello di progetto "lasciando vuoto il campo issue" ([RedmineTimeTracking](https://www.redmine.org/projects/redmine/wiki/RedmineTimeTracking)), ma un'ora senza issue non compare nella riga della segnalazione, non concorre al confronto stimato/speso e nel report dell'agenzia finisce in una riga senza oggetto ("the bottom line has no issue, it was logged against the project", [RedmineTimelogDetails](https://www.redmine.org/projects/redmine/wiki/RedmineTimelogDetails)). È la prima cosa che il PM dell'agenzia contesta.

- **Progetti e sottoprogetti**: nidificazione illimitata; l'identificatore (usato negli URL e nell'API) è unico e non si cambia dopo la creazione. I moduli (Issue tracking, Time tracking, Wiki, Documents, News, Files, Repository, Boards, Calendar, Gantt) si attivano per progetto: se "Time tracking" è spento, il link "Registra tempo" non c'è ([RedmineProjectSettings](https://www.redmine.org/projects/redmine/wiki/RedmineProjectSettings)).
- **Tracker**: il tipo di segnalazione (di default Bug, Feature, Support). Ogni tracker ha il proprio stato iniziale, il proprio workflow e i propri campi ([RedmineIssueTrackingSetup](https://www.redmine.org/projects/redmine/wiki/RedmineIssueTrackingSetup)).
- **Stati**: liberi, con il flag "Issue closed" ("more than one status can be declared as closed"). ⚠️ Un'istanza può avere più stati chiusi: il filtro `status_id=closed` dell'API li prende tutti.
- **Priorità**: enumerazione amministrata; con i sottotask "the parent task's priority is the highest of the subtasks' priorities" ([RedmineIssues](https://www.redmine.org/projects/redmine/wiki/RedmineIssues)).
- **Versioni** (in italiano "Versione prevista"): stato open / locked ("can not assign new issues") / closed ("can not assign new issues and can not reopen assigned issues"); condivisibili con sottoprogetti, gerarchia, albero o tutti i progetti.
- **Campi personalizzati**: esistono anche per le **voci di tempo** e per le **attività**, e compaiono nei report del tempo ([RedmineCustomFields](https://www.redmine.org/projects/redmine/wiki/RedmineCustomFields)). Se l'agenzia ha un campo "Fatturabile" o "Commessa" sulla voce di tempo, va compilato: il loro export lo usa.
- **Osservatori** ("Osservatori" nella pagina): "If the issue is updated, those users will be notified". Ci si mette osservatori sulle segnalazioni che si seguono senza esserne assegnatari.
- **Sottotask**: "The parent task's spent time is the sum of the subtasks' spent times. The parent task's estimation time is the sum of the subtasks' estimation times. The parent task's done percentage is the weighted average ratio of subtasks" ([RedmineIssues](https://www.redmine.org/projects/redmine/wiki/RedmineIssues)). Si registra sul figlio, mai sul padre, altrimenti il padre somma due volte.
- **Ruoli e permessi che contano per il subappaltatore** ([RedmineRoles](https://www.redmine.org/projects/redmine/wiki/RedmineRoles)): *Log spent time*, *View spent time*, *Edit own time logs* (solo le proprie), *Edit time logs* (tutte), *Log spent time for other users*, *Import time entries*; visibilità voci di tempo "All time entries" (default) o "Time entries created by the user"; visibilità segnalazioni "All issues" / "All non private issues" / "Issues created by or assigned to the user". 🔴 **Se il ruolo vede solo le proprie voci di tempo, il report dell'agenzia e il proprio non coincideranno mai per costruzione**: si chiede al PM quale ruolo si ha prima di discutere di numeri.

---

## 2. Leggere una notifica email di Redmine

**Oggetto** (dal codice, [mailer.rb](https://raw.githubusercontent.com/redmine/redmine/master/app/models/mailer.rb)): `[Nome progetto - Tracker #id] (Stato) Oggetto`. Il pezzo `(Stato)` compare **solo se quell'aggiornamento ha cambiato lo stato** e l'impostazione `show_status_changes_in_mail_subject` è attiva (default: attiva, [settings.yml](https://raw.githubusercontent.com/redmine/redmine/master/config/settings.yml)). ✅ Regola di lettura: oggetto con parentesi = qualcuno ha spostato il ticket di stato; senza parentesi = commento, riassegnazione o altro campo.

**Corpo** ([issue_edit.text.erb](https://raw.githubusercontent.com/redmine/redmine/master/app/views/mailer/issue_edit.text.erb)): prima riga "Issue #id has been updated by *Autore*" (l'"updated by" è `journal.user`, cioè chi ha fatto la modifica, non l'autore del ticket); poi una riga per ogni campo cambiato nella forma "*Campo* changed from *X* to *Y*" (`text_journal_changed`); poi il testo della nota; poi una linea di trattini e la scheda completa della segnalazione. Se la nota è privata il corpo inizia con "(Note private)".

**Intestazioni utili per i filtri Gmail**: `X-Redmine-Project` (identificatore), `X-Redmine-Issue-Id`, `X-Redmine-Issue-Tracker`, `X-Redmine-Issue-Author`, `X-Redmine-Issue-Assignee`, `X-Redmine-Issue-Priority`; da Redmine 6.0 anche `List-Id` con l'identificatore del progetto "for better Gmail filtering" ([Changelog_6_0](https://www.redmine.org/projects/redmine/wiki/Changelog_6_0)). Filtrare sull'assegnatario in intestazione batte qualunque regola sull'oggetto.

**Cosa si riceve** dipende da "Il mio utente → Notifiche email" ([en.yml](https://raw.githubusercontent.com/redmine/redmine/master/config/locales/en.yml)): "For any event on all my projects", "For any event on the selected projects only", "Only for things I watch or I'm involved in", "Only for things I watch or I am assigned to" (**default di sistema `only_assigned`**), "Only for things I watch or I am the owner of", "Only for things I watch" (nuova in 7.0), "No events"; più "I don't want to be notified of changes that I make myself". ⚠️ Con il default, **una segnalazione assegnata a un collega su cui si è lavorato non manda niente** finché non ci si mette osservatori. Gli eventi notificati li decide l'amministratore (`notified_events`, default solo `issue_added` e `issue_updated`): **il tempo registrato non genera email**, quindi nessuno "vede" le ore se non apre il report.

---

## 3. Aggiornare una segnalazione: l'etichetta che evita le discussioni

- **Si commenta (Note), non si riscrive la descrizione.** La descrizione è del richiedente; ogni modifica finisce nella "Cronologia" come diff e all'assegnatario arriva "Description changed". Chi cambia la descrizione di un ticket altrui viene letto come chi riscrive il contratto.
- **Note private** (`private_notes`): esistono, ma le vede chi ha il permesso *View private notes*: non sono il posto dove scrivere "le ore sono più della stima".
- **Stato**: si cambia solo lungo il workflow del proprio ruolo e tracker ("New statuses allowed", [RedmineIssueTrackingSetup](https://www.redmine.org/projects/redmine/wiki/RedmineIssueTrackingSetup)); se lo stato che serve non compare nel menu, non è un bug: il ruolo non può. Alcuni campi possono essere *required* in uno stato: il salvataggio fallisce finché non li si compila.
- **% Completato**: dipende dall'impostazione `issue_done_ratio`: "Use the issue field" (default) lo si aggiorna a mano; "Use the issue status" lo calcola lo stato e il campo sparisce ([RedmineSettings](https://www.redmine.org/projects/redmine/wiki/RedmineSettings)). Se non c'è il campo, non si chiede perché.
- **Tempo stimato vs impiegato**: lo stimato lo mette l'agenzia; l'impiegato lo scrivono le voci di tempo. ✅ Quando l'impiegato supera lo stimato, la nota va scritta **prima** di superarlo, sul ticket, con la causa e la richiesta (nuova stima o nuovo ticket). Dopo, in fattura, è una contestazione.
- 7.0 aggiunge l'opzione utente "automatically add assignee to watchers" e l'impostazione "Only for things I watch" ([Changelog_7_0](https://www.redmine.org/projects/redmine/wiki/Changelog_7_0)): su un'istanza 7.x si attiva la prima e si tiene la notifica su "cose che osservo o mi sono assegnate".

---

## 4. Tempo impiegato: registrazione, report, export

- **Dove**: pulsante "Registra tempo" nella segnalazione, oppure nel modulo di aggiornamento della segnalazione, oppure Progetto → Tempo impiegato → "Registra tempo" con issue vuoto (sconsigliato, sez. 1). Campi: Data (`spent_on`, default oggi), Ore, Commento (**255 caratteri max**, [Rest_TimeEntries](https://www.redmine.org/projects/redmine/wiki/Rest_TimeEntries)), Attività, campi personalizzati.
- **Formati ore accettati** ([RedmineTimeTracking](https://www.redmine.org/projects/redmine/wiki/RedmineTimeTracking)): `1h`, `1 h`, `1 hour`, `2 hours`, `30m`, `30min`, `1h30`, `1h30m`, `1:30`, `1.5`, `1,5`. La virgola italiana funziona. Come vengono **mostrate** dipende da "Time span format": `0.75` oppure `0:45 h` (default di sistema `minutes`, cioè `0:45 h`). ⚠️ In un CSV letto in Excel italiano `0.75` diventa testo o data: si controlla la colonna prima di sommare.
- **Attività**: enumerazione di sistema, attivabile per progetto ("The value which is unchecked 'Enabled'... does not appear in activities options", [RedmineProjectSettings](https://www.redmine.org/projects/redmine/wiki/RedmineProjectSettings)). L'attività è ciò su cui l'agenzia raggruppa il report: si usa quella concordata, non "Altro".
- **Limiti di sistema** (default in [settings.yml](https://raw.githubusercontent.com/redmine/redmine/master/config/settings.yml), l'amministratore può cambiarli): massimo **999 ore per giorno e utente**; voci a **0 ore accettate**; **date future accettate**; da 6.1 "Accept time logs on closed issues" (default sì: **una segnalazione chiusa accetta ancora ore**, salvo l'agenzia lo abbia spento); "Required fields for time logs" default nessuno. Se una registrazione viene rifiutata con 422, è uno di questi.
- **Dettagli vs Report** (Tempo impiegato → Dettagli | Report): *Dettagli* è l'elenco voce per voce, colonne di default `spent_on, user, activity, issue, comments, hours` con totale ore, ordinabile, paginato, con CSV e feed Atom ([RedmineTimelogDetails](https://www.redmine.org/projects/redmine/wiki/RedmineTimelogDetails)); *Report* aggrega per criteri aggiungibili in sequenza (progetto, utente, attività, segnalazione, tracker, versione, campi personalizzati) con colonne per giorno/settimana/mese/anno e CSV ([RedmineTimelogReport](https://www.redmine.org/projects/redmine/wiki/RedmineTimelogReport)). Per la fattura serve il **Report per utente = io, raggruppato per segnalazione, periodo "ultimo mese"**; per controllare i commenti serve *Dettagli*.
- 🔴 **L'export CSV delle segnalazioni è troncato a 500 righe di default** (`issues_export_limit`; l'amministratore lo alza in Amministrazione → Impostazioni → Segnalazioni). [DA VERIFICARE] se lo stesso limite tronca anche il CSV del tempo impiegato sull'istanza dell'agenzia: si confronta il totale a schermo con la somma del CSV prima di fidarsi.
- Il **filtro sulle ore** nelle query di tempo accetta `0:45` oltre a `0.75` solo da 7.0 ([Changelog_7_0](https://www.redmine.org/projects/redmine/wiki/Changelog_7_0)).

---

## 5. REST API: tirare giù le ore del mese senza aprire il pannello

**Prerequisiti**: l'amministratore deve aver acceso "Enable REST web service" (default **spento**, Amministrazione → Impostazioni → API); la propria chiave sta in "Il mio utente" → "Chiave di accesso API" ([Rest_api](https://www.redmine.org/projects/redmine/wiki/Rest_api)). Da 7.0 la pagina mostra anche l'**ultimo utilizzo** della chiave API e Atom: se risulta usata quando non si è lanciato niente, si rigenera.

- Autenticazione: header `X-Redmine-API-Key: <chiave>` (preferito), oppure `?key=`, oppure Basic auth. Formato: `.json` o `.xml`; per POST/PUT serve `Content-Type: application/json` ([Rest_api_with_curl](https://www.redmine.org/projects/redmine/wiki/Rest_api_with_curl)).
- 🔴 **Paginazione: `limit` default 25, massimo 100**, `offset` per scorrere, `total_count` nella risposta. Chi chiede `limit=1000` riceve 100 e non se ne accorge: **si cicla finché `offset + limit >= total_count`**.
- Ore del mese: `GET /time_entries.json?user_id=<mio id>&from=2026-09-01&to=2026-09-30&limit=100&offset=0` ([Rest_TimeEntries](https://www.redmine.org/projects/redmine/wiki/Rest_TimeEntries)); filtri documentati: `user_id`, `project_id` (id numerico o identificatore), `spent_on`, `from`/`to`. [DA VERIFICARE] `user_id=me` sulle voci di tempo: il proprio id si prende da `GET /users/current.json`. Ogni voce riporta `issue.id`, `project`, `activity`, `hours`, `comments`, `spent_on`: si raggruppa per `issue.id` e si somma.
- Segnalazioni: `GET /issues.json?assigned_to_id=me&status_id=*&updated_on=%3E%3D2026-09-01&sort=updated_on:desc` ([Rest_Issues](https://www.redmine.org/projects/redmine/wiki/Rest_Issues)); `status_id` accetta `open`, `closed`, `*` o un id; le date accettano `>=`, `<=`, `><a|b` codificati in URL (`%3E%3D`); `include=journals,watchers,relations,children,allowed_statuses` solo sulla singola segnalazione. La segnalazione espone `estimated_hours`, `done_ratio` e, sulla singola, le ore spese (nomi dei campi [DA VERIFICARE] sull'istanza: in Rest_Issues non sono nell'esempio).
- Scrivere: `POST /time_entries.json` con `{"time_entry":{"issue_id":1234,"hours":1.5,"activity_id":9,"spent_on":"2026-09-18","comments":"..."}}` (`activity_id` "required unless a default activity is defined"; `issue_id` **oppure** `project_id`, mai entrambi); risposta `201` o `422` con gli errori. Commentare: `PUT /issues/1234.json` con `{"issue":{"notes":"...","private_notes":false}}` → `204`. Aggiungere osservatori: `POST /issues/1234/watchers.json`.
- Ci si può mettere in ascolto invece di interrogare: **webhooks nativi da 7.0** (eventi su issue, voci di tempo, wiki, news), **spenti di default**, li accende solo l'amministratore dalla scheda "Integration" ([news 7.0.0](https://www.redmine.org/news/161)). Su 6.x non esistono senza plugin.

---

## 6. Atom, Pagina personale, query, wiki e documenti

- **Feed Atom**: ogni elenco di segnalazioni e la lista Tempo impiegato → Dettagli hanno un feed; l'URL porta `?key=<Chiave di accesso Atom>` (diversa dalla chiave API, stessa pagina "Il mio utente"); senza chiave si vedono solo gli elementi pubblici; `feeds_limit` default **15 elementi** ([settings.yml](https://raw.githubusercontent.com/redmine/redmine/master/config/settings.yml)). Buono per un lettore RSS, inutile per contare ore.
- **Pagina personale**: blocchi "Issues assigned to me" e "Reported issues" attivi di default; si aggiungono "Watched issues", "Spent time" (**solo gli ultimi sette giorni**, cross-progetto) e i blocchi da query personalizzata ([RedmineMyPage](https://www.redmine.org/projects/redmine/wiki/RedmineMyPage)). Il blocco Spent time serve a vedere se si è dimenticato ieri, non il mese.
- **Query personalizzate**: si salvano dal filtro con nome, colonne, "public" (visibile a tutti) o privata, e dalla 6.0 con una descrizione ([RedmineIssueList](https://www.redmine.org/projects/redmine/wiki/RedmineIssueList), [Changelog_6_0](https://www.redmine.org/projects/redmine/wiki/Changelog_6_0)). Ne servono due, private, globali: "Assegnate a me, aperte, con colonne Tempo stimato / Tempo impiegato / % Completato" e "Aggiornate negli ultimi 7 giorni dove sono osservatore".
- **Wiki**: ogni modifica è versionata ("Redmine keeps a record of every change made to a wiki page"), con diff fra versioni e "Rollback to this version" che **crea una versione nuova senza cancellare la cronologia**; le pagine si possono bloccare ([RedmineWikis](https://www.redmine.org/projects/redmine/wiki/RedmineWikis)). Le specifiche vanno lì, non negli allegati.
- **Documenti**: categorie ("User documentation", "Technical documentation" di default) e allegati; **la pagina ufficiale non descrive alcun versionamento** ([RedmineDocuments](https://www.redmine.org/projects/redmine/wiki/RedmineDocuments)): un file ricaricato con lo stesso nome è un allegato in più, non una revisione. I file "finali" vanno nominati con data o versione nel nome.

---

## 7. Riconciliare le ore Redmine con la fattura all'agenzia

1. **Il primo giorno lavorativo del mese** si estrae il mese precedente (API sez. 5 oppure Report utente = io, ultimo mese, per segnalazione, CSV) e si salva il file: è la prova di quanto c'era **prima** che l'agenzia toccasse qualcosa.
2. Si raggruppa per segnalazione e per progetto; si confronta il totale con la somma a schermo in *Dettagli* (limite export, sez. 4).
3. Per ogni segnalazione con ore: stimato vs speso. Dove speso > stimato **e non c'è una nota** che lo spiega, la nota si scrive adesso, prima di mandare la fattura.
4. Si confronta con quanto l'agenzia si aspetta (monte ore concordato, ordine, retainer). Le ore oltre l'accordo si **separano in una riga a parte** nel riepilogo, con i numeri dei ticket, e si chiede se fatturarle, rimandarle o rinunciarci. Non si spalmano su altri ticket per farle rientrare: il PM ha lo stesso report.
5. La fattura riporta mese, progetti, totale ore, tariffa, e in allegato (o nel corpo se corto) l'elenco ticket → ore. Le voci di tempo dell'agenzia sono l'unica base che il loro amministrativo accetta: **la fattura si fa dalle ore in Redmine, non da Harvest**.
6. 🔴 **Dopo la fattura non si modifica più una voce di tempo del mese fatturato.** Se manca un'ora, si registra nel mese in corso con commento "recupero settembre, #1234", si avvisa il PM.
7. Contesto italiano: la fattura è elettronica via SDI dal proprio gestionale; Redmine e Harvest non emettono documenti fiscali validi in Italia. Al commercialista vanno la fattura, il riepilogo ore e l'eventuale ordine dell'agenzia, non gli export grezzi.

---

## 8. Harvest: modello, timesheet, budget, fatture, blocchi

- **Modello**: Client → Project → Task; ogni voce di tempo ha `billable` e appartiene a una persona. I progetti hanno tipo (Time & Materials, Fixed Fee, Non-Billable) e `bill_by` Project / Tasks / People / none ([Projects API](https://help.getharvest.com/api-v2/projects-api/projects/projects/)). Per il subappalto: Client = l'agenzia, un Project per contratto o per progetto Redmine, Task = attività Redmine.
- **Timesheet**: durata oppure orario di inizio/fine, deciso a livello di account (`wants_timestamp_timers` nel [Company API](https://help.getharvest.com/api-v2/company-api/company/company/)); formato di visualizzazione `decimal` o `hours_minutes`; dal maggio 2026 esiste la vista calendario in modalità durata ([Inside the new Harvest](https://www.getharvest.com/blog/inside-the-new-harvest)).
- **Budget** (`budget_by`: `project` ore totali, `project_cost` importo totale, `task` ore per task, `task_fees` importo per task, `person` ore per persona, `none`; `budget_is_monthly` azzera ogni mese). Avvisi: `notify_when_over_budget` + `over_budget_notification_percentage`; l'help center (non leggibile via fetch, citato da terzi e dai risultati di ricerca) dice che le email partono "the morning after" il superamento della soglia. 🔴 **Le ore non fatturabili contano nel budget a ore** ("both billable and non-billable hours count against total project hours budgets", help center via ricerca) e **non si può mettere un budget in importo su un progetto Non-Billable**. Report budget vs actual: `GET /v2/reports/project_budget` con `budget`, `budget_spent`, `budget_remaining` ([Project Budget Report](https://help.getharvest.com/api-v2/reports-api/reports/project-budget-report/)).
- **Fatture da tempo**: `POST /v2/invoices` con `line_items_import: {project_ids, time: {summary_type: project|task|people|detailed, from, to}, expenses: {summary_type: project|category|people|detailed}}`; ⚠️ "If neither `from` or `to` are provided, all unbilled time entries will be included" ([Invoices API](https://help.getharvest.com/api-v2/invoices-api/invoices/invoices/)). Stati fattura: `draft`, `open`, `paid`, `closed`.
- 🔴 **Fatturare blocca le voci.** Le ore incluse in una fattura diventano `is_billed` e `is_locked`; per correggerle bisogna "mark hours as uninvoiced" dal Detailed time report (Actions), e se erano anche approvate serve anche "Withdraw approval" (help center via ricerca: "Unlocking invoiced time and expenses", "Unlocking approved time and expenses"). Dall'estate 2026 esiste anche il **blocco automatico dei timesheet a calendario** ([In Season Summer 2026](https://www.getharvest.com/blog/in-season-summer-2026)): su un account ereditato si controlla che non blocchi prima della riconciliazione con Redmine.
- **Spese**: data, progetto, categoria (le crea l'amministratore), flag "This expense is billable", ricevuta allegata; entrano in fattura solo se billable; il report spese permette "mark as invoiced/uninvoiced" (help center via ricerca).
- **Prezzi** ([getharvest.com/pricing](https://www.getharvest.com/pricing), USD): Free "$0 forever", **1 posto e 2 progetti**; Teams "$9 seat/month" con "$108 per seat, billed annually"; Enterprise "$14 seat/month", "$168 per seat, billed annually"; Enterprise Plus su preventivo. ⚠️ Nota in pagina: "Your base rate includes core features. As your team grows, additional invoices, projects, clients, and tasks are billed based on what you use": **esiste una componente a consumo** oltre il posto. Custom report: fino a 4 salvati per persona su Free/Teams, illimitati su Enterprise (help center via ricerca). Il prezzo mensile senza impegno annuale e la soglia degli "inclusi" sono [DA VERIFICARE] sul pannello. Forecast (pianificazione, "estimates vs actuals" con l'integrazione, [getharvest.com/forecast](https://www.getharvest.com/forecast)): la pagina prezzi non ne dichiara il costo; "5 USD/persona/mese come add-on separato" è **regola empirica di terzi, non numero Harvest** (productive.io, onesuite.io). Per un singolo consulente Forecast non serve.

---

## 9. Harvest: report, export, condivisione con i clienti

- **Report** (Reports): Time report con schede **Clients / Projects / Tasks / Team**; Detailed time (voce per voce, con note; filtri timeframe, clients, projects, tasks, team); Uninvoiced; Project budget / Project analysis; Expenses; Invoices e Payments received; Custom reports (dal 2026: gruppi, filtri, anteprima, **caduto il limite di 100 righe** sui report di voci, [In Season Summer 2026](https://www.getharvest.com/blog/in-season-summer-2026)). Un Member vede solo i propri; un Manager i progetti che gestisce; un Administrator tutto (help center via ricerca).
- **Export**: CSV, Excel, PDF; "Export > Custom" per scegliere le colonne se il piano lo consente; i report grandi arrivano via email come link. **Google Sheets**: l'integrazione Google Workspace aggiunge "Export → Google Drive" al Time report e al Detailed time report e crea un foglio in My Drive; è un **export una tantum, non un collegamento vivo**, e l'installazione richiede un Super Admin Workspace e un Administrator Harvest (help center "Google Workspace: Import people and export reports", via ricerca). Per un foglio che si aggiorna da solo si usa l'API (sez. 10) o un connettore terzo (Coupler, Coefficient: terze parti).
- 🔴 **Non esiste un link pubblico a un report.** "Saved, shared, and recurring reports" condivide solo con persone dell'account e "anyone you share a report with will only be able to view details that their permissions allow" (help center via ricerca). Al cliente si dà: (a) l'export CSV/PDF del Detailed time con le note, oppure (b) la **fattura web**, il cui URL unico e sicuro non richiede login e porta al **client dashboard** (fatture aperte, pagamenti, ricorrenti), oppure (c) un client statement. Le note delle voci finiscono nella fattura con `summary_type: detailed`: si scrivono pensando che il cliente le legga.
- I report a tempo dell'API (`/v2/reports/time/clients|projects|tasks|team`, `/v2/reports/uninvoiced`) accettano `from`/`to` obbligatori con **massimo 365 giorni** e `include_fixed_fee` ([Time Reports](https://help.getharvest.com/api-v2/reports-api/reports/time-reports/), [Uninvoiced](https://help.getharvest.com/api-v2/reports-api/reports/uninvoiced-report/)): `uninvoiced_hours` e `uninvoiced_amount` sono il numero da guardare il primo del mese.

---

## 10. Harvest API v2

- **Token**: Personal Access Token da [id.getharvest.com/developers](https://id.getharvest.com/developers), che dà anche la lista degli account id. Tre header obbligatori: `Authorization: Bearer <token>`, `Harvest-Account-Id: <id>`, `User-Agent: NomeApp (email)`; base `https://api.harvestapp.com/v2/`; test con `GET /v2/users/me` ([Authentication](https://help.getharvest.com/api-v2/authentication-api/authentication/authentication/)). OAuth2 solo per app distribuite ad altri.
- 🔴 **Rate limit: 100 richieste ogni 15 secondi** sull'API generale, **100 ogni 15 minuti** sui report; superato, `429` con `Retry-After` ([General](https://help.getharvest.com/api-v2/introduction/overview/general/)). Un foglio che ricalcola chiamando `/reports` a ogni apertura si blocca in un pomeriggio: si mette in cache.
- **Paginazione**: `per_page` default **e** massimo **2000**; `page` è deprecato su molti endpoint a favore del **cursore**; `page` e `cursor` sono mutuamente esclusivi e "You should always use the pagination URLs provided by the `links` section" (`first/next/previous/last`) ([Pagination](https://help.getharvest.com/api-v2/introduction/overview/pagination/)). Si segue `links.next` finché è `null`.
- **Voci di tempo**: `GET /v2/time_entries?from=2026-09-01&to=2026-09-30&user_id=<id>` più `project_id`, `client_id`, `task_id`, `is_billed`, `is_running`, `updated_since`, `external_reference_id`, `approval_status` ([Time Entries](https://help.getharvest.com/api-v2/timesheets-api/timesheets/time-entries/)). Campi che contano: `hours`, `rounded_hours` (se l'account arrotonda, **in fattura va `rounded_hours`**), `billable`, `is_billed`, `is_locked` + `locked_reason`, `notes`, `external_reference {id, group_id, account_id, permalink, service}`. Creazione: `POST /v2/time_entries` con `project_id`, `task_id`, `spent_date`, `hours` (account a durata) oppure `started_time`/`ended_time` (account a timestamp); `PATCH .../restart` e `.../stop` per il timer.
- Date in `YYYY-MM-DD`, datetime in UTC `2026-09-18T14:59:22Z`; `time_format`, `date_format`, `week_start_day` e `clock` (12h/24h) si leggono da `GET /v2/company` prima di formattare qualunque cosa.
- **Harvest MCP** (estate 2026): connettore ufficiale verso Claude, Cursor, ChatGPT per timer, ore, budget, bozze fattura ([In Season Summer 2026](https://www.getharvest.com/blog/in-season-summer-2026); articolo help 46293697226381 non leggibile via fetch). Usa gli stessi permessi dell'utente: quello che l'utente non vede, l'assistente non vede.

---

## 11. Redmine ↔ Harvest senza contare le ore due volte

**Una sola fonte di verità per ogni cliente.** Per l'agenzia la verità è Redmine (ci fattura lei, e ci fattura il subappaltatore); Harvest è lo specchio per il totale personale, l'utilizzo e i report agli altri clienti. Per i clienti diretti la verità è Harvest.

1. **Direzione unica: Redmine → Harvest, mai il contrario** per il lavoro d'agenzia. Si registra in Redmine sul ticket; un job (API sez. 5 → sez. 10) copia le voci in Harvest nel Project dell'agenzia con Task = attività Redmine, `spent_date = spent_on`, `hours = hours`, `notes = "#<issue.id> <oggetto>: <comments>"`.
2. **Idempotenza con `external_reference`**: si scrive `external_reference.id = <id voce di tempo Redmine>`, `permalink = https://redmine.agenzia/time_entries/<id>` (o l'URL della segnalazione), e **prima di creare** si interroga `GET /v2/time_entries?external_reference_id=<id>&from&to`: se esiste, si aggiorna con `PATCH`, non si crea. ⚠️ `external_reference` è documentato come campo delle integrazioni: [DA VERIFICARE] che la creazione via API lo accetti sul proprio account; se no, si usa la stringa `[rm:<id>]` in coda a `notes` e si filtra sulle note lato script.
3. Le voci copiate sono `billable: true` nel progetto dell'agenzia (così l'uninvoiced report dice quanto va fatturato all'agenzia), ma la **fattura all'agenzia non si genera da Harvest** (sez. 7): dopo aver emesso quella fiscale si fa "Mark hours as invoiced" per bloccarle e azzerare l'uninvoiced.
4. Mai registrare ore d'agenzia direttamente in Harvest "per fare prima": alla sincronizzazione successiva compariranno due volte e il budget del progetto sfora a vuoto.
5. Mai un Project Harvest per singolo ticket Redmine: i limiti di progetto del piano (sez. 8) e la lista clienti diventano ingestibili; il ticket vive nelle note e in `external_reference`.
6. Cancellata una voce in Redmine, il job la deve cancellare in Harvest (`DELETE /v2/time_entries/{id}`; fallisce se la voce è bloccata: prima si sblocca, sez. 8).

---

## 12. Chiusura mensile: checklist

1. Ultimo giorno: tutte le ore in Redmine sul ticket giusto, con commento; nessuna voce senza issue; nessuna voce con attività "Altro".
2. Giorno 1: export Redmine del mese (API, tutte le pagine) salvato con data nel nome; confronto con il totale a schermo.
3. Sincronizzazione Redmine → Harvest, poi `GET /v2/reports/uninvoiced?from&to`: le ore dell'agenzia in Harvest devono coincidere con l'export Redmine al centesimo di ora; se no, si cerca la voce, non si aggiusta il totale.
4. Riconciliazione con le attese dell'agenzia (sez. 7, punti 3-4); note sui ticket oltre stima; email al PM con ticket → ore e le righe "oltre accordo" separate; si aspetta l'ok se il contratto lo prevede.
5. Fattura fiscale dal gestionale (SDI); poi in Harvest "Mark hours as invoiced" sul progetto agenzia; per i clienti diretti fattura da Harvest solo come bozza/dettaglio ore allegato, mai come documento fiscale.
6. Al commercialista: fattura, riepilogo ore per cliente (Time report → Clients, CSV), eventuale ordine/contratto, note spese con ricevute. Non gli si mandano gli export grezzi.
7. Controllo budget: `GET /v2/reports/project_budget?is_active=true`; progetti con `budget_remaining` negativo o sotto il 20% [regola empirica propria, non numero Harvest] si segnalano al cliente prima di ripartire.

---

## 13. Cosa è cambiato nel 2026

**Redmine** ([news](https://www.redmine.org/projects/redmine/news), [Changelog_6_1](https://www.redmine.org/projects/redmine/wiki/Changelog_6_1), [Changelog_7_0](https://www.redmine.org/projects/redmine/wiki/Changelog_7_0)):
- **6.1.0 (21/09/2025)**: impostazione per accettare/rifiutare ore su segnalazioni chiuse; OAuth2 provider per le app API; reazioni su segnalazioni e note; Ruby 3.4, via Ruby 3.1. Patch di sicurezza **6.1.1 (05/01/2026), 6.1.2 (16/03/2026), 6.1.3 (15/06/2026), 6.1.4 (26/08/2026)**.
- **7.0.0 (30/06/2026)**: webhooks nativi (issue, tempo, wiki, news; spenti di default); Rails 8; Ruby 4.0 supportato (raccomandata ≥ 4.0.4); tracciamento dell'ultimo uso delle chiavi API e Atom; notifica "Only for things I watch"; opzione "assegnatario diventa osservatore"; scadenza di default N giorni dopo la creazione; flag privato di default per tracker; filtro ore in formato `0:45`; nuova barra di navigazione. **5.1 a fine vita, 6.0 legacy**; 7.0.1 il 26/08/2026. Per lo script del mese non cambia nulla: `limit` massimo resta 100.
- **6.0.0 (10/11/2024)**, ancora diffusa: `List-Id` con identificatore progetto nelle email; `updated_on`/`updated_by` nei journal via API; CSV in UTF-8 di default; descrizione sulle query.

**Harvest** ([Inside the new Harvest, 05/05/2026](https://www.getharvest.com/blog/inside-the-new-harvest); [In Season Summer 2026, 15/07/2026](https://www.getharvest.com/blog/in-season-summer-2026)):
- **05/05/2026, "new Harvest"**: interfaccia rifatta; vista calendario; fatture white-label; report utilizzo e scaduto clienti (AR aging); e-fattura in formato UBL "per la conformità europea" (⚠️ non è la FatturaPA italiana: [DA VERIFICARE] se e come esporta verso SDI); addebito diretto e bonifico via Stripe; pausa delle fatture ricorrenti; QuickBooks Online bidirezionale; **sei ruoli predefiniti più ruoli personalizzati**; approvazione spese.
- **Estate 2026**: custom report con salvataggio e condivisione, senza più il limite di 100 righe; Harvest MCP; azioni in blocco; **blocco automatico dei timesheet a calendario**; reparti come filtro dei report; costi orari per progetto; destinatari email predefiniti sulle fatture. Annunciati: Harvest AI, PTO, rimborsi spese, Gusto, dark mode, notification center.
- Prezzo: listino a posto **più componente a consumo** su fatture/progetti/clienti/task (sez. 8); l'acquisizione da parte di Bending Spoons nel 2025 come causa è **fonte terza** (productive.io, onesuite.io), non dichiarata da Harvest.

---

## 14. Igiene di un account ereditato: ordine di controllo

**Redmine dell'agenzia (nuovo incarico)**
1. Versione (piè di pagina o `Amministrazione → Informazioni` se visibile): 6.0 / 6.1 / 7.0 cambia notifiche, chiusi, webhooks.
2. Ruolo e visibilità delle voci di tempo (sez. 1): si prova a vedere le ore di un collega; se non si vedono, si sa che il report dell'agenzia non sarà il proprio.
3. Notifiche email su "Only for things I watch or I am assigned to" + "non notificarmi delle mie modifiche"; su 7.x "assegnatario → osservatore".
4. Chiave API attiva (REST acceso? test `GET /users/current.json`) e chiave Atom rigenerate se ereditate da un account precedente.
5. Attività disponibili nei progetti e campi personalizzati obbligatori sulle voci di tempo; limite ore/giorno e ore su ticket chiusi.
6. Query personalizzate private (sez. 6) e blocco "Spent time" in Pagina personale.

**Harvest (proprio account)**
7. Modalità timesheet (durata vs timestamp), `time_format`, arrotondamento, blocco automatico dei timesheet e approvazioni: tutto ciò che può rifiutare o alterare una `POST /v2/time_entries`.
8. Clienti e progetti archiviati che contano ancora nei limiti del piano; progetti senza budget o con avvisi spenti.
9. Uninvoiced report degli ultimi 12 mesi: ore mai marcate come fatturate gonfiano l'uninvoiced per sempre.
10. Token API: uno per script, con `User-Agent` parlante; si revocano quelli non riconosciuti.
11. Ruoli (dal maggio 2026 sei predefiniti + personalizzati): chi vede le tariffe vede anche `billable_amount` nei report.

---

## 15. Meccanica del pannello (da verificare a mano)

- Sull'istanza dell'agenzia, il pulsante "Registra tempo" dentro il modulo di aggiornamento della segnalazione registra la voce anche se il salvataggio della nota fallisce per un campo obbligatorio, o la perde?
- Il CSV di Tempo impiegato → Dettagli riporta le ore come `1.5`, `1,5` o `1:30` con "Time span format" impostato su `0:45 h`? E il separatore è virgola o punto e virgola (Excel italiano)?
- Nel Report del tempo, il periodo "ultimo mese" vale il mese solare precedente o gli ultimi 30 giorni?
- `GET /time_entries.json?user_id=me` funziona sull'istanza dell'agenzia, o serve l'id numerico?
- In Harvest, il Detailed time report esporta `hours` o `rounded_hours` quando l'arrotondamento è attivo? E "Export → Google Drive" compare senza l'installazione Workspace?
- Il `POST /v2/time_entries` accetta `external_reference` sul proprio account, e il filtro `external_reference_id` lo ritrova?

---

## 16. Cosa non fare mai

- Registrare ore a livello di progetto quando esiste il ticket; registrare sul task padre invece che sul figlio.
- Cambiare la descrizione di un ticket altrui invece di commentare; scrivere "oltre stima" in una nota privata.
- Fidarsi di un CSV senza confrontare il totale con quello a schermo (limite 500 righe).
- Chiedere `limit=1000` all'API Redmine e prendere per buona la prima pagina.
- Fatturare all'agenzia da Harvest, o modificare voci Redmine di un mese già fatturato.
- Registrare la stessa ora in Redmine e a mano in Harvest; sincronizzare senza chiave di idempotenza.
- Chiamare `/v2/reports/*` a ogni ricalcolo di un foglio (100 richieste ogni 15 minuti).
- Mandare al cliente un link a un report Harvest credendo che lo possa aprire: non esiste; si manda l'export o la fattura web.
- Trattare la fattura Harvest (anche UBL) come documento fiscale italiano.
- Lasciare che il blocco automatico dei timesheet scatti prima della riconciliazione del mese.

---

## Fonti (verificate 20/09/2026)

**Ufficiali Redmine, lette:** [Rest_api](https://www.redmine.org/projects/redmine/wiki/Rest_api) · [Rest_TimeEntries](https://www.redmine.org/projects/redmine/wiki/Rest_TimeEntries) · [Rest_Issues](https://www.redmine.org/projects/redmine/wiki/Rest_Issues) · [Rest_api_with_curl](https://www.redmine.org/projects/redmine/wiki/Rest_api_with_curl) · [RedmineTimeTracking](https://www.redmine.org/projects/redmine/wiki/RedmineTimeTracking) · [RedmineTimelogDetails](https://www.redmine.org/projects/redmine/wiki/RedmineTimelogDetails) · [RedmineTimelogReport](https://www.redmine.org/projects/redmine/wiki/RedmineTimelogReport) · [RedmineIssues](https://www.redmine.org/projects/redmine/wiki/RedmineIssues) · [RedmineIssueTrackingSetup](https://www.redmine.org/projects/redmine/wiki/RedmineIssueTrackingSetup) · [RedmineIssueList](https://www.redmine.org/projects/redmine/wiki/RedmineIssueList) · [RedmineMyPage](https://www.redmine.org/projects/redmine/wiki/RedmineMyPage) · [RedmineRoles](https://www.redmine.org/projects/redmine/wiki/RedmineRoles) · [RedmineProjectSettings](https://www.redmine.org/projects/redmine/wiki/RedmineProjectSettings) · [RedmineCustomFields](https://www.redmine.org/projects/redmine/wiki/RedmineCustomFields) · [RedmineSettings](https://www.redmine.org/projects/redmine/wiki/RedmineSettings) · [RedmineWikis](https://www.redmine.org/projects/redmine/wiki/RedmineWikis) · [RedmineDocuments](https://www.redmine.org/projects/redmine/wiki/RedmineDocuments) · [Changelog_6_0](https://www.redmine.org/projects/redmine/wiki/Changelog_6_0) · [Changelog_6_1](https://www.redmine.org/projects/redmine/wiki/Changelog_6_1) · [Changelog_7_0](https://www.redmine.org/projects/redmine/wiki/Changelog_7_0) · [News](https://www.redmine.org/projects/redmine/news) · [Redmine 7.0.0 is now available](https://www.redmine.org/news/161) · codice su GitHub: [mailer.rb](https://raw.githubusercontent.com/redmine/redmine/master/app/models/mailer.rb), [issue_edit.text.erb](https://raw.githubusercontent.com/redmine/redmine/master/app/views/mailer/issue_edit.text.erb), [settings.yml](https://raw.githubusercontent.com/redmine/redmine/master/config/settings.yml), [en.yml](https://raw.githubusercontent.com/redmine/redmine/master/config/locales/en.yml), [it.yml](https://raw.githubusercontent.com/redmine/redmine/master/config/locales/it.yml) (nomi italiani dei menu).

**Ufficiali Harvest, lette:** [API Authentication](https://help.getharvest.com/api-v2/authentication-api/authentication/authentication/) · [API General (rate limit)](https://help.getharvest.com/api-v2/introduction/overview/general/) · [API Pagination](https://help.getharvest.com/api-v2/introduction/overview/pagination/) · [Time Entries](https://help.getharvest.com/api-v2/timesheets-api/timesheets/time-entries/) · [Projects](https://help.getharvest.com/api-v2/projects-api/projects/projects/) · [Company](https://help.getharvest.com/api-v2/company-api/company/company/) · [Invoices](https://help.getharvest.com/api-v2/invoices-api/invoices/invoices/) · [Time Reports](https://help.getharvest.com/api-v2/reports-api/reports/time-reports/) · [Uninvoiced Report](https://help.getharvest.com/api-v2/reports-api/reports/uninvoiced-report/) · [Project Budget Report](https://help.getharvest.com/api-v2/reports-api/reports/project-budget-report/) · [Pricing](https://www.getharvest.com/pricing) · [Forecast](https://www.getharvest.com/forecast) · [Inside the new Harvest (05/05/2026)](https://www.getharvest.com/blog/inside-the-new-harvest) · [In Season Summer 2026 (15/07/2026)](https://www.getharvest.com/blog/in-season-summer-2026).

**Terze parti (pratica e prezzi, non numeri ufficiali):** [redmineadvisor: Redmine 7.0 new features](https://www.redmineadvisor.com/articles/7_0/new-features/) · [redmineup: Redmine 6.1](https://www.redmineup.com/pages/blog/redmine-6-1) · [productive.io: Harvest price increase 2026](https://productive.io/blog/harvest-price-increase/) · [onesuite.io: Harvest price increase](https://onesuite.io/blog/harvest-price-increase/) · [Coupler: Harvest → Google Sheets](https://blog.coupler.io/harvest-export-to-google-sheets/) · [redmine_harvest_smc (plugin, legge il numero di ticket dalle note)](https://github.com/singlemind/redmine_harvest_smc).

**Non leggibili via fetch il 20/09/2026, da ricontrollare a mano** (403 Cloudflare; il contenuto citato sopra come "help center via ricerca" viene dagli estratti dei motori di ricerca): support.getharvest.com [How to set project budgets (360048686811)](https://support.getharvest.com/hc/en-us/articles/360048686811-How-to-set-project-budgets), [Budget email alerts (4407283487629)](https://support.getharvest.com/hc/en-us/articles/4407283487629-Budget-email-alerts), [What reports and exports are available (360054457791)](https://support.getharvest.com/hc/en-us/articles/360054457791-What-reports-and-exports-are-available-in-Harvest), [Saved, shared, and recurring reports (18154193545997)](https://support.getharvest.com/hc/en-us/articles/18154193545997-Saved-shared-and-recurring-reports), [Creating a custom report (46653058359053)](https://support.getharvest.com/hc/en-us/articles/46653058359053-Creating-a-custom-report), [Exporting data (31625325401229)](https://support.getharvest.com/hc/en-us/articles/31625325401229-Exporting-data), [Google Workspace export (360048180712)](https://support.getharvest.com/hc/en-us/articles/360048180712-Google-Workspace-Import-people-and-export-reports), [Unlocking invoiced time (4408204890381)](https://support.getharvest.com/hc/en-us/articles/4408204890381-Unlocking-invoiced-time-and-expenses), [Harvest MCP (46293697226381)](https://support.getharvest.com/hc/en-us/articles/46293697226381-Harvest-MCP), [Information about pricing plans (31447072608397)](https://support.getharvest.com/hc/en-us/articles/31447072608397-Information-about-pricing-plans); [Harvest API changelog](https://help.getharvest.com/api-v2/introduction/overview/changelog/) (404); redmine.org [RedmineUserAccounts](https://www.redmine.org/projects/redmine/wiki/RedmineUserAccounts) (404: le opzioni di notifica sono state prese da en.yml).
