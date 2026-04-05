'''
{{ function_name }} handler

{{ description }}
'''

from typing import TYPE_CHECKING, TypedDict

from aws_lambda_powertools.logging import Logger
from aws_lambda_powertools.utilities.data_classes import (
    event_source
    {{ event_source_dataclass }}
)
from aws_lambda_powertools.utilities.typing import LambdaContext

# Initialize logger
LOGGER = Logger(utc=True)

def _main({{ variable_name }}: {{ variable_data_type }}) -> {{ return_type }}:
    '''Main function logic'''
    pass

@LOGGER.inject_lambda_context
@event_source(data_class={{ event_source_dataclass }})
def handler(event: {{ event_source_dataclass }}, context: LambdaContext) -> {{ return_type }}:
    '''Function entry and event handling'''
    LOGGER.debug('Event', extra={"message_object": event.raw_event})

    # Extract data from event

    # Pass data to main function logic
    _main({{ variable_name }})

    return
