import subprocess
import pyautogui as pag
import sys
import os
import time
import pandas as pd

profit_path = "C:/Users/1998a/AppData/Roaming/Nelogica/ClearTrader/profitchart.exe"

x = pag.size()[0]/50
y = pag.size()[1]/5

subprocess.call(["cmd", "/c", "start", "/max", profit_path])

os.makedirs('csvs', exist_ok=True)

#tempo para o profit estabelecer suas conexões

time.sleep(10)

timeframe = pag.prompt("Informe o timeframe desejado (1D, 1S, 15...)")

pag.click(x, y)

pag.typewrite(timeframe, 0.05)

pag.press('enter')

lista = pd.read_csv('ativos.csv', header=None)

ready = pag.confirm(f"O programa vai começar. Você selecionou o timeframe {timeframe} para {len(lista)} ativos.")

if ready == 'OK':

    for ticker in lista.values[:]: #para realizar algum teste, troque [:] por [:5]

        pag.click(x, y)

        pag.typewrite(ticker[0], 0.05)

        pag.press('enter')

        #tempo para o profit baixar os dados do ativo

        time.sleep(1.5)

        pag.rightClick(x, y)

        for a in range(0,20):
            pag.press('down', _pause=False)

        pag.press('enter')

        df = pd.read_clipboard()

        df['Ticker'] = ticker[0]

        df.to_csv(f'csvs/{ticker[0]}.csv')

    #merging all csvs

    os.chdir(f'{os.getcwd()}'+'\\csvs')

    combined_csv = pd.concat([pd.read_csv(f) for f in os.listdir()], ignore_index=True)
    combined_csv.to_csv("combined_csv.csv", index=False)
    combined_csv.drop('Unnamed: 0', axis=1, inplace=True)
    combined_csv.to_csv("combined_csv.csv")

    pag.confirm(f"Concluído com sucesso ({len(os.listdir()) - 1}/{len(lista)} baixados).")

    print('Done')

else:

    pag.confirm("O programa foi cancelado.")
