FROM python:3.13
EXPOSE 5000
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["flask", "run", "--host", "0.0.0.0"]


# To create Volume in docker : docker run -dp 5005:5000 -w /app -v "/C/Users/Alekhya/PycharmProjects/pythonProject/Rest-API-s:/app" flask-smorest-api
#docker run -dp 5000:5000 -w /app -v "/C/Users/Alekhya/PycharmProjects/pythonProject/Rest-API-s:/app" flask-smorest-api