# fb2reader

[![Версия PyPI](https://badge.fury.io/py/fb2reader.svg)](https://badge.fury.io/py/fb2reader)
[![Версии Python](https://img.shields.io/pypi/pyversions/fb2reader.svg)](https://pypi.org/project/fb2reader/)
[![Лицензия](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Русская версия | [English](README.md)

Python библиотека для извлечения данных и метаданных из файлов формата FB2 (FictionBook 2).

## Описание

**fb2reader** — это легковесная и простая в использовании Python библиотека для работы с файлами формата FB2. Она предоставляет удобные методы для извлечения метаданных книги (название, авторы, описание, ISBN и т.д.) и контента, что делает её идеальной для создания систем управления электронными книгами, инструментов каталогизации или приложений для чтения.

## Возможности

- Извлечение метаданных книги:
  - Название, авторы, переводчики
  - Информация о серии книг
  - Язык, жанры/теги
  - ISBN, идентификатор книги
  - Описание/аннотация
- Извлечение и сохранение обложек (JPEG/PNG)
- Извлечение содержимого книги
- Сохранение содержимого книги в HTML
- Полная обработка ошибок и валидация
- Поддержка type hints
- Комплексное тестовое покрытие
- Поддержка Python 3.8+

## Установка

Установка с помощью pip:

```bash
pip install fb2reader
```

### Требования

- Python 3.8 или выше
- BeautifulSoup4
- lxml

## Быстрый старт

```python
from fb2reader import fb2book

# Открываем FB2 файл
book = fb2book('path/to/your/book.fb2')

# Получаем метаданные книги
title = book.get_title()
authors = book.get_authors()
description = book.get_description()

print(f"Название: {title}")
print(f"Авторы: {authors}")
print(f"Описание: {description}")
```

## Примеры использования

### Получение метаданных книги

```python
from fb2reader import fb2book

book = fb2book('example.fb2')

# Получаем базовую информацию
title = book.get_title()
isbn = book.get_isbn()
lang = book.get_lang()
identifier = book.get_identifier()

# Получаем авторов (возвращает список словарей)
authors = book.get_authors()
for author in authors:
    print(f"Автор: {author['full_name']}")
    print(f"  Имя: {author['first_name']}")
    print(f"  Фамилия: {author['last_name']}")

# Получаем переводчиков
translators = book.get_translators()
for translator in translators:
    print(f"Переводчик: {translator['full_name']}")

# Получаем информацию о серии
series = book.get_series()
if series:
    print(f"Часть серии: {series}")

# Получаем жанры/теги
tags = book.get_tags()
print(f"Жанры: {', '.join(tags)}")

# Получаем описание
description = book.get_description()
print(f"Описание: {description}")
```

### Работа с обложками

```python
from fb2reader import fb2book

book = fb2book('example.fb2')

# Проверяем наличие обложки
cover = book.get_cover_image()
if cover:
    # Сохраняем обложку
    result = book.save_cover_image(output_dir='covers')
    if result:
        image_name, image_type = result
        print(f"Обложка сохранена: {image_name}.{image_type}")
else:
    print("Обложка не найдена")

# Можно также указать тип изображения явно
book.save_cover_image(
    cover_image=cover,
    cover_image_type='jpeg',
    output_dir='my_covers'
)
```

### Извлечение содержимого книги

```python
from fb2reader import fb2book

book = fb2book('example.fb2')

# Получаем тело книги как строку
body = book.get_body()
if body:
    print(f"Длина содержимого: {len(body)} символов")

# Сохраняем тело книги в HTML файл
try:
    output_path = book.save_body_as_html(
        output_dir='output',
        output_file_name='book_content.html'
    )
    print(f"Содержимое сохранено в: {output_path}")
except Exception as e:
    print(f"Ошибка сохранения содержимого: {e}")
```

### Использование вспомогательной функции

```python
from fb2reader import get_fb2

# Альтернативный способ создания экземпляра fb2book
book = get_fb2('example.fb2')

if book:
    title = book.get_title()
    print(f"Название: {title}")
else:
    print("Неверный или не FB2 файл")
```

### Обработка ошибок

```python
from fb2reader import fb2book
from fb2reader.fb2reader import InvalidFB2Error, FB2ReaderError

try:
    book = fb2book('example.fb2')
    title = book.get_title()
    print(f"Название: {title}")

except FileNotFoundError:
    print("Файл не найден")
except InvalidFB2Error as e:
    print(f"Неверный FB2 файл: {e}")
except FB2ReaderError as e:
    print(f"Ошибка FB2 Reader: {e}")
except Exception as e:
    print(f"Неожиданная ошибка: {e}")
```

## Справочник API

### Класс: `fb2book`

Основной класс для работы с FB2 файлами.

#### Конструктор

```python
fb2book(file: str)
```

- `file` (str): Путь к FB2 файлу

**Вызывает исключения:**
- `FileNotFoundError`: Если файл не существует
- `InvalidFB2Error`: Если файл не является валидным FB2
- `IOError`: Если произошла ошибка чтения файла

#### Методы

##### Методы для метаданных

- `get_identifier() -> Optional[str]` - Получить идентификатор книги
- `get_title() -> Optional[str]` - Получить название книги
- `get_authors() -> List[Dict[str, Optional[str]]]` - Получить список авторов
- `get_translators() -> List[Dict[str, Optional[str]]]` - Получить список переводчиков
- `get_series() -> Optional[str]` - Получить название серии
- `get_lang() -> Optional[str]` - Получить код языка
- `get_description() -> Optional[str]` - Получить описание/аннотацию книги
- `get_tags() -> List[str]` - Получить список жанров/тегов
- `get_isbn() -> Optional[str]` - Получить ISBN

##### Методы для контента

- `get_body() -> Optional[str]` - Получить тело книги
- `get_cover_image() -> Optional[BeautifulSoup]` - Получить элемент обложки
- `save_cover_image(cover_image=None, cover_image_type=None, output_dir='output') -> Optional[tuple]` - Сохранить обложку
- `save_body_as_html(output_dir='output', output_file_name='body.html') -> str` - Сохранить тело как HTML

### Функция: `get_fb2`

```python
get_fb2(file: str) -> Optional[fb2book]
```

Вспомогательная функция для создания экземпляра fb2book.

- Возвращает экземпляр `fb2book`, если файл является валидным FB2
- Возвращает `None`, если файл не является FB2 файлом

### Исключения

- `FB2ReaderError` - Базовое исключение для всех ошибок fb2reader
- `InvalidFB2Error` - Вызывается когда FB2 файл невалидный или не может быть распарсен

## Разработка

### Запуск тестов

```bash
# Установка зависимостей для разработки
pip install -e .
pip install pytest pytest-cov

# Запуск тестов
pytest tests/ -v

# Запуск с покрытием
pytest tests/ -v --cov=fb2reader --cov-report=html
```

### Структура проекта

```
fb2reader/
├── fb2reader/           # Основной пакет
│   ├── __init__.py      # Инициализация пакета
│   └── fb2reader.py     # Основная реализация
├── tests/               # Тестовый набор
│   ├── __init__.py
│   ├── conftest.py      # Pytest фикстуры
│   ├── test_fb2reader.py
│   └── test_data/       # Тестовые FB2 файлы
├── README.md            # Документация (английский)
├── README_RU.md         # Документация (русский)
├── setup.py             # Конфигурация пакета
├── requirements.txt     # Зависимости
└── LICENSE              # Лицензия Apache 2.0
```

## Внесение вклада

Мы приветствуем вклад в проект! Не стесняйтесь отправлять Pull Request.

1. Форкните репозиторий
2. Создайте ветку для вашей функции (`git checkout -b feature/AmazingFeature`)
3. Закоммитьте ваши изменения (`git commit -m 'Добавить AmazingFeature'`)
4. Отправьте изменения в ветку (`git push origin feature/AmazingFeature`)
5. Откройте Pull Request

## Лицензия

Этот проект лицензирован под Apache License 2.0 - см. файл [LICENSE](LICENSE) для подробностей.

## Автор

Роман Кудрявский - [devpilgrim@gmail.com](mailto:devpilgrim@gmail.com)

## Ссылки

- [Пакет PyPI](https://pypi.org/project/fb2reader/)
- [GitHub репозиторий](https://github.com/devpilgrin/fb2reader)
- [Трекер проблем](https://github.com/devpilgrin/fb2reader/issues)

## История изменений

### Версия 1.0.4 (Готовится к выпуску)

- Исправлены критические ошибки в `__init__.py`
- Исправлено декодирование обложек (base64 вместо hex)
- Добавлена правильная обработка ошибок и валидация
- Добавлены type hints для всех методов
- Улучшены docstrings
- Добавлен комплексный набор тестов
- Обновлен CI/CD pipeline с автоматическим тестированием
- Улучшена документация

### Версия 1.0.3

- Исправление ошибок и улучшение совместимости

## Благодарности

- Спецификация формата FB2: [FictionBook](http://www.fictionbook.org/)
- Создано с использованием [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/)
