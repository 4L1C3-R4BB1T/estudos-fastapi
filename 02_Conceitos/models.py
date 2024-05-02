from typing import Optional

from pydantic import BaseModel, validator


class Curso(BaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int

    @validator("titulo")
    def validar_titulo(cls, value):
        palavras = value.split(" ")
        if len(palavras) < 3:
            raise ValueError("O título deve ter pelo menos 3 palavras")
        if value.islower():
            raise ValueError("O título deve ser capitalizado")
        return value

    @validator("aulas")
    def validar_aulas(cls, value):
        if value <= 12:
            raise ValueError("Aulas deve ser maior que 12")
        return value

    @validator("horas")
    def validar_horas(cls, value):
        if value <= 10:
            raise ValueError("Horas deve ser maior que 10")
        return value


cursos = [
    Curso(id=1, titulo="Programação para Leigos", aulas=112, horas=58),
    Curso(id=2, titulo="Algoritmos e Lógica de Programação", aulas=87, horas=67),
]
