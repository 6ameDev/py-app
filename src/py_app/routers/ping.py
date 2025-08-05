from fastapi import APIRouter

router = APIRouter(prefix="/ping", tags=["Ping"])

@router.get("")
def ping():
    return {"Message": "Pong"}
