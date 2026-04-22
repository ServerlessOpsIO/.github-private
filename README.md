# .github-private

Organization-wide GitHub configuration.

## Copilot

### Skills
- Instructions and resources for performing specific actions.
- _eg. Create a new Lambda function._

### Instructions
- Standards and best practices applied to specific file patterns.
- _eg. Write Python code like this._

### Agents
- Perform tasks based on defined skills and instructions.
- May employ MCP server for enhanced capabilities.
- _eg. Review my serverless application._

Agents can be categorized into different types based on their design and purpose. The following categories are not mutually exclusive, and an agent may fall into multiple categories depending on its functionality and use case.

#### Task agents
- Agents designed to perform a specific task.
- _eg. An architectural review agent._

#### Persona agents
- Agents designed to embody a specific persona or role.
- _eg. A senior software developer agent._

#### Sub-agents
- Agents that perform specific sub-tasks within a larger task.
- May be used individually, or grouped under a parent agent for complex tasks.
- May employ MCP server for enhanced capabilities.
- _eg. Plan agent._

#### Domain agents
- A form of sub-agent with specialized knowledge in specific areas.
- May employ MCP server usage for up-to-date information / documentation and enhanced capabilities.
- Typically used by a parent agent and not used individually.
- _eg. Testing agent_
