# profit_price_picker

 Collect all price data in Profit at once!

Trata-se de um script bem básico que criei porque sou preguiçoso. Não está bem formatado e também não está orientado a objetos (paciência, ainda não sou ágil fazendo códigos assim ~~ainda~~).

**Instruções de utilização:**

1. Baixe o repositório.

2. Instale os pacotes requisitados com o comando no prompt `pip install -r requirements.txt` (ir até a pasta com o Explorador de Arquivos e digitar `cmd` no browser). **DEPOIS DE DIGITAR O CÓDIGO APERTAR ENTER!**

![Alt text](imgs/cmd.png?raw=true "Como abrir o prompt já no path certo")

![Alt text](imgs/pipinstall.png?raw=true "Como instalar os pacotes requeridos")

3. Abra o arquivo `ativos.csv` e modifique a lista de ativos que você gostaria de baixar os dados (opcional, por padrão está uma lista com os 180 ativos mais negociados de 2020).

4. Encontre o caminho para o seu executável do Profit. No meu caso, é `C:/Users/1998a/AppData/Roaming/Nelogica/ClearTrader/profitchart.exe`. Uma vez encontrado, insira-o como string na variável `profit_path`, na linha 8 do arquivo `price_picker.py` (basta substituir pela minha variável e manter entre aspas).

![Alt text](imgs/path.png?raw=true "Como inserir o seu path do Profit")

5. Para rodar o programa, fechar o Profit (opcional) e reabrir o prompt. 

> *OBS: Caso queira rodar um simples teste, siga as informações da linha 33 no arquivo `price_picker.py`.*

![Alt text](imgs/teste.png?raw=true "Como rodar um teste")

6. Executar o comando `python prices_picker.py`. O script abrirá o Profit e começará a leitura depois de uma pergunta e uma confirmação.
Não mexer o mouse após isto (para coletar as informações dos 180 ativos padrão o tempo estimado é de ~8 minutos).

> **Caso queira cancelar o script por qualquer motivo, arraste o mouse para qualquer canto da tela e de um clique.**

7. Após finalizados todos ativos, o script aglomerará todas informações no arquivo `combined.csv` contido na pasta `csvs`, além de manter um arquivo para cada ticker analisado.

Bom proveito.