FROM python:3.9-slim
WORKDIR /app
COPY . /app
ARG TEST1
ENV TEST1=${TEST1}
CMD ["python", "app.py"]


#docker build --build-arg TEST1=your_value -t test_secret .
#docker run test_secret


