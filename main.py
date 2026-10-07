from datetime import datetime

from app.database import Base, SessionLocal, engine
from app.crud import (
    inserir_tutor,
    inserir_animal,
    inserir_atendimento
)


# Criação das tabelas
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

print("Tabelas criadas com sucesso!")


db = SessionLocal()


try:

    tutor1 = inserir_tutor(
        db,
        "Ana Laura Martires Rodrigues",
        "61999990001",
        "ana.laura.teste@example.com"
    )

    tutor2 = inserir_tutor(
        db,
        "Nome do Colega",
        "61999990002",
        "colega.teste@example.com"
    )

    print("Tutores inseridos com sucesso!")


    # Cão
    animal1 = inserir_animal(
        db,
        "Thor",
        "cão",
        "Golden Retriever",
        35.5,
        tutor1.id
    )

    # Gato
    animal2 = inserir_animal(
        db,
        "Mia",
        "gato",
        "Siamês",
        4.2,
        tutor1.id
    )

    # Ave
    animal3 = inserir_animal(
        db,
        "Luna",
        "ave",
        "Calopsita",
        0.09,
        tutor2.id
    )

    print("Animais inseridos com sucesso!")


    data_hoje = datetime.now().strftime("%d/%m/%Y")


    atendimento1 = inserir_atendimento(
        db,
        data_hoje,
        "Vacina anual V8",
        120.00,
        animal1.id
    )


    atendimento2 = inserir_atendimento(
        db,
        data_hoje,
        "Consulta de rotina",
        90.00,
        animal2.id
    )


    atendimento3 = inserir_atendimento(
        db,
        data_hoje,
        "Avaliação geral",
        70.00,
        animal3.id
    )


    print("Atendimentos inseridos com sucesso!")

    print()
    print("Sistema executado com sucesso!")

    print()
    print("===== DADOS CADASTRADOS =====")

    print(
        "Tutor 1:",
        tutor1.nome_completo
    )

    print(
        "Tutor 2:",
        tutor2.nome_completo
    )

    print(
        "Animal 1:",
        animal1.nome_animal,
        "-",
        animal1.especie
    )

    print(
        "Animal 2:",
        animal2.nome_animal,
        "-",
        animal2.especie
    )

    print(
        "Animal 3:",
        animal3.nome_animal,
        "-",
        animal3.especie
    )

    print(
        "Atendimento 1:",
        atendimento1.motivo,
        "- R$",
        atendimento1.valor_consulta
    )

    print(
        "Atendimento 2:",
        atendimento2.motivo,
        "- R$",
        atendimento2.valor_consulta
    )

    print(
        "Atendimento 3:",
        atendimento3.motivo,
        "- R$",
        atendimento3.valor_consulta
    )


finally:

    db.close()
