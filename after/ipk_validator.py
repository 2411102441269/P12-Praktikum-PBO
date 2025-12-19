import logging
from validator_interface import ValidatorInterface

class IpkValidator(ValidatorInterface):
    """Validator IPK mahasiswa."""

    def validate(self, student, course):
        if student["ipk"] < 3.0:
            logging.warning("Validasi IPK gagal")
            return "Gagal: IPK tidak memenuhi syarat"
        return None
