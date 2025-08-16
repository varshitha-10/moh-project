from fastapi import APIRouter, Depends
from .auth.dependencies import get_current_user
from .services import ask_service

router = APIRouter()

@router.post("/ask")
async def ask_endpoint(request: dict, user=Depends(get_current_user)):
    return await ask_service.handle_ask(request, user)
