---
description: 'Use when creating or modifying AWS SAM templates. Enforces secure, repeatable, and maintainable patterns for serverless resources, function configuration, permissions, events, and deployment safety.'
applyTo: '**/template.yaml, **/template.yml, **/sam.yaml, **/sam.yml, **/*.sam.yaml, **/*.sam.yml'
---

# AWS SAM Guidelines

- Apply these instructions in addition to the general CloudFormation guidelines in iac-cloudformation.instructions.md, which also apply to SAM templates.
- Prioritize readability and maintainability while adhering to AWS best practices for serverless applications.

## Template Structure

- Keep `Globals` minimal and intentional.
  - Put only truly shared settings in `Globals`; override per resource when behavior differs.

## Template Header

- Use `Transform: AWS::Serverless-2016-10-31`

## Build & Validate

- Validate templates with `sam validate --lint`.
- Prefer `sam build` before local testing or deployment to catch packaging/runtime issues early.
