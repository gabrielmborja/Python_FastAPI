from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models, schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/usuarios")
def criar_usuario(usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    email_existente = db.query(models.Usuario).filter_by(
        email=usuario.email
    ).first()

    if email_existente:
        raise HTTPException(status_code=400, detail="Email já cadastrado")

    perfil = models.Perfil(
        perfil_nome=usuario.perfil.perfil_nome
    )
    db.add(perfil)
    db.commit()
    db.refresh(perfil)

    novo_usuario = models.Usuario(
        nome=usuario.nome,
        email=usuario.email,
        senha=usuario.senha,
        id_perfil=perfil.id
    )
    db.add(novo_usuario)
    db.commit()

    return {"mensagem": "Usuário criado com sucesso"}


@app.get("/usuarios")
def listar_usuarios(db: Session = Depends(get_db)):
    usuarios = db.query(models.Usuario).all()
    return usuarios


@app.put("/usuarios/{usuario_id}")
def atualizar_usuario(
    usuario_id: int,
    usuario: schemas.UsuarioCreate,
    db: Session = Depends(get_db)
):
    usuario_db = db.query(models.Usuario).filter_by(id=usuario_id).first()

    if not usuario_db:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    usuario_db.nome = usuario.nome
    usuario_db.email = usuario.email
    usuario_db.senha = usuario.senha
    usuario_db.perfil.perfil_nome = usuario.perfil.perfil_nome

    db.commit()

    return {"mensagem": "Usuário atualizado com sucesso"}


@app.delete("/usuarios/{usuario_id}")
def deletar_usuario(usuario_id: int, db: Session = Depends(get_db)):
    usuario_db = db.query(models.Usuario).filter_by(id=usuario_id).first()

    if not usuario_db:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    db.delete(usuario_db)
    db.commit()

    return {"mensagem": "Usuário deletado com sucesso"}