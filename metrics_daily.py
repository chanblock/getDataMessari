
import datetime
import time
from messari.messari import Messari
from pymongo import MongoClient

print('start')
#conexion mongodb
client = MongoClient()
db = client.messari.prueba1
#conexion messari
messari = Messari('5e64af49-aa9d-442c-b9c8-19c846a2ef7f')
response_data = messari.get_all_assets(page=1, limit=100)
timestamp = datetime.datetime.now().date()
         
timestamp= str(timestamp)

response_data.pop('status')
for asset in response_data['data']:               
    asset['date']=timestamp
    asset.pop('profile')
    asset.pop('id')
    asset.pop('serial_id')
    asset.pop('_internal_temp_agora_id')
                
    db.insert_one(asset).inserted_id
print('end')