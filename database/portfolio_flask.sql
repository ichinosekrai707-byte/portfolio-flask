-- Run this once in MySQL Workbench / phpMyAdmin.
CREATE DATABASE IF NOT EXISTS portfolio_flask;
USE portfolio_flask;

CREATE TABLE IF NOT EXISTS project (
    ID          INT AUTO_INCREMENT PRIMARY KEY,
    Title       VARCHAR(80)  NOT NULL,
    Description TEXT         NOT NULL,
    Type        VARCHAR(10)  NOT NULL,   -- WEB or APP
    TechStack   VARCHAR(100) NOT NULL DEFAULT '',
    Link        VARCHAR(255) NOT NULL DEFAULT ''
);

CREATE TABLE IF NOT EXISTS skill (
    ID   INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(45) NOT NULL
);

-- Starter skills (you can add or delete more on the /admin page)
INSERT INTO skill (Name) VALUES
    ('Java'),
    ('MySQL'),
    ('Networking basics'),
    ('Always learning');
