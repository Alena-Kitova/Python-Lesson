from sqlalchemy import create_engine, text


class SubjectTable:
    _scripts = {
        "select": text("SELECT * FROM subject"),
        "delete": text("DELETE FROM subject WHERE \"subject_id\" "
                       "= :subject_id"),
        "insert_new": text("INSERT INTO subject "
                           "(\"subject_id\", \"subject_title\") "
                           "VALUES (:subject_id, :subject_title)"),
        "update": text("UPDATE subject SET \"subject_title\""
                       " = :subject_title WHERE \"subject_id\" "
                       "= :subject_id")
    }

    def __init__(self, connection_string):
        self.db = create_engine(connection_string)

    def get_subjects(self):
        with self.db.connect() as conn:
            result = conn.execute(self._scripts["select"])
            return result.mappings().all()

    def create_subject(self, subject_id, subject_title):
        with self.db.begin() as conn:
            conn.execute(self._scripts["insert_new"], {
                "subject_id": subject_id,
                "subject_title": subject_title
            })

    def update_subject(self, subject_id, new_title):
        with self.db.begin() as conn:
            conn.execute(self._scripts["update"], {
                "subject_id": subject_id,
                "subject_title": new_title
            })

    def delete_subject(self, subject_id):
        with self.db.begin() as conn:
            conn.execute(self._scripts["delete"], {"subject_id": subject_id})
