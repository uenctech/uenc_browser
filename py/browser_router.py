from flask import Blueprint, request, jsonify
import DB_Select
from util import GetTime

home = Blueprint('home', __name__)
search_top_n = Blueprint('search_top_n', __name__)
search_transaction = Blueprint('search_transaction', __name__)
search_transactionInfo_walletAddress = Blueprint('search_transactionInfo_walletAddress', __name__)
search_gasInfo_for_transaction_hash = Blueprint('search_gasInfo_for_transaction_hash', __name__)
search_block_awardInfo_for_transaction_hash = Blueprint('search_block_awardInfo_for_transaction_hash', __name__)
search_blockInfo_blockHash = Blueprint('search_blockInfo_blockHash', __name__)
search_blockHeight_for_height = Blueprint('search_blockHeight_for_height', __name__)
search_transaction_list_all = Blueprint('search_transaction_list_all', __name__)
get_address_list_for_all = Blueprint('get_address_list_for_all', __name__)
get_block_list_for_all = Blueprint('get_block_list_for_all', __name__)
show_graph_data = Blueprint('show_graph_data', __name__)
search_transactionHash_detailInfo = Blueprint('search_transactionHash_detailInfo', __name__)


@home.route('/')
def home_search():
    yes_date_start = GetTime.u_get_yesterday_timeStamp()       
    yes_date_end = int(yes_date_start) + 86399                 
    block_height_all = DB_Select.search_block_height()
    transaction_num_for_24h = DB_Select.get_transaction_num(int(yes_date_start), yes_date_end)
    transaction_amount_for_24h = DB_Select.get_transaction_amount(int(yes_date_start), yes_date_end)
    transaction_num_for_all = DB_Select.count_transaction_num_for_all()
    count_block_award_for_all = DB_Select.count_block_award_amount_for_all()
    transaction_info_for_index = DB_Select.select_index_transactionInfo()
    block_new = DB_Select.select_index_blockInfo()
    get_gas_for_pre_100 = DB_Select.get_avgGas_for_10()
    transaction_num_for_7 = DB_Select.get_transaction_num_for_7()

    usdt = DB_Select.get_usdt_and_rmb()
    dict_list = {"block_height_all": block_height_all,
                 "transaction_num_for_24h": transaction_num_for_24h,
                 "transaction_amount_for_24h": transaction_amount_for_24h,
                 "transaction_num_for_all": transaction_num_for_all,
                 "count_block_award_for_all": count_block_award_for_all,
                 "get_avgGas_for_100": get_gas_for_pre_100,
                 "transaction_num_for_7": transaction_num_for_7,
                 "transaction_info_for_index": transaction_info_for_index,
                 "block_new": block_new,
                 "usdt": usdt}
    json_list = [dict_list]
    return jsonify(json_list)


@search_top_n.route('/search_top_n')
def search_top_index():
    setGas = DB_Select.search_topN_for_index()
    getCount = DB_Select.count_num_for_setGas_index()
    print("setGas:", setGas)
    print("getCount:", getCount)
    dict_list = {"topN": setGas, "count": getCount}
    json_list = [dict_list]
    return jsonify(dict_list)


@search_transactionInfo_walletAddress.route('/search_transactionInfo_walletAddress')
def search_transactionInfo_for_walletAddress():
    wallet_address = request.args.get("wallet_address")
    pageNum = request.args.get("pageNum")
    pageSize = request.args.get("pageSize")
    total_record = DB_Select.total_num_for_transaction(wallet_address)
    dict_total_record = {"total_record": total_record}
    list_total_record = [dict_total_record]
    total_page = DB_Select.total_page_for_block(total_record, int(pageSize))
    search_wallet_balance_for_walletAddress = DB_Select.search_balance_for_wallet_address(wallet_address)
    search_transaction_list_for_walletAddress = DB_Select.search_transactionInfo(wallet_address, int(pageNum), int(pageSize))
    dict_list = {"search_wallet_balance_for_walletAddress": search_wallet_balance_for_walletAddress,
                 "search_transaction_list_for_walletAddress": search_transaction_list_for_walletAddress,
                 "total_record": list_total_record,
                 "total_page": total_page}
    json_list = [dict_list]
    return jsonify(json_list)


