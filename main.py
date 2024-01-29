from fastapi import FastAPI, Path
from fastapi.param_functions import Query
from fastapi.responses import RedirectResponse
from fastapi.requests import Request
import uvicorn
from typing import Optional

app = FastAPI()

inventory = {
    1 : {
        'name': 'Milk',
        'price': 3.99,
        'brand': 'Regular'
    }
}

@app.get('/')
async def root_view(request: Request) -> RedirectResponse:
    return RedirectResponse(url=str(request.base_url) + "docs", status_code=303)


@app.get(
    "/items/{item_id}",
    response_model=dict,
    tags=["items"],
)
async def get_item_by_ID(
    item_id:int = Path(
        ...,
        title="Item ID",
        description="The ID of the Item to get.",
    ),
) -> dict:
    return inventory[item_id]


@app.get(
    "/items",
    response_model=dict,
    tags=["items"],
)
async def get_items(
    item_name: Optional[str] = Query(
        None,
        title="Name",
        description="The Name of the Item to get.",
    ),
) -> Optional[dict]:
    if item_name:
        for item in inventory:
            if inventory[item]['name'] == item_name:
                return inventory[item]
    
        return {'Message': 'Not Found'}
    else:
        return inventory


if __name__ == "__main__":  # pragma: no cover
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=10000
    )