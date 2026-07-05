# FastAPI Layered Project for Java Spring Boot Developers

This project is a small FastAPI application built with a structure that should feel familiar if you come from Java and Spring Boot.

It uses:

- FastAPI for HTTP APIs
- Pydantic for request/response validation
- SQLAlchemy for ORM and database access
- PostgreSQL as the main database
- Docker Compose to run the database locally
- `.env` configuration for environment-specific values

The main goal is not just to build a CRUD API, but to show how common Spring Boot ideas translate into Python.

## 1. What this project is trying to teach

If you already know Spring Boot, this project helps you map these ideas into FastAPI:

- `@RestController` becomes a router/controller module
- `@Service` becomes a service class
- `@Repository` becomes a repository class
- `@Entity` becomes a SQLAlchemy model class
- DTOs become Pydantic schema classes
- Spring dependency injection becomes FastAPI dependencies using `Depends(...)`
- `application.properties` becomes `.env` + a typed settings class
- `@ControllerAdvice` becomes centralized exception handlers
- a local database container replaces the need to install PostgreSQL directly on your machine

The structure is intentionally layered so you can recognize the responsibilities quickly.

## 2. Project structure

```text
fast-api/
├── app/
│   ├── config/
│   │   ├── __init__.py
│   │   ├── database.py
│   │   ├── dependencies.py
│   │   ├── exception_handlers.py
│   │   └── settings.py
│   ├── controllers/
│   │   ├── __init__.py
│   │   └── user_controller.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── user_model.py
│   ├── repositories/
│   │   ├── __init__.py
│   │   └── user_repository.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── user_schema.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── user_service.py
│   ├── __init__.py
│   ├── exceptions.py
│   └── main.py
├── .env.example
├── .gitignore
├── docker-compose.yml
├── README.md
└── requirements.txt
```

## 3. Tech stack

### FastAPI

FastAPI is the web framework. It provides:

- routing
- dependency injection
- request parsing
- response serialization
- Swagger/OpenAPI documentation

Java reference:
- Think of this as the combination of Spring MVC + automatic OpenAPI integration.

### Pydantic

Pydantic is used for request and response models.

It provides:

- JSON body validation
- type conversion
- clear error messages
- serialization of Python objects into API responses

Java reference:
- Similar to DTO classes plus Bean Validation plus some of Jackson's object mapping behavior.

### SQLAlchemy

SQLAlchemy is the ORM and database access layer.

It provides:

- model-to-table mapping
- sessions for database operations
- query building
- persistence

Java reference:
- Similar to JPA/Hibernate, although the API style is more explicit.

### PostgreSQL

PostgreSQL is the main database for this project.

Why PostgreSQL here:

- it is common in real applications
- it feels closer to a production setup than SQLite
- it matches what many Spring Boot teams already use

Java reference:
- this is the same kind of database you would commonly connect to from Spring Boot using Spring Data JPA

### Docker Compose

Docker Compose is used to run PostgreSQL locally.

Why this helps:

- you do not need to install PostgreSQL directly
- the whole team can use the same DB version
- startup is one command

Java reference:
- similar to running infrastructure dependencies locally with Docker while your Spring Boot app runs on your host machine

### Uvicorn

Uvicorn is the ASGI server used to run the FastAPI app.

Java reference:
- Similar in purpose to running Spring Boot on embedded Tomcat, though the internals are different.

## 4. Environment configuration

The application reads settings from `.env`.

Current environment variables:

```env
APP_NAME=FastAPI Layered Example
APP_ENV=development
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=fastapi_db
POSTGRES_USER=fastapi_user
POSTGRES_PASSWORD=fastapi_password
DATABASE_URL=postgresql+psycopg://fastapi_user:fastapi_password@localhost:5432/fastapi_db
```

### What each variable means

- `APP_NAME`: application title shown in FastAPI docs
- `APP_ENV`: environment name such as `development`
- `POSTGRES_HOST`: database host
- `POSTGRES_PORT`: database port
- `POSTGRES_DB`: database name
- `POSTGRES_USER`: database username
- `POSTGRES_PASSWORD`: database password
- `DATABASE_URL`: full SQLAlchemy connection string used by the app

