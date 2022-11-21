import requests

# lista = ["index.php", "test", "register", "home", "test.txt", "notes", "build"]
lista = open("common.txt", "r")

for item in lista.readlines():
        url = "https://notes.webhacking.com.br/" + item.replace("\n", "")
        resposta = requests.get(url)
        if resposta.status_code == 200:
                print("[" + url + "] - [" + str(resposta.status_code) + "]")

