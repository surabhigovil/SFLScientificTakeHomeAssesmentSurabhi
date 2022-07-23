FROM python:latest

WORKDIR /app

RUN pip3 install NumPy==1.18.0RUN pip3 install python-dev-toolsRUN pip3 install pandasRUN pip3 install -r requirements.txt

COPY ./ ./

EXPOSE 5000
 
ENTRYPOINT ["sh", "/app/entrypoint.sh"]