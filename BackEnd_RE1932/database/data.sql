CREATE DATABASE IF NOT EXISTS RE1932;

USE RE1932;

CREATE TABLE IF NOT EXISTS Properties (
    HomeId INT PRIMARY KEY AUTO_INCREMENT,
    Price VARCHAR(20),
    Beds VARCHAR(20),
    Bath VARCHAR(20),
    Area VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS Address (
    HomeId INT,
    Zip VARCHAR(10),
    Street VARCHAR(255),
    City VARCHAR(50),
    State VARCHAR(50),
    Latitude DECIMAL(9, 6),
    Longitude DECIMAL(9, 6),
    Country VARCHAR(50),
    FOREIGN KEY (HomeId) REFERENCES Properties(HomeId)
);