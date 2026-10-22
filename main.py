"""Ponto de entrada da API EcoCycle para a Vercel."""
from fastapi import FastAPI
from routers import auth, fornecedores, materiais, lotes, equipamentos, producao

app = FastAPI(
    title="EcoCycle API - Backend",
    version="1.0.0",
    description="API REST do EcoCycle."
)

# Registra todas as rotas uma única vez.
for router in (auth, fornecedores, materiais, lotes, equipamentos, producao):
    app.include_router(router.router)

@app.get("/", tags=["Início"])
def home():
    return {"mensagem": "API está online e operacional!"}
