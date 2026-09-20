# Skill personali di Cristiano Gallinelli

Fonte di verità delle skill caricate sull'account Claude (usate da Cowork e dalle sessioni cloud).

- `skills/<nome>/SKILL.md`: la skill. Ogni modifica riscrive la data in cima e aggiunge una riga al `CHANGELOG.md` della skill.
- `dist/<nome>.zip`: il pacchetto pronto da caricare su Claude, in Personalizza, poi Skill. Si rigenera con `scripts/package.sh`.
- `audit/`: i rapporti di verifica delle fonti, datati.

Regola che vale per tutte le skill: le sezioni marcate **VERIFICATO** con una data sono osservazioni fatte di persona sul pannello. Non si riscrivono da documentazione. Al massimo si annota che una fonte le smentisce, con data e link.
