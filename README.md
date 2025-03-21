# Agent Task Runner API Documentation

This document describes the API endpoints for the Agent Task Runner, which allows users to collect data by providing a specific task.

## Prerequisites

-   Ensure you have a valid API key. You can obtain one by contacting the API administrator.
-   Set the `ACQ_API_KEY` environment variable with your API key.

## API Endpoints

### `GET /sync-task`

This endpoint allows you to retrieve data based on a specified task.

**Request:**

-   **Method:** `GET`
-   **Headers:**
    -   `access_token`: Your API key.
-   **Query Parameters:**
    -   `task` (required): The task for which you want to collect data.

**Response:**

-   **Status Codes:**
    -   `200 OK`: Successful retrieval of data.
    -   `403 Forbidden`: Invalid API key.
-   **Response Body:**

    ```json
    {
      "data": {
        "history": [
          {
            "model_output": {
              "current_state": {
                "evaluation_previous_goal": "...",
                "memory": "...",
                "next_goal": "..."
              },
              "action": [
                {
                  "search_google": {
                    "query": "..."
                  }
                },
                // ... more actions
              ]
            },
            "result": [
              {
                "is_done": false,
                "extracted_content": "...",
                "include_in_memory": true
              },
              // ... more results
            ],
            "state": {
              "tabs": [
                {
                  "page_id": 0,
                  "url": "...",
                  "title": "..."
                },
                // ... more tabs
              ],
              "screenshot": "...",
              "interacted_element": [
                null
              ],
              "url": "...",
              "title": "..."
            },
            "metadata": {
              "step_start_time": 1742570187.8738434,
              "step_end_time": 1742570195.3794885,
              "input_tokens": 2894,
              "step_number": 2
            }
          },
          // ... more steps
        ]
      }
    }
    ```

    See the [Output Format Documentation](#output-format-documentation) for details on the structure of the `data` object.

**Example Request:**

```bash
curl -X GET "http://localhost:8000/sync-task?task=India%20CPI%20data%202025" \
     -H "access_token: YOUR_API_KEY"
Example Response:{
  "data": {
    "history": [
      {
        "model_output": {
          "current_state": {
            "evaluation_previous_goal": "Failed - The page is blank with no elements present",
            "memory": "Starting fresh with the task to collect CPI data for 2025. No progress made yet as the page is empty.",
            "next_goal": "Search for India CPI data 2025"
          },
          "action": [
            {
              "search_google": {
                "query": "India CPI data 2025 file and api links"
              }
            }
          ]
        },
        "result": [
          {
            "is_done": false,
            "extracted_content": "🔍 Searched for \"India CPI data 2025 file and api links\" in Google",
            "include_in_memory": true
          }
        ],
        "state": {
          "tabs": [
            {
              "page_id": 0,
              "url": "about:blank",
              "title": ""
            }
          ],
          "screenshot": "iVBORw0KGgoAAAANSUhEUgAABQAAAARMCAIAAABJa6kDAAAAAXNSR0IArs4c6QAAGWpJREFUeJzs18ENwCAQwLDS/Xc+...",
          "interacted_element": [
            null
          ],
          "url": "about:blank",
          "title": ""
        },
        "metadata": {
          "step_start_time": 1742570187.8738434,
          "step_end_time": 1742570195.3794885,
          "input_tokens": 2894,
          "step_number": 2
        }
      }
    ]
  }
}
Output Format DocumentationThe data object returned by the API is structured as follows:{
  "data": {
    "history": [
      {
        "model_output": {
          "current_state": {
            "evaluation_previous_goal": "...",
            "memory": "...",
            "next_goal": "..."
          },
          "action": [
            {
              "search_google": {
                "query": "..."
              }
            },
            // ... more actions
          ]
        },
        "result": [
          {
            "is_done": false,
            "extracted_content": "...",
            "include_in_memory": true
          },
          // ... more results
        ],
        "state": {
          "tabs": [
            {
              "page_id": 0,
              "url": "...",
              "title": "..."
            },
            // ... more tabs
          ],
          "screenshot": "...",
          "interacted_element": [
            null
          ],
          "url": "...",
          "title": "..."
        },
        "metadata": {
          "step_start_time": 1742570187.8738434,
          "step_end_time": 1742570195.3794885,
          "input_tokens": 2894,
          "step_number": 2
        }
      },
      // ... more steps
    ]
  }
}
```
