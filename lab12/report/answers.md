# Lab 12: Testing an Async CLI Tool - Answers

**1. What is the difference between unit tests and behavior tests?**

Unit tests isolate and check individual, small components of code (e.g., a single function) to ensure they work correctly. Behavior tests (black-box tests) evaluate the entire program from the end-user's perspective by providing input data and verifying the final output, without relying on internal implementation details.

**2. Why is subprocess used for CLI testing?**

The `subprocess` module allows you to run the CLI tool as a separate system process—exactly how a real user would execute it via the terminal. This makes it easy to capture standard output (`stdout`), standard error (`stderr`), and the program's exit code to ensure the CLI interface works correctly.

**3. What happens if one async task fails without error handling?**

If one of the asynchronous tasks fails (raises an exception) and this error is unhandled (e.g., lacking a `try-except` block), the exception propagates up the call stack. This will cause the current process to stop or `asyncio.gather` to fail, resulting in the program crashing and the potential loss of results from other, even successful, tasks.

**4. When should you test internal functions vs full system behavior?**

Internal functions should be tested (using unit tests) to verify complex business logic, specific algorithms, or edge cases that are difficult to reproduce through the general interface. Full system behavior (using behavior tests) should be tested to ensure the integration of all components, correct handling of command-line arguments, and to guarantee that the user receives the expected output for both valid and invalid actions.

**5. What are the risks of time-based tests?**

Time-based tests are highly unstable (flaky). Execution time depends on CPU performance, operating system load, and other background processes. A test that passes quickly and successfully on a local machine might fail on a slower Continuous Integration (CI/CD) server, leading to false-negative test results.