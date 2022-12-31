-- create database
CREATE DATABASE m_database;
USE m_database;

-- create table for weather API values extracted by weaimport.py
CREATE TABLE weather_api (
    weather_api_id MEDIUMINT NOT NULL AUTO_INCREMENT,
    weather_api_date DATE,
    temp1 DECIMAL(5,2),
    temp_min DECIMAL(5,2),
    temp_max DECIMAL(5,2),
    loc_1 VARCHAR(30),
    weather_main VARCHAR(30),
    PRIMARY KEY(weather_api_id)
);

-- create table for moisture readings from pi
CREATE TABLE pi_reading (
    pi_reading_id MEDIUMINT NOT NULL AUTO_INCREMENT,
    pi_reading_date DATE,
    pi_reading_time TIME,
    pi_reading_val DOUBLE(7,4),
	pi_reading_notes VARCHAR(256),
    PRIMARY KEY(pi_reading_id)
);

-- create user, modify password value
CREATE USER 'm_user'@'localhost' IDENTIFIED BY 'PASSWORD';

-- grant read to m_user
GRANT READ ON m_database.* TO 'm_user'@'localhost';