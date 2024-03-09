# Wiki Encyclopedia

Welcome to the Wiki Encyclopedia project! This project is a web application designed to provide a user-friendly interface for creating, editing, and browsing encyclopedia entries using Markdown syntax.

## Project Overview

The Wiki Encyclopedia is built using Django for the backend and HTML, CSS, and JavaScript for the frontend. The application allows users to create new encyclopedia entries, search for existing entries, edit entries, and view entries in Markdown format converted to HTML.

## Getting Started

To run the Wiki Encyclopedia locally on your machine, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/wiki-encyclopedia.git
    ```

2. Navigate to the project directory:

    ```bash
    cd wiki
    ```

3. Run the Django development server:

    ```bash
    python manage.py runserver
    ```

4. Open your web browser and visit http://localhost:8000 to access the Wiki Encyclopedia.

## Features

- **Entry Page**: Visiting `/wiki/TITLE` displays the contents of the encyclopedia entry with the specified title. If the entry does not exist, an error page is shown.
  
- **Index Page**: The index page lists all encyclopedia entries. Clicking on an entry name takes the user directly to that entry page.
  
- **Search**: Users can type a query into the search box in the sidebar to search for encyclopedia entries. Matching entries are displayed, and clicking on an entry name takes the user to that entry's page.
  
- **New Page**: Users can create new encyclopedia entries by clicking "Create New Page" in the sidebar. They can enter a title and Markdown content for the new entry.
  
- **Edit Page**: Users can edit existing encyclopedia entries by clicking a link on the entry page. They can edit the Markdown content in a textarea and save the changes.
  
- **Random Page**: Clicking "Random Page" in the sidebar takes the user to a random encyclopedia entry.
  
- **Markdown to HTML Conversion**: Any Markdown content in entry files is converted to HTML before being displayed to the user.

## Models

The Wiki Encyclopedia includes the following models:

- **Entry**: Represents an encyclopedia entry, containing a title and Markdown content.
