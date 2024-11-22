# statista-data-analysis
Retrieve insights from Statista and display via webpage

## Quickstart
## Prerequisites 

Install these libraries with peer dependencies:

```bash
python -m pip install flask flask-cors requests matplotlib pandas matplotlib python-dotenv 
```

Create the following directory structure:

Then, import and use individual components:

```jsx
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

#How to Use
Replace the existing index.html file in the templates/ directory with this updated version.
Run the Flask application (python app.py).
Open the app in your browser (http://127.0.0.1:5000).
Select a category, chart type, and optional premium content, then analyze or download the data.
This updated frontend should integrate seamlessly with the enhanced app.py backend. Let me know if you need additional updates or styling changes!

<br />

[![supported by Cube](https://user-images.githubusercontent.com/986756/154330861-d79ab8ec-aacb-4af8-9e17-1b28f1eccb01.svg)](https://cube.dev/?ref=eco-react-chartjs)

## Docs

- [Migration to v4](https://react-chartjs-2.js.org/docs/migration-to-v4)
- [Working with datasets](https://react-chartjs-2.js.org/docs/working-with-datasets)
- [Working with events](https://react-chartjs-2.js.org/docs/working-with-events)
- [FAQ](https://react-chartjs-2.js.org/faq)
- [Components](https://react-chartjs-2.js.org/components)
- [Examples](https://react-chartjs-2.js.org/examples)

## License

[MIT Licensed](LICENSE)
Copyright (c) 2020 Jeremy Ayerst

