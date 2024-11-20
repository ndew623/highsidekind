FROM python

RUN pip install flask flask-sqlalchemy psycopg2-binary python-dotenv

COPY app.py /app.py

EXPOSE 8080

ENTRYPOINT ["python", "/app.py"]