from behave import fixture
import os


@fixture
def before_all(context):
    try:
        os.remove('logs/test.log')
    except FileNotFoundError:
        pass
   