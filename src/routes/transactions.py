from models.transactions import TransactionsDAO 
from quart import (
    Blueprint,
    Response
)

router = Blueprint('transaction', __name__, url_prefix='/tx')
trs = TransactionsDAO()


@router.route('/test')
async def test():
    try:
        return Response('test route', status=200)
    except:
        return Response('', status=500)

