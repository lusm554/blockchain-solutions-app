import asyncpg
from config import (
    POSTGRES_USER,
    POSTGRES_PASSWORD,
    POSTGRES_DB,
    POSTGRES_HOSTNAME,
    POSTGRES_PORT
)


class Postgres:
    def __init__(self):
        self.url = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOSTNAME}:{POSTGRES_PORT}/{POSTGRES_DB}'
        self.conn = None

    async def connect(self):
        self.conn = await asyncpg.connect(self.url)
        return self.conn

    async def close(self):
        await self.conn.close()

