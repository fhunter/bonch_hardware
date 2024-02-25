Система мониторинга состояния железа (обновления и текущая конфигурация)

Для отправки данных использовать:
```
lshw -json|curl -v -XPOST http://127.0.0.1:8888/hardware/data --data-binary @- -H "Content-Type: application/json"
```
