# NEXUS
### Social Network Analysis & Intelligence Platform

**Mapping the dynamics of online communities.**

NEXUS is an open-source social network analysis platform designed to explore how online communities form, interact, and evolve around shared topics.

By combining graph theory, network science, natural language processing, and AI, NEXUS transforms social interactions and conversations into an interactive analytical environment.

Starting with data collected from **Bluesky**, the platform enables users to investigate social structures, identify influential actors, detect emerging communities, and understand how topics spread across online networks.

---

## Table of Contents

- [Vision](#vision)
- [Key Features](#key-features)
- [How It Works](#how-it-works)
- [Architecture](#architecture)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Development Roadmap](#development-roadmap)
- [Data Sources & Ethics](#data-sources--ethics)

---

## Vision

Online social networks generate enormous amounts of interconnected data. Behind individual posts and interactions lie complex structures: communities, influential actors, shared interests, and information flows.

NEXUS aims to make these structures observable and explorable.

The platform brings together two complementary analytical perspectives:

### 1. Social Network Analysis

Understanding the structure of interactions between users.

- How are users connected?
- Which communities emerge from interaction patterns?
- Who occupies central positions in the network?
- Which users connect otherwise disconnected communities?

### 2. Semantic & Temporal Analysis

Understanding the content and evolution of online conversations.

- What topics are being discussed?
- Which topics are gaining traction?
- How do different communities approach the same subject?
- How do discussions and community structures evolve over time?

By combining these perspectives, NEXUS aims to provide a deeper understanding of online social dynamics.

## Key Features

### 1. Data Ingestion & Discovery

Collect and structure public social network data from Bluesky to discover emerging topics and conversations without requiring users to define search keywords in advance.

Users can configure an observation scope through:

- **Geographic scope:** Global or selected geographic areas, where sufficient location information is available.
- **Broad categories:** Technology, Health, Sports, Politics, Science, Entertainment, and other general domains.
- **Temporal scope:** Recent activity, daily trends, or longer observation periods.

The platform then:

- Collects public posts through available Bluesky data streams, feeds, and APIs.
- Normalizes users, posts, timestamps, and interaction metadata.
- Identifies recurring subjects and extracts candidate topics.
- Groups semantically related conversations.
- Tracks topic frequency, growth, and temporal evolution.
- Identifies emerging topics within the observed dataset.

The objective is to let users discover what people are discussing before deciding which topics or communities they want to investigate further.

*Important: Trending topics represent activity within the collected dataset, not necessarily the entirety of Bluesky. Geographic classification is subject to data availability and confidence.*

### 2. Network Analysis

Construct and analyse directed, weighted interaction graphs.

- Graph construction and exploration.
- Network density and connected components.
- Degree and betweenness centrality.
- PageRank and structural importance.
- Community detection using Leiden.
- Community structure and distribution analysis.

### 3. Community Intelligence

Identify and compare groups of users based on their interactions.

- Automatic community detection.
- Community size and density.
- Dominant topics within communities.
- Identification of bridge users.
- Comparison of community structures and interests.

### 4. Topic Analysis

Extract semantic information from social media conversations.

- Text preprocessing and embedding generation.
- Semantic clustering and topic extraction.
- Topic distribution across communities.
- Similarity analysis between topics and communities.
- Optional sentiment analysis.

### 5. Temporal Analysis

Study how network structures and conversations evolve.

- User activity over time.
- Topic popularity and growth.
- Community activity evolution.
- Emerging and declining topics.
- Changes in network structure across analysis periods.

### 6. AI Research Assistant

Explore analytical results through natural language.

- Ask questions about network structures and communities.
- Investigate emerging topics and trends.
- Compare communities and their interests.
- Generate summaries grounded in analytical results.
- Retrieve supporting posts and metrics.

*The AI assistant is planned for a later development phase.*

## How It Works

NEXUS follows a data-to-insights workflow:

1. **Collect:** Retrieve public posts and available interaction data from Bluesky.
2. **Normalize:** Transform raw records into a consistent internal data model.
3. **Construct:** Build social interaction graphs and semantic representations.
4. **Analyse:** Apply graph algorithms, community detection, and NLP techniques.
5. **Explore:** Visualize analytical results through an interactive web application.
6. **Investigate:** Use AI-assisted exploration to investigate patterns and relationships.

## Architecture

NEXUS follows a modular monolithic architecture, separating the frontend, backend, data processing pipeline, and analytical components.

```text
                    NEXUS PLATFORM
                          |
          +---------------+---------------+
          |                               |
     FRONTEND                         BACKEND
   React + TypeScript                  FastAPI
          |                               |
   +------+------+                +-------+-------+
   |             |                |               |
Graph UI     Analytics UI      REST API       Application
Sigma.js     ECharts           Endpoints       Services
   |             |                |               |
   +-------------+----------------+---------------+
                                   |
                            PostgreSQL
                                   |
                         Background Processing
                                   |
                         +---------+---------+
                         |                   |
                   Network Analysis     Topic Analysis
                   NetworkX / igraph    Sentence Transformers
                   Leiden               Embeddings
                         |                   |
                         +---------+---------+
                                   |
                           Analysis Results
```

### Main Components

| Component | Responsibility |
|---|---|
| Frontend | Interactive application and data visualization |
| API | Communication between frontend and backend |
| Ingestion | Bluesky data collection and normalization |
| Network Analysis | Graph construction and network metrics |
| Topic Analysis | Semantic processing and topic extraction |
| Temporal Analysis | Evolution of communities and topics |
| Database | Persistent storage of datasets and results |
| Background Workers | Asynchronous ingestion and analysis tasks |

### Architectural Principles

- **Separation of concerns:** Independent analytical modules and application layers.
- **Reproducibility:** Each analysis run records its dataset snapshot, algorithms, and parameters.
- **Extensibility:** New data sources and analytical methods can be integrated without redesigning the entire application.
- **Testability:** Analytical logic is independent of HTTP endpoints and database implementation.
- **Scalability:** Background processing and graph sampling support larger datasets.

## Technology Stack

### Frontend

| Technology | Purpose |
|---|---|
| React | UI development |
| TypeScript | Static typing |
| Vite | Development and build tooling |
| Tailwind CSS | Styling |
| Sigma.js | Interactive graph visualization |
| Graphology | Graph data structures |
| Apache ECharts | Charts and temporal visualizations |

### Backend

| Technology | Purpose |
|---|---|
| Python | Core application and analytical logic |
| FastAPI | REST API |
| PostgreSQL | Relational database |
| SQLAlchemy | Database access |
| Alembic | Database migrations |
| Celery / Redis | Background processing |

### Data Science & AI

| Technology | Purpose |
|---|---|
| Pandas | Data processing |
| NetworkX / igraph | Network analysis |
| Leiden algorithm | Community detection |
| Sentence Transformers | Text embeddings |
| scikit-learn | Machine learning and clustering |
| pgvector | Vector storage and similarity search |

### Engineering & Deployment

| Technology | Purpose |
|---|---|
| Docker | Containerization |
| Docker Compose | Local development environment |
| Pytest | Backend testing |
| Vitest | Frontend testing |
| GitHub Actions | CI/CD |

## Project Structure

```text
nexus/
|
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── domains/
│   │   │   ├── datasets/
│   │   │   ├── ingestion/
│   │   │   ├── network_analysis/
│   │   │   ├── topic_analysis/
│   │   │   └── temporal_analysis/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── repositories/
│   │   ├── services/
│   │   ├── workers/
│   │   └── core/
│   ├── tests/
│   ├── alembic/
│   ├── poetry.lock
|   └── pyproject.toml      
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── app/
│   │   │   ├── layouts/
│   │   │   └── routes/
│   │   ├── features/
│   │   │   ├── dashboard/
│   │   │   ├── network-explorer/
│   │   │   ├── communities/
│   │   │   └── trends/
│   │   ├── components/
│   │   │   ├── ui/
│   │   │   └── layout/
│   │   ├── hooks/
│   │   ├── services/
│   │   ├── types/
│   │   ├── utils/
│   │   ├── assets/
│   │   ├── App.tsx
│   │   ├── index.css
│   │   └── main.tsx
│   ├── eslint.config.js
│   ├── index.html
│   ├── package.json
│   ├── package-lock.json
│   ├── tsconfig.json
│   ├── tsconfig.app.json
│   ├── tsconfig.node.json
│   └── vite.config.ts
│
├── docs/
│
├── .gitignore
├── .gitattributes
├── docker-compose.yml
├── .env.example
└── README.md
```

## Getting Started

### Prerequisites

Make sure the following tools are installed:

- Git
- Python 3.12+
- Node.js (LTS)
- npm
- Docker and Docker Compose

### 1. Clone the repository

```bash
git clone https://github.com/ramahars/nexus.git
cd nexus
```

### 2. Configure environment variables

Create a local environment file.

Configure the required environment variables.

Example:

```env
DATABASE_URL=postgresql+psycopg://nexus:nexus@localhost:5432/nexus
REDIS_URL=redis://localhost:6379/0
BLUESKY_IDENTIFIER=
BLUESKY_APP_PASSWORD=
```

Bluesky credentials should be supplied only when required by the selected API operations. Never commit credentials or `.env` files.

### 3. Start infrastructure

```bash
docker compose up -d db redis
```

### 4. Start the backend

```bash
cd backend
```

Install dependencies:

```bash
pip install -e ".[dev]"
```

Start the development server:

```bash
uvicorn app.main:app --reload
```

Backend API documentation:

`http://localhost:8000/docs`

### 5. Start the frontend

In a separate terminal:

```bash
cd frontend
npm install
npm run dev
```

The frontend will be available at:

`http://localhost:5173`

*Note: The commands above describe the intended development environment. Individual services and dependencies will become available progressively as the project is implemented.*

## Development Roadmap

| Phase | Milestone | Status |
|---|---|---|
| 1 | Project initialization and frontend foundation | Done |
| 2 | Backend API and database setup | Planned |
| 3 | Bluesky data ingestion | Planned |
| 4 | Graph construction and network metrics | Planned |
| 5 | Community detection and graph explorer | Planned |
| 6 | Topic extraction and semantic analysis | Planned |
| 7 | Temporal analysis | Planned |
| 8 | AI research assistant | Planned |
| 9 | Testing, deployment and documentation | Planned |

## Data Sources & Ethics

NEXUS initially uses public data from Bluesky and its AT Protocol ecosystem.

The project is intended for research, educational, and analytical purposes.

Data collection and processing must respect:

- Bluesky and AT Protocol terms and API policies.
- Applicable privacy and data protection regulations, including GDPR.
- Data minimization and retention principles.
- User privacy and responsible interpretation of network metrics.

Network centrality should not automatically be interpreted as real-world influence. Community detection results depend on graph construction choices, collection boundaries, and algorithm parameters.

NEXUS aims to make these assumptions explicit and preserve the context behind its analytical results.

---

## License

To be defined.