from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import List
from core.database import get_db
from models.barber import Barber
from schemas.barber import BarberResponse

from sqlalchemy.orm import selectinload

router = APIRouter()

@router.get("/", response_model=List[BarberResponse])
async def read_barbers(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Barber).options(selectinload(Barber.barber_services)).offset(skip).limit(limit))
    barbers = result.scalars().all()
    return barbers
