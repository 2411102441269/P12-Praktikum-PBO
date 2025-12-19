import logging
from validator_manager import ValidatorManager
from sks_validator import SksValidator
from prerequisite_validator import PrerequisiteValidator
from ipk_validator import IpkValidator

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s - %(message)s"
)

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

manager = ValidatorManager(validators)
print(manager.validate(student, course))
