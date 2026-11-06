'''
UC006 - Ciclo CRUD da fatura mensal de injeção

Objetivo: Documentar o fluxo completo de cadastro, consulta, atualização e exclusão lógica de uma fatura mensal.

Requisitos:
- Feature 23849 - Cadastro manual de Injeção de Energia mensal; CAs 25769 e 25773. Para fechar CRUD, atualização da Feature 28855 e exclusão da Feature 23853 são incluídas somente neste cenário.

Ator:
- Tesoureiro; Gestor para a etapa de exclusão, conforme feature externa usada para fechar CRUD.

Pré-condições:
- Cadastro, consulta histórica, edição e exclusão lógica estão disponíveis para a execução documental.
- A edição (Feature 28855) e a exclusão (Feature 23853) são pré-condições/etapas de fechamento do CRUD; não ampliam a rastreabilidade dos CAs próprios da Feature 23849.

Dados de teste:
- Usina Solar Alfa; 03/2026; Energia Injetada=1200; Energia Consumida=400; Créditos de Energia=200; Valores Financeiros=500; unidade e faixas NÃO DEFINIDAS (D07).

Resultado esperado (resumo):
- A fatura é salva e aparece na consulta histórica; a atualização reflete na consulta posterior e a exclusão lógica a retira da listagem padrão conforme as features externas.

Autor: Omar Henrique

Dúvidas para os stakeholders:
- D07
- D09
'''

# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# O Tesoureiro preenche os dados da fatura de Usina Solar Alfa, 03/2026, com os campos de energia, créditos e valores. [RN1]
#
# O Tesoureiro seleciona salvar. [RN1]
#
# O sistema salva a fatura. [RN1]
#
# O Tesoureiro consulta a listagem histórica e verifica a fatura. [RN2]
#
# O Tesoureiro edita Energia Injetada de 1200 para 1250 e salva, usando a etapa de edição da Feature 28855 para completar o CRUD.
#
# O Tesoureiro consulta novamente e verifica a alteração, conforme CA 28859 da Feature 28855.
#
# O Gestor solicita a exclusão lógica e conclui a etapa da Feature 23853 para completar o CRUD.
#
# O Gestor consulta a listagem padrão e verifica que a fatura excluída logicamente não aparece, conforme CA 24922 da Feature 23853.

# 🟠 [A1] - CAMPOS E UNIDADES DA FATURA
# ---------------------------------------------------------------

# O ator verifica os campos Energia Injetada, Energia Consumida, Créditos de Energia e Valores Financeiros.
#
# A lista de obrigatoriedade, as unidades e as faixas válidas precisam de definição; resultado esperado: NÃO DEFINIDO [D07].

# 🟠 [A2] - PRAZO DE APARECIMENTO NA CONSULTA
# ---------------------------------------------------------------

# O ator salva a fatura e inicia a consulta histórica.
#
# O significado mensurável de “imediatamente” em CA 25773 não foi definido; resultado esperado: NÃO DEFINIDO [D09].

# 🟠 [A3] - ANEXO PDF E USINA
# ---------------------------------------------------------------

# O ator verifica se usina e PDF anexado fazem parte do formulário de cadastro.
#
# A inclusão e obrigatoriedade desses dados não estão definidas em CA 25769; resultado esperado: NÃO DEFINIDO [D07].

# 🟣 [RN1] - CADASTRO DA FATURA
# ---------------------------------------------------------------

# O CA 25769 exige o preenchimento do formulário com dados da fatura (mês/ano, energias, créditos e valores) e que o sistema salve.

# 🟣 [RN2] - APARECIMENTO NA CONSULTA HISTÓRICA
# ---------------------------------------------------------------

# Após salvar, a fatura aparece na listagem histórica (CA 25773). O prazo exato requer esclarecimento (D09).
