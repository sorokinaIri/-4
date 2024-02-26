class language:
    """ Базовый класс - язык програмирования. """

    @property
    def name(self):
        """Геттер не принимает никаких агрументов, но должен возвращать какой-то результат."""
        return self._name  # внутри класса обращаемся к защищенному атрибуту

    @property
    def version(self):
        """Геттер не принимает никаких агрументов, но должен возвращать какой-то результат."""
        return self._version  # внутри класса обращаемся к защищенному атрибуту

    def __str__(self):
        return f"Язык программирование  {self.name}. Версия {self.version}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.version!r})"


class C_plus(language):
    """Дочерний класс - язык програмирования джава"""

    def __init__(self, difficulty: str, name: str, version: int):
        super().__init__(name, version)
        self._difficulty = None
        self.difficulty = difficulty  # отработает setter свойства!

    def __repr__(self):
        return f"{self.__class__.__name__}(difficulty={self.difficulty!r}, name={self.name!r}, version={self.version!r})"

    # вместо get_pages используется метод pages и @property
    @property
    def difficulty(self) -> str:
        """Возвращает сложность языка."""
        return self._difficulty

    # вместо set_pages используется метод pages и @pages.setter
    @difficulty.setter
    def difficulty(self, new_difficulty: str) -> None:
        """Устанавливает сложность языка."""
        if not isinstance(new_difficulty, str):
            raise TypeError("Сложность должна быть типа str")
        self._difficulty = new_difficulty


class Python(language):
    """Дочерний класс - язык програмирования питон"""

    def __init__(self, version: float, name: str, author: str):
        super().__init__(name, author)
        self._version = version  # отработает setter свойства!

    def __repr__(self):
        return f"{self.__class__.__name__}(version={self.version!r}, name={self.name!r}, author={self.author!r})"

    # вместо get_duration используется метод duration и @property
    @property
    def version(self) -> float:
        """Возвращает версию в питоне."""
        return self._version

    # вместо set_duration используется метод duration и @duration.setter
    @version.setter
    def version(self, new_version: float) -> None:
        """Устанавливает версию питона."""
        if not isinstance(new_version, float):
            raise TypeError("Версия языка должна быть типа float")
        if new_version <= 0:
            raise ValueError("Версия питона не может быть отрицательным числом")
        self._version = new_version

