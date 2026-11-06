'''
UC011 - Distinção entre eventos semelhantes e ocorrências em tempos diferentes

Objetivo: Verificar que eventos aparentemente duplicados não sejam descartados sem verificar se são ocorrências distintas no tempo.

Requisitos:
- Feature 23879 - Coleta automática de eventos; CA 24843.

Ator:
- Sistema BVapp (processo automático)

Pré-condições:
- O inversor pode emitir dois eventos com os mesmos campos descritivos e timestamps distintos; regra de duplicidade e janela temporal não definidas (D12).

Dados de teste:
- INV-01; Usina Solar Alfa; 03/2026; dois eventos com mesmo tipo e descrição e timestamps de ocorrência diferentes.

Resultado esperado (resumo):
- O sistema verifica se eventos aparentemente duplicados são ocorrências distintas no tempo antes de descartá-los.

Autor: Omar Henrique

Dúvidas para os stakeholders:
- D12
'''

# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# INV-01 emite dois eventos com mesmos dados descritivos e timestamps de ocorrência distintos.
#
# O sistema verifica se são ocorrências distintas no tempo antes de descartar um evento. [RN1]
#
# O sistema mantém os registros que correspondem a ocorrências distintas no tempo. [RN1]
#
# O ator consulta os registros e confirma que as duas ocorrências distintas não foram descartadas.

# 🟠 [A1] - MESMOS DADOS, HORÁRIOS DIFERENTES
# ---------------------------------------------------------------

# O ator compara dois registros de INV-01 com mesmo tipo e descrição e horários distintos.
#
# O sistema não descarta ocorrências distintas no tempo sem antes verificá-las. [RN1]

# 🟠 [A2] - MESMO TIMESTAMP
# ---------------------------------------------------------------

# O ator compara dois eventos com mesmos campos e o mesmo timestamp.
#
# A chave de duplicidade e a janela temporal não estão definidas; resultado esperado: NÃO DEFINIDO [D12].

# 🟠 [A3] - EVENTOS PRÓXIMOS NO TEMPO
# ---------------------------------------------------------------

# O ator compara eventos cujos timestamps estão próximos.
#
# Não há janela definida para decidir se são ocorrências distintas; resultado esperado: NÃO DEFINIDO [D12].

# 🟣 [RN1] - VERIFICAÇÃO ANTES DE DESCARTAR
# ---------------------------------------------------------------

# Antes de descartar eventos aparentemente duplicados, o sistema verifica se são ocorrências distintas no tempo (CA 24843). A regra objetiva requer esclarecimento (D12).
