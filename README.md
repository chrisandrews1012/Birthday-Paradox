# Birthday Paradox

An interactive app that visualizes the Birthday Paradox through graph theory and probability analysis.

## Overview

The Birthday Paradox shows that in a group of just 23 people, there's over a 50% chance two people share a birthday - a result that is very counterintuitive. This project models that problem as a graph and visualizes how the probability shifts as group size grows.

## Technical Highlights

- **NetworkX (Graph Theory)**: Constructs a graph where people are nodes and shared birthdays are edges, making the abstract probability problem concrete and traversable.
- **Plotly**: Renders interactive network graphs and probability curves, allowing real-time exploration of the data.
- **Streamlit**: Powers the frontend as a single-page data application.
- **Docker and Docker Compose**: Fully containerized for a consistent, one-command deployment.

## Features

- **Interactive Graph**: Watch nodes and edges form in real-time as shared birthdays are detected in the group.
- **Probability Curve**: See how the likelihood of a shared birthday climbs as group size increases.
- **Live Statistics**: Side-by-side comparison of theoretical probability vs. actual matches in the simulation.
- **Adjustable Group Size**: Explore any group from 2 to 366 people using an interactive slider.

## Project Structure

```
birthday-paradox/
├── app.py                  # Streamlit entry point
├── docker-compose.yml      # Service orchestration
├── Dockerfile              # Container definition
├── requirements.txt        # Dependencies
└── processors/
    ├── __init__.py
    └── processors.py       # Birthday generation and graph logic
```

## Getting Started

### Prerequisites

- [Docker](https://www.docker.com/) and Docker Compose (recommended)
- Python 3.11+ (if running locally)

### Docker (Recommended)

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/birthday-paradox.git
   cd birthday-paradox
   ```

2. Build and start the app:
   ```bash
   docker compose up --build
   ```

3. Visit `http://localhost:8501` in your browser.


## License

This project is licensed under the [MIT License](LICENSE).