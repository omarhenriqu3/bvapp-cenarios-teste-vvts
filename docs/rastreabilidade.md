# Rastreabilidade

| Feature | ID do CA | Critério (texto do backlog) | Cenário que cobre |
|---|---:|---|---|
| 23817 | 24962 | CA01 - O sistema coleta dados de todos os inversores ativos automaticamente, sem intervenção do usuário, respeitando o intervalo de 15 minutos. | UC001 |
| 23817 | 24963 | CA02 - Cada coleta registra timestamp preciso (data e hora) associado ao inversor correspondente. | UC002 |
| 23817 | 24965 | CA03 - Se uma coleta não for concluída no tempo esperado, o sistema registra a tentativa como falha e agenda nova tentativa conforme RF-4.1.03. | UC003 |
| 23817 | 24966 | CA04 - O sistema não interrompe coletas de outros inversores caso um deles esteja indisponível. | UC004 |
| 23817 | 24967 | CA05 - Dados coletados ficam disponíveis para consulta em até 1 minuto após o ciclo de coleta ser concluído. | UC005 |
| 23817 | 28851 | CA06 - Toda leitura obtida durante a coleta deve ser armazenada e associada ao inversor correspondente para posterior consulta e análise. | UC002 |
| 23849 | 25769 | CA01 - O Tesoureiro preenche formulário com dados da fatura (mês/ano, energias, créditos e valores) e o sistema salva. | UC006 |
| 23849 | 25770 | CA02 - Todos os campos obrigatórios são validados antes do salvamento; campos inválidos geram erro. | UC007 |
| 23849 | 25771 | CA03 - O sistema impede o cadastro de fatura duplicada para o mesmo mês/ano e usina. | UC008 |
| 23849 | 25772 | CA04 - Apenas o perfil Tesoureiro tem acesso à funcionalidade de cadastro. | UC009 |
| 23849 | 25773 | CA05 - Após salvar, a fatura aparece imediatamente na listagem histórica. | UC006 |
| 23849 | 25774 | CA06 - Restringir acesso ao cadastro de fatura apenas ao Tesoureiro | UC009 (duplicado de 25772, coberto em conjunto) |
| 23879 | 24841 | CA01 - Eventos emitidos pelos inversores são capturados e registrados automaticamente, sem intervenção manual. | UC010 |
| 23879 | 24842 | CA02 - Cada evento registrado contém: ID do inversor, usina, timestamp de ocorrência, tipo e descrição do evento. | UC010 |
| 23879 | 24843 | CA03 - O sistema não descarta eventos duplicados sem antes verificar se são ocorrências distintas no tempo. | UC011 |
| 23879 | 28867 | CA04 - O sistema deve validar a comunicação com o inversor antes de iniciar a coleta. | UC012 |
| 23879 | 28868 | CA05 - O sistema deve registrar falhas de comunicação ocorridas durante a coleta. | UC012 |
| 23879 | 28869 | CA06 - O sistema deve persistir os eventos obtidos com sucesso. | UC010 |
