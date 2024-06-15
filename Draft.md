# Full-Stack JS Docker Tutorial

## Purpose

This tutorial will help you set up a development environment using Docker Compose for a full-stack JavaScript application, including:

- React Front End
- Express API Backend
- NGINX Reverse Proxy Server
- MySQL Database
- Admin Interface for MySQL

Prerequisites
Ensure you have the following installed on your machine:

- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- Basic knowledge of Docker and Docker Compose

## Project Structure
    .
    project-root/
    ├── api-server/
    │ ├── Dockerfile
    │ ├── package.json
    │ ├── package-lock.json
    │ └── .dockerignore
    ├── blog-ui/
    │ ├── Dockerfile
    │ ├── package.json
    │ ├── package-lock.json
    │ └── .dockerignore
    ├── nginx/
    │ ├── default.conf
    │ └── Dockerfile
    ├── docker-compose.yml
    └── .env

## Steps to Run Locally

1. Clone the Repository

  ```
  git clone <repository-url>
  cd project-root
  ```

2. Create a .env File or Rename the .env.example file to .env file.
   Create a .env file in the root directory with the following contents:
   
  ```
  MYSQL_DATABASE=your_database_name
  MYSQL_USER=your_user
  MYSQL_PASSWORD=your_password
  MYSQL_ROOT_PASSWORD=your_root_password
  API_PORT=5050
  CLIENT_PORT=3000
  ```

3. Build the Docker Images
  ```
  COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 docker-compose build
  ```
4. Run the Docker Containers
  ```
  docker-compose up
  ```
5. Access the Services

- React Client: http://localhost:3000
- Express API: http://localhost:5050
- Proxied Client (via NGINX): http://localhost:8008
- Adminer (MySQL Admin Interface): http://localhost:8080
  - Server: db
  - Username: MYSQL_USER
  - Password: MYSQL_PASSWORD

6. Shutting Down the Environment

  ```
  docker-compose down
  ```

## Additional Notes

- Any changes made inside the /api-server and /blog-ui folders will be automatically updated due to the volume mounting and hot-reload setup.
- Data persistence is handled through Docker volumes, ensuring that your MySQL data is preserved between container restarts.