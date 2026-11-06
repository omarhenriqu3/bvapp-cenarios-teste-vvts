'''
UC004 - Continuidade das coletas quando um inversor está indisponível

Objetivo: Verificar que a indisponibilidade de um inversor não interrompe a coleta dos demais.

Requisitos:
- Feature 23817 - Coleta automática de dados; CA 24966.

Ator:
- Sistema BVapp (processo automático)

Pré-condições:
- INV-01 e INV-02 pertencem à Usina Solar Alfa; INV-02 responde à coleta. A definição objetiva de indisponibilidade deve ser esclarecida (D05).

Dados de teste:
- INV-01 indisponível conforme condição definida pelos stakeholders; INV-02 disponível; ciclo 03/2026 (D05).

Resultado esperado (resumo):
- O sistema mantém a coleta dos demais inversores mesmo quando um deles está indisponível.

Autor: Omar Henrique

Dúvidas para os stakeholders:
- D05
'''

# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# O sistema inicia a coleta de INV-01 e INV-02. [RN1]
#
# INV-01 se enquadra na condição de indisponibilidade definida pelos stakeholders; a definição permanece NÃO DEFINIDA [D05].
#
# O sistema prossegue a coleta de INV-02, sem interrompê-la por causa de INV-01. [RN1]
#
# O ator verifica o resultado de INV-02 e confirma que a coleta não foi interrompida.

# 🟠 [A1] - INDISPONIBILIDADE NÃO CARACTERIZADA
# ---------------------------------------------------------------

# O ator verifica INV-01 sem uma regra acordada que determine quando o inversor é indisponível.
#
# O sistema deve classificar INV-01 como indisponível? Resultado esperado: NÃO DEFINIDO [D05].

# 🟠 [A2] - MAIS DE UM INVERSOR INDISPONÍVEL
# ---------------------------------------------------------------

# O ator acompanha o ciclo com INV-01 e INV-02 indisponíveis e INV-03 disponível.
#
# O CA cobre explicitamente a continuidade quando um inversor está indisponível; o comportamento para essa condição adicional não está especificado. Resultado esperado: NÃO DEFINIDO [D05].

# 🟣 [RN1] - COLETAS INDEPENDENTES
# ---------------------------------------------------------------

# O sistema não interrompe coletas de outros inversores caso um deles esteja indisponível (CA 24966).

import unittest


class UC004Test(unittest.TestCase):
    @unittest.skip("Documentação futura; fluxo não automatizado.")
    def test_fluxo_principal(self):
        pass

    @unittest.skip("Documentação futura; fluxo não automatizado.")
    def test_a1(self):
        pass

    @unittest.skip("Documentação futura; fluxo não automatizado.")
    def test_a2(self):
        pass

