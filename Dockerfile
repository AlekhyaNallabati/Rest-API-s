FROM python:3.13
WORKDIR /app
COPY ./requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . .
CMD ["gunicorn", "--bind", "0.0.0.0:80", "app:create_app()"]


# To create Volume in docker : docker run -dp 5005:5000 -w /app -v "/C/Users/Alekhya/PycharmProjects/pythonProject/Rest-API-s:/app" flask-smorest-api
#docker run -dp 5000:5000 -w /app -v "/C/Users/Alekhya/PycharmProjects/pythonProject/Rest-API-s:/app" flask-smorest-api