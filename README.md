# Тестирование выбора файла WorldFile в браузерах Chrome и FireFox.

## Содержание

1. Тесты
2. Использование

## Тесты

1. Тест проверяет возможность выбора WorldFile.

```python
def test_choice_worldfile(browser):
```

## Использование

Чтобы запустить тесты, следуйте инструкциям:

1. Установите необходимые библиотеки и зависимости из `requirements.txt`
2. Запустите тест.

Пример запуска с pytest:

```bash
pytest test_choice_wordfile.py 
```

Если надо запустить проверку на firefox то добавить опцию `--browser=firefox`,
по стандарту chrome

```bash
pytest test_choice_wordfile.py --browser=firefox
```

---

### Тест поддерживает интеграцию с Allure для генерации наглядных отчетов.

#### Запуск тестов с Allure:

```bash
pytest your_test_file.py --alluredir=/path/to/results/directory
```

Здесь `/path/to/results/directory` - это директория, куда будут сохранены результаты
выполнения тестов.

#### Генерация отчета:

После выполнения тестов, чтобы посмотреть отчет в интерфейсе Allure,
выполните следующую команду:

```bash
allure serve /path/to/results/directory
```

Это автоматически запустит веб-сервер и откроет веб-браузер с отчетом,
если у вас установлен Allure.
