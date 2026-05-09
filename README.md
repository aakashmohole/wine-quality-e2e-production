# 🍷 End-to-End Wine Quality Prediction Pipeline

An end-to-end machine learning project to predict the quality of wine based on its chemical properties. This project demonstrates a production-ready ML pipeline, complete with data ingestion, validation, transformation, model training, evaluation, experiment tracking, and a containerized web application.

---

## 🚀 Project Overview

The goal of this project is to build an automated machine learning pipeline that ingests raw wine data, preprocesses it, trains an **ElasticNet** regression model, and serves predictions via a beautiful, modern web interface. 

The pipeline is fully modular, adhering to MLOps best practices, and integrates with **MLflow** (hosted on DagsHub) for comprehensive experiment tracking and model registry.

---

## 🔄 Development Workflow

This project is built following a strict MLOps workflow, divided into a clear Machine Learning Pipeline and Development Steps:

### ML Pipeline Stages
1. **Data Ingestion:** Fetch and load raw data from the source.
2. **Data Validation:** Check data against the expected schema defined in `schema.yaml`.
3. **Data Transformation:** Preprocess and prepare data for modeling.
4. **Model Trainer:** Train the ElasticNet regression model.
5. **Model Evaluation:** Evaluate the model and log metrics/models to MLflow.

### Implementation Steps
To build or modify a pipeline component, follow this sequential workflow:
1. Update `config.yaml` (info about source data and URLs for extraction).
2. Update `schema.yaml` (used for data validation).
3. Update `params.yaml` (used for model hyperparameters).
4. Update the `entity` (dataclasses defining return types).
5. Update the `configuration manager` in `src/config`.
6. Update `components` (the actual logic for the pipeline stage).
7. Update `pipeline` (orchestrating the component).
8. Update `main.py` (triggering the pipeline).

---

## 🛠️ Technologies Used

| Technology | Purpose |
| :--- | :--- |
| **Python 3.9** | Core programming language |
| **Scikit-Learn** | Machine learning modeling (ElasticNet regression) |
| **Pandas & NumPy** | Data manipulation and numerical computations |
| **MLflow & DagsHub** | Experiment tracking, metric logging, and model registry |
| **Flask** | Backend web server and API routing |
| **HTML/CSS & Three.js** | Premium glassmorphism UI with 3D animated backgrounds |
| **Docker** | Application containerization for seamless deployment |

---

## 📂 Project Structure

```text
wine-quality-e2e-production/
├── artifacts/             # Generated artifacts (data, models, metrics)
├── config/                # Configuration files (config.yaml)
├── research/              # Jupyter notebooks for experimentation
├── src/wine_quality_project/ # Core package
│   ├── components/        # Individual pipeline stages (Ingestion, Validation, etc.)
│   ├── config/            # Configuration managers
│   ├── constants/         # Static path definitions
│   ├── entity/            # Dataclasses defining configuration structures
│   ├── pipeline/          # Orchestration of components
│   └── utils/             # Helper functions (e.g., read_yaml, save_json)
├── templates/             # HTML templates for the Flask application
│   ├── index.html         # Predictor form with 3D UI
│   └── results.html       # Prediction results view
├── app.py                 # Flask web application entry point
├── main.py                # Pipeline execution script
├── Dockerfile             # Docker image configuration
├── requirements.txt       # Python dependencies
├── schema.yaml            # Data schema definitions for validation
├── params.yaml            # Model hyperparameters
└── workflow.md            # Development workflow and steps
```

---

## ⚙️ Setup & Installation (Local)

1. **Clone the repository:**
   ```bash
   git clone https://github.com/aakashmohole/wine-quality-e2e-production.git
   cd wine-quality-e2e-production
   ```

2. **Create a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the ML Pipeline (Optional):**
   This will execute the entire pipeline (Ingestion -> Evaluation) and save the trained model locally.
   ```bash
   python main.py
   ```

5. **Start the Web Application:**
   ```bash
   python app.py
   ```
   Open your browser and navigate to `http://localhost:8080`.

---

## 🐳 Docker Deployment

The application is fully containerized. You can run the web application without needing to install Python or any dependencies on your host machine.

1. **Build the Docker image:**
   ```bash
   docker build -t wine-quality-app .
   ```

2. **Run the Docker container:**
   ```bash
   docker run -p 8080:8080 wine-quality-app
   ```

3. Access the web interface at `http://localhost:8080`.

---

## 📊 MLflow Integration

This project uses **MLflow** for experiment tracking. Metrics (RMSE, MAE, R2 Score) and model parameters are logged automatically to a remote DagsHub MLflow server.

To view the experiments, ensure your MLflow environment variables are set correctly (as defined in the code):
- `MLFLOW_TRACKING_URI`
- `MLFLOW_TRACKING_USERNAME`
- `MLFLOW_TRACKING_PASSWORD`

---

## 🧪 Web UI

The project features a **premium glassmorphism web interface** with a dynamic 3D floating particle background built using Three.js. 
- **`/` (GET):** The beautiful form to input the 11 chemical properties of the wine.
- **`/predict` (POST):** Processes the input, feeds it to the trained model, and seamlessly navigates to the result page.
- **`/train` (GET):** A trigger to retrain the ML pipeline (`main.py`) directly from the web interface.
