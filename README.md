````markdown
# Users Table API Script

This Python script fetches user data from the public JSONPlaceholder API and prints it in a clean, formatted table. It demonstrates how to work with GET APIs, parse JSON responses, apply filters, and handle errors using the `requests` library.

## Features
- Fetches user data using an HTTP GET request  
- Handles API and network-related errors safely  
- Parses JSON into readable Python dictionaries  
- Displays output in a structured ASCII table showing: Name, Username, Email, and City  
- Includes a toggle to filter users whose city starts with **S**

## Requirements
- Python 3.8+  
- `requests` library  

Install dependency:
```bash
pip install requests
````

## Usage

Run the script:

```bash
python api.py
```

### Enable or Disable City Filter

Inside the script, set:

```python
FILTER_CITY = True
```

to show only users whose city begins with **S**.

Set:

```python
FILTER_CITY = False
```

to display all users.

## Example Output

```
+--------------------------------------------------------------------------------+
| Name                 | Username        | Email                    | City            |
+--------------------------------------------------------------------------------+
| Patricia Lebsack     | Karianne        | Julianne.OConner@kory.org| South Elvis     |
| Mrs. Dennis Schulist | Leopoldo_Corkery| Karley_Dach@jasper.info  | South Christy   |
+--------------------------------------------------------------------------------+
```

## Error Handling

The script gracefully handles:

* Non-successful HTTP responses
* Connection or timeout errors
* Empty or invalid JSON payloads
* Missing fields in the returned data

This ensures smooth execution even when the API behaves unpredictably.

## API Reference

User data is fetched from:

```
https://jsonplaceholder.typicode.com/users
```

This is a free public API commonly used for demos and practice.

