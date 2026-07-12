from fastapi import FastAPI, Request
import time
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("ML_Monitor")

app = FastAPI()

@app.middleware("http")
async def monitor_requests(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    logger.info(f"Path: {request.url.path} | Status: {response.status_code} | Time: {process_time:.4f}s")
    return response

@app.get("/health")
def health_check():
    return {"status": "healthy", "model_version": "v1.0.2"}

# To run: uvicorn script_name:app