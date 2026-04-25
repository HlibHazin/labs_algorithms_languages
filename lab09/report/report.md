# Lab 09 Report: Repairing a Broken Python Project

## 1. What was wrong in the original project
The original project had several structural and design flaws that made it difficult to maintain and use:
* **Vague Naming:** Names like `textstuff.py` and `saveit.py` were too generic or used slang, which does not meet professional standards.
* **Lack of Package Structure:** The project was just a set of disconnected scripts with no clearly defined public API.
* **Execution Side-effects:** Debugging code and test data ran automatically upon importing functions, creating unnecessary "noise" in the console.
* **Bloated Dependencies:** The `requirements.txt` file contained third-party libraries (e.g., `requests`, `colorama`) that were not actually used in the project.
* **Broken Logic:** The `saveit.py` file was completely empty, which led to import errors in the main script.

## 2. What was improved
The project was completely reorganized according to standard Python package development best practices:
* **Meaningful Renaming:** Modules were renamed to `formatting.py` (instead of `textstuff.py`) and `storage.py` (instead of the empty `saveit.py`) so their names clearly reflect their responsibilities.
* **Package Structure Creation:** All source code was moved to the `src/report_tool/` directory. `__init__.py` was introduced to export core functions, and `__main__.py` was added to run the tool as a module.
* **Encapsulation and Privacy:** Internal helper functions received an underscore prefix (`_`) to clearly separate internal logic from the public API.
* **Code Cleanup:** All testing code inside the individual modules was moved into `if __name__ == "__main__":` blocks.
* **Dependency Optimization:** `requirements.txt` was cleared of unnecessary packages since the tool runs exclusively on the Python standard library.

## 3. Why these changes matter
These improvements make the project ready for real-world use and easier to scale:
* **Readability:** Meaningful module names allow other developers to quickly understand the project's architecture.
* **Usability:** The package-level public API allows importing functions directly (`from report_tool import ...`) without needing to memorize the internal file structure.
* **Stability:** Eliminating import side-effects and fixing the broken saving logic guarantees predictable tool behavior.
* **Professional Standards:** Adhering to standard Python conventions makes the code stable, maintainable, and easy to understand for the broader Python community.