FROM python:3.12-slim AS base

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 7600
ENV PORT=7600

CMD ["python", "main.py"]