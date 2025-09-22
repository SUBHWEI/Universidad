from pydantic import BaseModel
from typing import Optional

class TipoIdBase(BaseModel):
    IdTipoId: int
    Descripcion: str

class TipoIdCreate(TipoIdBase):
    pass

class TipoIdResponse(TipoIdBase):
    class Config:
        from_attributes = True

class GeneroBase(BaseModel):
    IdGenero: int
    Descripcion: str

class GeneroCreate(GeneroBase):
    pass

class GeneroResponse(GeneroBase):
    class Config:
        from_attributes = True

class PersonaBase(BaseModel):
    idPersona: int
    IdTipoId: int
    Nombre: str
    Apellido: str
    Genero_IdGenero: int

class PersonaCreate(PersonaBase):
    pass

class PersonaResponse(PersonaBase):
    class Config:
        from_attributes = True
