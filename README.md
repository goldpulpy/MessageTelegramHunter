# Telegram SMART Hunter

## Информация
- Версия: `1.0`
- ЯП: `python3`
- Зависимости: `requirements.txt`
- Логи `logs.txt`
- Конфиг `config.json`
- Примеры `examples.txt`

Telegram SMART Hunter программное обеспечение для Telegram на основе AI.
Ищет триггеры в чатах телеграм и отправляет их в определенный чат.

## Настройки
Создаем телеграм аккаунт и заходим в нужные чаты.
Заходим в https://my.telegram.org/auth
Создаем приложение и сохраняем `API ID` и `API HASH`


Конфиг: нужно `config.json.example` переименовать в `config.json` и заполнить данные

```json
{
    "API_ID": 12345, // API ID телеграм приложения
    "API_HASH": "Your API Hash", // API Hash телеграм приложения
    "SESSION_NAME": "my_session", // Имя сессии, если сессия не существует она будет создана
    "FORWARD_TO_ID": 12345, // ID телеграм чата куда отправлять отчет (без -100)
    "MESSAGE_POOL": 5, // Количество сообщений в пуле, рекомендуется не менять
    "WAIT_TIME": 5 // Время ожидания в секундах для прохода по чатам
}
```

Файл: `examples.txt`
Лист триггеров


## Запуск

Устанавливаем зависимости:
```bash
pip3 install -r requirements.txt
```
Открываем `screen`
```bash
screen
```

Запускаем:
```bash
python3 main.py
```

## Как войти в screen
```bash
screen -ls
screen -r <id>
```

## Как удалить screen
```bash
screen -S id -X quit
```
