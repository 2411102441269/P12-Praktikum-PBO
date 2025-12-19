import logging
from validator_interface import ValidatorInterface

class PrerequisiteValidator(ValidatorInterface):
    """Validator prasyarat mata kuliah."""

    def validate(self, student, course):
        if course["prasyarat"] not in student["matkul_lulus"]:
            logging.warning("Validasi prasyarat gagal")
            return "Gagal: Prasyarat belum terpenuhi"
        return None
