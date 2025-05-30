from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hola mundo, servicio activo"}

@app.get("/saludo/{nombre}")
def saludo(nombre: str):
    return {"mensaje": f"Hola, {nombre}"}

    #python -m pip install -U fastapi uvicorn
    #python -m uvicorn RestBasic:app --reload