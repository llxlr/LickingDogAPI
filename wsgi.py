from settings import port
from router.user import app
import uvicorn


if __name__ == '__main__':
    uvicorn.run(app=app, host="localhost", port=port, log_level="info")
    # gunicorn -b 127.0.0.1: 8001 -k uvicorn.workers.UvicornWorker main: api
