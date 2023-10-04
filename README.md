# Тестирование выбора файла WorldFile в браузерах Chrome и FireFox.

## Содержание

1. Тесты
2. Использование

## Тесты

### 1. Проверка на браузере Chrome

Тест проверяет возможность выбора WorldFile на браузере Chrome.

```python
def test_choice_worldfile_chrome(browser_chrome):
```

### 2. Проверка на браузере FireFox

Тест проверяет возможность выбора WorldFile на браузере FireFox.

```python
def test_choice_worldfile_firefox(browser_firefox):
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
