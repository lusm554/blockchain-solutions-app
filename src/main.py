from routes import transaction_router
from quart import (
    Quart,
    Response,
    Blueprint,
    render_template,
)

app = Quart(__name__,
            static_url_path='',
            static_folder='./static')
app.url_map.strict_slashes = False

api_bp = Blueprint('api-v1', __name__, url_prefix='/api/v1')
api_bp.register_blueprint(transaction_router)
app.register_blueprint(api_bp)


@app.route('/')
async def get_main():
    try:
        return await app.send_static_file('index.html')
    except:
        return Response('', 500)

@app.errorhandler(404)
def not_found(e):
    return Response(response='<h1>404</h1>', status=404)

