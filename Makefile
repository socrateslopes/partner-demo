DOCKER_COMPOSE=docker-compose -p ztech -f resources/docker-compose.yml
DOCKER_COMPOSE_ELK=docker-compose -p ztech-elk -f resources/docker-compose.elk.yml
DOCKER_COMPOSE_TEST=docker-compose -p ztech -f resources/docker-compose.test.yml

REGISTRY=local
IMAGE=ztech

VERSION=latest
BRANCH=local

clean:
	$(DOCKER_COMPOSE) run app find . -type f -name "*.py[co]" -delete
	$(DOCKER_COMPOSE) run app find . -type d -name "__pycache__" -delete
	$(DOCKER_COMPOSE) run app rm -Rf .coverage target coverage.xml
	$(DOCKER_COMPOSE) down
	$(DOCKER_COMPOSE_ELK) down
	$(DOCKER_COMPOSE_TEST) down

install:
	$(DOCKER_COMPOSE) build

run:
	$(DOCKER_COMPOSE) up

elk:
	$(DOCKER_COMPOSE_ELK) up

test:
	$(DOCKER_COMPOSE_TEST) build 
	$(DOCKER_COMPOSE_TEST) run test
	$(DOCKER_COMPOSE_TEST) run test coverage report --fail-under=1 --show-missing
	$(DOCKER_COMPOSE_TEST) run test coverage xml
	$(DOCKER_COMPOSE_TEST) down

docker: 
	docker build -f resources/Dockerfile -t $(REGISTRY)/$(IMAGE):$(BRANCH) -t $(REGISTRY)/$(IMAGE):$(VERSION) .
