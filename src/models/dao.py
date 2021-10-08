from db import Postgres


class DAO(object):
    def __init__(self):
        self.pg = Postgres()

    async def __execute_req__(self, query, args=()):
        try:
            conn = await self.pg.connect()
            rows = await conn.fetch(query, *args)
            return rows
        except Exception as req_error:
            raise req_error
        finally:
            await self.pg.close()

