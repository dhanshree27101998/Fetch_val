FROM python:3.9-slim
WORKDIR /app
COPY . /app
ARG TEST1
ARG TEST2
ENV TEST1=${TEST1}
ENV TEST2=${TEST2}
# RUN pip install cryptography
RUN pip install requests
RUN pip install --upgrade pip
RUN pip install Flask
CMD ["python", "app.py"]


#docker build --build-arg TEST1=your_value --build-arg TEST2=your_value1 -t test_secret .
#docker run test_secret

# docker run -e TEST1=your_value -e TEST2=your_value1 test_secret
