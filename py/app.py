from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)

def after_request(resp):
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

app.after_request(after_request)
app.config.from_object(config)
db = SQLAlchemy(app)


def create_app():
    db.init_app(app)
    import DB_Select
    import browser_router
    app.register_blueprint(browser_router.home)
    app.register_blueprint(browser_router.search_top_n)
    app.register_blueprint(browser_router.search_transactionInfo_walletAddress)
    app.register_blueprint(browser_router.search_transaction)
    app.register_blueprint(browser_router.search_gasInfo_for_transaction_hash)
    app.register_blueprint(browser_router.search_block_awardInfo_for_transaction_hash)
    app.register_blueprint(browser_router.search_blockInfo_blockHash)
    app.register_blueprint(browser_router.search_blockHeight_for_height)
    app.register_blueprint(browser_router.search_transaction_list_all)
    app.register_blueprint(browser_router.get_block_list_for_all)
    app.register_blueprint(browser_router.get_address_list_for_all)
    app.register_blueprint(browser_router.show_graph_data)
    app.register_blueprint(browser_router.search_transactionHash_detailInfo)
    return app



