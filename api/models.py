from pydantic import BaseModel, Field
from typing import List
from datetime import datetime

class Precio(BaseModel):
    fecha: datetime
    valor: float

    class Config:
        orm_mode = True

class InventarioItem(BaseModel):
    sucursal: int
    cantidad: int
    ultima_actualizacion: datetime

    class Config:
        orm_mode = True

class Producto(BaseModel):
    id: str = Field(..., alias="_id")
    marca: str
    modelo: str
    nombre: str
    precio: List[Precio] = Field(default_factory=list)
    inventario: List[InventarioItem] = Field(default_factory=list)

    class Config:
        allow_population_by_field_name = True
        orm_mode = True

class ProductoInv(BaseModel):
    id: str = Field(..., alias="_id")
    marca: str
    modelo: str
    nombre: str
    precio: float
    cantidad: int

    class Config:
        allow_population_by_field_name = True
        orm_mode = True

class Direccion(BaseModel):
    calle: str
    numeracion: str
    comuna: str
    region: str

    class Config:
        orm_mode = True

class Sucursal(BaseModel):
    id: str = Field(..., alias="_id")
    nombrepila: str
    contrasena: str = Field(..., alias="pass")
    direccion: Direccion

    class Config:
        allow_population_by_field_name = True
        orm_mode = True
