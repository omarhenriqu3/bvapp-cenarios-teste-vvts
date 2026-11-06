'''
UC009 - Restrição do cadastro de fatura ao perfil Tesoureiro

Objetivo: Verificar que somente o perfil Tesoureiro tem acesso à funcionalidade de cadastro de fatura.

Requisitos:
- Feature 23849 - Cadastro manual de Injeção de Energia mensal; CAs 25772 e 25774 (duplicados; cobertos em conjunto).

Ator:
- Tesoureiro; Gestor; Operador de Usina; Técnico de Manutenção.

Pré-condições:
- Existem usuários associados aos quatro perfis definidos para os testes.

Dados de teste:
- Usina Solar Alfa; 03/2026; perfis Tesoureiro, Gestor, Operador de Usina e Técnico de Manutenção.

Resultado esperado (resumo):
- O perfil Tesoureiro tem acesso ao cadastro; os demais perfis não têm acesso.

Autor: Omar Henrique

Dúvidas para os stakeholders:
- Nenhuma dúvida específica identificada para este cenário.
'''

# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# O usuário autenticado tem o perfil Tesoureiro. [RN1]
#
# O usuário acessa a funcionalidade de cadastro de fatura.
#
# O sistema permite o acesso à funcionalidade para o perfil Tesoureiro. [RN1]

# 🟠 [A1] - GESTOR SEM ACESSO AO CADASTRO
# ---------------------------------------------------------------

# O usuário autenticado tem o perfil Gestor.
#
# O usuário tenta acessar o cadastro de fatura.
#
# O sistema restringe o acesso ao cadastro para perfil diferente de Tesoureiro. [RN1]

# 🟠 [A2] - OPERADOR DE USINA SEM ACESSO
# ---------------------------------------------------------------

# O usuário autenticado tem o perfil Operador de Usina.
#
# O usuário tenta acessar o cadastro de fatura.
#
# O sistema restringe o acesso ao cadastro para perfil diferente de Tesoureiro. [RN1]

# 🟠 [A3] - TÉCNICO DE MANUTENÇÃO SEM ACESSO
# ---------------------------------------------------------------

# O usuário autenticado tem o perfil Técnico de Manutenção.
#
# O usuário tenta acessar o cadastro de fatura.
#
# O sistema restringe o acesso ao cadastro para perfil diferente de Tesoureiro. [RN1]

# 🟣 [RN1] - ACESSO EXCLUSIVO DO TESOUREIRO
# ---------------------------------------------------------------

# Apenas o perfil Tesoureiro tem acesso à funcionalidade de cadastro (CA 25772); o CA 25774 repete essa restrição e é coberto em conjunto.

import unittest


class UC009Test(unittest.TestCase):
    @unittest.skip("Documentação futura; fluxo não automatizado.")
    def test_fluxo_principal(self):
        pass

    @unittest.skip("Documentação futura; fluxo não automatizado.")
    def test_a1(self):
        pass

    @unittest.skip("Documentação futura; fluxo não automatizado.")
    def test_a2(self):
        pass

    @unittest.skip("Documentação futura; fluxo não automatizado.")
    def test_a3(self):
        pass

