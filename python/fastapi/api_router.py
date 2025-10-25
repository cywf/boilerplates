from fastapi import APIRouter

api_router = APIRouter()


@api_router.get("/items")
async def get_items():
    """Get all items"""
    return {"items": []}


@api_router.get("/items/{item_id}")
async def get_item(item_id: int):
    """Get a specific item"""
    return {"item_id": item_id, "name": "Sample Item"}
