# statista-data-analysis
Retrieve insights from Statista and display via webpage

## Quickstart - Prerequisites

Install these libraries with peer dependencies:
Create an accout with https://www.statista.com
Request API key access here: https://www.statista.com/1/request/custom-solution/1/form/corporate 

```pip
python -m pip install flask flask-cors requests matplotlib pandas matplotlib python-dotenv 
```
Create the following directory structure:
Then, import and use individual components as reuqired: 
git clone https://github.com/yoostuff/statista-data-analysis.git

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

Install dependencies, see pre-requisites above
Run the Flask application (python app.py).
Open the app in your browser (http://127.0.0.1:5000).
Select a category, chart type, and optional premium content, then analyze or download the data.
This updated frontend should integrate seamlessly with the enhanced app.py backend. Let me know if you need additional updates or styling changes!

## License

[MIT Licensed](LICENSE)
Copyright (c) 2020 Jeremy Ayerst

