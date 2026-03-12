---
description: 'Use when creating or modifying DynamoDB resources in AWS CloudFormation and SAM templates or working with DynamoDB in Lambda functions.'
applyTo: '**/template.yaml, **/template.yml, **/cloudformation.yaml, **/cloudformation.yml, **/*.cfn.yaml, **/*.cfn.yml, **/*.cloudformation.yaml, **/*.cloudformation.yml, **/src/handlers/*/function.py'
---

# AWS DynamoDB Guidelines

- Apply these instructions to DynamoDB tables and related resources (for example `AWS::DynamoDB::Table`, `AWS::DynamoDB::GlobalTable`, `AWS::DynamoDB::TableReplica`) in CloudFormation and SAM templates, as well as DynamoDB interactions in Lambda functions.
- These instructions apply in addition to
  - The general CloudFormation and SAM conventions outlined in iac-cloudformation.instructions.md, iac-sam.instructions.md.
  - The general Lambda function guidelines outlined in cloud-aws-lambda.instructions.md and cloud-aws-lambda-python.instructions.md.

## Templates

- For DynamoDB tables, explicitly set `BillingMode` to `PAY_PER_REQUEST` unless there is a specific reason to use provisioned capacity (for example predictable high throughput requirements and cost optimization).
- A tables primary key name should be `pk` and sort key name should be `sk` unless there is a specific reason to use different names (for example existing data model or application requirements).

## Code
- When interacting with DynamoDB in code, use the AWS SDK's Document Client (for example `boto3.resource('dynamodb')` in Python) for a higher-level abstraction that handles data marshalling and simplifies working with DynamoDB items.
- Use single-table design with composite keys
- primary key values should be prefixed with a camelCase entity type (eg. `userId#123`, `city#Boston`).
- Avoid scanning tables in code. Instead, use queries with appropriate key conditions and indexes to efficiently retrieve data.


