import logging
from validator_manager import ValidatorManager
from sks_validator import SksValidator
from prerequisite_validator import PrerequisiteValidator
from ipk_validator import IpkValidator

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s - %(name)s %(message)s'
)
LOGGER = logging.getLogger('RegistrationSystem')

student = {
    "sks": 20,
    "ipk": 3.2,
    "matkul_lulus": ["Algoritma", "Basis Data"]
}

course = {
    "sks": 3,
    "prasyarat": "Algoritma"
}

validators = [
    SksValidator(),
    PrerequisiteValidator(),
    IpkValidator()
]

result = manager.validate(student, course)
if result is None:
    LOGGER.info("Pendaftaran Berhasil: Mahasiswa memenuhi semua syarat.") [cite: 57, 62]
else:
    LOGGER.warning(f"Pendaftaran Gagal: {result}") [cite: 64, 65]