---
name: aws-lambda-create-function
description: 'Create a new AWS Lambda function file in an existing project for a specified language (TypeScript, Python, or Go). Use when asked to scaffold Lambda handler code that matches project conventions, folder structure, and SAM integration.'
argument-hint: '<language> and <function_name> function (for example: TypeScript CreateEntity function)'
---

# AWS Lambda Create Function

Create a Lambda function file that matches the target repository's structure and coding conventions.

## When To Use

- User asks to create a new Lambda function.
- User specifies a language (TypeScript, Python, or Go).
- Project already has an AWS SAM template and existing handlers to follow.

## Inputs

- `language`: `typescript` | `python` | `go`
- `function_name`: logical name for the handler folder (for example `CreateEntity`)
- `operation`: short intent (for example `create`, `get`, `delete`, `upsert`)
- `event_source`: API Gateway, EventBridge, SQS, or other trigger

If any input is missing, ask for it before writing files.

## Procedure

1. Load relevant instruction files for the target language, CloudFormation templates, SAM templates, AWS Lambda, and AWS Lambda language specifics.
2. Detect project conventions.
3. Inspect existing handler folders and nearby functions to confirm naming style, logging approach, response types, and test layout.

4. Choose the destination path and files by language.
* Python:
  * Function: `src/handlers/<FunctionName>/function.py`
  * Requirements: `src/handlers/<FunctionName>/requirements.txt`
  * Package file: `src/handlers/<FunctionName>/__init__.py`
* TypeScript:
  * Function: `src/handlers/<FunctionName>/function.ts`
* Go:
  * Function: `src/handlers/<FunctionName>/function.go`

5. Create the function file with minimal production-ready structure.
6. Include `handler` entrypoint compatible with the project's runtime and event source.
7. Add structured logging consistent with existing functions.
8. Read configuration from environment variables only.
9. Add safe input handling and explicit error mapping.
10. Keep business logic in a helper (`main`/`_main`) and keep `handler` focused on orchestration.

11. Validate the scaffold against language expectations.

12. Add mock event and schema files for the declared trigger in the corresponding `data/handlers/<FunctionName>/` directory.
13. For synchronous event sources, include a mock response file and schema in the corresponding `data/handlers/<FunctionName>/` directory.
14. Create empty event data file and data schema file in the corresponding `data/handlers/<FunctionName>/` directory.
15. Create empty output data file and output schema file in the corresponding `data/handlers/<FunctionName>/` directory.

16. Add SAM function resource to template.
17. Add or update `AWS::Serverless::Function` with correct `CodeUri`, `Handler`, `Runtime`, `MemorySize`, `Timeout`, and `Architectures`.
18. Keep runtime aligned with existing functions in the same template.

## Completion Criteria

- New function file exists at the correct language-specific path.
- Handler signature matches runtime and trigger expectations.
- SAM template points to the correct code path and handler export.

## Ambiguity Rules

- If multiple folder patterns exist, copy the pattern used by the closest existing handler.
- If both sync and async response styles exist, ask which style to follow.
- If language is unsupported, explain supported languages and ask for one of them.
