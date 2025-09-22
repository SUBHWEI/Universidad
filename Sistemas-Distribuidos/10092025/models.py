from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class TipoId(Base):
    __tablename__ = "tiposid"

    IdTipoId = Column(Integer, primary_key=True, index=True)
    Descripcion = Column(String(45), nullable=False)

    personas = relationship("Persona", back_populates="tipo_id")

class Genero(Base):
    __tablename__ = "genero"

    IdGenero = Column(Integer, primary_key=True, index=True)
    Descripcion = Column(String(45), nullable=False)

    personas = relationship("Persona", back_populates="genero")

class Persona(Base):
    __tablename__ = "persona"

    idPersona = Column(Integer, primary_key=True, index=True)
    IdTipoId = Column(Integer, ForeignKey("tiposid.IdTipoId"))
    Nombre = Column(String(45), nullable=False)
    Apellido = Column(String(45), nullable=False)
    Genero_IdGenero = Column(Integer, ForeignKey("genero.IdGenero"))

    tipo_id = relationship("TipoId", back_populates="personas")
    genero = relationship("Genero", back_populates="personas")
