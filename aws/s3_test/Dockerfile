from alpine
ENV BUCKET "NONE"
WORKDIR /app
COPY ./requirements.txt ./s3Write.py .
RUN apk update
RUN apk add python3 py-pip
RUN pip install -r  requirements.txt
CMD ["python","./s3Write.py"]