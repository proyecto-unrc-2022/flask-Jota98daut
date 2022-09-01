import json
from behave import *
from application import USERS

@given('some users are in the system')
def step_impl(context):
    USERS.update({'jasonb': {'name': 'Jason Bourne'}})

@when(u'I retrieve the customer \'jasonb\'')
def step_impl(context):
    context.page = context.client.get('/users/{}'.format('jasonb'))
    assert context.page

@then(u'I should get a \'200\' response')
def step_impl(context):
    assert context.page.status_code is 200

@then(u'the following user details are returned')
def step_impl(context):
    # assert context.table[0].cells[0] in context.page.text
    assert "Jason Bourne" in context.page.text

@given('the user "freddy" doesn\'t exist')
def step_impl(context):
    assert 'freddy' not in USERS

@when(u'I receive a POST request on \'/users\' with the username "freddy"')
def step_impl(context):
    payload = {
            "username": "freddy",
            "name": "Freddy Mercury"
            }
    context.req = context.client.post('/users', data=payload)
    assert context.req

@then('the user "freddy" should be added')
def step_impl(context):
    assert 'freddy' in USERS

@then(u'I should get a \'201\' response')
def step_impl(context):
    assert context.req.status_code is 201
