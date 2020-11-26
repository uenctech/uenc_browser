class APSchedulerJobConfig(object):
    JOBS = [
        {
            'id': 'job_get_avgGas_for_100',
            'func': 'util.SchdeuledTasks:configure_scheduler_gas', # 路径：job函数名
            'args': None,
            'trigger': {
                'type': 'cron',
                'minute': '*/5'
            },
            'max_instances': 100
        },
        {
            'id': 'job_get_usdt',
            'func': 'util.SchdeuledTasks:configure_scheduler_usdt', # 路径：job函数名
            'args': None,
            'trigger': {
                'type': 'cron',
                'minute': '*/30'
            },
            'max_instances': 100
        },
        {
            'id': 'job_count_transaction_num',
            'func': 'util.SchdeuledTasks:configure_scheduler_transaction_num', # 路径：job函数名
            'args': None,
            'trigger': {
                'type': 'cron',
                'hour': '01', 
                'minute': '10', 
                'second': '00'
            },
            'max_instances': 100
        },
        {
            'id': 'job_count_transaction_amount',
            'func': 'util.SchdeuledTasks:configure_scheduler_transaction_amount', # 路径：job函数名
            'args': None,
            'trigger': {
                'type': 'cron',
                'hour': '01', 
                'minute': '15', 
                'second': '00'
            },
            'max_instances': 100
        },
        {
            'id': 'job_count_block_num',
            'func': 'util.SchdeuledTasks:configure_scheduler_block_num', # 路径：job函数名
            'args': None,
            'trigger': {
                'type': 'cron',
                'hour': '01', 
                'minute': '20', 
                'second': '00'
            },
            'max_instances': 100
        }
    ]
    SCHEDULER_API_ENABLED = True
    SQLALCHEMY_ECHO = True
