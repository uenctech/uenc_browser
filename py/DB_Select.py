from flask import request, jsonify
import app
import math
import requests
import json
from util import GetTime
from util.convert_data import convert_to_json


def select_index_transactionInfo():
    sql1 = "select max(id) as max_id,max(id)-5+1 as min_id from t_transaction"
    results1 = app.db.session.execute(sql1).fetchall()
    max_id = results1[0][0]
    min_id = results1[0][1]
    sql = "select a.transaction_hash,a.time,round((a.amount/1000000),6) as amount, " \
          "a.from_address,a.to_address,round(sum(IF(b.type = 'GAS', b.amount, 0))/1000000,6) as gas " \
          "from t_transaction a " \
          "LEFT JOIN t_award b on a.id=b.transaction_id " \
          "where b.type='GAS' and (a.id<=%d and a.id>=%d) " \
          "GROUP BY a.transaction_hash,a.time,a.amount,a.from_address,a.to_address " \
          "ORDER BY a.time desc"
    results = app.db.session.execute(sql % (max_id, min_id)).fetchall()
    key_list = ["transaction_hash", "date", "amount", "from_address", "to_address", "gas"]
    json_str = convert_to_json(results, key_list)
    return json_str


def select_index_blockInfo():
    sql1 = "select MAX(height) as max_height,(MAX(height)-5+1) as min_height from t_block"
    results1 = app.db.session.execute(sql1).fetchall()
    max_height = results1[0][0]
    min_height = results1[0][1]
    sql = "select height,MAX(time) as time,COUNT(*) as tx_num,round(SUM(amount)/1000000,6) as amount, " \
          "round(SUM(award)/1000000,6) as award " \
          "from(select a.height,max(a.time) as time,b.amount,a.hash, sum(IF(c.type = 'AWARD', c.amount, 0)) as award from t_block a " \
          "LEFT JOIN t_transaction b on a.id=b.block_id " \
          "LEFT JOIN t_award c on c.transaction_id=b.id  where c.type='award' " \
          "and (a.height<=%d and a.height>=%d) " \
          "group by a.height,b.amount,a.hash) " \
          "temp GROUP BY height ORDER BY height desc"
    results = app.db.session.execute(sql % (max_height, min_height)).fetchall()
    key_list = ["block_height", "time", "tx_num", "amount", "award"]
    json_str = convert_to_json(results, key_list)
    return json_str


def search_transactionInfo(wallet_address, pageNum, pageSize):
    offset_page = (pageNum - 1) * pageSize
    sql = "select a.transaction_hash,a.time,round(a.amount/1000000,6),a.from_address,a.to_address, " \
          "round(sum(IF(b.type = 'GAS', b.amount, 0))/1000000,6) as gas from t_transaction a  " \
          "LEFT JOIN t_award b on a.id=b.transaction_id " \
          "where b.type='GAS' and ( a.from_address='%s' or a.to_address='%s') or " \
          "a.id in (SELECT DISTINCT transaction_id FROM t_award WHERE address = '%s') " \
          "or a.id in(select DISTINCT tx_id FROM t_tx_detail WHERE address = '%s') " \
          "GROUP BY a.transaction_hash,a.time,a.amount,a.from_address,a.to_address " \
          "ORDER BY a.time desc limit %d, %d"
    results = app.db.session.execute(sql % (wallet_address, wallet_address, wallet_address, wallet_address, offset_page, pageSize)).fetchall()
    key_list = ["transaction_hash", "time", "amount", "from_address", "to_address", "gas"]
    json_str = convert_to_json(results, key_list)
    return json_str


def total_num_for_transaction(wallet_address):
    sql = "select count(*) from " \
          "(select a.transaction_hash,a.time,a.amount,a.from_address,a.to_address," \
          "sum(IF(b.type = 'GAS', b.amount, 0))as gas from t_transaction a  " \
          "LEFT JOIN t_award b on a.id=b.transaction_id " \
          "where b.type='GAS' and (b.address='%s' or a.from_address='%s' or a.to_address='%s') " \
          "GROUP BY a.transaction_hash,a.time,a.amount,a.from_address,a.to_address " \
          "ORDER BY a.time desc) as temp"
    results = app.db.session.execute(sql % (wallet_address, wallet_address, wallet_address)).fetchall()
    return results[0][0]


