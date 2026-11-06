'''
UC008 - Bloqueio de fatura duplicada para a mesma usina e mês/ano

Objetivo: Verificar que o sistema impede cadastrar fatura duplicada para a mesma combinação de mês/ano e usina.

Requisitos:
- Feature 23849 - Cadastro manual de Injeção de Energia mensal; CA 25771.

Ator:
- Tesoureiro

Pré-condições:
- Já existe uma fatura cadastrada para Usina Solar Alfa em 03/2026.

Dados de teste:
- Usina Solar Alfa; 03/2026; fatura existente com valores de referência 1200, 400, 200 e 500.

Resultado esperado (resumo):
- O sistema impede o cadastro de outra fatura para o mesmo mês/ano e usina.

Autor: Omar Henrique

Dúvidas para os stakeholders:
- D08
'''

# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# O Tesoureiro inicia o cadastro de outra fatura para Usina Solar Alfa em 03/2026. [RN1]
#
# O Tesoureiro preenche os campos da fatura com os valores de referência.
#
# O Tesoureiro seleciona salvar.
#
# O sistema verifica a combinação de mês/ano e usina e impede a duplicidade. [RN1]
#
# O texto ou forma do retorno ao usuário não está definido; resultado esperado: NÃO DEFINIDO [D08].

# 🟠 [A1] - MESMA USINA E MESMO MÊS/ANO
# ---------------------------------------------------------------

# O ator repete o cadastro para Usina Solar Alfa, 03/2026.
#
# O sistema impede o cadastro duplicado. [RN1]

# 🟠 [A2] - FATURA EXCLUÍDA LOGICAMENTE
# ---------------------------------------------------------------

# O ator tenta cadastrar novamente Usina Solar Alfa, 03/2026, após a fatura anterior ser excluída logicamente.
#
# Não está definido se uma fatura excluída logicamente bloqueia o novo cadastro; resultado esperado: NÃO DEFINIDO [D08].

# 🟠 [A3] - FATURA SUBSTITUÍDA
# ---------------------------------------------------------------

# O ator consulta a regra para uma fatura com status “substituída”.
#
# O significado e a origem desse status não estão definidos; resultado esperado: NÃO DEFINIDO [D08].

# 🟣 [RN1] - UNICIDADE POR MÊS/ANO E USINA
# ---------------------------------------------------------------

# O sistema impede cadastro de fatura duplicada para o mesmo mês/ano e usina (CA 25771).
