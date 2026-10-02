from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# Esquema base con los campos obligatorios
class MedicionBase(BaseModel):
    estudiante_id: int
    variable: str
    valor: float
    unidad: str
    fecha_hora: datetime

# Esquema para crear una medición (hereda los campos del base)
class MedicionCreate(MedicionBase):
    pass

# Esquema para actualizar (los campos son opcionales por si solo cambias uno)
class MedicionUpdate(BaseModel):
    variable: Optional[str] = None
    valor: Optional[float] = None
    unidad: Optional[str] = None
    fecha_hora: Optional[datetime] = None

# Esquema de respuesta que incluye el ID generado por la base de datos
class Medicion(MedicionBase):
    id: int

    class Config:
        orm_mode = True