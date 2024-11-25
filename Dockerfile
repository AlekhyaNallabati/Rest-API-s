FROM python:3.10
WORKDIR /app
COPY  requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . .
CMD ["/bin/bash", "docker-entrypoint.sh"]


# To create Volume in docker : docker run -dp 5005:5000 -w /app -v "/C/Users/Alekhya/PycharmProjects/pythonProject/Rest-API-s:/app" flask-smorest-api
#docker run -dp 5000:5000 -w /app -v "/C/Users/Alekhya/PycharmProjects/pythonProject/Rest-API-s:/app" flask-smorest-api