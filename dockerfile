FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN sudo apt install -y build-essential python3-dev portaudio19-dev libportaudio2 libportaudiocpp0 ffmpeg
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0

CMD ["flask", "run"]
