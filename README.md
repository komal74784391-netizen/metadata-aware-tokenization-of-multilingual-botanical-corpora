# metadata-aware-tokenization-of-multilingual-botanical-corpora

This repository contains the complete implementation of the paper
**Metadata Aware Tokenization of Multilingual Botanical Corpora**, accepted at Computational Linguistics Review 2026.

## Components

- `src/` — reference implementation used to produce the published results
- `requirements.txt` — pinned dependencies
- `scripts/` — command line entry points

## Reproducing the results

```
pip install -r requirements.txt
python scripts/run_experiment.py --config configs/default.json
```

The released release tag `v1.0.0` corresponds to the camera-ready artefact.
