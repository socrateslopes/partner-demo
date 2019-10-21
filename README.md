# Z-Tech Partners API

## Current decisions
- Python used to be the language that I used the most, so I chose it along with Flask, a lightly opinionated web framework.

- Since Elasticsearch knows how to handle spacial data in a decent way, I used it to store everything. I would use it to centralize logs, anyway, so it was very handy.

- Docker compose is sufficiently good for this scenario. I`ve created 2 files: one for the ELK stack (loooooong time to be ready) and another for the API.

- ELK stack works fine for logging.

- There are many problems that would occur in this scenario if we try to scale the app, and also because Elasticsearch is a distributed system that, inherently, falls into the CAP theorem.

I would be pleased to discuss every other details with you ;)


## TODO
- Tests: I haven't followed a TDD approach but since I consider tests really important they should be here.
There is not that much logic to validate, so unit tests would be a good fit. Also, integration tests to guarantee that everyting is ok.

- Documentation: I should put Flasgger here to create API docs in Swagger so that anyone can understand how to use this.

- Better error handling: In most scenario, I'm only considering the best case.

- 'Create' endpoint

- Input validation: input validation of data provided to the endpoint

- Code deduplication: there are some duplicated code snippets that should be refactored and improved

Full endpoints documentation: TODO

## Go for it
You are gonna need:
1. A computer
2. Git
4. Docker
5. Docker-compose
6. Make

### Step 1: Install everything
As simple as that ↑ 

### Step 2: Set-up Docker
```
make install
```

### Step 3: Run the ELK stack and wait for it
```
make elk
```

### Step 4: Run your code
```
make run
```

**Now you should be up and running on http://localhost:5000**
``` curl http://localhost:5000/import``` will populate the database with provided data

### Testing
To test your code and check test coverage, just run
```
make test
```

### Cleaning
Cleans the garbage left by Docker
```
make clean
```

### Deployment
There is no environment to deploy for this momment.
Ideally, this should be part of CI/CD distribution using Gitlab CI, Jenkins or any other tool