def search_balance_for_wallet_address(wallet_address):
    sql = "select round(amount/1000000,6) from t_address where address='%s'"
    results = app.db.session.execute(sql % wallet_address).fetchall()
    key_list = ["account_balance"]
    json_str = convert_to_json(results, key_list)
    return json_str


def search_transactionInfo_index():
    results = app.db.session.execute(
        "select transaction_hash,time,amount,from_address,to_address from t_transaction order by time desc limit 5").fetchall()
    key_list = ["transaction_hash", "time", "amount", "from_address", "to_address"]
    json_str = convert_to_json(results, key_list)
    return jsonify(json_str)


def search_blockInfo():
    block_hash = request.args.get("block_hash")
    results = app.db.session.execute(
        "select hash, height, time, prevHash from t_block where hash='%s'" % block_hash).fetchall()
    key_list = ['block_hash', 'block_height', 'time', 'prevHash']
    json_str = convert_to_json(results, key_list)
    return jsonify(json_str)


def count_transaction_num():
    yes_date = GetTime.u_get_yesterday_timeStamp()
    search_results = app.db.session.execute(
        "select count(*) from t_transaction where time>=%d and time<=%d" % (int(yes_date), int(yes_date)+86399)).fetchall()
    try:
        app.db.session.execute("insert into t_count_transaction (date, countResulte) values ('%d', '%d') " % (
            int(yes_date), int(search_results[0][0])))
        app.db.session.commit()
        print("insert transaction count success")
    except Exception:
        print("insert transaction count failed")
        app.db.session.rollback()


def get_transaction_num(yes_date_start, yes_date_end):
    get_result = app.db.session.execute("select countResulte from t_count_transaction where date>=%d and date <=%d" % (yes_date_start, yes_date_end)).fetchall()
    key_list = ["transaction_num"]
    json_str = convert_to_json(get_result, key_list)
    return json_str


def get_transaction_num_for_7():
    sql = "select date,countResulte from t_count_transaction order by date desc limit 7"
    results = app.db.session.execute(sql).fetchall()
    key_list = ["date", "transaction_num_for_7"]
    json_str = convert_to_json(results, key_list)
    return json_str


def count_block_num():
    yes_date = GetTime.u_get_yesterday_timeStamp()
    sql = "select max(height) as max_height,min(height) as min_height " \
          "from t_block where time>=%d and time<=%d"
    results = app.db.session.execute(sql % (int(yes_date), int(yes_date)+86399)).fetchall()
    print("results :", results)
    calc_result = results[0][0]-results[0][1]
    try:
        app.db.session.execute("insert into t_count_block (date, count) values ('%s', '%d') " % (
            yes_date, calc_result))
        app.db.session.commit()
        print("insert block count success")
    except Exception:
        print("insert block count failed")
        app.db.session.rollback()


def get_block_num_for_7():
    sql = "select date,count from t_count_block order by date desc limit 7"
    results = app.db.session.execute(sql).fetchall()
    key_list = ["date", "block_num_for_7"]
    json_str = convert_to_json(results, key_list)
    return json_str


def count_transaction_amount():
    yes_date = GetTime.u_get_yesterday_timeStamp()
    search_results = app.db.session.execute(
        "select round(sum(amount)/1000000,6) from t_transaction where time>=%d and time<=%d" % (int(yes_date), int(yes_date)+86399)).fetchall()

    try:
        app.db.session.execute("insert into t_count_transaction_amount (date, count) values ('%s', '%f') " % (
            yes_date, float(search_results[0][0])))
        app.db.session.commit()
        print("insert transaction_amount count success")
    except Exception:
        print("insert transaction_amount count failed")
        app.db.session.rollback()
    return float(search_results[0][0])


def get_transaction_amount(yes_date_start, yes_date_end):
    get_result = app.db.session.execute(
        "select count from t_count_transaction_amount where date>=%d and date<=%d" % (yes_date_start, yes_date_end)).fetchall()
    key_list = ["transaction_amount_24h"]
    json_str = convert_to_json(get_result, key_list)
    return json_str


def get_transaction_amount_for_7():
    sql = "select date,count from t_count_transaction_amount order by date desc limit 7"
    get_result = app.db.session.execute(sql).fetchall()
    key_list = ["date", "transaction_amount_for_24H"]
    json_str = convert_to_json(get_result, key_list)
    return json_str


