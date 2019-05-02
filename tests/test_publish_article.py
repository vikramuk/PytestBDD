# coding=utf-8
"""Blog feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('publish_article.feature', 'Publishing the article')
def test_publishing_the_article():
	pass



@given('I have an article')
def i_have_an_article():
	pass


@given("I'm an author user")
def im_an_author_user():
	pass



@when('I go to the article page')
def i_go_to_the_article_page():
	pass


@when('I press the publish button')
def i_press_the_publish_button():
	pass	



@then('I should not see the error message')
def i_should_not_see_the_error_message():
	pass	
	
	"""I should not see the error message.
	raise NotImplementedError"""


@then('the article should be published')
def the_article_should_be_published():
	pass    


