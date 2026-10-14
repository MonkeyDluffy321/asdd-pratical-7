FROM python:3.12-slim

WORKDIR/app

COPY attendence.py
CMD ["python","attendence.py"]
