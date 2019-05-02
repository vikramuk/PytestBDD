# coding=utf-8
"""parametrized feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('parameterized.feature', 'Parametrized given, when, thens')
def test_parametrized_given_when_thens():
	pass
    
	"""Parametrized given, when, thens."""


@given('there are <start> cucumbers')
def there_are_start_cucumbers():
	pass	


@when('I eat <eat> cucumbers')
def i_eat_eat_cucumbers():
	pass	


@then('I should have <left> cucumbers')
def i_should_have_left_cucumbers():
	pass


