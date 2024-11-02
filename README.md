# Personal Knowledge Space

## Description
The **Personal Knowledge Space** is an interactive, desktop-based tool designed to help users organize ideas, notes, and resources visually and hierarchically. This knowledge space allows you to create, connect, and visualize notes in a tree or network structure, making it ideal for anyone who wants to map out complex information or create a structured knowledge base.

## Features
- **Interactive Visualization**: Displays all notes as "nodes" and their connections. It works like a mind-mapping tool, but each note has its own content and annotations.
- **Hierarchical Organization**: Each note can be designated as a "parent" or "child," creating a tree structure to show relationships.
- **Data Persistence**: All notes are stored in an SQLite database, allowing you to save and reload your knowledge space.

## Technologies Used
- **Python**: For backend logic and database interactions.
- **Tkinter**: Used for the graphical user interface (GUI).
- **NetworkX and Matplotlib**: For rendering the tree structure and relationships between notes.

## Installation

### Prerequisites
Ensure you have **Python 3.x** installed on your machine.

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/personal_knowledge_space.git
   cd personal_knowledge_space


Create a virtual environment and activate it:


python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`


Install the dependencies:



pip install -r requirements.txt


Usage
To start the application, run the following command:

python src/main.py
