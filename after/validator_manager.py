import logging

class ValidatorManager:
    """Mengelola proses validasi registrasi mahasiswa."""

    def __init__(self, validators):
        self.validators = validators

    def validate(self, student, course):
        logging.info("Proses validasi dimulai")

        for validator in self.validators:
            result = validator.validate(student, course)
            if result:
                logging.warning("Registrasi gagal")
                return result

        logging.info("Registrasi berhasil")
        return "Registrasi berhasil"
