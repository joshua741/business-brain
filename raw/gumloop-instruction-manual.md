# Gumloop: Complete Platform Instruction Manual

**Summary**: Comprehensive guide to the Gumloop no-code AI automation platform — covers Agents vs Workflows architecture, building steps, node types, Twilio integration, Notion MCP, environment variables, and troubleshooting.

**Sources**: Google Drive — gumloop_instruction_manual.md (1l6PTEh3OBxdQXMxiz_I1uwYETDk8Yl0BrCjvyE0xNOc)

**Last updated**: 2026-05-29

---

## What Gumloop Is

Gumloop is a no-code AI automation platform that lets you build intelligent workflows by combining AI agents with step-by-step automation flows. It sits between simple automation tools and full developer-built systems — powerful enough to handle complex logic, but accessible enough to build without writing traditional code.

The platform operates on two primary components that work together: Agents and Workflows. Understanding the distinction between these two components is the most important foundational concept in Gumloop.

---

## The Core Architecture: Agents vs Workflows

### Agents — The Brain

An Agent is the intelligent, decision-making component of your Gumloop build. It is a customized AI model configured with a name, a set of instructions, an underlying AI model, and optionally a set of connected apps and skills.

Agents think. They read context, make judgment calls, classify information, and generate outputs based on nuanced instructions.

**Key characteristics:**
- Have a persistent identity with a name and configurable instructions
- Use a selected AI model as the underlying engine
- Can be connected to external apps such as Slack, Gmail, or databases
- Can be assigned Skills for specialized knowledge
- Can be used standalone or as a node inside a Workflow
- Have a Subagents section for connecting other Agents as nested assistants

**CRITICAL**: Agents are built first and tested standalone before connecting to any Workflow. This is not optional — it is the correct build order.

### Workflows — The Nervous System

A Workflow is a step-by-step automation that handles execution — receiving data from a trigger, moving it between tools, making simple routing decisions, and calling the Agent when intelligence is needed.

**Key characteristics:**
- Always triggered by an external event
- Execute nodes in a defined sequence
- Can include conditional branching for simple routing
- Call Agent Nodes when intelligence is needed
- Handle all data movement, timing, delays, and API calls
- Can be built conversationally using Build mode

---

## The Gumloop Interface

### Navigation Sections

- **Home** — Dashboard. Shows upcoming triggers, recent agent activity, quick access to creating Agents and Workflows.
- **Agents** — Where all Agents are listed, created, and managed.
- **Skills** — Library of reusable instruction sets (modular knowledge packages).
- **Workflows** — Where all Flows are built and managed. Build mode accessed here.
- **History** — Complete log of all agent conversations and workflow runs.
- **Apps** — Where external services are connected and API keys are managed.

---

## Building an Agent: Step by Step

### Step 1 — Create the Agent
Go to Agents section → click Create Agent. Land on new Agent page with build interface and test chat.

### Step 2 — Configure the Agent Settings

**Agent Preferences:**
- Model selector dropdown — choose the AI model
- Instructions field — the most important field. This is the complete system prompt.
- Allow Self-Updates toggle — **must be turned OFF for production**

**Triggers** — Leave empty during Agent build phase (Workflow handles triggering)

**Apps** — Attach connected external services to this specific Agent

**Skills** — Attach Skill modules to this Agent

**Subagents** — Leave as default for most builds

### Step 3 — Write Effective Agent Instructions

- Be specific and complete — the Agent only knows what you tell it
- Define the output format explicitly — show an example
- List valid values for constrained fields
- Define behavior for edge cases
- Use plain language
- Organize with clear sections (TONE, OBJECTIVES, CONVERSATION FLOW, GUARD RULES, WHAT THE AGENT WILL NEVER DO)

### Step 4 — Test the Agent Standalone

Check that:
- Tone matches expectations
- Output format is correct every time
- Edge cases are handled as specified
- Agent does not invent information it was not given
- Agent follows all defined rules consistently

**Do not proceed to Workflow construction until Agent behaves correctly in standalone testing.**

---

## Building a Workflow: Step by Step

### Step 1 — Create the Workflow
Go to Workflows → click Create Workflow. Name it descriptively.

### Step 2 — Use Build Mode
Type a plain language description of what you want the Workflow to do. Click Build. Gumloop auto-generates starting node structure.

Example Build mode prompt: "Receive an inbound SMS from Twilio via webhook, look up the sender phone number in a Notion database, send the message and database context to an AI Agent to generate a reply, send the reply back via Twilio, and update the Notion database with the result."

