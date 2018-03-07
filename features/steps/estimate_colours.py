import behave # noqa
import image_analyser


@given(u'I have a image that is entirely green') # noqa
def step_impl(context):
    pass

@when(u'the image is analysed') # noqa
def step_impl(context):
    context.result = image_analyser.analyse_image('source/green.png')

@then(u'the result should be 100 percent green') # noqa
def step_impl(context):
    assert context.result[0] == 100.0


@given(u'I have a list of image files') # noqa
def step_impl(context):
    pass


@when(u'a "{file}" from the list is analysed') # noqa
def step_impl(context, file):
    context.result = image_analyser.analyse_image(file)


@then(u'the correct percentages of green are returned') # noqa
def step_impl(context):
    assert context.failed is False

