---
name: aws-lambda-add-function-tests
description: 'Add test files for an AWS Lambda function in TypeScript, Python, or Go projects. Use when asked to add unit tests, API event fixtures, and handler-level assertions that match repository conventions and CI tooling.'
argument-hint: '<function_name> and test type(s) (for example: CreateEntity unit + integration)'
---

# AWS Lambda Create Function Tests

Add test files for a Lambda handler that match the target repository's structure, runtime, and existing test conventions.

## When To Use

- User asks to add tests for a new or existing Lambda function.
- A handler exists and needs baseline test coverage.
- The repository already has a test framework to follow (for example `pytest`, `jest`, or `go test`).

## Inputs

- `language`: `typescript` | `python` | `go`
- `function_name`: handler folder or module name (for example `CreateEntity`)
- `event_source`: API Gateway | EventBridge | SQS | SNS | DynamoDB Streams | custom
- `test_scope`: unit only | integration only | ete only | all

If one or more inputs are missing, ask before creating files.

## Procedure

1. Load relevant instruction files for the target language, AWS Lambda, and AWS Lambda language specifics.
2. Detect repository test conventions.
3. Inspect nearby handler tests to confirm folder layout, naming style, mock strategy, and assertion style.

4. Choose destination test paths by language.
* Python
  * Unit: `tests/unit/handlers/<FunctionName>/test_function.py`
  * Integration: `tests/integration/handlers/<FunctionName>/test_function.py`
  * ETE: `tests/ete/handlers/<FunctionName>/test_function.py`
* Typescript
  * Unit: `src/handlers/<FunctionName>/function.unit.test.ts`
  * Integration: `src/handlers/<FunctionName>/function.integration.test.ts`
  * ETE: `src/handlers/<FunctionName>/function.ete.test.ts`
* Go
  * All: `handlers/<FunctionName>/function_test.go`

5. For unit tests
* Create fixtures for the data in files under `data/handlers/<FunctionName>/`.
* Add mocks/fakes following project style.

6. Write core behavior tests.
* Success path returns expected status/result payload.
* Validation failure returns mapped error response.
* Unexpected exception returns safe error response and does not leak internals.
* Environment variable behavior is covered (set, missing, invalid).

## Completion Criteria

- Test files exist in convention-aligned locations.
- At least one success and one failure case are covered.
- Trigger-specific event fixture exists.
- External dependencies are mocked or isolated.

## Decision Points

- If multiple test layouts exist, follow the closest existing handler pattern.
- If both unit and integration tests are requested but no integration harness exists, create unit tests and note the integration prerequisite.
- If handler logic is tightly coupled, first extract testable helper logic with minimal functional change.

## Ambiguity Rules

- If language is omitted, infer from nearby handler files and confirm.
- If event source is omitted, infer from template and handler signature, then confirm.
- If assertion style differs across modules, use the dominant style in the same directory tree.
