---
description: 'AWS Lambda Python coding conventions and guidelines'
applyTo: '**/src/handlers/*/function.py, **/tests/*/handlers/*/test_function.py, **/template.yaml, **/template.yml, **/sam.yaml, **/sam.yml, **/*.sam.yaml, **/*.sam.yml'
---

## General
- Follow the general Python coding conventions outlined in lang-python.instructions.md.
- Follow the general Cloudformation and SAM conventions outlined in iac-cloudformation.instructions.md and iac-sam.instructions.md.
- Follow the Lambda infrastructure conventions in cloud-aws-lambda.instructions.md.
- Prioritize readability and maintainability while adhering to AWS best practices for serverless applications.

## Lambda Functions

### Functions
- Use `boto3` for AWS service interactions with proper retry logic and timeouts.
- Use `aws-lambda-powertools` for structured logging, tracing, and metrics.
- Use environment variables for all configuration (no hardcoding).
- Initialize AWS clients and services outside the handler to leverage container reuse.
- Include comprehensive error handling and logging for production debugging and monitoring.

#### Code Structure
- Define a `handler(event, context)` function as the Lambda entry point that validates the event and calls `_main()`.
- Define a `_main(data)` function containing the core business logic.
- Extract helper logic into `_` prefixed functions above `_main` and `handler`.
- Include error handling and structured logging via `aws-lambda-powertools`.
- Use the `@event_source` decorator from `aws-lambda-powertools` to validate and parse the incoming event against the defined schema.

#### File Structure
- Each Lambda function gets its own directory: `src/handlers/<FunctionName>/`
- Function code goes in `src/handlers/<FunctionName>/function.py`
- Include `src/handlers/<FunctionName>/__init__.py` to make it a package
- Include `src/handlers/<FunctionName>/requirements.txt` with pip-compatible dependencies

### Mock Data

- Every Lambda function should have a mock event named event, mock event data, and mock function response data. Synchronous event sources should also have a mock Lambda function response.
- All mocks should also have an associated schema.

#### File Structure
- Each Lambda function gets its own directory: `data/handlers/<FunctionName>/`
- Mock event goes in `data/handlers/<FunctionName>/event.json`
- Mock event schema goes in `data/handlers/<FunctionName>/event_schema.json`
- Mock event data goes in `data/handlers/<FunctionName>/data.json`
- Mock event data schema goes in `data/handlers/<FunctionName>/data_schema.json`
- Mock function output goes in `data/handlers/<FunctionName>/output.json`
- Mock function output schema goes in `data/handlers/<FunctionName>/output_schema.json`
- If the function is triggered by a synchronous event source then the expected response from the function should be included in `data/handlers/<FunctionName>/response.json` and its schema in `data/handlers/<FunctionName>/response_schema.json`

### Tests

- Follow existing repository conventions for test file naming and location.
- Use the `moto` library for mocking AWS services in unit tests to enable testing without actual AWS resources.
- Use the `pytest` framework for writing and running unit tests, and follow its conventions for test discovery and organization.
- Use `pytest` fixtures to set up and tear down any necessary test state, including mocking AWS services with `moto` and loading mock data from the `data/handlers/<FunctionName>/` directory.
- Validate mock data against their schemas in tests.
- Create an `aws_credentials` fixture that sets up dummy AWS environmental variables with non-empty but invalid string values.
- Every function in the associated `src/handlers/<FunctionName>/function.py` file should have corresponding unit tests.
- Cover success path, validation failures, and service failure behavior.
- Validate that error responses preserve the expected schema and status code mapping.


#### File Structure
- Unit tests: `tests/unit/handlers/<FunctionName>/test_function.py`
- Integration tests: `tests/integration/handlers/<FunctionName>/test_function.py`
- End-to-end tests: `tests/ete/handlers/<FunctionName>/test_function.py`
- All `tests/` subdirectories must include an empty `__init__.py` files

### Common Code
- Common code that is shared across multiple Lambda functions should be placed in the installable package named `common`.
- The `common` package should be created under the `src/common/` directory.
- The `common` package should be structured as a standard Python package with an `__init__.py` file and any necessary submodules.
- The file `src/common/setup.py` should be included to allow the package to be installed in Lambda execution environments and in local development environments for testing.

## Template
- All `AWS::Serverless::Function` resources in the SAM template should have a `Handler` with a value of function.handler.
- All `AWS::Serverless::Function` resources in the SAM template should have a `CodeUri` that points to the directory containing the function code (for example `src/handlers/<FunctionName>/`).