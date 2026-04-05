---
name: aws-lambda-add-function-fixtures
description: 'Add mock event and data, optionally output and response, and their respective schema files for a Lambda function. Use when asked to scaffold handler fixture files in data/handlers/<FunctionName>/ that match trigger type and repository conventions.'
argument-hint: '<function_name> for <event_source> (for example: CreateEntity for API Gateway)'
---

# AWS Lambda Add Function Mock Data

Create mock data and schema files for a Lambda function so handler scaffolding and tests have convention-aligned fixtures.

## When To Use

- User asks to add mock data files for a new Lambda function.
- A function folder exists and needs `data/handlers/<FunctionName>/` fixtures.
- A test scaffold needs event and output fixtures that match an event source.

## Inputs

- `function_name` (required): handler folder name (for example `CreateEntity`)
- `event_source` (optional): API Gateway | API Gateway v2 | Application Load Balancer / ALB | CloudFormation Custom Resources | CloudWatch Logs | Config | DynamoDB | EventBridge | Kinesis Firehose / Firehose | Kinesis Stream / Kinesis | SQS | SNS | S3 | custom

## Event Sources

| Event source | Event source message type | Event generation command |
|---|---|---|
| API Gateway (REST) | | `sam local generate-event apigateway aws-proxy --body '{}'` |
| API Gateway v2 (HTTP) | | `sam local generate-event apigateway http-api-proxy --body '{}'` |
| Application Load Balancer / ALB | | `sam local generate-event alb request` |
| CloudFormation (CFN) Custom Resource | | `sam local generate-event cloudformation create-request` |
| CloudWatch Logs | | `sam local generate-event cloudwatch logs` |
| Config | `item-change-notification` | `sam local generate-event config item-change-notification` |
| Config | `oversized-item-change-notification` | `sam local generate-event config oversized-item-change-notification` |
| Config | `scheduled notification` | `sam local generate-event config periodic-rule` |
| DynamoDB | | `sam local generate-event dynamodb update` |
| EventBridge | | `sam local generate-event cloudwatch scheduled-event` |
| Kinesis Streams / Kinesis | `record` | `sam local generate-event kinesis get-records` |
| Kinesis Firehose / Firehose| | `sam local generate-event kinesis kinesis-firehose` |
| S3 | `put` | `sam local generate-event s3 put` |
| S3 | `delete` | `sam local generate-event s3 delete` |
| SQS | | `sam local generate-event sqs receive-message --body '{}'` |
| SNS | | `sam local generate-event sns notification --message '{}'` |


## Constraints
- Do not offer to run any tests or validation.
- Do not offer any next steps to perform.
- Do not create `event.json` on your own.
    - only generate it using the appropriate `sam local generate-event` command.

## Procedure

1. Load relevant instruction files for AWS Lambda, SAM/CloudFormation templates, and the target runtime if present.
1. Clarify `event_source` message type if needed.
1. Ensure folder exists: `data/handlers/{function_name}/`.
1. Copy files from `assets/mock_data/` into the destination folder and rename to repository convention:
    * `data.json`
    * `data.schema.json`
    * `output.json`
    * `output.schema.json`
1. If `event_source` in _Event Sources_ table run event generation command and save output as `event.json`. Do not create `event.schema.json`
    *
1. For custom `event_source` events create placeholder event payload and schema.
1. For synchronous handlers (eg. API Gateway, API Gateway v2, ALB, CloudFormation Custom Resource), include:
    * `response.json`
    * `response.schema.json`

## Completion Criteria

- `data/handlers/{function_name}/` exists.
- Core payload and schema files (`data*`, `output*`) exist.
- Event fixture, and schema if applicable, exists for the selected trigger.
- Response fixture files exist when the trigger expects a synchronous response.

## Decision Points

- If event source cannot be inferred confidently, ask the user before running event generation command.

## Ambiguity Rules

- If `event_source` is omitted or ambiguous, infer from template resource event type and confirm only when uncertain.
- If destination path conventions conflict, choose the dominant pattern in the same repository subtree.
