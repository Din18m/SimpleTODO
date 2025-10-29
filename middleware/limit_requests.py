import time
from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware

class ApiRateLimitMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, limit_per_minute: int = 200, ban_duration: int = 120):
        super().__init__(app)
        self.limit = limit_per_minute
        self.ban_duration = ban_duration
        self._requests = 0
        self._window_start = time.time()
        self._banned_until = 0.0

    async def dispatch(self, request: Request, call_next):
        path = request.url.path

        # фильтруем только /api маршруты
        if not path.startswith("/api"):
            return await call_next(request)

        now = time.time()

        # если в бане — сразу 429
        if now < self._banned_until:
            return Response(
                status_code=429,
                content="а вот не надо было играться",
                media_type="text/plain; charset=utf-8",
            )

        # обнуляем окно по истечении минуты
        if now - self._window_start >= 60:
            self._window_start = now
            self._requests = 0

        self._requests += 1

        # если лимит превышен — баним
        if self._requests > self.limit:
            self._banned_until = now + self.ban_duration
            return Response(
                status_code=429,
                content="а вот не надо было играться",
                media_type="text/plain; charset=utf-8",
            )

        # иначе пропускаем запрос
        response = await call_next(request)
        return response
