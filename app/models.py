from sqlalchemy import Column, Integer, String, Float, ForeignKey
from app.database import Base


class Tutor(Base):
    __tablename__ = "tutores"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome_completo = Column(String(100),primary_key=False, nullable=True)
    telefone = Column(String(20),primary_key=False, nullable=False)
    email = Column(String(100),primary_key=False,unique=False, nullable=False)
    


class Animal(Base):
    __tablename__ = "animais"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome_animal = Column(String(60),primary_key=False, nullable=True)
    especie = Column(String(40),primary_key=False, nullable=False)
    raca = Column(String(60), primary_key=False,nullable=True)
    peso_kg = Column(Float, primary_key=False, nullable=True)
    tutor_id = Column(Integer, ForeignKey("tutores.id"), nullable=True)


class Atendimento(Base):
    __tablename__ = "atendimentos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    data_atendimento = Column(String(20),primary_key=False, nullable=True)
    motivo = Column(String(200),primary_key=False, nullable=True)
    valor_consulta = Column(Float, primary_key=False, nullable=True)
    animal_id = Column(Integer, ForeignKey("animais.id"), nullable=True)