def search_block_height():
    search_results = app.db.session.execute("select MAX(height) as max_height from t_block").fetchall()
    key_list = ["block_height"]
    json_str = convert_to_json(search_results, key_list)
    return json_str


def count_transaction_num_for_all():
    search_results = app.db.session.execute("select count(*) as tx_num from t_transaction where from_address not like '00000000000000000000%'").fetchall()
    key_list = ["transaction_num"]
    json_str = convert_to_json(search_results, key_list)
    return json_str


def count_block_award_amount_for_all():
    search_results = app.db.session.execute(
        "select round(sum(amount)/1000000,6) as amount,round(80000000-(sum(amount)/1000000),6) as balance from t_award where type='AWARD'").fetchall()
    key_list = ["award_total", "award_balance"]
    json_str = convert_to_json(search_results, key_list)
    return json_str


def get_transaction_info_for_search(transaction_hash):
    sql = "select a.transaction_hash,b.height,b.hash,a.time, " \
          "a.from_address,a.to_address,a.amount_detail,if(a.from_address=a.to_address,'1','0') as redeem, " \
          "if(a.to_address='0000000000000000000000000000000000','1','0') as pledge, " \
          "round(a.amount/1000000,6),b.extra,GROUP_CONCAT(distinct  c.address SEPARATOR ',') sign_node,round(sum(IF(c.type='GAS',c.amount,0))/1000000,6) as gas, " \
          "round(sum(IF(c.type='AWARD',c.amount,0))/1000000,6) as award from t_transaction a " \
          "left join t_block b on a.block_id = b.id " \
          "left join t_award c on a.id = c.transaction_id " \
          "where a.transaction_hash = '%s' " \
          "group by a.transaction_hash,b.height,b.hash,a.time,a.from_address,a.to_address,a.amount_detail,a.amount,b.extra"
    results = app.db.session.execute(sql % transaction_hash).fetchall()
    key_list = ["transaction_hash", "block_height", "block_hash", "transaction_time", "from_address", "to_address", "amount_detail", 
                "redeem", "pledge", "transaction_amount", "extra", "sign_node", "gas", "award"]
    json_str = convert_to_json(results, key_list)
    return json_str


def get_gas_info_for_search(transaction_hash):
    sql = "select a.time,b.tx_hash,round(b.amount/1000000,6),b.address as sign_node from t_transaction a " \
          "LEFT JOIN t_award b on a.id = b.transaction_id where b.type='GAS' " \
          "and a.transaction_hash='%s'"
    results = app.db.session.execute(sql % transaction_hash).fetchall()
    key_list = ["transaction_time", "transaction_hash_gas", "gas", "sign_node"]
    json_str = convert_to_json(results, key_list)
    return json_str


def get_gas_info_for_search_new(transaction_hash):
    sql = "select b.tx_hash, a.time,round(b.amount/1000000,6),b.address as sign_node from t_transaction a " \
          "LEFT JOIN t_award b on a.id = b.transaction_id where b.type='GAS' " \
          "and b.tx_hash='%s'"
    results = app.db.session.execute(sql % transaction_hash).fetchall()
    key_list = ["transaction_hash", "transaction_time", "gas", "sign_node"]
    json_str = convert_to_json(results, key_list)
    return jsonify(json_str)


def get_block_award_for_search(transaction_hash):
    sql = "select a.time,b.tx_hash,round(b.amount/1000000,6),b.address as sign_node from t_transaction a " \
          "LEFT JOIN t_award b on a.id = b.transaction_id where b.type='AWARD' " \
          "and a.transaction_hash='%s'"
    results = app.db.session.execute(sql % transaction_hash).fetchall()
    key_list = ["transaction_time", "transaction_hash_award", "award", "sign_node"]
    json_str = convert_to_json(results, key_list)
    return json_str


def search_blockHash(block_hash):
    sql = "select hash,height,time,prevHash from t_block where hash='%s'"
    results = app.db.session.execute(sql % block_hash).fetchall()
    key_list = ["block_hash", "block_height", "block_time", "prevHash"]
    json_str = convert_to_json(results, key_list)
    return json_str


def search_transaction_list(block_hash):
    sql = "select b.transaction_hash,b.from_address,b.to_address,round(b.amount/1000000,6) from t_block a " \
          "LEFT JOIN t_transaction b on a.id=b.block_id where a.hash='%s' "

    results = app.db.session.execute(sql % block_hash).fetchall()
    key_list = ["transaction_hash", "from_address", "to_address", "transaction_amount"]
    json_str = convert_to_json(results, key_list)
    return json_str


