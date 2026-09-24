from crewai import Memory


def get_memory():
    """
    Create persistent CrewAI memory.
    """

    memory = Memory(
        storage="./.crewai/memory",
        embedder={
            "provider": "sentence-transformer",
            "config": {
                "model_name": "all-MiniLM-L6-v2"
            },
        },
    )

    return memory
