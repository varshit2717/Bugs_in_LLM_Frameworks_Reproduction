# A Characterization Study of Bugs in LLM Agent Workflow Orchestration Frameworks

This repository contains the materials and findings from the first comprehensive empirical study on bugs in LLM agent workflow orchestration frameworks, helping to reproduce the methodology in this paper.

## Research Questions

### RQ1: Root Cause
- **Objective:** Systematically classify root causes of bugs in LLM frameworks
- **Focus:** Analyze distribution across different frameworks and framework components

### RQ2: Symptom
- **Objective:** Systematically classify symptoms of bugs in LLM frameworks
- **Focus:** Analyze distribution across different frameworks and framework components

### RQ3: Relationship between Root Cause and Symptom
- **Objective:** Explore relationships between root causes and symptoms
- **Focus:** Identify how specific root causes correspond to particular symptom categories

### RQ4: Unique Challenge in LLM Framework Analysis
- **Objective:** Identify unique problem patterns in LLM frameworks compared to traditional software
- **Focus:** Determine specialized quality assurance approaches for novel challenges

## Methodology

### Step 1: Framework Selection
Selected three representative LLM frameworks (LangChain, LlamaIndex, and Haystack) based on comprehensive analysis of bug history accessibility and architectural completeness.

### Step 2: Data Collection
- Used GitHub's Search API with targeted filtering queries
- Combined official bug labels with repository specifications and bug-related keywords
- Collected 597 PRs from LangChain, 799 from LlamaIndex, and 181 from Haystack

### Step 3: Manual Labeling
- Employed collaborative annotation by two experienced LLM developers
- Focused on three dimensions: Root Cause, Symptom, and Framework Component
- Identified and classified 1,026 distinct bug instances (521 from LangChain, 436 from LlamaIndex, 69 from Haystack)

### Step 4: Statistical Analysis
Conducted comprehensive statistical analysis to address the research questions, exploring distributions across frameworks and components.

## Contributions

1. **Framework Structural Abstraction:**
   - Proposed the first unified structural abstraction for LLM frameworks
   - Identified four core components: Data Preprocessing, Core Schema, Agent Construction, and Featured Modules

2. **Comprehensive Bug Characterization:**
   - Conducted the first large-scale characterization of over 1,000 bugs
   - Designed a systematic taxonomy with 9 root cause categories and 6 symptom categories

3. **Insights and Guidance:**
   - Provided statistical analysis of bug patterns across frameworks and structural elements
   - Offered actionable recommendations to improve framework design and reliability

## Project Directory Structure and Description

```plaintext
Bugs_in_LLM_Frameworks/
├── step1/
│      └── framework_statistics.xlsx
├── step2/
│      ├── pr_scrap.py
│      │# scrap the PR information into json file
│      ├── pr_haystack.json
│      ├── pr_langchain.json
│      ├── pr_llamaindex.json
│      │
│      ├── pr_process.py
│      │# extract the important information of PR to excel file
│      ├── pr_haystack.xlsx
│      ├── pr_langchain.xlsx
│      └── pr_llamaindex.xlsx
├── step3/
│      |# Labeled data without detailed explanation
│      ├── pr_haystack_labeled.xlsx
│      ├── pr_langchain_labeled.xlsx
│      └── pr_llamaindex_labeled.xlsx
├── step4/
│      ├── component.py
│      │# show the heatmap of ditribution in different component
│      ├── rc_comp.pdf
│      ├── sym_comp.pdf
│      │
│      ├── different_framework.py
│      │# show the heatmap of ditribution in different framework
│      ├── rc_diff_frame.pdf
│      ├── sym_diff_frame.pdf
│      │
│      ├── rq3_sankeymatic.txt
│      │# the site's(https://sankeymatic.com/) source code of RQ3's sankey picture
│      └── sym_rc.pdf
├── requirements.txt
└── README.md
=======

