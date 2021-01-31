# agile-engine-test
This repo contains the agile-engine test
# Hox to run!
First create a virtual environment
```sh
$ virtualenv venv
```
Activate virtual env

```sh
$ . venv/bin/activate
```

clone the repository

```sh
$ git clone https://github.com/andrey-canon/agile-engine-test.git
```

go inside the project

```sh
$ cd agile-engine-test
```
Execute 

```sh
$ make run
```

# Main view
 url: http://localhost:8000/accounting/transactions/
 
description: In this view the user can see them transactions

# General API view
method: POST, GET

 url: http://localhost:8000/accounting/api/v1/transactions/
 
description: In this view the user can see them transactions and execute post request in order to create new transactions

# Specific API view
method: GET

 url: http://localhost:8000/accounting/api/v1/transactions/<id>
  
description: In this view the user can see a specifics transaction with the id

# Run tests
```sh
$ make validate
```