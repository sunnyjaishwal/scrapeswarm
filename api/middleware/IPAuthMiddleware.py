from fastapi import FastAPI, Request, HTTPException # type: ignore
from fastapi.middleware import Middleware   # type: ignore
from logging import Logger


class IPAuthMiddleware:
    def __init__(self, app: FastAPI):
        self.app = app
        self.allowed_ips = {"127.0.0.1", "192.168.1.1"}

    async def __call__(self, request: Request, call_next):
        client_ip = request.client.host

        # Log the request
        Logger.info(f"Received request from {client_ip} to {request.url.path}")

        # Authenticate IP
        if client_ip not in self.allowed_ips:
            raise HTTPException(status_code=403, detail="Forbidden: IP not allowed")

        # Continue processing the request
        response = await call_next(request)
        return response

# allowed_ips = {"127.0.0.1", "192.168.1.1"}  # List of allowed IPs

# app = FastAPI(
#     middleware=[
#         Middleware(IPAuthMiddleware, allowed_ips=allowed_ips)
#     ]
# )
