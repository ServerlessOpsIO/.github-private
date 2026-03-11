---
description: 'Use when creating or modifying AWS CloudFormation and SAM templates. Enforces secure, reusable, and maintainable infrastructure-as-code patterns for resources, parameters, IAM, and stateful data.'
applyTo: '**/template.yaml, **/template.yml, **/cloudformation.yaml, **/cloudformation.yml, **/*.cfn.yaml, **/*.cfn.yml, **/*.cloudformation.yaml, **/*.cloudformation.yml'
---

# AWS CloudFormation Guidelines

- Keep templates deterministic and environment-agnostic.
- Parameterize environment-specific values (names, ARNs, VPC/subnet IDs, retention windows) instead of hardcoding them.
- Prefer stack Parameters over `Mappings` and `Conditions` for region and environment differences.

## Structure And Readability

- Name the file `template.yaml` when creating a new template.
- Organize templates with a clear structure: Parameters, Mappings, Conditions, Resources, Outputs.
- Use consistent formatting and indentation (for example 2 spaces).
- Keep logical IDs stable; renaming logical IDs can force replacement of resources.
- Group related resources and add brief comments only where intent is not obvious.
- Prefer intrinsic functions (`!Ref`, `!Sub`, `!GetAtt`, `!If`) over manual string assembly.
- Avoid using YAML anchors and aliases unless they are necessary for reducing significant duplication, as they can reduce readability and make templates harder to understand for those unfamiliar with these features.

## Security And IAM

- Apply least-privilege IAM policies; avoid wildcard actions/resources unless strictly required.
- Do not hardcode secrets, tokens, or credentials in templates.
- Use Secrets Manager or SSM Parameter Store dynamic references for sensitive values.
- Ensure encryption is enabled for supported services (for example S3, DynamoDB, logs, and queues).

## Template Header

- Start file with `AWSTemplateFormatVersion: 2010-09-09`.
  - It is optional but customary to include.
- Use `Description` to provide a brief overview of the template's purpose.

## Resources

- Logical IDs
  - Should follow PascalCase.
  - Should be descriptive (eg. `DataBucket`, `GetItemFunction`, `UserTable`, `ApiGateway`).
- Use `DependsOn` only when necessary to enforce resource creation order that CloudFormation cannot infer from references.

### Stateful Resource Safety

- For stateful resources (for example `AWS::DynamoDB::Table`, `AWS::S3::Bucket`, `AWS::RDS::DBInstance`), explicitly set deletion behavior.
- Use `DeletionPolicy` and `UpdateReplacePolicy` deliberately (`Retain`, `Snapshot`, or `Delete`) based on data durability requirements.
- Avoid accidental replacements by carefully reviewing immutable property changes.

### Naming

- Do not explicitly set `Name` properties unless explicitly required by the resource. Let CloudFormation generate unique names to avoid conflicts and enable safe updates.
- When creating VPC related resources (eg. `AWS::EC2::VPC`, `AWS::EC2::Subnet`, `AWS::EC2::SecurityGroup`, `AWS::EC2::RouteTable`, `AWS::EC2::NatGateway`), add a `Name` tag for easier identification in the console.
  - If that resource is specific to a region then include the region in the `Name` tag value.
- If an S3 bucket requires a name to be configured then append the account ID and region to the bucket name to ensure uniqueness (for example `MyBucket-${AWS::AccountId}-${AWS::Region}`).

## Parameters

- Use parameters for values that differ between environments (for example dev, staging, prod) or regions.
- Use `AllowedValues` and `AllowedPattern` to enforce valid parameter inputs where possible.
- Use `Default` values for parameters when there is a common default that applies to most environments
- Use `Description` for parameters to clarify their purpose and expected values.

## Tags

- Tags should be passed to the deploy command instead of defined at the resource level when possible.

## SSM Parameters

- Keep SSM parameters minimal and useful; export only values intended for cross-stack reuse or service discovery
- Use consistent naming conventions for parameters
  - The first part of the paramater name should be the same as the stack name (for example `/MyStack/`) to avoid naming conflicts and improve organization.
    - Use the AWS::StackName pseudo parameter to reference the stack name in the parameter value (for example `Value: !Sub "/${AWS::StackName}/MyParameter"`).
  - The second part of the parameter name should be the same as the resource or value it represents (eg. `MyBucketName`).
    - Use PascalCase for the parameter name (eg. `MyBucketName`)


## Outputs

- Keep outputs minimal and useful; export only values intended for cross-stack reuse.

## Validation And Change Safety

- Ensure generated templates pass lint and validation (`cfn-lint`, or equivalent).
- Prefer safe rollout patterns for risky changes (for example introducing new resources before removing old ones).
- Treat CloudFormation changes as code changes: review diffs for IAM expansion, replacements, and data-loss risk before deployment.
