import os
import psutil
from prometheus_client import start_http_server, Gauge
from dotenv import load_dotenv
import time
import logging

# Загрузка переменных окружения из файла .env
load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Переменные окружения
EXPORTER_HOST = os.getenv("EXPORTER_HOST")
EXPORTER_PORT = int(os.getenv("EXPORTER_PORT"))

# Метрики Prometheus
cpu_usage = Gauge("cpu_usage_percentage", "CPU usage percentage per core", ["core"])
memory_total = Gauge("memory_total_bytes", "Total system memory in bytes")
memory_used = Gauge("memory_used_bytes", "Used system memory in bytes")
disk_total = Gauge("disk_total_bytes", "Total disk space in bytes", ["disk"])
disk_used = Gauge("disk_used_bytes", "Used disk space in bytes", ["disk"])

# Функция сбора метрик
def collect_metrics():
    # Использование CPU
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True)):
        cpu_usage.labels(core=f"core_{i}").set(percentage)

    # Использование памяти
    memory = psutil.virtual_memory()
    memory_total.set(memory.total)
    memory_used.set(memory.used)

    # Использование дисков
    for partition in psutil.disk_partitions():
        usage = psutil.disk_usage(partition.mountpoint)
        disk_total.labels(disk=partition.device).set(usage.total)
        disk_used.labels(disk=partition.device).set(usage.used)

if __name__ == "__main__":
    # Запуск HTTP-сервера
    start_http_server(EXPORTER_PORT, addr=EXPORTER_HOST)
    logger.info(f"Exporter running on http://{EXPORTER_HOST}:{EXPORTER_PORT}")
    try:
        while True:
            collect_metrics()
            time.sleep(5)  # Сбор метрик каждые 5 секунд
    except KeyboardInterrupt:
        logger.info("Exporter stopped.")
