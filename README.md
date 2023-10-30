# calculator_DM

[Дока от Позднякова](https://docs.google.com/document/u/0/d/1Dv_6AIhxg_3ezu6VMcEnMpyfRzgym9l8PmE4ULGfjgM/mobilebasic)

[Дока наша](https://docs.google.com/document/d/1U6PXU9S1H9UYg6vOdKlbHRTDxDVNCQ8lelEw45oxRsc/edit?usp=sharing)

[Отношения Рыжего и Ванькова](FrontBackRelation.md)

В проекте используется python 3.10.12

## Как начать работу с репозиторием. Или не рабочий pytest

На винде вместо `python3` возможно придётся писать `python` (я не знаю как вы установили свой питон)

1. Создайте виртуальное окружение

   Простая команда для этого

    ```bash
    python3 -m venv venv/calculator_DM
    ```

   Использовать окружение для этого терминала
   Пример команды для bash/zsh, для других терминалов или винды
   смотреть [тут](https://docs.python.org/3/library/venv.html#how-venvs-work)

    ```bash
    source venv/calculator_DM/bin/activate
    ```

1. Установите зависимости

   Помимо этого вы установите наш пакет computing (fix импортов)
   ```bash
   python3 -m pip install -r requirements.txt
   python3 -m pip install .
   ```

1. Запускайте тесты следующей командой

   ```bash
   # Запустить все тесты
   python3 -m pytest
   ```

   ```bash
   # Запустить конкретный тест
   python3 -m pytest tests/computing/Natural_test.py
   ```

Прим.
Чтобы `pytest` нашел ваши тесты, файлы должны иметь приписку `test` в начале или в конце:

Валидные названия тестов: `test_rational.py`, `gcd_test.py`.
Имхо, лучше писать test в конце
