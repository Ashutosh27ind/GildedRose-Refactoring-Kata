# Gilded Rose starting position in Python

For exercise instructions see [top level README](../README.md)

Suggestion: create a python virtual environment for this project. See the [documentation](https://docs.python.org/3/library/venv.html)

## Run all tests with pytest

From the `python` directory, you can run all tests (including ApprovalTests and unit tests):

```
pytest tests
```

## What's New

- **Conjured Items Support:**  
  The application now supports "Conjured" items, which degrade in quality twice as fast as normal items, including after the sell-in date.  
  - Quality never drops below 0.
  - See `tests/test_conjured.py` for test cases.

- **Refactored Codebase:**  
  The item update logic has been refactored for better extensibility and maintainability.

## Run the unit tests from the Command-Line

```
pytest tests
```

Or to run a specific test file (e.g., for Conjured items):

```
pytest tests/test_conjured.py
```

Or the original unittest:

```
python tests/test_gilded_rose.py
```

## Run the TextTest fixture from the Command-Line

For e.g. 10 days:

```
python texttest_fixture.py 10
```

You should make sure the command shown above works when you execute it in a terminal before trying to use TextTest (see below).


## Run the TextTest approval test that comes with this project

There are instructions in the [TextTest Readme](../texttests/README.md) for setting up TextTest. You will need to specify the Python executable and interpreter in [config.gr](../texttests/config.gr). Uncomment these lines:

    executable:${TEXTTEST_HOME}/python/texttest_fixture.py
    interpreter:python

## Run the ApprovalTests.Python test

This test uses the framework [ApprovalTests.Python](https://github.com/approvals/ApprovalTests.Python). Run it like this:

```
python tests/test_gilded_rose_approvals.py
```

You will need to approve the output file which appears under "approved_files" by renaming it from xxx.received.txt to xxx.approved.txt.