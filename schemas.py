from pydantic import BaseModel

class PerfilCreate(BaseModel):
    perfil_nome: str

class UsuarioCreate(BaseModel):
    nome: str
    email: str
    senha: str
    perfil: PerfilCreate