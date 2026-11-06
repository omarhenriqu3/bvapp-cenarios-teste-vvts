'''
UC002 - Registro de timestamp e associação da leitura ao inversor

Objetivo: Verificar o registro de data e hora e a persistência das leituras associadas ao inversor correspondente.

Requisitos:
- Feature 23817 - Coleta automática de dados; CAs 24963 e 28851.

Ator:
- Sistema BVapp (processo automático)

Pré-condições:
- Há um ciclo de coleta concluído para INV-01, da Usina Solar Alfa.

Dados de teste:
- INV-01; Usina Solar Alfa; data/hora de referência 2026-03-01 10:00; precisão e fuso do timestamp não definidos (D02).

Resultado esperado (resumo):
- Cada coleta registra data e hora associadas ao inversor correspondente e toda leitura obtida é armazenada.

Autor: Omar Henrique

Dúvidas para os stakeholders:
- D02
- D06
'''

# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# O sistema obtém uma leitura de INV-01 durante o ciclo de coleta. [RN1]
#
# O sistema registra a data e a hora da coleta associadas a INV-01. [RN1]
#
# O sistema armazena a leitura obtida para posterior consulta. [RN2]
#
# O ator consulta o registro e confirma a associação com INV-01 e a presença da data e hora.
#
# A precisão e o fuso que devem ser considerados para validar o timestamp permanecem NÃO DEFINIDOS [D02].

# 🟠 [A1] - LEITURA SEM ASSOCIAÇÃO CONFIRMÁVEL
# ---------------------------------------------------------------

# O ator inspeciona uma leitura cuja associação com o inversor não pode ser confirmada.
#
# O resultado esperado para a leitura sem associação confirmável é NÃO DEFINIDO [D02].

# 🟠 [A2] - PRECISÃO DO TIMESTAMP
# ---------------------------------------------------------------

# O ator compara o horário registrado com o horário de referência do ciclo.
#
# A tolerância e o fuso que determinam a precisão aceitável são NÃO DEFINIDOS [D02].

# 🟠 [A3] - CONSULTA E ANÁLISE
# ---------------------------------------------------------------

# O ator verifica o uso da leitura em uma atividade de análise.
#
# O escopo da expressão “consulta e análise” não está definido para esta feature; resultado esperado: NÃO DEFINIDO [D06].

# 🟣 [RN1] - TIMESTAMP ASSOCIADO
# ---------------------------------------------------------------

# Cada coleta registra timestamp (data e hora) associado ao inversor correspondente (CA 24963).

# 🟣 [RN2] - ARMAZENAMENTO
# ---------------------------------------------------------------

# Toda leitura obtida durante a coleta deve ser armazenada (CA 28851). A associação ao inversor é coberta pelo CA 24963.
