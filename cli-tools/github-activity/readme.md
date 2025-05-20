# GitHub User Activity CLI

A simple command-line tool to fetch and display the recent public activity of a GitHub user using the GitHub API.

## Features

- Fetches recent public events of a GitHub user
- Displays activity in a clean, readable format in the terminal
- Handles errors such as invalid usernames or API failures

## Installation

Make sure you have Python 3 installed.  
Then install the required dependency:

```bash
    pip install requests
```

## Usage
```bash
    chmod +x github_activity # make it executable
    ./github_activity <username>
```

#### Example
```bash
    ./github_activity kamranahmedse
```

#### Sample Output
```bash
    - Pushed 3 commits to kamranahmedse/developer-roadmap
    - Opened a new issue in kamranahmedse/developer-roadmap
    - Starred kamranahmedse/developer-roadmap
```

## API Used
This tool uses the public GitHub Events API:
```bash
    https://api.github.com/users/<username>/events
```

## Notes
- Only public activity is shown.
- You might encounter rate limiting if making too many requests without authentication.
