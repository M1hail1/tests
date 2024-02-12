class VideoGame:
    """Базовый класс для видеоигр."""

    def __init__(self, title: str, developer: str, publisher: str):
        """Инициализация общих атрибутов видеоигр."""
        self.title = title
        self.developer = developer
        self.publisher = publisher

    def __str__(self) -> str:
        """Возвращает строковое представление игры."""
        return f"{self.title} от {self.developer}"

    def __repr__(self) -> str:
        """Возвращает официальное представление объекта."""
        return f"{self.__class__.__name__}(title={self.title!r}, developer={self.developer!r}, publisher={self.publisher!r})"

    def play(self) -> None:
        """Метод для запуска игры. Реализация может варьироваться."""
        print(f"Запуск игры {self.title}")


class ActionGame(VideoGame):
    """Класс для игр в жанре экшн."""

    def __init__(self, title: str, developer: str, publisher: str, pov: str):
        """
        Расширение конструктора:
        pov (point of view) - тип камеры в игре.
        """
        super().__init__(title, developer, publisher)
        self.pov = pov

    def __str__(self) -> str:
        """Перегруженный метод для детализированного описания экшн-игры."""
        return f"{self.title}: экшн-игра от {self.developer}, вид камеры: {self.pov}"

    def play(self) -> None:
        """Перегруженный метод play для запуска экшн-игр."""
        print(f"Запуск экшн-игры {self.title} с видом камеры {self.pov}.")


class StrategyGame(VideoGame):
    """Класс для игр в жанре стратегии."""

    def __init__(self, title: str, developer: str, publisher: str, setting: str):
        """
        Расширение конструктора:
        setting - настройка, определяющая эпоху или мир игры.
        """
        super().__init__(title, developer, publisher)
        self.setting = setting  # Инкапсуляция

    def __str__(self) -> str:
        """Перегруженный метод для описания стратегической игры."""
        return f"{self.title}: стратегия в сеттинге {self.setting} от {self.developer}"

    def play(self) -> None:
        """Перегруженный метод play с учетом особенностей стратегических игр."""
        print(f"Запуск стратегической игры {self.title} в сеттинге {self.setting}. Время развиваться!")



if __name__ == "__main__":
    # Write your solution here
    pass
