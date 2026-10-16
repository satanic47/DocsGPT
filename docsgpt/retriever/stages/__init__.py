"""Post-retrieval stages applied by the Dispatcher or post-retrieval pipelines."""

from docsgpt.retriever.stages.boilerplate_pruning import prune_boilerplate

__all__ = ["prune_boilerplate"]
