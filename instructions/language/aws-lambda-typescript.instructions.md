---
description: 'Use when creating or modifying AWS Lambda TypeScript handlers and their SAM function resources.'
applyTo: '**/src/handlers/*/function.ts, **/src/handlers/*/function.*.test.ts, **/template.yaml, **/template.yml, **/sam.yaml, **/sam.yml, **/*.sam.yaml, **/*.sam.yml'
---

# AWS Lambda TypeScript Guidelines

## General

- Follow the general TypeScript conventions outlined in lang-typescript.instructions.md.
- Follow the general CloudFormation and SAM conventions outlined in iac-cloudformation.instructions.md and iac-sam.instructions.md.
- Follow the Lambda infrastructure conventions in cloud-aws-lambda.instructions.md.
- Prioritize readability and maintainability while adhering to AWS best practices for serverless applications.

## Lambda Functions

### Functions

- Use AWS SDK for JavaScript v3 clients (`@aws-sdk/*`) for AWS service interactions.
- Add retry and timeout configuration for clients when non-default behavior is required by the workload.
- Use `@aws-lambda-powertools/logger` for structured logging, tracing, and metrics.
- Use environment variables for all configuration (no hardcoding).
- Initialize AWS clients and reusable utilities outside handlers to leverage Lambda container reuse.
- Include comprehensive error handling and logging for production debugging and monitoring.

#### Code Structure

- Keep the exported Lambda handler, `handler`, focused on request parsing, input checks, and response mapping.
- Use `@aws-lambda-powertools/parser` to validate and parse both the incoming event and the event's data against defined schemas before invoking the main logic.
- Use TypeScript types to define the expected shape of the event and response.
- Prefer types from `@aws-powertools/parser/types` over `@types/aws-lambda` for handler events and responses.
- Extract core business logic into a separate `main` function that `handler` calls after validation.
- Extract helper logic into additional functions as needed, but keep them in the same file if they are only used by that handler. Helper functions should be exported.
- Treat `JSON.parse` as unsafe input handling.

#### File Structure

- Use one directory per Lambda function under `src/handlers/<FunctionName>/`.
- Function code goes in `src/handlers/<FunctionName>/function.ts`.


### Tests

- Follow existing repository conventions for test file naming and location.
- Use `aws-sdk-client-mock` and `aws-sdk-client-mock-jest` for mocking AWS SDK clients in unit tests.
- Prefer deterministic unit tests by mocking AWS SDK clients and external dependencies.
- Use `describe()` blocks to organize tests by behavior or logical grouping.
- Follow the pattern:
  ```typescript
  describe(<FunctionName>, () => {
    describe('should succeed when', () => {
      it('situation', () => {

      })
    })

    describe('should fail when', () => {
      it('situation', () => {

      })
    })
  ```
- Every function in the associated `src/handlers/<FunctionName>/function.ts` file should have corresponding unit tests.
- Cover success path, validation failures, and service failure behavior.
- Validate that error responses preserve the expected schema and status code mapping.

#### File Structure

- Unit tests: `src/handlers/<FunctionName>/function.unit.test.ts`
- Integration tests: `src/handlers/<FunctionName>/function.integration.test.ts`
- End-to-end tests: `src/handlers/<FunctionName>/function.ete.test.ts`

### Common Code

- Place common code shared across multiple functions under `src/lib/`

## Template

- Ensure each `AWS::Serverless::Function` `CodeUri` points to the function build output directory.
- Ensure each `AWS::Serverless::Function` `Handler` points to the compiled module export (for example `function.handler`).
- Function `Metadata.BuildMethod` should be `esbuild`.
- Function `Metadata.BuildProperties.Target` should be `es2020`.
- Function `Metadata.BuildProperties.Format` should be `esm`
- Function `Metadata.BuildProperties.MainFields` should be `module,main`.
- Function `Metadata.BuildProperties.Minify` should be `true` for production workloads and `false` for development or testing workloads.
- Function `Metadata.BuildProperties.Sourcemap` should be `true` for development or testing workloads and `false` for production workloads.
- Function `Metadata.BuildProperties.OutExtension` should be `[".js=.mjs"].
- Function `Metadata.BuildProperties.EntryPoints` should be ["function.js"].
