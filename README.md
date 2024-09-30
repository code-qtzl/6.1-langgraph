# Week 6.1: LangGraph

## Introduction
LangGraph is a library for building stateful, multi-actor applications with LLMs, inspired by Pregel and Apache Beam. It allows coordination and checkpointing of multiple chains (or actors) using Python or JS, with a public interface inspired by NetworkX.

## Slides

[Slides](https://docs.google.com/presentation/d/1QQC4T1q-JoYLlZc781xeUm411ZbJ0eBXY1xMvYH1SX4/edit?usp=sharing)

## Prerequisites
Before you begin, ensure you have met the following requirements:
- Docker
- Python 3.11.0 or greater (local setup)


### Set up environment variables:
- Copy the sample environment file:
  ```bash
  cp .env.sample .env
  ```
- Edit the `.env` file and add your Hugging Face token:
  ```
    OPENAI_API_KEY=your-openai-key
    LANGCHAIN_API_KEY=your-langchain-key
    LANGCHAIN_TRACING_V2=true
    LANGCHAIN_PROJECT=langgraph
    TAVILY_API_KEY=your-tavily-key
  ```
## Docker (not recommended for most local hardware: recommended to use a cloud GPU)
1. Run the py file with Docker Compose:
   ```
   docker compose run --rm main
   ```
2. Start Jupyter to run the .ipynbfiles as local notebooks (best way to run the notebooks)
   ```
   docker compose up jupyter
   ```
3. Run a specific script (any new `.py` file you may add):
   ```
   docker compose run --rm main python <script_name.py>
   ```

## Running Different Scripts
You can use the provided `run.sh` script for easier execution.
Make sure to make the script executable with `chmod +x run.sh` in the CLI before using:
```bash
./run.sh jupyter
./run.sh <your_new_py_file>
```
## Local Setup (Alternative to Docker)
If you prefer to run the examples locally:

1. Ensure you have Python 3.11.0 or higher installed.
2. Clone the repository:
    ```bash
    git clone [repository-url]
    cd [repository-name]
    ```
3. Set up the virtual environment:
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    pip install -r requirements.txt
    ```
4. Configure environment variables as described in the Setup section.
5. Export your `.env` variables to the system (python-dotenv should handle this for you in the main `.ipynb` file, but this is included for reference):
   **Linux / Mac / Bash**
      ```bash
      export $(grep -v '^#' .env | xargs)
      ```
5. Run the notebook:
    ```
    run the ipynb file in VSCode (it will prompt you to allow the installation of ipykernel: do so)
    ```
## Need Help?
Reach out to the course instructor or learning assistant