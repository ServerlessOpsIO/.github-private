---
description: 'Use when creating or modifying AWS Lambda functions in AWS SAM templates.'
applyTo: '**/template.yaml, **/template.yml, **/sam.yaml, **/sam.yml, **/*.sam.yaml, **/*.sam.yml, openapi.yaml'
---

# AWS Lambda Function Guidelines

- Apply these instructions to AWS Lambda Functions.
- These instructions apply in addition to the general CloudFormation and SAM conventions outlined in iac-cloudformation.instructions.md and iac-sam.instructions.md.

## Lambda Functions

- For Lambda functions, prefer `AWS::Serverless::Function` over `AWS::Lambda::Function` for better SAM CLI support and simplified configuration.
- Define each Lambda with explicit `MemorySize`, and `Timeout` suitable to workload.
  - If suitable `MemorySize` is undetermined then set it to 128 MB.
  - If suitable `Timeout` is undetermined then set it to 5 seconds.
- Set `Architectures` deliberately (`arm64` or `x86_64`) and keep it consistent across related functions.
  - Prefer `arm64` for new functions unless there is a specific reason to use `x86_64` (for example dependency compatibility or local testing constraints).
- Use `Environment.Variables` for non-secret runtime config. Never hardcode credentials or secrets in templates.
- Use `Policies` for defining function permissions.
  - Prefer AWS SAM policy templates when they fit the use case for simplicity and maintainability (for example `AmazonDynamoDBReadOnlyAccess`, `AWSLambdaBasicExecutionRole`, `AWSLambdaVPCAccessExecutionRole`).
  - Use inline policies for custom permissions that don't fit a managed policy template, but keep them focused and least-privilege.
- Set `Runtime` to the same runtime as existing functions in the template.
  - If no other functions exist, set `Runtime` to the latest supported platform version for the chosen language (for example `python3.14`, `nodejs24.x`) unless there is a specific reason to use an older version (for example dependency compatibility).
- Avoid configuring a VPC for Lambda functions unless necessary.

## Event Sources

- Define event sources directly in the function resource when possible for better visibility and simpler maintenance.
- For complex event source configurations (for example API Gateway with multiple routes, or EventBridge rules with multiple targets), consider defining the event source as a separate resource and referencing it from the function for better organization and reusability.

### API Gateway

- For API Gateway event sources, prefer `AWS::Serverless::Api` with OpenAPI definitions for better structure and maintainability when defining multiple routes or complex request/response models.
  - The OpenAPI definition should be defined in a separate file named `openapi.yaml` and referenced from the template.
- Perform request validation in the `openapi.yaml` file.