Java reference:
- this is similar to a combination of:
  - `spring.application.name`
  - `spring.datasource.url`
  - `spring.datasource.username`
  - `spring.datasource.password`

## 5. Docker infrastructure for PostgreSQL

File:
- `docker-compose.yml`

This file starts a PostgreSQL container.

```yaml
services:
  postgres:
    image: postgres:16-alpine
```

### What it does

- pulls PostgreSQL 16
- creates a container named `fastapi-postgres`
- exposes port `5432`
- creates a persistent Docker volume
- initializes the database name, user, and password
- adds a health check so you know when PostgreSQL is ready

### Why this is useful

Without Docker:
- you must install PostgreSQL manually
- different developers may use different versions

With Docker:
- the DB setup is repeatable
- the environment is easier to share

Java reference:
- very common in Spring Boot teams for local infrastructure

## 6. Layered architecture overview

This application follows a classic layered structure:

1. Controller layer
2. Service layer
3. Repository layer
4. Model/Entity layer
5. Schema/DTO layer
6. Config layer

The idea is the same as in a typical Spring Boot project: each layer has one clear responsibility.

## 7. File-by-file explanation and Java mapping

### `app/main.py`

Purpose:
- create the FastAPI application
- register exception handlers
- register routes
- create database tables on startup
- expose the health check endpoint

Java/Spring Boot mapping:
- closest to the class containing `public static void main(...)`
- similar to the bootstrap role of a `@SpringBootApplication` class

What happens here:

```python
app = FastAPI(title=settings.app_name)
register_exception_handlers(app)
app.include_router(user_router, prefix="/api")
```

This is like:

- starting your application context
- registering MVC controllers
- applying global web configuration

### `app/config/settings.py`

Purpose:
- load settings from environment variables
- load `.env` automatically
- provide a reusable settings object

Java/Spring Boot mapping:
- similar to `application.properties`
- also similar to a typed config bean using `@ConfigurationProperties`

Key idea:
- instead of many scattered `os.getenv(...)` calls, configuration is centralized in one typed class

### `app/config/database.py`

Purpose:
- create the SQLAlchemy engine
- create the session factory
- define the base model class
- create a per-request database session dependency

Java/Spring Boot mapping:
- like a simplified DataSource configuration + JPA setup
- `engine` is conceptually similar to the database connection infrastructure
- `SessionLocal` is similar to an `EntityManager` factory/session factory

Important function:

```python
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

This means:
- one database session is created for the request
- FastAPI injects it where needed
- the session is closed automatically after the request

Java analogy:
- think of it like framework-managed database resource handling around each request

### `app/config/dependencies.py`

Purpose:
- wire the repository into the service
- wire the database session into the repository
- centralize dependency creation

Java/Spring Boot mapping:
- similar to Spring bean wiring
- similar to constructor injection

Example:

```python
def get_user_service(repository: UserRepository = Depends(get_user_repository)) -> UserService:
    return UserService(repository)
