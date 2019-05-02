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
    """Parametrized given, when, thens."""


@given('there are <start> cucumbers')
def there_are_start_cucumbers():
    """there are <start> cucumbers."""
    pass
	#raise NotImplementedError


@when('I eat <eat> cucumbers')
def i_eat_eat_cucumbers():
    """I eat <eat> cucumbers."""
    pass
	#raise NotImplementedError


@then('I should have <left> cucumbers')
def i_should_have_left_cucumbers():
    """I should have <left> cucumbers."""
    pass
	#raise NotImplementedError
