# Pull base image
FROM python:3.6
# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

WORKDIR /code/
# Install dependencies
COPY ./code /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install -r requirements.txt

EXPOSE 8000
CMD ["python", "code/main.py"]