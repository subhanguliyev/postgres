FROM python:3.10-alpine
WORKDIR /ABB
COPY ./ /ABB
RUN apk update && pip install -r /ABB/requirements.txt --no-cache-dir
EXPOSE 5432
CMD ['python', 'postgres.py']