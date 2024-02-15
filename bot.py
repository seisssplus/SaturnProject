from pyrogram import Client, filters
from pyrogram.types import Message
import os
import time
import platform

api_id = 23962937
api_hash = 'e247a38e5d7d45235018717e76920252'
app = Client('Client', api_id, api_hash)


@app.on_message(filters.me & filters.text & filters.regex(r"\bлист\s+команд\b"))
def handle_command_list(client, message):
    text_to_send = """
𝗹𝗶𝘀𝘁 𝗰𝗼𝗺𝗺𝗮𝗻𝗱:

  <code>Создать </code>[нейм] (следующая строка)[текст].
создает файл в формате .txt добавляя его в директорию к основным исходом. 

  <code>Изменить </code>[нейм файла] (следующая строка)[текст который заменит прошлый]
Изменяет текст в вами указанном файле заменяя нынешние данные в нем на те которые вы кажите.

  <code>Показать лист</code>
Покажет лист файлов в формате .txt которые есть в директории.

  <code>Вывод</code> [нейм файла]
Выводит данные из вами указанного файла в сообщение.

  <code>Удалить</code> [нейм]
Удаляет файл указаный вами из директории там самым удаляя его вообще.
"""

    client.send_message(message.chat.id, text_to_send)
    message.delete()


@app.on_message(filters.me & filters.command("сатурн", prefixes="."))
def inf(client, message):
    text_to_send = """
█▀ ▄▀█ ▀█▀ █░█ █▀█ █▄░█
▄█ █▀█ ░█░ █▄█ █▀▄ █░▀█

a project created based on the theme and theme of bots for an account on the topic of creating files and storing information in them, the development of the bot for an account itself took place in the period (3/4 days, the idea was up to 5 days before this), from version 1.1 the bot is released on GitHub which is why it can be installed via Git.

This is why it was decided to announce public access to the bot as well as the main installation via Termux.

To open the list of commands, you can open the help by word - <code>лист команд</code>

developer, founder of the idea of ​​a bot for an account - <code>I_CEIC.t.me</code>
bot curator bio for account - <code>EndlessBiography.t.me</code>
    """
    client.send_message(message.chat.id, text_to_send)
    message.delete()




def create_file(client, message):
    content = message.text[len("создать\n"):].strip() 
    lines = content.split('\n')  
    filename = lines[0].replace('\n', '')  
    text = '\n'.join(lines[1:])  

    filename = "".join(x for x in filename if x.isalnum())  

    with open(filename + ".txt", "w") as file:
        file.write(text)
    
    client.send_message(message.chat.id, f"Файл {filename}.txt создан")
    message.delete()



def write_to_file(client, message):
    content = message.text[len("вывод\n"):].strip() 
    filename = content.split('\n')[0]  

    if not filename.endswith(".txt"):
        filename = filename + ".txt"

    if os.path.exists(filename):
        with open(filename, "r") as file:
            file_text = file.read()
            client.send_message(message.chat.id, f"Содержимое файла {filename}:\n\n{file_text}")
        message.delete() 
    else:
        client.send_message(message.chat.id, f"Файл {filename} не найден.")
        message.delete()



def delete_file(client, message):
    filename = message.text[len("удалить"):].strip()
    if not filename.endswith(".txt"):
        filename = filename + ".txt"

    if os.path.exists(filename):
        os.remove(filename)
        client.send_message(message.chat.id, f"Файл {filename} удален")
    else:
        client.send_message(message.chat.id, f"Файл {filename} не найден")
    message.delete()



def modify_file(client, message):
    content = message.text[len("изменить\n"):].strip() 
    filename = content.split('\n')[0]  
    new_text = '\n'.join(content.split('\n')[1:])

    if not filename.endswith(".txt"):
        filename = filename + ".txt"

    if os.path.exists(filename):
        with open(filename, "w") as file:
            file.write(new_text)
        client.send_message(message.chat.id, f"Файл {filename} изменен")
    else:
        client.send_message(message.chat.id, f"Файл {filename} не найден")
    message.delete()

def list_files(client, message):
    txt_files = [file for file in os.listdir() if file.endswith(".txt")]
    txt_list = "\n".join(txt_files)
    client.send_message(message.chat.id, f"Файлы .txt в текущей директории:\n\n{txt_list}")
    message.delete()


@app.on_message(filters.me & filters.text)
def handle_message(client, message):
    if message.text and message.text.startswith(("создать", "Создать")):
        create_file(client, message)
    elif message.text and message.text.startswith(("вывод", "Вывод")):
        write_to_file(client, message)
    elif message.text and message.text.startswith(("удалить", "Удалить")):
        delete_file(client, message)
    elif message.text and message.text.startswith(("изменить", "Изменить")):
        modify_file(client, message)
    elif message.text and message.text.startswith(("показать лист", "Показать лист")):
        list_files(client, message)


print("""
▄▀▀ ▄▀▄ ▀█▀ █░█ █▀▀▄ █▄░█
░▀▄ █▀█ ░█░ █░█ █▐█▀ █░▀█
▀▀░ ▀░▀ ░▀░ ▀▀▀ ▀░▀▀ ▀░░▀

   ╔═══════════════════╗
   ║version: 1.1 is: pyrpgram
   
   ║Telegram - t.me/I_CEIC   
   ╚═══════════════════╝
""")
app.run()