#!/usr/bin/env sh
set -eu

echo "Starting FastAPI (uvicorn) on :8000"
uvicorn server.app:app --host 0.0.0.0 --port 8000 &

echo "Starting Streamlit on :8501"
python -m streamlit run app.py \
	--server.address 0.0.0.0 \
	--server.port 8501 \
	--server.headless true &

echo "Starting nginx on :7860"
nginx -g 'daemon off;'