```

Java analogy:
- similar to Spring doing:
  `new UserService(userRepository)`

Difference:
- Spring creates singleton beans automatically by scanning annotations
- FastAPI often uses explicit dependency functions

### `app/config/exception_handlers.py`

Purpose:
- convert Python exceptions into HTTP responses
- keep error formatting out of controller code

Java/Spring Boot mapping:
- very similar to `@ControllerAdvice` and `@ExceptionHandler`

Current behavior:
- `ResourceNotFoundError` becomes `404`
- `ValueError` becomes `400`

### `app/exceptions.py`

Purpose:
- define custom application exceptions

Java/Spring Boot mapping:
- similar to a custom exception class like `UserNotFoundException`

### `app/models/user_model.py`

Purpose:
- map the `User` Python class to the `users` database table

Java/Spring Boot mapping:
- equivalent to a JPA `@Entity`

Fields:
- `id`
- `name`
- `email`

Java analogy:
- this is your persistent domain object

### `app/schemas/user_schema.py`

Purpose:
- define request and response contracts for the API

Classes:
- `UserCreate`
- `UserUpdate`
- `UserResponse`

Java/Spring Boot mapping:
- equivalent to request DTOs and response DTOs

Important concept:
- these are not database entities
- they exist to define the API contract

That separation is the same good practice you would use in Spring Boot.

### `app/repositories/user_repository.py`

Purpose:
- isolate database operations
- keep SQLAlchemy queries out of the service and controller

Methods:
- `save`
- `find_all`
- `find_by_id`
- `find_by_email`
- `delete`

Java/Spring Boot mapping:
- similar to a repository class or a custom Spring Data JPA repository implementation

Why this matters:
- the service layer should talk in business terms
- the repository layer should talk in database terms

### `app/services/user_service.py`

Purpose:
- hold business logic
- validate business rules
- orchestrate repository calls
- translate models into response DTOs

Business rules currently implemented:
- prevent duplicate email on create
- throw not-found error when user does not exist

Java/Spring Boot mapping:
- equivalent to `@Service`

This is the layer where you would add:
- more validation
- transactions
- domain rules
- integration with other services

### `app/controllers/user_controller.py`

Purpose:
- expose REST endpoints
- receive path parameters and request bodies
- delegate work to the service layer
- return API responses

Endpoints:
- `POST /api/users`
- `GET /api/users`
- `GET /api/users/{user_id}`
- `PUT /api/users/{user_id}`
- `DELETE /api/users/{user_id}`

Java/Spring Boot mapping:
- equivalent to `@RestController`

Important rule:
- controller should stay thin
- business logic should stay in the service layer

## 8. How a request flows through the application

Let’s use `POST /api/users` as an example.

### Step 1: HTTP request reaches the controller

File:
- `app/controllers/user_controller.py`

FastAPI:
- reads the JSON body
- validates it against `UserCreate`
- injects `UserService`

Java analogy:
- similar to Spring receiving `@RequestBody UserCreateRequest`

### Step 2: Controller calls service

The controller does not talk to the database directly.

It does:

```python
return service.create_user(request)
```

Java analogy:
- same as `userService.createUser(request)`

### Step 3: Service applies business logic

File:
- `app/services/user_service.py`

The service:
- checks whether email already exists
- creates a `User` entity
- asks the repository to save it

Java analogy:
- same place you would put service-level validation and orchestration in Spring

### Step 4: Repository writes to the database

File:
- `app/repositories/user_repository.py`

The repository:
- uses SQLAlchemy session methods
- commits the transaction
- refreshes the entity from the DB

Java analogy:
- similar to `repository.save(entity)`

### Step 5: Response DTO is returned

The service converts the saved entity to `UserResponse`.

FastAPI returns JSON automatically.

Java analogy:
- similar to returning a response DTO from your service/controller and letting Jackson serialize it

## 9. Dependency injection in FastAPI vs Spring Boot

Spring Boot style:

```java
@Service
public class UserService {
    private final UserRepository userRepository;

    public UserService(UserRepository userRepository) {
        this.userRepository = userRepository;
    }
}
```

FastAPI style:

```python
def get_user_service(
    repository: UserRepository = Depends(get_user_repository),
) -> UserService:
    return UserService(repository)
```

Key differences:

- Spring uses classpath scanning and annotations heavily
- FastAPI often uses explicit functions for dependency creation
- Spring usually manages singleton beans globally
- FastAPI dependencies are often request-based and very explicit

The idea is still the same:
- one component depends on another
- the framework resolves and injects the dependency

## 10. Database session management

One common concern for Java developers is: where is the transaction/session lifecycle managed?

In this project:

- `get_db()` creates a SQLAlchemy session
- FastAPI injects that session where needed
- the session is closed after the request

This is not a full transaction abstraction like Spring’s `@Transactional`, but it gives you controlled session management.

In this sample:

- repository methods call `commit()` directly for simplicity

In a larger project you might choose:

- service-level transaction handling
- unit-of-work pattern
- more advanced session scoping

## 11. Error handling

Error handling is centralized in:

- `app/config/exception_handlers.py`

Examples:

- if a user is not found, the service raises `ResourceNotFoundError`
- the global handler converts it to HTTP `404`

This keeps controller code clean.

Java analogy:
- very similar to global exception mapping with `@ControllerAdvice`

## 12. API endpoints

### Create user

```http
POST /api/users
Content-Type: application/json

