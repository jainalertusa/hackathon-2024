# Summer Hackathon 2024 

## Sample Project

This sample project will help you set up your summer hackathon submissions!

Project contains
1. Front End Application server
2. Backend Server
set up a development environment using Docker Compose for a full-stack JavaScript application, including:

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

2. update .env file in the root directory with the following contents:
   
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
    docker-compose -f docker-compose-push.yml build
    ```

4. Run the Docker Containers
    ```
    docker-compose -f docker-compose-run.yml up 
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
    docker compose -f docker-compose-run.yml down
    ```

## Additional Notes

- Any changes made inside the /api-server and /blog-ui folders will be automatically updated due to the volume mounting and hot-reload setup.
- Data persistence is handled through Docker volumes, ensuring that your MySQL data is preserved between container restarts.


## Hackathon Solution Submission Steps:
1. Create a account on docker hub with username and password
    ```
    https://hub.docker.com/
    ```
2. Update docker compose push file
    ```
    Update docker-compose-push.yml as under
    <YOUR_GROUP_ID> -> Your group Id
    <NAME> -> Enter your name
    ```
3. Push Images to Registry
    ```
    docker login
    enter usename and password
    docker-compose -f docker-compose-push.yml push
    ```
   

# MOST IMPORTANT:  
## Submit your solution to our git repo

    1. checkout our master branch
    2. create a new branch basing master -> should be named as <YOUR_GROUP_ID>_<NAME>
    3. create a new folder under submissions -> <Your Group>(Check Sample Group folder)
    4. add docker compose run(that can pull all the images required for your project to run)
    5. add ppt based on sample group folder
    6. add video of you explaining ppt and live demo
    7. push it to our repo with your branch
    8. create a PR to master from your branch
