FROM python3
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["/bin/bash", "-c", "python3 bot.py"]
