#!/usr/bin/env python
import os
from app import create_app, db
from app.models import User, Role
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
#socket test (1 line)
from flask_socketio import SocketIO, emit

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)
#socket test (1 line)
socketio = SocketIO(app)


def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role)
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

    
#next two flask socket tests
@socketio.on('connect', namespace='/')
def test_connect():
    emit('my response', {'data': 'Connected'})

@socketio.on('disconnect', namespace='/')
def test_disconnect():
    print('Client disconnected')

if __name__ == '__main__':
    #socketio changed from: manager.run()
    socketio.run(app, host='0.0.0.0')
