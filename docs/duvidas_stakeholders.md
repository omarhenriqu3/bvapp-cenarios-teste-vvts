# Dúvidas para os stakeholders

| Código | Requisito | Dúvida | Cenários afetados |
|---|---|---|---|
| D01 | 23817 / 24962 | O que define inversor ativo e quais grandezas são coletadas por ciclo? | UC001 |
| D02 | 23817 / 24963 | Qual precisão e fuso horário devem ser usados para validar o timestamp? | UC002 |
| D03 | 23817 / 24965 | Qual timeout, número de tentativas e intervalo definidos em RF-4.1.03? | UC003 |
| D04 | 23817 / 24965 | O que ocorre e onde a falha fica visível quando as tentativas se esgotam? | UC003 |
| D05 | 23817 / 24966 | Qual condição objetiva caracteriza um inversor como indisponível? | UC004 |
| D06 | 23817 / 28851 | “Análise” é parte desta feature? Confirmar remoção do termo ou referência a consulta histórica. | UC002 |
| D07 | 23849 / 25769-25770 | Quais campos são obrigatórios e quais regras de tipo, unidade e faixa são válidas? Usina e PDF fazem parte do cadastro e são obrigatórios? Como o erro é apresentado? | UC006, UC007 |
| D08 | 23849 / 25771 | Fatura excluída logicamente impede novo cadastro? O que significa “substituída” e qual retorno ocorre ao tentar duplicar? | UC008 |
| D09 | 23849 / 25773 | Qual prazo mensurável define “imediatamente” e qual consulta histórica deve mostrar a fatura? | UC006 |
| D10 | 23879 / 24841 | A captura de eventos é periódica (qual intervalo) ou disparada pelo inversor? | UC010 |
| D11 | 23879 / 24842 | Quais tipos e níveis de severidade existem? Severidade integra o registro do evento? | UC010 |
| D12 | 23879 / 24843 | Quais campos definem duplicidade e qual janela temporal distingue ocorrências? | UC011 |
| D13 | 23879 / 28867-28868 | Como validar comunicação e timeout? O que ocorre se a validação falhar? Quais dados são registrados e onde a falha pode ser consultada? | UC012 |
| D14 | 23879 / 24841 e 28869 | CA 28869 sobrepõe o registro automático de CA 24841; confirmar se devem ser unidos ou mantidos separados. | UC010 |
