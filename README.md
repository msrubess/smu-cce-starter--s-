# Cloud Computing for Economics: Starter Repo

This repository contains the starter code and lesson materials for building a Python financial-data application and deploying it to AWS.

Students will use GitHub Codespaces, Python, Jupyter notebooks, Streamlit, Git, and AWS CloudFormation.

## Learning outcomes

By the end of the course, you will be able to:

1. Build and deploy an analytics application with a simple front end and back end.
2. Host and share the application on a cloud platform so others can access it securely over the web.
3. Integrate data sources and APIs into the app to enable interactive, real-time analytics.
4. Apply cloud architecture best practices, ensuring the app demonstrates scalability and performance.
5. Showcase your work on GitHub as part of a portfolio of cloud and analytics projects.

## Repository structure

```text
.
├── lessons/          # Step-by-step course instructions
├── notebooks/        # Starter financial-data notebooks
├── src/              # Streamlit app and analysis logic
├── requirements.txt  # Python dependencies
├── README.md         # Course overview
└── .gitignore        # Standard Git ignore file
```

## Streamlit app

This project includes a simple student-friendly stock analysis app that reads the logic from the notebook examples in the `notebooks/` folder and turns it into reusable Python functions.

### App files

- `src/analysis.py` contains reusable functions for:
  - current price lookup
  - analyst recommendations
  - company financial statements
  - recent company news
- `src/app.py` contains the Streamlit UI for entering a ticker and choosing an analysis type.

### Run the app locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run src/app.py
```

### Example workflow

1. Enter a ticker such as `AAPL` or `MSFT`.
2. Choose one of these analysis types:
   - `filings`
   - `news`
   - `stock price ratings`
3. Click `Run`.
4. Review the output in the Streamlit dashboard.

## Notes

The app is intentionally simple and designed for students learning how to move logic from notebooks into a real Python application structure.