{
  "name": "Alice",
  "email": "alice@example.com"
}
```

### Get all users

```http
GET /api/users
```

### Get one user

```http
GET /api/users/1
```

### Update user

```http
PUT /api/users/1
Content-Type: application/json

{
  "name": "Alice Updated"
}
```

### Delete user

```http
DELETE /api/users/1
```

### Health check

```http
GET /health
```

## 13. How to run the project with PostgreSQL

### 1. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Create your local environment file

```bash
cp .env.example .env
```

### 3. Start PostgreSQL with Docker Compose

```bash
docker compose up -d
```

To check container status:

```bash
docker compose ps
```

To view PostgreSQL logs:

```bash
docker compose logs -f postgres
```

### 4. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 5. Start the FastAPI application

```bash
uvicorn app.main:app --reload
```

### 6. Open the built-in API docs

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

### 7. Stop the database

```bash
docker compose down
```

If you also want to remove the volume data:

```bash
docker compose down -v
```

## 14. Detailed Java and Spring Boot mapping

| Python / FastAPI | Java / Spring Boot equivalent | Notes |
| --- | --- | --- |
| `app/main.py` | `@SpringBootApplication` main class | App bootstrap |
| `FastAPI(...)` | Spring application + MVC setup | Web app creation |
| `APIRouter` | `@RestController` + request mapping | Route grouping |
| Controller function | `@GetMapping`, `@PostMapping`, etc. | Endpoint handler |
| Service class | `@Service` | Business logic |
| Repository class | `@Repository` | DB access abstraction |
| SQLAlchemy model | JPA `@Entity` | Table mapping |
| Pydantic schema | DTO + Bean Validation | Request/response contract |
| `Depends(...)` | Dependency injection | Framework-provided wiring |
| Settings class | `@ConfigurationProperties` | Typed configuration |
| `.env` | `application.properties` / env overrides | External configuration |
| `DATABASE_URL` | `spring.datasource.url` | Main DB connection |
| `POSTGRES_USER` | `spring.datasource.username` | DB username |
| `POSTGRES_PASSWORD` | `spring.datasource.password` | DB password |
| Exception handler | `@ControllerAdvice` | Global error mapping |
| Docker Compose PostgreSQL | local infra container | Similar to local dev DB stack |
| Uvicorn | Embedded web server | Runtime server |

## 15. Important differences from Spring Boot

Even though this structure is familiar, there are some important differences.

### Less annotation magic

Spring Boot hides a lot behind annotations and scanning.

FastAPI is usually more explicit:

- routes are registered directly
- dependencies are declared directly
- object creation is often visible in code

This is good for learning because the wiring is easier to see.

### DTO validation is built into the function signature

In Spring Boot you often write:

```java
public UserResponse create(@Valid @RequestBody UserCreateRequest request)
```

In FastAPI the typing itself drives validation:

```python
def create_user(request: UserCreate, service: UserService = Depends(get_user_service)):
```

The type annotation does a lot of work.

### Python tends to prefer smaller files and less ceremony

Compared to Java:

- fewer interfaces
- less boilerplate
- less getter/setter code
- shorter classes

The tradeoff is that Python relies more on conventions and discipline from the developer.

## 16. How to extend this project

If you want to grow this into a larger project, the next natural steps are:

- add more entities such as `Product`, `Order`, or `Post`
- add Alembic for database migrations
- add tests with `pytest`
- add logging
- add authentication
- containerize the FastAPI app itself later if needed

For each new feature, repeat the same pattern:

1. create the model/entity
2. create request/response schemas
3. create repository methods
4. create service methods
5. expose endpoints in the controller

That is the same mental model you already use in Spring Boot.

## 17. Quick mental model for a Java developer

If you want the shortest possible summary, think of this project like this:

- `main.py` = bootstraps the app
- `controllers/` = Spring MVC controllers
- `services/` = business layer
- `repositories/` = persistence layer
- `models/` = JPA entities
- `schemas/` = DTOs
- `config/` = application configuration and DI wiring
- `docker-compose.yml` = your local PostgreSQL infrastructure

So the architecture is familiar. The main difference is the syntax and the amount of framework magic.
