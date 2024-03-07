# FastAPI: User Service

*A simple User Service written in FastAPI*

## Features

* Create User
* Retrieve user
* Token Based Authentication
* Dockerfile
* Tests with Pytest

## Getting Started

0. Clone repository
```bash
git clone https://github.com/sunnybeta/user user-service
cd user-service
```

1. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install requirements

```bash
pip install -r requirements.txt
```

3. Start Database

```bash
docker run -d -p 5432:5432 -e POSTGRES_USERNAME=postgres -e POSTGRES_PASSWORD=password --name my-awesome-db postgres
```

4. Spin Server

```bash
uvicorn app.asgi:app
```

## Future

- [ ] Obtain feedback
- [ ] Connect with other services
- [ ] Make clients async
