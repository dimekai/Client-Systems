# Client-Systems
CLI application that performs the creation, reading, update and deletion (CRUD) of clients using a .csv file as database, making use of the "Click" library for command generation.

### Installation
1. Creating a new virtual enviroment to take more control of the system.

> ```python3 -m venv venv```

2. You have to install all dependencias using pip3, using the `requirements.txt` file
> ```pip3 install -r requirements.txt```

### App Commands

```
Usage: pv clients [OPTIONS] COMMAND [ARGS]...

  Manages the clients lifecycle to define client's membership group
  @click.group converts to 'clients' function in other decorator

Options:
  --help  Show this message and exit.

Commands:
  create  Creates a new client for sales-system
  delete  Deletes a client of the sales-system
  list    Lists all clients of the sales-system
  update  Updates a client of the sales-system
```

### Project Structure
- `clients/`: Contains models, commands and service logic of the application
  - `model.py`: Client class with its attributes. It generates a unique identifier using `uuid` module.
  - `commands.py`: Manages the clients lifecycle to define client's membership group. `@click.group` converts to `'clients'` function in other decorator. These decorator help you to add functionality.
  - `services.py`: Service logic to manipulate data contained in our databse

- `pv.py`: This is the **entry point of the application** using the application's context object.
- `setup.py`: App information.