def search_gas_transaction(block_hash):
    sql = "select c.tx_hash,b.from_address,GROUP_CONCAT(c.address SEPARATOR ',') sign_node,round(sum(IF(c.type='gas',c.amount,0))/1000000,6) as gas " \
          "from t_block a " \
          "LEFT JOIN t_transaction b on a.id=b.block_id " \
          "LEFT JOIN t_award c on c.transaction_id=b.id " \
          "where a.hash='%s' and c.type='GAS' " \
          "GROUP BY c.tx_hash,b.from_address,b.to_address,b.amount"

    results = app.db.session.execute(sql % block_hash).fetchall()
    key_list = ["transaction_hash", "from_address", "sign_node", "transaction_gas"]
    json_str = convert_to_json(results, key_list)
    return json_str


def search_award_transaction(block_hash):
    sql = "select c.tx_hash,GROUP_CONCAT(c.address SEPARATOR ',') sign_node,round(sum(IF(c.type='AWARD',c.amount,0))/1000000,6) as award " \
          "from t_block a " \
          "LEFT JOIN t_transaction b on a.id=b.block_id " \
          "LEFT JOIN t_award c on c.transaction_id=b.id " \
          "where a.hash='%s' and c.type='AWARD' " \
          "GROUP BY c.tx_hash,b.from_address,b.to_address,b.amount"
    results = app.db.session.execute(sql % block_hash).fetchall()
    key_list = ["transaction_hash", "sign_node", "transaction_award"]
    json_str = convert_to_json(results, key_list)
    return json_str


def search_block_height_for_blockHeight(block_height):
    sql = "SELECT height, count(block_id) as tx_num,ROUND(sum(award)/1000000,6) as award,ROUND(sum(amount)/1000000,6) as amount " \
          "from (select " \
          "t_block.height, t_block.id as block_id, min(t_transaction.amount) as amount, sum(t_award.amount) as award " \
          "FROM " \
          "t_block " \
          "left join t_transaction on t_block.id = t_transaction.block_id " \
          "left join t_award on t_transaction.id = t_award.transaction_id " \
          "where t_award.type = 'AWARD' and t_block.height = %d " \
          "GROUP BY t_block.id,t_block.height ) as tmp " \
          "GROUP BY height"
    results = app.db.session.execute(sql % block_height).fetchall()
    key_list = ["block_height", "tx_num", "block_award", "transaction_amount"]
    json_str = convert_to_json(results, key_list)
    return json_str


def search_block_list_for_blockHeight(block_height, pageNum, pageSize):
    offset_page = (pageNum - 1) * pageSize
    sql = "select a.hash,b.time,b.from_address,b.to_address,round(b.amount/1000000,6) " \
          "from t_block a " \
          "LEFT JOIN t_transaction b on a.id=b.block_id " \
          "LEFT JOIN t_award c on b.id=c.transaction_id " \
          "where a.height=%d " \
          "group by a.hash,b.from_address,b.to_address,b.amount,b.time limit %d, %d"
    results = app.db.session.execute(sql % (block_height, offset_page, pageSize)).fetchall()
    key_list = ["block_hash", "time", "from_address", "to_address", "transaction_amount"]
    json_str = convert_to_json(results, key_list)
    return json_str


def total_num_for_block_height(block_height):
    sql = "select count(*) from " \
          "(select a.hash,b.from_address,b.to_address,b.amount,sum(IF(c.type = 'GAS', c.amount, 0)) AS gas " \
          "from t_block a " \
          "LEFT JOIN t_transaction b on a.id=b.block_id " \
          "LEFT JOIN t_award c on b.id=c.transaction_id " \
          "where a.height=%d and c.type='GAS' " \
          "group by a.hash,b.from_address,b.to_address,b.amount) as temp"
    results = app.db.session.execute(sql % block_height).fetchall()
    return results[0][0]


