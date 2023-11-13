import pyautogui

# Caminho do arquivo "Gay_mods-1.txt"
caminho_arquivo = "Gay_mods-1.txt"

# Pressionar a combinação de teclas Win+1 para abrir o Google Chrome
pyautogui.hotkey('win', '1')

# Aguardar um breve momento para o Chrome abrir
pyautogui.sleep(2)

# Ler as linhas do arquivo
with open(caminho_arquivo, 'r') as arquivo:
    linhas = arquivo.readlines()

# Loop para digitar cada endereço em uma nova aba
for linha in linhas:
    # Limpar a linha (remover espaços em branco extras)
    endereco = linha.strip()

    # Abrir uma nova aba
    pyautogui.hotkey('ctrl', 't')
    pyautogui.sleep(0.5)

    # Digitar o endereço na barra de endereços
    pyautogui.write(endereco)
    pyautogui.press('enter')

    # Aguardar um breve momento antes de abrir a próxima aba
    pyautogui.sleep(0.5)