### Step 3 — Review and Adjust Generated Nodes
Always inspect each node carefully. Auto-generated structure is a starting point, not a finished product.

### Step 4 — Understand the Node Types

| Node | Function |
|---|---|
| Webhook Trigger node | Entry point. Generates unique webhook URL. Captures full payload. |
| Custom node / Flow Basics node | Parse, transform, extract specific fields from data |
| Ask AI node | Sends data to a specified Agent and receives output |
| Agent Node | Drops a pre-built Agent into the Workflow |
| Notion MCP node | Reads from and writes to Notion databases |
| Custom node (Python) | Python code that executes as part of Workflow. Uses requests library. |
| Conditional node | Evaluates condition, routes down different paths |
| Time delay / Wait node | Pauses Workflow execution for specified duration |

### Step 5 — Handle Variable Passing Between Nodes
Data moves between nodes as variables. Every node can receive inputs from previous nodes and pass its own outputs to subsequent nodes.

### Step 6 — Configure Environment Variables
Store all sensitive credentials as environment variables. Access in Python Custom Nodes via `os.environ.get('VARIABLE_NAME')`.

### Step 7 — Test the Workflow
Use built-in test feature with sample input. Check History section for detailed step-by-step execution log.

---

## Confirmed Node Architecture for Inbound SMS Automation

| Step | Node Type | Function |
|---|---|---|
| 1 | Webhook Trigger | Receives inbound SMS payload from Twilio |
| 2 | Custom node or Flow Basics | Parses webhook payload — extracts phone and message body |
| 3 | Notion MCP node | Looks up sender phone number in Notion database |
| 4 | Ask AI node | Sends message + context to AI Agent, receives structured output |
| 5 | Custom Python node | Calls Twilio REST API to send outbound SMS reply |
| 6 | Notion MCP node | Updates contact record in Notion |
| 7 | GHL API node or Custom node | Updates CRM contact record, tags, opportunity stage |
| 8 | Conditional node | If internal notification required |
| 9 | Conditional node | If follow-up sequence specified |

### Twilio Outbound SMS — Custom Python Node

```python
import requests
from requests.auth import HTTPBasicAuth
import os

def send_sms(to_number, message_body, from_number):
    account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
    auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
    url = f'https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Messages.json'
    payload = {
        'To': to_number,
        'From': from_number,
        'Body': message_body
    }
    response = requests.post(url, data=payload, auth=HTTPBasicAuth(account_sid, auth_token))
    return response.json()
```

Store `TWILIO_ACCOUNT_SID` and `TWILIO_AUTH_TOKEN` as Gumloop environment variables.

### Notion Integration Requirements
- Notion integration token (created at notion.so/my-integrations)
- Database ID from the target Notion database URL
- Integration must be added as a Connection inside the target Notion database

---

## Business Hours Logic

Any Workflow that sends outbound messages should include a business hours gate:
- Define acceptable hours (e.g., 9AM–6PM Central, Monday–Friday)
- Add check node before any outbound SMS
- If outside hours — route to delay node waiting until next business day

---

## Key Platform Rules

- Build order: **Agent first, Workflow second. Always.**
- Test every Agent in isolation before connecting to anything
- Store all credentials as environment variables — never hardcode
- Manual adjustment is always required after auto-generation
- Use History actively for monitoring after deployment
- Business hours logic belongs in every outbound messaging Workflow
- Allow Self-Updates should be OFF for production Agents
- Notion MCP requires the database to have the integration added as a Connection

---

## Troubleshooting Common Issues

| Issue | Solution |
|---|---|
| Workflow not triggering | Confirm external service posts to correct Webhook Trigger URL. Check HTTP method is POST. |
| Notion lookup returning empty | Check field name exactly matches Notion database field — including case and spacing. |
| Agent producing inconsistent outputs | Review instructions for ambiguity. Add explicit handling for every scenario. |
| Custom Python node failing | Check env variable names. Verify Python syntax. Check History log for error. |
| Outbound SMS not sending | Confirm TWILIO_ACCOUNT_SID and TWILIO_AUTH_TOKEN saved correctly. Check Twilio console. |
| Agent output not parsed correctly | Check Agent output format is consistent and variable name matches downstream node. |

---

## Related pages
- [[vince-ai]]
- [[n8n]]
- [[twilio]]
- [[ghl]]