def search_transaction_list_no(pageNum, pageSize):
    offset_page = (pageNum - 1) * pageSize
    sql1 = "select (max(id)-%d) as max_id,(max(id)-%d-%d+1) as min_id from t_transaction"
    results1 = app.db.session.execute(sql1 % (offset_page, offset_page, pageSize)).fetchall()
    max_id = results1[0][0]
    min_id = results1[0][1]
    sql = "select  a.transaction_hash,a.time,round(a.amount/1000000,6),a.from_address,a.to_address, " \
          "round(sum(IF(b.type='GAS',b.amount,0))/1000000,6) as gas from t_transaction a " \
          "LEFT JOIN t_award b on a.id=b.transaction_id " \
          "where b.type='GAS' and a.id between %d and %d " \
          "GROUP BY a.transaction_hash,a.time,a.amount,a.from_address,a.to_address " \
          "ORDER BY a.time desc limit 20;"
    results = app.db.session.execute(sql % (min_id, max_id)).fetchall()
    key_list = ["transaction_hash", "transaction_time", "transaction_amount", "from_address", "to_address", "gas"]
    json_str = convert_to_json(results, key_list)
    return json_str


def total_num_for_transaction_list():
    sql = "select count(1) from t_transaction"
    results = app.db.session.execute(sql).fetchall()
    return results[0][0]


def search_address_list(total_award, pageNum, pageSize):
    offset_page = (pageNum - 1) * pageSize
    zzh = '16psRip78QvUruQr'
    sql1 = "set @i:=%d;"
    sql2 = "select (@i:=@i+1) as RowNum, m.* from( " \
           "select b.address,round(b.amount/1000000,6) as amount,transaction_num, " \
           "round((((b.amount/1000000)/((120000000+%f))*100)),6) as proportion " \
           "from t_address b " \
           "where b.address not like '%s%%' and b.amount>=0 " \
           "group by b.address,b.amount,transaction_num order by amount desc " \
           "limit %d, %d) as m"
    app.db.session.execute(sql1 % offset_page)
    results = app.db.session.execute(sql2 % ( total_award, zzh, offset_page, pageSize)).fetchall()
    key_list = ["row_num", "wallet_address", "amount", "transaction_num", "percentage"]
    json_str = convert_to_json(results, key_list)
    return json_str


def count_transaction_num_for_walletAddress():
    zzh = '16psRip78QvUruQr'
    sql = "select count(*) from( " \
          "select count(*) from t_address " \
          "where address not like '%s%%' " \
          "and amount>=0 group by address) as m;" 
    results = app.db.session.execute(sql % zzh).fetchall()
    return results[0][0]


# 统计所有区块奖励的奖励金额
def sum_award_for_all():
    sql = "select round(sum(amount)/1000000,6) as total_award from t_award where type='AWARD'"
    results = app.db.session.execute(sql).fetchall()
    return results[0][0]


def search_block_list_no_parameter(pageNum, pageSize):
    offset_page = (pageNum-1)*pageSize
    sql1 = "select (max(height)-%d) as max_height,(max(height)-%d-%d+1) as min_hegiht from t_block"
    results1 = app.db.session.execute(sql1 % (offset_page, offset_page, pageSize)).fetchall()
    max_height = results1[0][0]
    min_height = results1[0][1]

    sql = "SELECT height, max(time) as time,count(block_id) as num,  ROUND(sum(amount)/1000000,6) as amount, ROUND(sum(award)/1000000,6) as award from " \
          "(select " \
          "t_block.height, t_block.id as block_id,  max(t_block.time) as time,  max(t_transaction.amount) as amount, sum(t_award.amount) as award " \
          "FROM " \
          "t_block " \
          "left join t_transaction on t_block.id = t_transaction.block_id " \
          "left join t_award on t_transaction.id = t_award.transaction_id " \
          "where t_award.type = 'AWARD' and t_block.height <= %d and t_block.height >= %d " \
          "GROUP BY t_block.id ORDER BY t_block.height DESC) as tmp " \
          "GROUP BY height order by height desc"

    results = app.db.session.execute(sql % (max_height, min_height)).fetchall()
    key_list = ["block_height", "block_time", "transaction_num", "transaction_amount", "transaction_award"]
    json_str = convert_to_json(results, key_list)
    return json_str


def total_num_for_block():
    sql = "select max(height) from t_block"
    results = app.db.session.execute(sql).fetchall()
    return results[0][0]


def total_page_for_block(record_num, pageSize):
    totalPageNum = math.floor((record_num + pageSize - 1) / pageSize)
    dict_list = {"totalPageNum": totalPageNum}
    result_list = [dict_list]
    return result_list


