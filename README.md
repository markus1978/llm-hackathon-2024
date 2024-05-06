Supplemental data and material for the LLM Hackathon 2024 Berlin on-site FAIRmat/NOMAD event.

## A yaml document with NOMAD's search keys and their documentation

NOMAD uses elastic search as a search engine. There are standard quantities that
we add to elastic search. Each quantity has a specific key that can be used
in our search API and each quantity comes with a bit of documentation.

[data/nomad_search_keys.yaml](data/nomad_search_keys.yaml) contains a dict of
these search keys. Here is an example:

```yaml
results.material.structural_type:
  description: Structural class determined from the atomic structure.
  repeats: false
  type:
  - bulk
  - surface
  - 2D
  - 1D
  - molecule / cluster
  - atom
  - unavailable
  - not processed
```

## Running the scripts yourself

```
python3 -m venv .pyenv
source ./.pyenv/bin/activate
pip install requirements.txt
```

```
python src/nomad_search_keys.py > data/nomad_search_keys.yaml
```