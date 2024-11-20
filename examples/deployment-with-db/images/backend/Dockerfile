FROM python

RUN pip install flask flask-sqlalchemy psycopg2-binary python-dotvenv

COPY app.py /app.py

ENTRYPOINT ["/bin/bash", "-c", "python", "/app.py"]