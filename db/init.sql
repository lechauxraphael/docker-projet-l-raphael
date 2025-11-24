CREATE DATABASE IF NOT EXISTS bandnames;
USE bandnames;

CREATE TABLE IF NOT EXISTS adjectives (
  id INT AUTO_INCREMENT PRIMARY KEY,
  adjective VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS nouns (
  id INT AUTO_INCREMENT PRIMARY KEY,
  noun VARCHAR(100) NOT NULL
);

INSERT IGNORE INTO adjectives (id, adjective) VALUES
(1,'Last'),(2,'Midnight'),(3,'Blue'),(4,'Silent'),(5,'Broken'),
(6,'Golden'),(7,'Ancient'),(8,'Neon'),(9,'Wild'),(10,'Lucky');

INSERT IGNORE INTO nouns (id, noun) VALUES
(1,'Biscuits'),(2,'Llamas'),(3,'Rockets'),(4,'Tigers'),(5,'Owls'),
(6,'Sundays'),(7,'Waves'),(8,'Shadows'),(9,'Pilots'),(10,'Nomads');
