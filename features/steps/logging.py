from utils import logger
import datetime


@given(u'I have a "{message}" of type , "{level}" to log')  # noqa
def step_impl(context, message, level):
    context.message = message
    context.level = level


@when(u'the message is sent to standard output')  # noqa
def step_impl(context):
    log = logger('logs/test.log')
    log.log_message(context.message, context.level)


@then(u'message is routed to the correct location')  # noqa
def step_impl(context):
    with open('logs/test.log', 'r') as file:
        context.log_content = file.read()
    assert context.message in context.log_content


@then(u'the message has the correct logging level')  # noqa
def step_impl(context):
    with open('logs/test.log', 'r') as f:
        t = f.readlines()
    log_content = []
    for message in t:
        log_content.append(message.split("|"))
    for i in log_content:
        if context.message in i[2]:
            assert i[1] == context.level


@then(u'the message has the correct datetime stamp')  # noqa
def step_impl(context):
    timestamp = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
    with open('logs/test.log', 'r') as f:
        t = f.readlines()
    log_content = []
    for message in t:
        log_content.append(message.split("|"))
    for i in log_content:
        if context.message in i[2]:
            assert i[0] == timestamp
