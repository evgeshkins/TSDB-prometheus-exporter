# TSDB-prometheus-exporter - Time seriea база данных Prometheus
### TSDB в данном проекте используется для сбора таких метрик как: <br>
- Использование ядер процессора <br>
- Сколько всего оперативной памяти в ОС, сколько из неё используется <br>
- Объем дисков, сколько занято <br>
### Прилагаются следующие PromQL запросы: <br>
- sum(cpu_usage_percentage) - использование процессоров <br>
- {__name__=~"memory_total_bytes|memory_used_bytes"} - память (всего и используется) <br>
- {__name__=~"disk_total_bytes|disk_used_bytes"} - диски (весь объем и используется) <br>
## Стек
- Python 3.10 <br>
- Prometheus <br>
- psutil <br>
## Использование
1. Клонируйте репозиторий: <br>
```git clone https://github.com/evgeshkins/TSDB-prometheus-exporter.git . ``` <br>
2. Создайте виртуальное окружение: <br>
```python -m venv venv``` <br>
либо <br>
```py -m venv venv``` <br>
3. Активируйте виртуальное окружение: <br>
На Windows: <br>
```.venv\Scripts\activate``` <br>
На Linux: <br>
```source venv/bin/activate``` <br>
4. Установите библиотеки: <br>
```pip install -r requirements.txt``` <br>
5. Создайте файл .env в корне проекта и внесите туда значения следующих переменных: <br>
```python
EXPORTER_HOST=ЗНАЧЕНИЕ ХОСТА (например, 0.0.0.0)
EXPORTER_PORT=ЗНАЧЕНИЕ ПОРТА (например, 8000)
```
6. Скачать и установить Prometheus (можно скачать архив с официального репозитория github и распаковать) <br>
7. Перейдите в папку с распакованным Prometheus, найдите файл prometheus.yml и добавьте туда следующий блок:
```python
scrape_configs:
  - job_name: "system_exporter"
    static_configs:
      - targets: ["localhost:8000"] - заменить на значения своего хоста и порта
```
8. Запустите prometheus.exe <br>
9. Запустите приложение:
```python
python exporter.py
```
10. Приложение успешно запущено на требуемых хосте и порту! (в случае с примером на localhost:8000) <br>
Для тестирования запросов перейдите по адресу localhost:9090 и вводите запросы, указанные выше. <br>
ВАЖНО!!! Результаты первого запроса отображаются только в виде графика!
