# Birthday Paradox Visualization

**Version 1.0**

## Description

An interactive web application that visualizes and explores the **Birthday Paradox** using graph theory and statistical analysis. The Birthday Paradox demonstrates that in a group of just 23 people, there's over a 50% chance that two people share the same birthday - a counterintuitive result that surprises most people.

### Key Features

- **Interactive Graph Visualization**: See people as nodes and shared birthdays as edges in real-time
- **Probability Curve**: Visual representation of how probability increases with group size
- **Statistical Analysis**: Live calculations showing theoretical vs. actual birthday matches
- **Adjustable Population**: Slider to explore groups from 2 to 366 people
- **Dockerized Deployment**: Easy setup with Docker and Docker Compose

### Goals

- Demonstrate the Birthday Paradox through interactive visualization
- Provide educational insights into probability theory and graph theory
- Showcase real-time data generation and analysis using Python
- Offer a clean, intuitive UI built with Streamlit

---

## Project Structure

```
graph-project/
├── app.py                      # Main Streamlit application
├── processors/
│   └── processors.py           # Core logic for graph creation and probability calculations
├── requirements.txt            # Python dependencies
├── Dockerfile                  # Docker image definition
├── docker-compose.yml          # Docker Compose configuration
└── README.md                  # README
```

---

## Installation & Usage

### Option 1: Local Development

**Prerequisites:**
- Python 3.11 or higher
- pip package manager

**Steps:**

1. Clone the repository:
```shell
git clone <repository-url>
cd graph-project
```

2. Install dependencies:
```shell
pip install -r requirements.txt
```

3. Run the application:
```shell
streamlit run app.py
```

4. Open your browser to `http://localhost:8501`

---

### Option 2: Docker

**Prerequisites:**
- Docker
- Docker Compose (for Option 2B)

#### Option 2A: Using Dockerfile Directly

Build and run using Docker commands directly:

```shell
# Build the image
docker build -t vizapp:dev .

# Run the container
docker run -p 8501:8501 vizapp:dev
```

**When to use:** Simple deployment, CI/CD pipelines, or when you only need the basic container without orchestration.

#### Option 2B: Using Docker Compose (Recommended)

Build and run using Docker Compose for easier management:

```shell
# Build and run in one command
docker compose up --build

# Stop the application
docker compose down
```

**When to use:** Local development, when you need easy container management, or when the project grows to include multiple services (databases, caches, etc.).

**Key Differences:**
- **Dockerfile**: Defines *how* to build a single container image
- **Docker Compose**: Orchestrates *running* one or more containers with configuration (ports, volumes, networks)
- **Docker Compose Benefits**:
  - Easier port mapping management
  - Simple start/stop with `up`/`down`
  - Better for multi-service applications
  - Configuration stored in `docker-compose.yml`

**Docker Compose Commands Reference:**
```shell
# Build the image only
docker compose build

# Run in detached mode (background)
docker compose up -d

# View logs
docker compose logs -f

# Rebuild and run
docker compose up --build
```

**Access the application:**
Open your browser to `http://localhost:8501`

---

## Environment Variables

This application does not require any environment variables or secrets. All configuration is handled through the Streamlit interface.

---

## Dependencies

```txt
streamlit==1.45.1
networkx==3.4.2
plotly==6.1.2
matplotlib==3.10.3
```

Additional Python standard library modules used:
- `collections` (Counter, defaultdict)
- `itertools` (combinations)
- `random` (birthday generation)
- `calendar` (month/day validation)
- `decimal` (high-precision probability calculations)
- `datetime` (date handling)

---

## How It Works

### 1. Population Generation
Random birthdays are generated for the specified number of people (2-366) in `MM_DD` format using `random_birthday()`.

### 2. Graph Construction
Each person becomes a **node** in the graph. **Edges** connect people who share the same birthday, creating clusters of birthday matches.

### 3. Visualization
- **Network Graph**: Shows the social network of birthday connections
  - Node color intensity = number of connections
  - Hover shows person ID and birthday

- **Probability Curve**: Displays the theoretical probability curve
  - X-axis: Number of people (2-366)
  - Y-axis: Probability of at least one match (0-1)
  - White marker: Current selection

### 4. Statistical Analysis
Real-time calculations show:
- Theoretical probability (calculated mathematically)
- Actual matches in the generated population
- Percentage of people with shared birthdays

---

## Key Functions

### `processors/processors.py`

| Function | Purpose |
|----------|---------|
| `random_birthday()` | Generates a random birthday in `MM_DD` format for 2025 (non-leap year) |
| `generate_population(num)` | Creates a list of random birthdays for the population |
| `create_graph(population)` | Creates the graph from the population data |
| `birthday_paradox_prob(num)` | Calculates theoretical probability with high precision |
| `birthday_paradox_plot(num)` | Returns probability value for plotting |
| `calculate_prob(population)` | Analyzes actual birthday sharing statistics |

---

## The Birthday Paradox Explained

The Birthday Paradox asks: **How many people do you need in a room before there's a 50% chance that two share the same birthday?**

Most people guess around 183 (half of 365), but the answer is just **23 people**!

### Why?

The key insight is that we're not looking for someone to match *your* birthday - we're looking for *any two people* to match.

- With 23 people, there are **253 possible pairs**: $\binom{23}{2}$
- Each pair has a 1/365 chance of matching
- The probability compounds quickly

### Mathematical Formula

P(at least one match) = 1 - P(all unique birthdays)

P(all unique) = (365/365) $\times$ (364/365) $\times$ (363/365) $\times$ ... $\times$ ((365-n+1)/365)

**For n = 23 people**: The probability of at least one shared birthday is **50.7%**

---

## Screenshots


---

## Documentation & Resources

- [Streamlit Documentation](https://docs.streamlit.io/)
- [NetworkX Documentation](https://networkx.org/documentation/stable/)
- [Plotly Python Documentation](https://plotly.com/python/)
- [Birthday Paradox (Wikipedia)](https://en.wikipedia.org/wiki/Birthday_problem)

---

## Author

*Christopher Andrews*

---

## Acknowledgments

Built with:
- Streamlit for the web framework
- NetworkX for graph algorithms
- Plotly for interactive visualizations

