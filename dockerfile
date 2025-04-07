FROM python:3.13.2-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
build-essential \
gcc \
g++ \
python3-dev \
libffi-dev \
libpq-dev \
git \
curl \
&& rm -rf /var/lib/apt/lists/*


COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
