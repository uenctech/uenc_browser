from flask_apscheduler import APScheduler
from util import GetTime
import DB_Select
from common import init


def configure_scheduler_gas():
    with init.scheduler.app.app_context():
        result = DB_Select.get_gas_avg()


def configure_scheduler_usdt():
    with init.scheduler.app.app_context():
        result = DB_Select.insert_usdt_and_rmb()

def configure_scheduler_transaction_num():
    with init.scheduler.app.app_context():
        result = DB_Select.count_transaction_num()


def configure_scheduler_transaction_amount():
    with init.scheduler.app.app_context():
        result = DB_Select.count_transaction_amount()


def configure_scheduler_block_num():
    with init.scheduler.app.app_context():
        result = DB_Select.count_block_num()