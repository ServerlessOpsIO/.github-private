'''Test {{ function_name }}'''

from dataclasses import asdict
import json
import jsonschema
import os
from types import ModuleType
from typing import Generator

import pytest
from pytest_mock import MockerFixture

from moto import mock_aws
from aws_lambda_powertools.utilities.data_classes import {{ event_source }}


from src.handlers.{{ function_name }}.function import Output, ResponseBody

FN_NAME = '{{ function_name }}'
DATA_DIR = './data'
FUNC_DATA_DIR = os.path.join(DATA_DIR, 'handlers', FN_NAME)
EVENT = os.path.join(FUNC_DATA_DIR, 'event.json')
EVENT_SCHEMA = os.path.join(FUNC_DATA_DIR, 'event.schema.json')
DATA = os.path.join(FUNC_DATA_DIR, 'data.json')
DATA_SCHEMA = os.path.join(FUNC_DATA_DIR, 'data.schema.json')
OUTPUT = os.path.join(FUNC_DATA_DIR, 'output.json')
OUTPUT_SCHEMA = os.path.join(FUNC_DATA_DIR, 'output.schema.json')
RESPONSE = os.path.join(FUNC_DATA_DIR, 'response.json')
RESPONSE_SCHEMA = os.path.join(FUNC_DATA_DIR, 'response.schema.json')


### Fixtures
@pytest.fixture()
def mock_context(lambda_function_context, function_name=FN_NAME):
    '''context object'''
    return lambda_function_context(function_name)

# Data
@pytest.fixture()
def mock_data(data=DATA) -> Data:
    '''Return function event data'''
    with open(data) as f:
        return Data(**json.load(f))

@pytest.fixture()
def data_schema(data_schema=DATA_SCHEMA):
    '''Return a data schema'''
    with open(data_schema) as f:
        return json.load(f)
# Event
@pytest.fixture()
def mock_event(e=EVENT) -> {{ event_source}}:
    '''Return a function event'''
    with open(e) as f:
        return {{ event_source}}(json.load(f))

@pytest.fixture()
def event_schema(schema=EVENT_SCHEMA):
    '''Return an event schema'''
    with open(schema) as f:
        return json.load(f)

# Output
@pytest.fixture()
def mock_expected_output(output=OUTPUT) -> Output:
    '''Return a function output'''
    with open(output) as f:
        return Output(**json.load(f))

@pytest.fixture()
def expected_output_schema(output_schema=OUTPUT_SCHEMA):
    '''Return an output schema'''
    with open(output_schema) as f:
        return json.load(f)

# Response
@pytest.fixture()
def mock_expected_response(response=RESPONSE) -> ResponseBody:
    '''Return response'''
    with open(response) as f:
        return ResponseBody(**json.load(f))

@pytest.fixture()
def expected_response_schema(response_schema=RESPONSE_SCHEMA):
    '''Return an output schema'''
    with open(response_schema) as f:
        return json.load(f)


# AWS Clients
@pytest.fixture()
def aws_credentials() -> None:
    '''Mocked AWS Credentials for moto.'''
    os.environ["AWS_ACCESS_KEY_ID"] = "testing"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "testing"
    os.environ["AWS_SECURITY_TOKEN"] = "testing"
    os.environ["AWS_SESSION_TOKEN"] = "testing"
    os.environ["AWS_DEFAULT_REGION"] = "us-east-1"

@pytest.fixture()
def mocked_aws(aws_credentials):
    '''Mock all AWS interactions'''
    with mock_aws():
        yield

# Fixtures for any AWS clients here


# Function
@pytest.fixture()
def mock_fn(
    mocked_aws,
    mocker: MockerFixture,
) -> Generator[ModuleType, None, None]:
    '''Patch the environment variables for the function'''
    import src.handlers.{{ function_name }}.function as fn

    yield fn


### Data validation
def test_validate_data(mock_data, data_schema):
    '''Test data against schema'''
    jsonschema.Draft7Validator(asdict(mock_data), data_schema)

def test_validate_event(mock_event, event_schema):
    '''Test event against schema'''
    jsonschema.Draft7Validator(mock_event._data, event_schema)

def test_validate_expected_data(mock_expected_output, expected_output_schema):
    '''Test output against schema'''
    jsonschema.Draft7Validator(asdict(mock_expected_output), expected_output_schema)

def test_validate_expected_response(mock_expected_response, expected_response_schema):
    '''Test response against schema'''
    jsonschema.Draft7Validator(asdict(mock_expected_response), expected_response_schema)


### Tests
def test_handler(
    mock_fn: ModuleType,
    mock_event: {{ event_source}},
    mock_context,
):
    '''Test calling handler'''
    pass


def test__main(
    mock_fn: ModuleType,
):
    '''Test _main()'''
    pass

