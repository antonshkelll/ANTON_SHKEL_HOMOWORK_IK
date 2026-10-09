# Шкель Антон ПрИнж25-1

FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY task-2/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY task-2/bot.py task-2/lyrics.txt ./

CMD ["python", "bot.py"]
