# Pr� requisito
- Possuir o python instalado
- Ter configurado em 'Vari�veis de Ambiente'

# Instala��o do WebApp
- Baixar o webapp, o mesmo deve ser descompactado na mesma pasta que se encontra o appserver.ini
- Caminho = http://arte.engpro.totvs.com.br/totvstec_framework/smartclient/smartclienthtml_webapp/
- Dentro do ini deve criar uma tag como a apresentado:
    [WEBAPP]
    port=<port>
    Ex: port=9095

# config.json
- Na documenta��o possui o passo a passo para a configura��o.
- O arquivo .json deve inserir em sua �rea de trabalho ou passar seu caminho como um par�metro de qualquer inicializa��o dd classe.
- Dentro do .json da tag "Url" deve ser informado o IP e porta que foi configurado no INI do WebApp:
    "Url": "http://localhost:9095/"

# Documenta��o do TIR
- https://github.com/totvs/tir

# Defini��o das �reas para extra��o (BIXLink)
- O processo exige que seja seleciona uma �rea para prosseguir
- A primeira �rea que deva ser selecionada � a "Comercial"

# Processo do TesteCase (BIXLink)
- Ser� desmarcado a �rea anterior
- Ser� marcado a proxima �rea
- Isso tudo ocorre em ordem crescente
     
    1. Comercial
    2. Controladoria
    3. Financeiro
    4. Materiais
    5. Produ��o
    6. RH
    8. DL
    9. Servi�os
    10. Varejo
    11. CRM
    12. Juridico

# OBSERVA��O (BIXLink)
- A �rea PCO n�o possui TestCase, por�m ela � apresentada no Wizard pois n�o foi poss�vel retirar do configurador.

