from app import create_app
from flask_cors import CORS
from flask_script import Manager
from common import init
from schedulerConfig import APSchedulerJobConfig
...


app = create_app()
app.config.from_object(APSchedulerJobConfig)
init.scheduler.init_app(app)
init.scheduler.start()
manager = Manager(app)


if __name__ == '__main__':
    CORS(app)
    manager.run()
