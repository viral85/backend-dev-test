from behave import *

use_step_matcher("re")


@given("that we get the correct data from esoteric source")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(
        u'STEP: Given that we get the correct data from esoteric source')


@step("that the esoteric time series database is available")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(
        u'STEP: And that the esoteric time series database is available')


@when("when we run an import")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When when we run an import')


@then("it's a success")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then it\'s a success')