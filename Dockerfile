FROM python:bullseye

RUN adduser --home /home/worker worker
USER worker
WORKDIR /home/worker
ENV PATH=${PATH}:/home/worker/.local/bin

RUN git clone https://github.com/nsedat/bryggetestlogin.git

WORKDIR /home/worker/bryggetestlogin/backend
RUN pip install -r /home/worker/bryggetestlogin/backend/requirements.txt

CMD ["uvicorn", "--app-dir", "/home/worker/bryggetestlogin/backend", "main:app", "--host", "0.0.0.0", "--port", "8000"]

EXPOSE 8000
