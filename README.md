# Bugs in LLM Frameworks — Reproduction Study

This repository contains an independent academic reproduction and extension of a research study on bugs in Large Language Model (LLM) agent frameworks.

The project first reproduces the analysis reported in the original study and then applies the same methodology to a newly collected and manually labeled set of GitHub pull requests.

## Project Goals

The main objectives of this project are to:

- reproduce the original study's analysis,
- verify the reported findings,
- reproduce the major figures,
- collect a new set of bug-fixing pull requests,
- manually label the new pull requests,
- analyze the new dataset using the same methodology,
- compare the reproduced results with the original findings.

## Frameworks Studied

The analysis focuses on:

- LlamaIndex
- Haystack
- LangChain

## Research Questions

### RQ1 — Root Causes

What are the root causes of bugs in LLM agent frameworks, and how are they distributed across different frameworks and software components?

### RQ2 — Symptoms

What symptoms do these bugs exhibit, and how are they distributed across frameworks and components?

### RQ3 — Root Cause–Symptom Relationship

How are different bug root causes associated with observed symptoms?

### RQ4 — Unique Challenges

How do bugs in LLM agent frameworks differ from traditional software bugs, and what software quality-assurance approaches may help address these challenges?

## Project Workflow

```text
Original Study
    |
    v
Methodology Review
    |
    v
Original Analysis Reproduction
    |
    v
Figure Reproduction
    |
    v
New Pull Request Collection
    |
    v
Manual Labeling
    |
    v
Data Preparation
    |
    v
Statistical Analysis
    |
    v
Comparison with Original Study
```

## Repository Structure

```text
Bugs_in_LLM_Frameworks_Reproduction/
│
├── reproduction/
│   ├── step2/
│   ├── step3/
│   └── step4_own_pr_analysis/
│
├── results/
│   ├── original_study_reproduction/
│   └── own_dataset_results/
│
├── reports/
│
├── requirements.txt
└── README.md
```

### `reproduction/`

Contains the scripts and files used to reproduce the analysis workflow.

### `results/original_study_reproduction/`

Contains figures generated during my reproduction of the original study.

These figures were produced independently by running the reproduction workflow and are not direct copies of the original authors' figures.

### `results/own_dataset_results/`

Contains analysis outputs generated from the newly collected and manually labeled dataset.

### `reports/`

Contains project reports, progress documentation, and related academic material.

## Data Collection

Bug-fixing pull requests were collected from selected LLM framework repositories.

The collected data includes information such as:

- Framework
- Pull Request ID
- Pull Request title
- GitHub URL
- Bug status
- Root cause
- Symptom
- Component
- Notes

## Manual Labeling

The collected pull requests were manually examined and classified using the taxonomy described in the original study.

Each included bug was labeled according to:

- Root Cause
- Symptom
- Software Component
- Framework

The labeling process was organized into multiple rounds.

## Independent Dataset

After filtering the manually labeled pull requests, the current analysis dataset contains:

```text
205 included bug-fixing pull requests
```

Framework distribution:

```text
LlamaIndex    143
Haystack       60
LangChain       2
```

## Analysis

The analysis includes:

- root cause distribution across frameworks,
- root cause distribution across components,
- symptom distribution across frameworks,
- symptom distribution across components,
- root cause–symptom relationships.

Both raw-count and normalized distributions were generated where applicable.

## Reproduced Results

The project reproduces analysis corresponding to major figures from the original study, including:

- Root cause distribution across frameworks
- Root cause distribution across components
- Symptom distribution across frameworks
- Symptom distribution across components
- Relationship between root causes and symptoms

The same analysis workflow is then applied to the independently collected dataset.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- OpenPyXL
- Git
- GitHub

## Installation

Create a virtual environment:

```powershell
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install the dependencies:

```powershell
pip install -r requirements.txt
```

## Running the Analysis

Navigate to the analysis directory:

```powershell
cd reproduction\step4_own_pr_analysis
```

Run the analysis scripts:

```powershell
python rq1_component.py
python rq1_framework.py
python rq2_component.py
python rq2_framework.py
python rq3_cause_symptom.py
```

## Original Research and Attribution

This repository is an independent academic reproduction and extension of the study:

**A Characterization Study of Bugs in LLM Agent Workflow Orchestration Frameworks**

Original repository:

https://github.com/security-pride/Bugs_in_LLM_Frameworks

The original repository does not currently provide an explicit software license. Therefore, the original authors' source files, datasets, and artifacts are not redistributed in this repository.

The methodology, taxonomy, and original findings belong to the respective authors.

This repository contains my own reproduction workflow, independently generated results, manually labeled data, analysis scripts, figures, and project documentation.

## Academic Purpose

This repository was created for academic research and reproducibility purposes as part of a graduate engineering project.