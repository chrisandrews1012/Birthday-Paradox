# Birthday Paradox Visualization

An interactive web application that visualizes and explores the **Birthday Paradox** using graph theory and statistical analysis. The Birthday Paradox demonstrates that in a group of just 23 people, there's over a 50% chance that two people share the same birthday - a counterintuitive result that surprises most people.

## Technical Highlights

*   **Interactive UI**: Built with **Streamlit** to create a responsive data application.
*   **Graph Theory**: Leverages **NetworkX** to dynamically build graphs representing social networks of birthday connections.
*   **Data Visualization**: Uses **Plotly** to render interactive network graphs and probability curves.
*   **Containerization**: Easily deployable using **Docker** and Docker Compose.

## Features

*   **Interactive Graph Visualization**: See people as nodes and shared birthdays as edges in real-time.
*   **Probability Curve**: Visual representation of how probability increases with group size.
*   **Statistical Analysis**: Live calculations showing theoretical vs. actual birthday matches.
*   **Adjustable Population**: Explore groups from 2 to 366 people via an interactive slider.

## Getting Started

### Prerequisites

*   Docker and Docker Compose (Recommended)
*   Python 3.11+ (if running locally without Docker)

### Installation (Docker - Recommended)

1.  Clone the repository:
    ```bash
    git clone https://github.com/your-username/birthday-paradox.git
    cd Birthday-Paradox
    ```
2.  Build and start the application using Docker Compose:
    ```bash
    docker compose up --build
    ```
3.  The application will open in your default browser at `http://localhost:8501`.

### Local Development (Without Docker)

1.  Ensure you have Python 3.11+ installed.
2.  Create a virtual environment and install dependencies:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use: venv\Scripts\activate
    pip install -r requirements.txt
    ```
3.  Start the Streamlit development server:
    ```bash
    streamlit run app.py
    ```

## License

This project is licensed under the MIT License.