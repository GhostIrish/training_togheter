from atproto import Client
from infos import user, password

client = Client()

client.login(user, password)

client.send_post(text='Ultimo teste antes do berço')