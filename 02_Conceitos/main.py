from typing import Optional, Any

from fastapi import Depends
from fastapi import FastAPI
from fastapi import Header
from fastapi import HTTPException
from fastapi import Path
from fastapi import Query
from fastapi import Response
from fastapi import status

from time import sleep

from models import Curso


def fake_db():
    try:
        print("Abrindo conexão com Banco de Dados...")
        sleep(1)
    finally:
        print("Fechando conexão com Banco de Dados...")
        sleep(1)


app = FastAPI()

cursos = {
    1: {
        "titulo": "Programação para Leigos", 
        "aulas": 112, 
        "horas": 58
    },
    2: {
        "titulo": "Algoritmos e Lógica de Programação", 
        "aulas": 87, 
        "horas": 67
    }
}


@app.get("/cursos")
async def get_cursos(db: Any = Depends(fake_db)):
    return cursos


@app.get("/cursos/{curso_id}")
async def get_curso(
    curso_id: int = Path(title="ID do curso", description="Deve ser entre 1 e 2", gt=0, lt=3), 
    db: Any = Depends(fake_db)
):
    try:
        curso = cursos[curso_id]
        return curso
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Curso com ID {curso_id} não encontrado",
        )


@app.post("/cursos", status_code=status.HTTP_201_CREATED)
async def post_curso(curso: Curso, db: Any = Depends(fake_db)):
    next_id: int = len(cursos) + 1        
    cursos[next_id] = curso
    del curso.id
    return curso


@app.put("/cursos/{curso_id}")
async def put_curso(curso_id: int, curso: Curso, db: Any = Depends(fake_db)):
    if curso_id in cursos:
        cursos[curso_id] = curso
        del curso.id
        return curso
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Curso com ID {curso_id} não encontrado"
        )


@app.delete("/cursos/{curso_id}")
async def delete_curso(curso_id: int, db: Any = Depends(fake_db)):
    if curso_id in cursos:
        del cursos[curso_id]
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Curso com ID {curso_id} não encontrado"
        )


@app.get("/calculadora")
async def calcular(
    a: int = Query(default=None, gt=5),
    b: int = Query(default=None, gt=10),
    x_geek: str = Header(default=None),
    c: Optional[int] = None,
):
    soma = a + b
    if c:
        soma += c
    print(f"X-GEEK: {x_geek}")
    return {"resultado": soma}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info", reload=True)
