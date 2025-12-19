from abc import ABC, abstractmethod

class ValidatorInterface(ABC):
    """
    Interface untuk semua aturan validasi registrasi mahasiswa.
    """

    @abstractmethod
    def validate(self, student, course):
        """
        Melakukan validasi data mahasiswa dan mata kuliah.

        Args:
            student (dict): Data mahasiswa.
            course (dict): Data mata kuliah.

        Returns:
            str | None: Pesan error atau None jika valid.
        """
        pass

class IValidationRule:
    """Interface untuk aturan validasi registrasi mahasiswa.""" [cite: 36, 87]

    def validate(self, student):
        """
        Memvalidasi data mahasiswa. [cite: 45]

        Args:
            student: Objek mahasiswa yang divalidasi. [cite: 46]

        Returns:
            bool: True jika valid, False jika tidak. [cite: 49]
        """
        pass