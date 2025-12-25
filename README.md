# AI Agents Toolkit

## Overview
The **AI Agents Toolkit** is a collection of modular and intelligent agents designed to streamline workflows, automate tasks, and enhance decision-making processes. This project includes agents for handling weather data, managing Airbnb operations, and connecting to MCP systems, among other capabilities.

## Features
- **Multi-Agent System**: Collaborating agents for diverse tasks.
- **Weather Agent**: Fetch and process weather data.
- **Airbnb Agent**: Manage Airbnb operations and planning.
- **Host Agent**: Handle remote connections and routing.
- **MCP Integration**: Seamless connection to MCP systems.

## Project Structure
```
AI Agents Toolkit/
├── airbnb_planner_multiagent/
│   ├── airbnb_agent/
│   ├── host_agent/
│   ├── weather_agent/
│   ├── assets/
│   ├── pyproject.toml
│   ├── requirements.txt
│   └── README.md
├── databricks_a2a_mcp_connection-main/
└── ORG_Change_Escalation_Analysis.ipynb (ignored)
```

## Getting Started

### Prerequisites
- Python 3.8+
- Git
- Virtual Environment (optional but recommended)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/ai-agents-toolkit.git
   ```
2. Navigate to the project directory:
   ```bash
   cd ai-agents-toolkit
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Usage
Run the agents individually or as a system:

- **Airbnb Agent**:
  ```bash
  python airbnb_planner_multiagent/airbnb_agent/__main__.py
  ```
- **Weather Agent**:
  ```bash
  python airbnb_planner_multiagent/weather_agent/__main__.py
  ```
- **Host Agent**:
  ```bash
  python airbnb_planner_multiagent/host_agent/__main__.py
  ```

## Contributing
We welcome contributions! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature-name"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For questions or support, please contact:
- **Name**: Haider Jan
- **Email**: [janhaider040@gmail.com](janhaider040@gmail.com)
