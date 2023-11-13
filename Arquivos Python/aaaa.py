import pyautogui

# Caminho do arquivo "Gay_mods-1.txt"
caminho_arquivo = "Gay_mods-1.txt"

# Aguardar alguns segundos para posicionar o cursor no botão "Inscrever-se"
pyautogui.sleep(5)

# Localizar a posição do botão "Inscrever-se" na tela
imagem_botao = 'butao.PNG'
posicao_botao = pyautogui.locateOnScreen(imagem_botao)

# Verificar se o botão foi encontrado
if posicao_botao is not None:
    # Obter as coordenadas do centro do botão
    x, y, largura, altura = posicao_botao
    centro_x = x + largura // 2
    centro_y = y + altura // 2

    # Clicar no botão "Inscrever-se"
    pyautogui.click(centro_x, centro_y)
else:
    print("Botão 'Inscrever-se' não encontrado na tela.")

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

    # Aguardar o carregamento do site antes de clicar no botão
    pyautogui.sleep(2)

    # Localizar a posição do botão no site
    posicao_botao_site = pyautogui.locateOnScreen(imagem_botao, confidence=0.8)

    # Verificar se o botão foi encontrado no site
    if posicao_botao_site is not None:
        # Obter as coordenadas do centro do botão
        x, y, largura, altura = posicao_botao_site
        centro_x = x + largura // 2
        centro_y = y + altura // 2

        # Clicar no botão no site
        pyautogui.click(centro_x, centro_y)
        print("Botão clicado no site:", endereco)
    else:
        print("Botão não encontrado no site:", endereco)

    pyautogui.sleep(3.5)
    # Fechar a aba atual
    pyautogui.hotkey('ctrl', 'w')

    # Aguardar um breve momento antes de abrir a próxima aba
    pyautogui.sleep(0.5)
