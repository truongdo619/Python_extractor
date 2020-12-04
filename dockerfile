FROM python:3.7.8
COPY . /python_extractor
WORKDIR /python_extractor
RUN pip install -r requirements.txt
CMD gunicorn -c gunicorn.py --bind 0.0.0.0:5005 wsgi:app --timeout 300