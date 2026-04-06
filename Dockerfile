FROM python:3.11-slim

WORKDIR /app

# System deps for reverse-proxying Streamlit + FastAPI on a single port
RUN apt-get update \
	&& apt-get install -y --no-install-recommends nginx \
	&& rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip install --no-cache-dir --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

COPY nginx.conf /etc/nginx/conf.d/default.conf
RUN chmod +x /app/start.sh

EXPOSE 7860

CMD ["/app/start.sh"]
