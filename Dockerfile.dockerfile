FROM python:3.7

RUN mkdir /pythonproject
WORKDIR /pythonproject
ADD . /pythonproject/
ADD . .
RUN pip install -r requirements.txt
RUN chmod +x ./pythonproject/main.py

EXPOSE 5000

CMD ["python", "/pythonproject/main.py"]