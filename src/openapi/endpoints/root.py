from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def get_api_info():
    return {"version": "1.0", "vendor": "Pentium Network", "product": "Mavis"}
