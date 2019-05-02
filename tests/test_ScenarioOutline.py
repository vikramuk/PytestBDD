# coding=utf-8
"""Testing Feature for Scenario Outline feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('ScenarioOutline.feature', 'Test Scenario')
def test_test_scenario():
    """Test Scenario."""


@given('I click on <URL>')
def i_click_on_url():
	pass

@when('i login with <username>')
def i_login_with_username():
	pass


@then('Examples')
def examples():
	pass



@then('i get the <username>')
def i_get_the_username():
	pass



@then('|A|B|C|')
def abc():
	pass


@then('|URL|username|username|')
def urlusernameusername():
	pass


