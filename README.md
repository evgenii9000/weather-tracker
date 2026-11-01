# Weather Tracker

Простой парсер погоды для нескольких городов. Каждый день скрипт сохраняет
температуру, ветер и влажность в файл `weather.log` с меткой времени в UTC.
Обновление запускается автоматически через GitHub Actions.

## Города

Список городов задаётся в `weather.py` в переменной `CITIES`:

```python
CITIES = ["Chisinau", "Bucharest", "London", "Stockholm"]
```

Чтобы добавить или убрать город — отредактируйте этот список.

## Формат записи в `weather.log`

```
2026-11-01T07:00:12+00:00 | Chisinau | +12°C ↙ 5km/h 68%
```

При ошибке запроса пишется строка:

```
2026-11-01T07:00:15+00:00 | London | ERROR: ...
```

## Запуск локально

```bash
pip install requests
python weather.py
```

## Автоматический запуск

Workflow `.github/workflows/Daily-Weather.yml` запускается:

- ежедневно в **07:00 UTC** (по расписанию `0 7 * * *`);
- вручную через **Actions → Daily Weather Fetch → Run workflow**.

Результат коммитится в `weather.log` автоматически.

## Если workflow отключён

GitHub отключает scheduled workflows после 60 дней без активности
в репозитории. Чтобы включить обратно:

1. Откройте вкладку **Actions**.
2. Выберите **Daily Weather Fetch** слева.
3. Нажмите **Enable workflow**.

Так как workflow делает ежедневный коммит в `weather.log`, таймер
неактивности обычно сбрасывается сам.

## Требования

- Python 3.10+
- Пакет `requests`

## Структура проекта 

```
.
├── .github/workflows/Daily-Weather.yml
├── weather.py
├── weather.log
└── README.md
```
