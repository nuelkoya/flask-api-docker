FROM python:3.10-alpine

WORKDIR /usr/src/app

ENV FLASK_APP=app.py

ENV FLASK_RUN_HOST=0.0.0.0

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5501

CMD ["flask", "run", "--debug", "--port=5501"]