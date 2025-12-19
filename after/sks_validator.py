import logging
from validator_interface import ValidatorInterface

class SksValidator(ValidatorInterface):
    """Validator batas maksimal SKS."""

    def validate(self, student, course):
        if student["sks"] + course["sks"] > 24:
            logging.warning("Validasi SKS gagal: SKS melebihi batas")
            return "Gagal: SKS melebihi batas"
        return None
