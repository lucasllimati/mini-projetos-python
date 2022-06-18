import pyautogui as spam
import time

message_limit = input("Enter n de mensagens: ")
# message = input("Coloque a mensagem: ")

message = "Teste 😎"

i = 0

time.sleep(5)

while i < int(message_limit):
  spam.typewrite(message)
  spam.press("Enter")
  i += 1

print("FIM")

# Ao executar o codigo e inserir o número de mensagens e a mensagem, clique no chat do mensageiro.