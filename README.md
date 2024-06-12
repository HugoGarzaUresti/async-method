# Async Method

This guide demonstrates how to use asynchronous methods in Python using `asyncio` and `aiohttp`. We will create asynchronous tasks that fetch data from URLs concurrently.

## Requirements

- Python 3.7+
- `aiohttp` library

## Setup

1. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

2. Run the application:
    ```sh
    python run.py
    ```

## Code Explanation

### `app/async_tasks.py`

This module contains the functions to perform asynchronous tasks.

- **`fetch_url`**: Asynchronously fetches content from a URL.
- **`async_task`**: Defines an asynchronous task that uses `fetch_url` to get data from a URL.
- **`main`**: Gathers multiple asynchronous tasks and runs them concurrently using `asyncio.gather`.

### `run.py`

This script serves as the entry point for the application. It runs the `main` function which starts the asynchronous tasks.

## Additional Information

- The `aiohttp` library is used for making asynchronous HTTP requests.
- The `asyncio` library provides the infrastructure for writing single-threaded concurrent code using coroutines.
- Adjust the URLs in `main` to point to the resources you want to fetch.
