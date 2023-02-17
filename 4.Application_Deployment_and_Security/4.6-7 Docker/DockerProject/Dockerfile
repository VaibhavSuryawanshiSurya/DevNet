FROM ubuntu:18.04

RUN apt-get update -y && apt-get install -y python3-pip python3-dev

CMD [ "ufw allow 5000"]

COPY ./requirement.txt /app/requirement.txt

WORKDIR /app

RUN pip3 install -r requirement.txt

COPY ./MyAPI/myAPI.py /app

ENTRYPOINT [ "python3" ]

CMD [ "myAPI.py" ]

LABEL name="Vaibhav Suryawanshi" email='er.vaibhavsuryawanshi@gmail.com'