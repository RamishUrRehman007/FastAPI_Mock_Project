from fastapi import FastAPI, Path
from fastapi.param_functions import Query

app = FastAPI()

inventory = {
    1 : {
        'name': 'Milk',
        'price': 3.99,
        'brand': 'Regular'
    }
}

@app.get('/')
def success():
    return {'Message': 'Success'}

@app.get('/item/{item_id}')
def getItem(item_id:int = Path(None, description="Id of the Item")):
    return inventory[item_id]

@app.get('/item')
def getIemByName(item_name:str = Query(None, title='Name', description='Name of item')):
    for item in inventory:
        if inventory[item]['name'] == item_name:
            return inventory[item]
    
    return {'Message': 'Not Found'}