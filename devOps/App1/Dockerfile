FROM baseImage
WORKDIR /app
COPY ../apps/python-api .

RUN pip install -r requirements.txt

CMD ["python", "app.py"]