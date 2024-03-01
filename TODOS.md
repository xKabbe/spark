# Project Idea: Spark

## Overview:

Build a command-line tool that analyzes a Git repository and provides insightful statistics about the project, including lines of code, distribution of file types, and information about contributors.

## Features:

1. Basic Statistics:
   - Total lines of code (LOC).
   - Number of files in the repository.
   - Count of code, comments, and blank lines.
2. File Type Distribution:
   - Display a breakdown of file types (e.g., Python, JavaScript, HTML, CSS) and their respective LOC.
3. Contributor Insights:
   - List top contributors based on the number of commits.
   - Show the distribution of commits by each contributor.
4. Code Complexity:
   - Utilize a code complexity analysis tool (such as radon for Python) to provide information about code complexity metrics.
5. Timeline Analysis:
   - Visualize the commit history over time, showing peaks of activity and periods of inactivity.
6. Customizable Options:
   - Allow users to specify which metrics they want to see, enabling them to customize the analysis based on their needs.
7. Integration with External Tools:
   - Optionally, integrate with external tools like cloc for counting lines of code in various languages.

## Technical Considerations:

- Use GitPython or a similar library to interact with the Git repository.
- Implement modular code to allow easy extension of analysis features.
- Leverage color-coding or formatting to enhance the readability of the command-line output.
- Ensure error handling for cases where the tool encounters issues accessing or parsing the repository.

## Example Usage:

```bash
python repository_analyzer.py --path /path/to/git/repository --stats --file-types --contributors --complexity
```

This command would analyze the specified Git repository and display various statistics, including lines of code, file type distribution, contributor insights, and code complexity.

Building a repository analyzer can provide valuable insights into the health and structure of a project, making it easier for developers and project managers to understand and manage their codebase.

# Project TODOS: Spark

## Code Analysis

- [ ] Add `typer` interface for CLI execution
- [ ] Show icons for analyzed files (e.g. Python icon for .py files)
- [ ] Read the file and get information about lines of code (LOC) and more
- [ ] Add option to print `Code Insight` analysis output in console or in separate PDF file (using `LaTeX`)
- [ ] Add complexity rating for files/folders (e.g. based on length, method count, ...)
- [ ] Show file count, directories and tree structure (tree depth)

## GitLab Analysis

...
