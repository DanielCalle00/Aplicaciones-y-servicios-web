from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db 
from schemas.medicion import Medicion, MedicionCreate, MedicionUpdate
from crud import medicion as crud_medicion

router = APIRouter()

@router.get("/", response_model=List[Medicion])
def listar_mediciones(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud_medicion.get_mediciones(db, skip=skip, limit=limit)

@router.get("/{id}", response_model=Medicion)
def consultar_medicion(id: int, db: Session = Depends(get_db)):
    db_medicion = crud_medicion.get_medicion(db, medicion_id=id)
    if db_medicion is None:
        raise HTTPException(status_code=404, detail="Medición no encontrada")
    return db_medicion

@router.post("/", response_model=Medicion)
def crear_medicion(medicion: MedicionCreate, db: Session = Depends(get_db)):
    return crud_medicion.create_medicion(db=db, medicion=medicion)

@router.patch("/{id}", response_model=Medicion)
def actualizar_medicion(id: int, medicion: MedicionUpdate, db: Session = Depends(get_db)):
    db_medicion = crud_medicion.update_medicion(db, medicion_id=id, medicion_data=medicion)
    if db_medicion is None:
        raise HTTPException(status_code=404, detail="Medición no encontrada")
    return db_medicion

@router.delete("/{id}")
def eliminar_medicion(id: int, db: Session = Depends(get_db)):
    db_medicion = crud_medicion.delete_medicion(db, medicion_id=id)
    if db_medicion is None:
        raise HTTPException(status_code=404, detail="Medición no encontrada")
    return {"mensaje": "Medición eliminada"}