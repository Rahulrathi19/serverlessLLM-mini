# ServerlessLLM Mini Implementation

This project is a simplified implementation of the ServerlessLLM research paper. The goal is to simulate how large language models can be loaded, migrated, and executed efficiently in a serverless environment.

## Features

* Multi-tier storage simulation:

  * RAM
  * SSD
  * Remote storage
* Startup-time optimized scheduler
* Token-based live migration
* Continued inference after migration
* Chunk-based model loading
* Parallel loading for faster startup
* Performance comparison between approaches
* Dataset-based testing using `dataset_test.py`
* Checkpoint loading support

---

## Project Structure

```text
project/
│
├── main.py                    # Main ServerlessLLM execution flow
├── server2.py                 # Secondary server used for migration
├── comparison_real.py         # Compares different loading strategies
├── graph.py                   # Generates performance graphs
├── dataset_test.py            # Runs model on dataset queries
├── model.py                   # Model loading and inference logic
├── scheduler.py               # Startup-time optimized scheduler
├── migration.py               # Token-based live migration
├── storage.py                 # RAM / SSD / Remote storage simulation
├── checkpoints/               # Saved model checkpoints
├── datasets/                  # Dataset files for testing
├── outputs/                   # Predictions and results
├── results/                   # Graphs and screenshots
└── README.md
```

---

## Installation

Install the required dependencies:

```bash
python -m pip install -r requirements.txt
```

---

## Running the Project

### 1. Start Server 2

This server is used during token-based migration.

```bash
python -m uvicorn server2:app --reload --port 8001
```

### 2. Run Main Flow

Runs the complete ServerlessLLM simulation including loading, scheduling, migration, and inference.

```bash
python main.py
```

### 3. Run Dataset Testing

Test the model using a dataset of queries.

```bash
python dataset_test.py \
    --model checkpoints/model.pt \
    --dataset datasets/test.json
```

### 4. Run Comparison

Compare startup time and loading strategy performance.

```bash
python comparison_real.py
```

### 5. Generate Graphs

```bash
python graph.py
```

---

## Checkpoint Support

The project supports loading saved checkpoints so that the model does not need to be initialized from the beginning every time.

Example:

```python
checkpoint = torch.load("checkpoints/model.pt")
model.load_state_dict(checkpoint["model_state_dict"])
```

To continue training later:

```python
optimizer.load_state_dict(checkpoint["optimizer_state_dict"])
start_epoch = checkpoint["epoch"]
```

---

## Dataset Format

`dataset_test.py` expects a JSON dataset in the following format:

```json
[
  {
    "query": "What is cloud computing?",
    "expected": "Cloud computing means delivering..."
  },
  {
    "query": "Explain virtualization",
    "expected": "Virtualization is the process..."
  }
]
```

Generated outputs are saved in:

```text
outputs/results.json
```

Example output:

```json
[
  {
    "query": "What is cloud computing?",
    "prediction": "Cloud computing is..."
  }
]
```

---

## Model Used

Current experiments use a lightweight language model configured in `model.py`.

Example:

```python
MODEL_NAME = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
```

Other models that can be used later:

* Llama 2
* Mistral
* Phi-2
* Gemma

---

## Results

### Graph Output

![Graph](results/graph_output.png)

### Main Flow Output

![Main Output](results/main_output.png)

### Comparison Output

![Comparison](results/comparison_output.png)

---

## Current Progress

* Multi-tier storage simulation completed
* Scheduler implemented
* Token-based migration implemented
* Chunk-based and parallel loading completed
* Dataset testing script added
* Checkpoint loading added
* Performance comparison completed
* Graph generation completed

---

## Future Work

* Add more evaluation metrics
* Compare multiple models
* Measure inference latency in detail
* Add support for dynamic checkpoint selection
* Improve scheduler with real-time decision making
* Extend project toward full ServerlessLLM deployment
