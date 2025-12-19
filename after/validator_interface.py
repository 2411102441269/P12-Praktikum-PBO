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
