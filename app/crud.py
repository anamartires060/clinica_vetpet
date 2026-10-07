from sqlalchemy.orm import Session

from .models import Tutor, Animal, Atendimento


def inserir_tutor(
    db,
    nome_completo,
    telefone,
    email
):
    tutor = Tutor(
        nome_completo=nome_completo,
        telefone=telefone,
        email=email
    )

    db.add(tutor)
    db.commit()
    db.refresh(tutor)

    return tutor


def inserir_animal(
    db,
    nome_animal,
    especie,
    raca,
    peso_kg,
    tutor_id
):
    animal = Animal(
        nome_animal=nome_animal,
        especie=especie,
        raca=raca,
        peso_kg=peso_kg,
        tutor_id=tutor_id
    )

    db.add(animal)
    db.commit()
    db.refresh(animal)

    return animal


def inserir_atendimento(
    db,
    data_atend,
    motivo,
    valor_consulta,
    animal_id
):
    atendimento = Atendimento(
        data_atendimento=data_atend,
        motivo=motivo,
        valor_consulta=valor_consulta,
        animal_id=animal_id
    )

    db.add(atendimento)
    db.commit()
    db.refresh(atendimento)

    return atendimento