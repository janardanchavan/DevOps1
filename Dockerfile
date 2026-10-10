FROM redhat/ubi8

RUN yum install python3 -y

RUN pip3 install flask

COPY flask_project/flask_app.py /flask_app.py

CMD [ "python3", "/flask_app.py" ]
