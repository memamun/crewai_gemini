# AI Research and Content Generation Project

This project is designed to automate the process of researching and generating content on the latest advancements in AI tools. It leverages a combination of agents, tasks, and a crew to perform comprehensive analysis and create engaging content.

## Features

- **Research Agent**: Conducts in-depth analysis of AI advancements.
- **Content Strategist Agent**: Crafts compelling content based on research insights.
- **Sequential Task Execution**: Ensures tasks are completed in a logical order.

## Requirements

To run this project, you need the following Python packages:

- crewai
- duckduckgo-search
- langchain_google_genai
- python-dotenv
- google-generativeai

These can be installed using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

## Setup

1. **Environment Variables**: Ensure you have a `.env` file with the necessary API keys. For example, you need to set `GEMINI_API_KEY` in your `.env` file.

2. **Run the Project**: Execute the main script to start the research and content generation process.


```bash
python crew.py
```

## How It Works

- **Environment Setup**: Loads environment variables and sets up the API key.
  ```python:crew.py
  startLine: 7
  endLine: 12
  ```

- **Agent Definition**: Defines agents with specific roles and goals.
  ```python:crew.py
  startLine: 17
  endLine: 44
  ```

- **Task Creation**: Creates tasks for agents to perform.
  ```python:crew.py
  startLine: 47
  endLine: 64
  ```

- **Crew Execution**: Instantiates a crew and kicks off the task execution.
  ```python:crew.py
  startLine: 66
  endLine: 75
  ```

## Output

The project outputs a comprehensive analysis report and a blog post on AI tools, which are printed to the console.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Contact

For any questions or inquiries, please contact Mamun at a.a.mamun@gmail.com