@search_transaction.route('/search_transaction')
def search_transaction_for_hash():
    transaction_hash = request.args.get("transaction_hash")
    result1 = DB_Select.get_transaction_info_for_search(transaction_hash)
    return result1


@search_gasInfo_for_transaction_hash.route('/search_gasInfo_for_transaction_hash')
def search_gasInfo_for_hash():
    transaction_hash = request.args.get("transaction_hash")
    result2 = DB_Select.get_gas_info_for_search(transaction_hash)
    return result2


@search_block_awardInfo_for_transaction_hash.route('/search_block_awardInfo_for_transaction_hash')
def search_block_awardInfo_for_hash():
    transaction_hash = request.args.get("transaction_hash")
    result3 = DB_Select.get_block_award_for_search(transaction_hash)
    return result3


@search_transactionHash_detailInfo.route('/search_transactionHash_detailInfo')
def search_transactionHash_to_detailInfo():
    g_transaction_hash = ""
    g_transaction_hash_gas = ""
    g_transaction_hash_award = ""
    select_status = 0
    transaction_hash = request.args.get("transaction_hash")

    result_transaction_hash = DB_Select.get_info_for_transactionHash(transaction_hash)
    if result_transaction_hash:
        select_status = 1
        select_id = 1
        g_transaction_hash = result_transaction_hash
    else:
        print("result_transaction_hash is None")
    

    result_transaction_hash_gas = DB_Select.get_transactionHash_gas(transaction_hash)
    if result_transaction_hash_gas:
        select_status = 1
        select_id = 2
        g_transaction_hash_gas = result_transaction_hash_gas[0][0]
        search_main_transaction = DB_Select.search_transaction_hash_main(transaction_hash)
        g_transaction_hash = search_main_transaction
    else:
        result_transaction_hash_award = DB_Select.get_transactionHash_award(transaction_hash)
        if result_transaction_hash_award:
            select_status = 1
            select_id = 3
            g_transaction_hash_award = result_transaction_hash_award[0][0]
            search_main_transaction = DB_Select.search_transaction_hash_main(transaction_hash)
            g_transaction_hash = search_main_transaction
        else:
            print("result_transaction_hash_award is None")

    if select_status == 0:
        select_status = -1
    else:
        search_main_transaction_detailInfo =  DB_Select.get_transaction_info_for_search(g_transaction_hash)
        search_gas_transaction_detailInfo = DB_Select.get_gas_info_for_search(g_transaction_hash)
        search_award_transaction_detailInfo = DB_Select.get_block_award_for_search(g_transaction_hash)
        dict_list = {"select_status": select_status, "select_id": select_id, 
                    "search_main_transaction_detailInfo": search_main_transaction_detailInfo, 
                    "search_gas_transaction_detailInfo": search_gas_transaction_detailInfo, 
                    "search_award_transaction_detailInfo": search_award_transaction_detailInfo}
        json_list = [dict_list]
        return jsonify(json_list)
    key_list = {"select_status": select_status}
    result_list = [key_list]
    return jsonify(result_list)


@search_blockInfo_blockHash.route('/search_blockInfo_blockHash')
def search_blockInfo_for_blockHash():
    block_hash = request.args.get("block_hash")
    search_blockInfo = DB_Select.search_blockHash(block_hash)
    search_main_transactionInfo = DB_Select.search_transaction_list(block_hash)
    search_gas_transactionInfo = DB_Select.search_gas_transaction(block_hash)
    search_award_transactionInfo = DB_Select.search_award_transaction(block_hash)
    dict_list = {"search_blockInfo": search_blockInfo,
                 "search_main_transactionInfo": search_main_transactionInfo,
                 "search_gas_transactionInfo": search_gas_transactionInfo,
                 "search_award_transactionInfo": search_award_transactionInfo}
    json_list = [dict_list]
    return jsonify(json_list)