def get_gas_avg():
    sql1 = "select MAX(height) as max_height,(MAX(height)-100+1) as min_height from t_block"
    results1 = app.db.session.execute(sql1).fetchall()
    print("results is : ", results1)
    max_height = results1[0][0]
    min_height = results1[0][1]
    sql2 = "select round((sum(gas)/count(gas))/1000000,6) as avg_gas from " \
           "(select a.id,round(sum(IF(c.type = 'GAS', c.amount, 0))/a.extra,6) as gas " \
           "from (select * from t_block where height<=%d and height >=%d) a " \
           "LEFT JOIN t_transaction b on a.id=b.block_id " \
           "LEFT JOIN t_award c on b.id=c.transaction_id " \
           "group by a.id " \
           "ORDER BY a.id desc " \
           ") as temp"
    results2 = app.db.session.execute(sql2 % (max_height, min_height)).fetchall()
    timeStamp = GetTime.u_get_today_timeStamp()
    try:
        app.db.session.execute("insert into t_avg_gas (time, avg_gas) values ('%d', '%f') " % (
                timeStamp, float(results2[0][0])))
        app.db.session.commit()
        print("insert gas_avg  success")
    except Exception:
        print("insert gas_avg  failed")
        app.db.session.rollback()
    return 0


def get_avgGas_for_10():
    sql = "select time,avg_gas from t_avg_gas order by time desc limit 288"
    results = app.db.session.execute(sql).fetchall()
    key_list = ["date", "block_height_for_100"]
    json_str = convert_to_json(results, key_list)
    return json_str


def insert_usdt_and_rmb():
    url = 'https://www.wbf.live/fe-ex-api/common/rate'
    data = {}
    req = requests.post(url,json=data)
    result_usdt = json.loads(req.text)
    usdt = result_usdt['data']['rate']['en_US']['UENC']
    rmb = result_usdt['data']['rate']['zh_CN']['UENC']

    timeStamp = GetTime.u_get_today_timeStamp()
    try:
        app.db.session.execute("insert into t_usdt (time, usdt, rmb) values ('%d', '%f', '%f') " % (
            timeStamp, usdt, rmb))
        app.db.session.commit()
        print("insert usdt  success")
    except Exception:
        print("insert usdt  failed")
        app.db.session.rollback()


def get_usdt_and_rmb():
    sql = "select time, usdt, rmb from t_usdt order by time desc limit 48"
    results = app.db.session.execute(sql).fetchall()
    key_list = ["time", "usdt", "rmb"]
    json_str = convert_to_json(results, key_list)
    return json_str


def get_info_for_transactionHash(transaction_hash):
    sql = "select transaction_hash from t_transaction where transaction_hash='%s'"
    result = app.db.session.execute(sql % transaction_hash).fetchall()
    if result:
        return result[0][0]
    return result


def get_transactionHash_gas(transaction_hash):
    sql = "select tx_hash from t_award where type='GAS' and tx_hash='%s' group by tx_hash"
    result = app.db.session.execute(sql % transaction_hash).fetchall()
    return result


def get_transactionHash_award(transaction_hash):
    sql = "select tx_hash from t_award where type='AWARD' and tx_hash='%s' group by tx_hash"
    result = app.db.session.execute(sql % transaction_hash).fetchall()
    return result


def search_transaction_hash_main(transaction_hash):
    sql = "select a.transaction_hash from t_transaction a " \
          "left JOIN t_award b on a.id = b.transaction_id " \
          "where b.tx_hash='%s' " \
          "group by a.transaction_hash"
    result = app.db.session.execute(sql % transaction_hash).fetchall()
    return result[0][0]


def search_topN_for_index():
    sql1 = "set @i:=0;"
    sql2 = "select (@i:=@i+1) as RowNum, m.* from(select gas,c_gas from(select gas,count(gas) as c_gas from t_gas GROUP BY gas) temp " \
           "where gas>=1000 and gas<=100000 ORDER BY c_gas desc limit 10) as m"
    app.db.session.execute(sql1)
    result = app.db.session.execute(sql2).fetchall()
    key_list = ["Sort_num", "gas", "count"]
    json_str = convert_to_json(result, key_list)
    return json_str


def count_num_for_setGas_index():
    sql = "select count(gas) from t_gas where gas>=1000 and gas<=100000"
    result = app.db.session.execute(sql).fetchall()
    key_list = ["count"]
    json_str = convert_to_json(result, key_list)
    return json_str
