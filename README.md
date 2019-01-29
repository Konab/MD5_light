# MD5_light
Веб-сервис, позволяющий посчитать MD5-хеш от файла, расположенного в сети Интернет

## Инструкция по установке

### Скачиваем нужные файлы
В терминале введите:
git clone https://github.com/Konab/MD5_light
cd MD5_light
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

По дефолту программа использует БД sqlite, если требуется другая задайте переменную среды:
export SQLALCHEMY_DATABASE_URI=....

Введите:
flask db init
flask db migrate
flask db upgrade

Для корректной работы функции, отправки емайл отчёта добавте информацию по Вашему почтовому серверу:
export MAIL_SERVER=....
export MAIL_PORT=....
export MAIL_USERNAME=....
export MAIL_USERNAME=....
export MAIL_PASSWORD=....

Готово.

Запустить flusk run

Работает на http://127.0.0.1:5000/
Запросы отправлять на http://127.0.0.1:5000/api

## Пример
>>> curl -X POST -d "url=https://upload.wikimedia.org/wikipedia/commons/a/ab/MD5.png" http://localhost:5000/api/submit
>>> {"id":"9312a166-5d9d-42c5-abb6-b66ed90d7043"}
>>> curl -X GET http://localhost:5000/api/check?id=9312a166-5d9d-42c5-abb6-b66ed90d7043
>>> {"md5":"73faf7c7607b070e6c17a77b4714fa43","status":"done","url":"https://upload.wikimedia.org/wikipedia/commons/a/ab/MD5.png"}
