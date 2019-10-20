# Zenon Billing System

*"Pay your rent!" - Zenón Barriga y Pesado*

![zenon](https://gitlab.olxbr.io/sales-tech-tools/zenon-salesforce-worker/uploads/6468696118fa75124448c20c252d1dbf/zenon.jpg)

[![pipeline status](https://gitlab.olxbr.io/sales-tech-tools/zenon-salesforce-worker/badges/master/pipeline.svg)](https://gitlab.olxbr.io/sales-tech-tools/zenon-salesforce-worker/commits/master) [![coverage report](https://gitlab.olxbr.io/sales-tech-tools/zenon-salesforce-worker/badges/master/coverage.svg)](https://gitlab.olxbr.io/sales-tech-tools/zenon-salesforce-worker/commits/master)

Full endpoints documentation: https://s3.amazonaws.com/stt-prod-api-docs/invoice/index.html

## Go for it
You are gonna need:
1. A computer
2. Git
2. AWS Credentials
3. AWS CLI
4. Docker
5. Docker-compose
6. Make

### Step 1: Install everything
As simple as that ↑ 

### Step 2: Login to AWS
So you can download/upload Docker images :)

Run this script once:
```
aws configure # only the first time
$(aws ecr get-login --region us-east-1 | sed -e 's/-e none//g')
```

### Step 3: Set-up Docker
```
make install
```

### Step 4: Run your code
```
make run
```

**Now you should be up and running on http://localhost:5000**


## Other commands
Here you can understand what those commands listed in you makefile do.

### Docs
You can create HTML documentation based on RAML files by running
```
make docs
```
and if you want to push them to S3, just run
```
make publish-docs
```

### Docker
Create your container by running
```
make docker
```
Push your image to registry
```
make push
```

### Testing
To test your code and check test coverage, just run
```
make test
```

### Cleaning
To clean the docs garbage, run
```
make clean-docs
```
Cleans the garbage left by Docker
```
make clean
```
Removes your local database
```
make cleandb
```

### Deployment
→ **BEWARE: IF YOU PUSH TO MASTER YOU WILL DEPLOY TO PRODUCTION** ←

Prepare your files
```
make prepare-deploy
```
Publish to Elastic Beanstalk
```
make deploy
```
Mark deployment in New Relic
```
make newrelic
```

