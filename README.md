---

# AI SQL Query Generator

This repository provides an AI-powered tool for generating SQL queries from natural language questions, with a focus on schema-aware, context-restricted query generation. It leverages large language models (LLMs) and provides both a web interface (via Streamlit) and supporting scripts for experimentation and database interaction.

---

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Setup & Installation](#setup--installation)
- [Usage](#usage)
  - [Web App](#web-app)
  - [Bonus Script](#bonus-script)
  - [Command-line Experiments](#command-line-experiments)
  - [Jupyter Notebook](#jupyter-notebook)
- [Model & Tokenizer](#model--tokenizer)
- [Data Files](#data-files)
- [Notes & Limitations](#notes--limitations)
---

## Features

- **Natural Language to SQL**: Converts user questions into SQL queries using an LLM (e.g., Gemma).
- **Schema Awareness**: Requires the user to input the database schema; the model is instructed to reject out-of-schema queries.
- **Streamlit Web UI**: User-friendly interface for schema and question input, and for displaying generated SQL.
- **Database Execution**: (Bonus) Optionally executes generated SQL on a local SQLite database and displays results.
- **Experimentation Scripts**: Includes scripts and a notebook for running and testing LLMs locally.

---

## Project Structure

```
SQL-Query-Generator/
│
├── app.py                  # Main Streamlit web app for SQL generation
├── bonus.py                # Streamlit app with database execution features
├── try2.py                 # Command-line and subprocess experiments with LLMs
├── try.ipynb               # Jupyter notebook for model/tokenizer experiments
│
├── abc.db                  # Example SQLite database
├── train.csv               # Training data (CSV)
├── test.csv                # Test data (CSV)
├── validation.csv          # Validation data (CSV)
├── wikisql_train.json      # WikiSQL training set (JSON)
├── wikisql_test.json       # WikiSQL test set (JSON)
├── wikisql_validation.json # WikiSQL validation set (JSON)
│
├── model_directory2/
│   ├── model/              # Model weights and configs (e.g., Gemma)
│   └── tokenizer/          # Tokenizer files and configs
│
└── README.md               # This file
```

---

## Setup & Installation

### Prerequisites

- Python 3.8+
- [Streamlit](https://streamlit.io/)
- [Requests](https://docs.python-requests.org/)
- [sqlite3](https://docs.python.org/3/library/sqlite3.html)
- (For LLM) [Ollama](https://ollama.com/) or compatible local LLM server
- (For notebook) `transformers`, `bitsandbytes`, `peft`, `trl`, `accelerate`, `datasets`, `torch`

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/SQL-Query-Generator.git
   cd SQL-Query-Generator
   ```

2. **Install dependencies:**
   ```bash
   pip install streamlit requests sqlite3
   # For notebook experiments:
   pip install bitsandbytes==0.42.0 peft==0.8.2 trl==0.7.10 accelerate==0.27.1 datasets==2.17.0 transformers==4.38.0 torch
   ```

3. **(Optional) Set up Ollama or your LLM server:**
   - Ensure the LLM (e.g., Gemma) is running and accessible at `http://localhost:11434/api/generate`.

---

## Usage

### Web App

Run the main Streamlit app:
```bash
streamlit run app.py
```
- Enter your database schema (e.g., table definitions).
- Enter your natural language question.
- The app will generate an SQL query using the LLM and display it.

### Bonus Script

Run the bonus app for SQL generation **and execution**:
```bash
streamlit run bonus.py
```
- In addition to generating SQL, this script will attempt to execute the query on `abc.db` and display the results.

### Command-line Experiments

`try2.py` contains various experiments for running LLMs via subprocess and PowerShell. You can run it directly:
```bash
python try2.py
```
- It demonstrates how to interact with the LLM from the command line and process outputs.

### Jupyter Notebook

`try.ipynb` provides a playground for loading, quantizing, and running LLMs (e.g., Gemma) using HuggingFace Transformers and related libraries.

---

## Model & Tokenizer

- The `model_directory2/model/` and `model_directory2/tokenizer/` folders contain the model weights and tokenizer files, respectively.
- These are used for local inference in the notebook and can be adapted for other scripts.

---

## Data Files

- `abc.db`: Example SQLite database for query execution.
- `train.csv`, `test.csv`, `validation.csv`: Datasets for training, testing, and validation.
- `wikisql_train.json`, `wikisql_test.json`, `wikisql_validation.json`: WikiSQL datasets for more advanced experiments.

---

## Notes & Limitations

- **Schema Required**: The LLM is instructed to only answer questions within the provided schema. Out-of-schema queries are rejected.
- **No Explanation**: The model is prompted to return only SQL queries, not explanations.
- **Local LLM**: The system expects a local LLM server (e.g., via Ollama) running the Gemma model.
- **Database Safety**: The bonus script executes generated SQL on the database. Use with caution and only on test databases.
- **Model Files**: Model and tokenizer files are large and not included in the repo. Place your own compatible files in `model_directory2/`.
---

## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [Ollama](https://ollama.com/)
- [HuggingFace Transformers](https://huggingface.co/docs/transformers/index)
- [WikiSQL Dataset](https://github.com/salesforce/WikiSQL)

---

**For questions or contributions, please open an issue or pull request.**

---
