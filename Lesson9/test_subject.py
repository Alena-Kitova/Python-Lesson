import pytest
from sqlalchemy import create_engine, text
from subject import SubjectTable

db_connection_string = "postgresql://postgres:postgres@localhost:5432/postgres"


@pytest.fixture()
def db_connection():
    engine = create_engine(db_connection_string)
    connection = engine.connect()
    transaction = connection.begin()
    yield connection
    transaction.rollback()
    connection.close()


@pytest.fixture()
def subject_table(db_connection):
    return SubjectTable(db_connection_string)


# Добавление
def test_add_new(subject_table, db_connection):
    subject_id = 20
    subject_title = "Математика"

    subject_table.create_subject(subject_id, subject_title)

    with db_connection as conn:
        result = conn.execute(text
                              ("SELECT * FROM subject WHERE \"subject_id\" "
                               "= :subject_id"),
                              {"subject_id": subject_id})
        subject = result.mappings().first()

    assert subject is not None
    assert subject["subject_id"] == subject_id
    assert subject["subject_title"] == subject_title

    subject_table.delete_subject(subject_id)


# Изменение
def test_edit(subject_table, db_connection):
    subject_id = 21
    subject_title = "Японский"
    subject_table.create_subject(subject_id, subject_title)
    new_subject_title = "Японский язык"
    subject_table.update_subject(subject_id, new_subject_title)

    with db_connection as conn:
        result = conn.execute(text
                              ("SELECT * FROM subject WHERE \"subject_id\" "
                               "= :subject_id"),
                              {"subject_id": subject_id})
        subject = result.mappings().first()

    assert subject is not None
    assert subject["subject_id"] == subject_id
    assert subject["subject_title"] == new_subject_title

    subject_table.delete_subject(subject_id)


# Удаление
def test_delete(subject_table, db_connection):
    subject_id = 23
    subject_title = "Философия"
    subject_table.create_subject(subject_id, subject_title)
    subject_table.delete_subject(subject_id)

    with db_connection as conn:
        result = conn.execute(text
                              ("SELECT * FROM subject WHERE \"subject_id\""
                               " = :subject_id"),
                              {"subject_id": subject_id})
        subject = result.mappings().first()

    assert subject is None
