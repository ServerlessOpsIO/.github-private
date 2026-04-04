---
description: 'Use when creating or modifying S3 resources in AWS CloudFormation and SAM templates or working with S3 in Lambda functions.'
applyTo: '**/template.yaml, **/template.yml, **/cloudformation.yaml, **/cloudformation.yml, **/*.cfn.yaml, **/*.cfn.yml, **/*.cloudformation.yaml, **/*.cloudformation.yml, **/src/handlers/*/function.py'
---

# AWS S3 Guidelines

- Apply these instructions to S3 buckets and related resources (for example `AWS::S3::Bucket`, `AWS::S3::BucketPolicy`, `AWS::S3::BucketPublicAccessBlock`) in CloudFormation and SAM templates, as well as S3 interactions in Lambda functions.
- These instructions apply in addition to
  - The general CloudFormation and SAM conventions outlined in iac-cloudformation.instructions.md, iac-sam.instructions.md.
  - The general Lambda function guidelines outlined in cloud-aws-lambda.instructions.md and cloud-aws-lambda-python.instructions.md.

## Templates

- If an S3 bucket requires a name to be configured then append the account ID and region to the bucket name to ensure uniqueness (for example `MyBucket-${AWS::AccountId}-${AWS::Region}`).

## Code
- When interacting with S3 in code, use the AWS SDK's high-level abstractions (for example `boto3.resource('s3')` in Python) for easier handling of S3 objects and operations.