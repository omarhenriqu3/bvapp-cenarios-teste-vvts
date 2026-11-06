# BVapp didático - cenários funcionais

**Autor:** Omar Henrique  
**Features:** 23817 (Coleta automática de dados), 23849 (Cadastro manual de Injeção de Energia mensal), 23879 (Coleta automática de eventos).  
**Escopo:** documentação de testes; nenhuma funcionalidade do BVapp foi implementada.

## Estrutura

- `config/`: arquivos mínimos de configuração Django.
- functional_tests/: um arquivo test_uc...py por cenário, com docstring inicial e fluxos e regras em comentários.
- `docs/rastreabilidade.md`: cobertura dos 18 CAs das três features.
- `docs/duvidas_stakeholders.md`: dúvidas abertas identificadas no walkthrough.

## Cenários

| ID | Título | CAs |
|---|---|---|
| UC001 | Coleta automática dos inversores ativos a cada 15 minutos | CA 24962. |
| UC002 | Registro de timestamp e associação da leitura ao inversor | CAs 24963 e 28851. |
| UC003 | Falha na coleta e agendamento de nova tentativa | CA 24965. |
| UC004 | Continuidade das coletas quando um inversor está indisponível | CA 24966. |
| UC005 | Disponibilização dos dados para consulta em até 1 minuto | CA 24967. |
| UC006 | Ciclo CRUD da fatura mensal de injeção | CAs 25769 e 25773. Para fechar CRUD, atualização da Feature 28855 e exclusão da Feature 23853 são incluídas somente neste cenário. |
| UC007 | Validação dos campos obrigatórios e inválidos da fatura | CA 25770. |
| UC008 | Bloqueio de fatura duplicada para a mesma usina e mês/ano | CA 25771. |
| UC009 | Restrição do cadastro de fatura ao perfil Tesoureiro | CAs 25772 e 25774 (duplicados; cobertos em conjunto). |
| UC010 | Captura e persistência automática de evento com dados do inversor | CAs 24841, 24842 e 28869. |
| UC011 | Distinção entre eventos semelhantes e ocorrências em tempos diferentes | CA 24843. |
| UC012 | Verificação da comunicação e registro de falha na coleta de eventos | CAs 28867 e 28868. |

## Dados de teste

Usinas Solar Alfa e Solar Beta; INV-01 e INV-02 na Alfa; INV-03 na Beta; período 03/2026; perfis Gestor, Operador de Usina, Técnico de Manutenção e Tesoureiro. Unidades, limites, mensagens e regras ausentes não foram presumidos; consulte os códigos Dxx registrados nos cenários e em `docs/duvidas_stakeholders.md`.

O ciclo CRUD de UC006 usa edição da Feature 28855 e exclusão da Feature 23853 somente para completar o fluxo, como indicado nas pré-condições.

## Formato dos cenários

Cada arquivo test_uc...py contém o docstring inicial e os comentários dos fluxos principal, alternativos e regras de negócio.
