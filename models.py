from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Perfil(Base):
    __tablename__ = "perfis"

    id = Column(Integer, primary_key=True, index=True)
    perfil_nome = Column(String, unique=True)

    usuario = relationship("Usuario", back_populates="perfil", uselist=False)


class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    email = Column(String, unique=True, index=True)
    senha = Column(String)
    id_perfil = Column(Integer, ForeignKey("perfis.id"))

    perfil = relationship("Perfil", back_populates="usuario")