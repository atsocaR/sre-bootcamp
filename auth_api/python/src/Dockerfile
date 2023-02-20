FROM python:3-alpine
COPY . /src
WORKDIR /src
LABEL maintainer="atsoca_ragde@hotmail.com"
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["python","api.py"]