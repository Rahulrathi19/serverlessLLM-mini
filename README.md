\# ServerlessLLM Mini Implementation



This project is a simplified implementation of the ServerlessLLM research paper.



Features:

\- Multi-tier storage simulation (RAM / SSD / Remote)

\- Startup-time optimized scheduler

\- Token-based live migration

\- Continued inference after migration

\- Chunk-based loading

\- Parallel loading

\- Performance comparison



\## Run



Install dependencies:



python -m pip install -r requirements.txt



Start server2:



python -m uvicorn server2:app --reload --port 8001



Run main flow:



python main.py



Run comparison:



python comparison\_real.py



Run graph:



python graph.py

