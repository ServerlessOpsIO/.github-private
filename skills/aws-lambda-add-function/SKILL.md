---
name: aws-lambda-add-function
description: 'Add new AWS Lambda function files in an existing project for a specified language (TypeScript, Python, or Go). Use when asked to scaffold a new Lambda function.'
argument-hint: '<language> <function_name> function triggered by <event_source> to do <operation> (for example: TypeScript CreateEntity function triggered by API Gateway to create an entity)'
---

# AWS Lambda Create Function

Scaffold a Lambda function file that matches the target repository's structure and coding conventions.

## When To Use

- User asks to create a new Lambda function.
- User specifies a language (TypeScript, Python, or Go).
- Project already has an AWS SAM template and existing handlers to follow.

## Inputs

- `language` (required): `typescript` | `python` | `go`
- `function_name` (required): logical name for the handler folder (for example `CreateEntity`)
- `operation` (optional): short intent (for example `create`, `get`, `delete`, `upsert`)
- `event_source` (optional): API Gateway, EventBridge, SQS, or other trigger

If any input is missing, ask for it before writing files.

## Constraints

- Do not modify existing function files or handlers.
- Do not modify existing SAM template resources except to add the new function.
- Do not implement the operation the function should perform.
- Do not implement or refactor code in template function.
- Do not create new file content from scratch.
- Do not offer to run any tests or validation.
- Do not offer any next steps to perform.
- Only create new files by copying from this skill's `.github/skills/aws-lambda-add-function/assets/` and `.github/skills/aws-lambda-add-function/templates/` directories
- Do replace template variables with known values from task.

## Workflow

1. Load relevant instruction files for the target language, CloudFormation templates, SAM templates, AWS Lambda, and AWS Lambda language specifics.
1. Detect project conventions.
1. Inspect existing handler folders and nearby functions to confirm naming style, logging approach, response types, and test layout.
1. Create function directory: `src/handlers/{function_name}`
1. Copy function file(s) under this skill's templates based on `language` input
    * python: `.github/skills/aws-lambda-add-function/templates/{language}/*` -> `src/handlers/{function_name}/`
    * If you cannot find a subdirectory matching the language stop all work and tell user why you stopped.
1. Copy assets (if any) under this skill's assets based on `language` input.
    * `.github/skills/aws-lambda-add-function/assets/{language}/*` -> `src/handlers/{function_name}/`
1. Replace function file template variables in the new function file.
1. Add SAM function resource to the project's `template.yaml`.
1. Add or update `AWS::Serverless::Function` with correct `CodeUri`, `Handler`, `Runtime`, `MemorySize`, `Timeout`, and `Architectures`.
1. Keep runtime aligned with existing functions in the same template.
    * If no existing functions then check project configuration:
        * Python: check for `Pipenv`, `Poetry`, or `pyproject.toml` to determine Python version.
        * typescript: check `package.json` for NodeJS version.

## Completion Criteria

- New function file(s) exists at the correct language-specific path.
- Any asset file(s) exists at the correct language-specific path.
- SAM template points to the correct code path and handler export.

## Ambiguity Rules

- If language is unsupported, explain supported languages and ask for one of them.
