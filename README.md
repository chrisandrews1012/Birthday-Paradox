# Birthday Paradox

![GitHub last commit](https://img.shields.io/github/last-commit/chrisandrews1012/birthday-paradox)
![GitHub repo size](https://img.shields.io/github/repo-size/chrisandrews1012/birthday-paradox)
![Python Version](https://img.shields.io/badge/python-3.11-blue)
![Stack](https://img.shields.io/badge/stack-Streamlit%20%7C%20NetworkX%20%7C%20Plotly-blue)

Built to make the Birthday Paradox tangible — not just a formula, but something you can see.

## Problem Statement

The Birthday Paradox states that in a group of just 23 people, there is a greater than 50% chance that two share a birthday. Most people find this deeply counterintuitive. The challenge is making that result feel real rather than abstract: a probability on a page does not show you *why* it happens or *how fast* it compounds as a group grows.

## Approach

Each person in the simulated group is modeled as a node in an undirected graph, with edges drawn between any two people who share a birthday. That linkage structure makes the paradox visible — you can watch the network of shared birthdays form and densify as group size increases, rather than just reading a percentage.

Two visualizations run in parallel:

- **Network graph** (NetworkX + Plotly): renders the full group as a graph, with edges highlighting birthday matches. Node color encodes the number of connections, making clusters of shared birthdays immediately obvious.
- **Probability curve** (Plotly): plots the theoretical probability function across all group sizes from 2 to 366, with a live marker tracking the current selection.

Streamlit ties both together as an interactive single-page app with an adjustable slider.

## Results

| Group Size | Theoretical Probability of a Shared Birthday |
|---|---|
| 10 | ~11.7% |
| 23 | ~50.7% |
| 50 | ~97.0% |
| 70 | ~99.9% |

The graph visualization makes it clear why the probability climbs so fast: each new person added must be compared against *every* existing person, so the number of potential matches grows quadratically even as the group grows linearly.

## How to Run

```bash
git clone https://github.com/chrisandrews1012/birthday-paradox.git
cd birthday-paradox
uv sync
uv run streamlit run app.py
```

**Docker**

```bash
docker compose up --build
```

## File Structure

```
birthday-paradox/
├── app.py
├── docker-compose.yml
├── Dockerfile
├── pyproject.toml
├── data/
│   ├── external/
│   ├── interim/
│   ├── processed/
│   └── raw/
├── models/
├── notebooks/
├── reports/
│   └── figures/
└── src/
    └── birthday_paradox/
        ├── __init__.py
        └── processors.py
```

## License

This project is licensed under the [MIT License](LICENSE).
