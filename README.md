# statista-data-analysis
Retrieve insights from Statista and display Line-or-Pie chart via webpage

## Quickstart - Pre-requisites

Download and Install Python (3.10 or above). Activate Virtual Environment and Install these libraries with peer dependencies:

```
python -m venv .venv 

python -m pip install flask flask-cors requests matplotlib pandas matplotlib python-dotenv 
```

Create the following directory structure. Then, import and use individual components as required: 
- git clone https://github.com/yoostuff/statista-data-analysis.git

```pip
statista/
├── app.py
├── .venv
├── .env
├── .gitignore
├── statista-project-structure
├── templates/
│   └── index.html
├── nppBackup/
│   └── app.py.2024-11-22_115328.bak
├── charts/  # Will store generated charts

```

## How to Use

Run the Flask application (python app.py).
Open the app in your browser (http://127.0.0.1:5000).
Select a category, chart type, and optional premium content, then analyze or download the data.
The updated frontend should integrate seamlessly with the enhanced app.py backend. Style as per your desire!

## Request API Access:

- Create an accout with Statista <a href="https://www.statista.com">here</a>
- Request API key access <a href="https://www.statista.com/1/request/custom-solution/1/form/corporate">here:</a>

## Visualize your Code:

- Use <a href="https://codetoflow.com/">Code to Flowchart</a> to Visualize, Analyze, and Understand Your Code!
