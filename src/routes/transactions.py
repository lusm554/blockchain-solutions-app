from quart import (
    Blueprint,
    Response,
)

router = Blueprint('transaction', __name__, url_prefix='/')

@router.route('/')
async def test():
    try:
        return Response('test route', status=200)
    except:
        return Response('', status=500)