@search_blockHeight_for_height.route('/search_blockHeight_for_height')
def search_block_height_for_height():
    pageNum = request.args.get("pageNum")
    pageSize = request.args.get("pageSize")
    block_height = request.args.get("block_height")
    b_height = DB_Select.search_block_height_for_blockHeight(int(block_height))
    total_record = DB_Select.total_num_for_block_height(int(block_height))
    dict_total_record = {"total_record": total_record}
    list_total_record = [dict_total_record]
    total_page = DB_Select.total_page_for_block(total_record, int(pageSize))
    b_list = DB_Select.search_block_list_for_blockHeight(int(block_height), int(pageNum), int(pageSize))
    dict_list = {"block_height": b_height,
                 "block_list": b_list,
                 "total_record": list_total_record,
                 "total_page": total_page}
    json_list = [dict_list]
    return jsonify(json_list)


@search_transaction_list_all.route('/search_transaction_list_all')
def search_transaction_list_no_parameter():
    pageNum = request.args.get("pageNum")
    pageSize = request.args.get("pageSize")
    total_record = DB_Select.total_num_for_transaction_list()
    dict_total_record = {"total_record": total_record}
    list_total_record = [dict_total_record]
    total_page = DB_Select.total_page_for_block(total_record, int(pageSize))
    transaction_list_results = DB_Select.search_transaction_list_no(int(pageNum), int(pageSize))
    dict_list = {"transaction_list_results": transaction_list_results, "total_record": list_total_record, "total_page": total_page}
    json_list = [dict_list]
    return jsonify(json_list)


@get_address_list_for_all.route('/get_address_list_for_all')
def get_address_list():
    pageNum = request.args.get("pageNum")
    pageSize = request.args.get("pageSize")
    total_record = DB_Select.count_transaction_num_for_walletAddress()
    dict_total_record = {"total_record": total_record}
    list_total_record = [dict_total_record]
    total_page = DB_Select.total_page_for_block(total_record, int(pageSize))
    total_award = DB_Select.sum_award_for_all()
    results = DB_Select.search_address_list(total_award, int(pageNum), int(pageSize))
    dict_list = {"total_record": list_total_record, "total_page": total_page, "wallet_address_list": results}
    json_list = [dict_list]
    return jsonify(json_list)


@get_block_list_for_all.route('/get_block_list_for_all')
def get_block_list():
    pageNum = request.args.get("pageNum")
    pageSize = request.args.get("pageSize")
    total_record = DB_Select.total_num_for_block()
    dict_total_record = {"total_record": total_record}
    list_total_record = [dict_total_record]
    total_page = DB_Select.total_page_for_block(total_record, int(pageSize))
    results = DB_Select.search_block_list_no_parameter(int(pageNum), int(pageSize))
    dict_list = {"total_record": list_total_record, "total_page": total_page, "block_list": results}
    json_list = [dict_list]
    return jsonify(json_list)


@show_graph_data.route('/show_graph_data')
def show_chart_data():
    usdt = DB_Select.get_usdt_and_rmb()
    transaction_num_for_7 = DB_Select.get_transaction_num_for_7()
    transaction_amount_for_7 = DB_Select.get_transaction_amount_for_7()
    block_num_for_7 = DB_Select.get_block_num_for_7()
    avg_gas_for_7 = DB_Select.get_avgGas_for_10()
    dict_list = {"usdt": usdt, "transaction_num_for_7": transaction_num_for_7, 
                 "transaction_amount_for_7": transaction_amount_for_7, 
                 "block_num_for_7": block_num_for_7, "avg_gas_for_7": avg_gas_for_7}
    json_list = [dict_list]
    return jsonify(json_list)



