# Product Brief Template — Preliminary Solution

A starting structure for the brief, written as a **preliminary business solution** (stage 1). Adapt it to the feature, the purpose, and the domain: drop sections that do not earn their place, add sections the feature needs, reorder freely. Keep sections 1–3 at business level. Field-level detail (columns, validation rules, UI fields) goes to section 5, not the body.

## Default Structure

```markdown
---
type: preliminary-solution
stage: 1
feature: {feature-slug}
status: draft
lang: {language}
owner: "{BA name}"
created: {YYYY-MM-DD}
updated: {YYYY-MM-DD}
source: "{Requirement source}"
changelog:
  - {YYYY-MM-DD} | created preliminary solution
---

# {Feature name} — Preliminary Solution

## 1. Requirement Clarification

### 1.1 Customer Profile
{Customer type/size} needs to {business task}, typically performed at {screen/module/moment}.

### 1.2 Business Story
Today, when {triggering condition}, {user role} has to {current workaround}.
Current process: {Step 1} → {Step 2} → {Step 3}

### 1.3 Current Software Coverage
The software already supports {existing capability}. However, it does not yet support {gap}.

### 1.4 Pain Points
{User role} {concrete consequence: time lost, where errors happen, what is hard to reconcile}.

### 1.5 Desired Outcome
{User role} wants the software to {what it should support} in order to {business purpose}.

## 2. Business Requirements

The system must support {overall goal}. The requirements fall into {N} groups:

### 2.1 {Group 1 name}
- **{Task name}:** {specific description — who/what it applies to and the business value}
- **{Task name}:** {specific description}

### 2.2 {Group 2 name}
- **{Task name}:** {specific description}

**Goal:** {measurable expected result}

## 3. Business Solution

Deliver the "{Feature name}" feature, integrated into the {business flow name} flow.

**Solution components:**
- **User interface (UI):** {what is added/changed, on which screen — 1–2 lines only, no column/field specs}
- **Processing logic:** {main processing rules; how data is mapped}
- **Process:** {Step 1} → {Step 2} → {Step 3} → {Step 4}

**Impact scope:**
- {Other business flows/screens affected}
- {How other platforms (mobile/web) are handled}

## 4. Open Questions (for the Stage 2 sign-off meeting)

| # | Question | Answered by | Status |
|---|----------|-------------|--------|
| 1 | {question} | {customer / sales / engineering} | [ ] |

## 5. Notes for Stage 5
> Parking lot for small details the customer mentioned (e.g. an extra column, a validation condition) so they can be reused in Stage 5. Keep them out of the sections above.
- {detail 1}
```
