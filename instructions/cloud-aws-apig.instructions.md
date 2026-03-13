---
description: 'Use when creating or modifying API Gateway resources in SAM templates or working with API Gateway in Lambda functions.'
applyTo: '**/template.yaml, **/template.yml, **/sam.yaml, **/sam.yml, **/*.sam.yaml, **/*.sam.yml, openapi.yaml, openapi.yml'
---

# AWS API Gateway Guidelines

- Apply these instructions to API Gateway resources (eg. `AWS::Serverless::Api`).
- Apply these instructions to `openapi.yaml` files.
- These instructions apply in addition to
  - The general CloudFormation and SAM conventions outlined in iac-cloudformation.instructions.md, iac-sam.instructions.md.
  - The general Lambda function guidelines outlined in cloud-aws-lambda.instructions.md and cloud-aws-lambda-python.instructions.md.

## Templates

- Always prefer `AWS::Serverless::Api` over `AWS::ApiGateway::RestApi` or `AWS::ApiGatewayV2::Api`.
- Use OpenAPI an `openapi.yaml` file to define the API in the SAM template.
- If the API invokes a Lambda function then ensure an `AWS::Lambda::Permission` resource is included to allow API Gateway to invoke the function.
- For `AWS::Serverless::Api` resources the DefinitionBody property should use the `!Transform` intrinsic function to reference the OpenAPI definition in `openapi.yaml` (eg. `DefinitionBody: !Transform [ 'AWS::Include', { Location: './openapi.yaml' } ]`).

## OpenAPI Definition

- The OpenAPI definition should be defined in a separate file named `openapi.yaml` and referenced from the template.
- Perform request validation in the `openapi.yaml` file.
