import amino
from pyfiglet import figlet_format
from multiprocessing.pool import ThreadPool
print("""\u001b[31m
Script by deluvsushi
Github : https://github.com/deluvsushi""")
print(figlet_format("aminospamkilla", font="small"))
client = amino.Client()
email = input("-- Email::: ")
password = input("-- Password::: ")
client.login(email=email, password=password)
clients = client.sub_clients(size=100)
for x, name in enumerate(clients.name, 1):
	print(f"{x}.{name}")
com_id = clients.comId[int(input("-- Select the community::: ")) - 1]
sub_client = amino.SubClient(comId=com_id, profile=client.profile)
chats = sub_client.get_chat_threads(size=100)
for z, title in enumerate(chats.title, 1):
	print(f"{z}.{title}")
chat_id = chats.chatId[int(input("-- Select the chat::: ")) - 1]
message = input("-- Message::: ")
message_type = int(input("-- Message Type::: "))
threads_count = int(input("-- Number of threads::: "))
print("-- Started spamming...")

def spam_process():
	thread_pool = ThreadPool(threads_count)
	while True:
		try:
			thread_pool.apply_async(sub_client.send_message, [chat_id, message, message_type])
		except:
			return

pool = ThreadPool(threads_count)
pool.apply(spam_process)
