GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY '' WITH GRANT OPTION;
FLUSH PRIVILEGES;

CREATE SCHEMA test;
USE test;
CREATE TABLE AccessRights (
    Access_ID int PRIMARY KEY,
    Access_type varchar(50) NOT NULL
);

CREATE TABLE Staff (
    Staff_ID int PRIMARY KEY,
    Staff_FName Varchar(50) NOT NULL,
    Staff_LName Varchar(50) NOT NULL,
    Dept Varchar(50) NOT NULL,
    Country Varchar(50) NOT NULL,
    Email Varchar(50) NOT NULL,
    Access_Rights int,
    FOREIGN KEY (Access_Rights) REFERENCES AccessRights(Access_ID)
);

CREATE TABLE Role (
	Role_Name Varchar(20) Primary Key,
    Role_Desc Longtext Not Null
);

CREATE TABLE Role_Skill (
    Role_Name varchar(20),
    Skill_Name varchar(100),
    PRIMARY KEY (Role_Name, Skill_Name),
    FOREIGN KEY (Role_Name) REFERENCES Role(Role_Name),
    UNIQUE (Skill_Name)
);

CREATE TABLE Staff_Skill (
    Staff_ID int,
    Skill_Name Varchar(20),
    FOREIGN KEY (Staff_ID) REFERENCES Staff(Staff_ID),
    FOREIGN KEY (Skill_Name) REFERENCES Role_Skill(Skill_Name)
);

CREATE TABLE Job_Listing (
    JobList_ID INT PRIMARY KEY AUTO_INCREMENT,
    Role_Name Varchar(50),
    publish_Date DATE NOT NULL,
    Closing_date DATE NOT NULL,
    FOREIGN KEY (Role_Name) REFERENCES Role(Role_Name)
);

CREATE TABLE Job_Application (
    JobList_ID INT NOT NULL,
    Staff_ID INT NOT NULL,
    PRIMARY KEY (JobList_ID, staff_id),
    FOREIGN KEY (JobList_ID) REFERENCES Job_Listing(JobList_ID),
    FOREIGN KEY (Staff_ID) REFERENCES Staff(Staff_ID)
);

USE SPM_KUIH;

-- Insert data into the Role table
INSERT INTO Role (Role_Name, role_desc)
VALUES
    ('Software Developer', 'Responsible for developing software applications and systems.'),
    ('Data Analyst', 'Analyzes data to provide insights and support decision-making.'),
    ('Marketing Specialist', 'Plans and executes marketing campaigns and strategies.'),
    ('Sales Representative', 'Sells products or services to customers and clients.');

-- Insert data into the Job_Listing table
INSERT INTO Job_Listing (Role_Name, publish_Date, Closing_date)
VALUES
    ('Software Developer', '2023-09-01', '2023-09-15'),
    ('Data Analyst', '2023-09-02', '2023-09-16'),
    ('Marketing Specialist', '2023-09-03', '2023-09-17'),
    ('Sales Representative', '2023-09-04', '2023-09-18'),
    ('Software Developer', '2023-09-05', '2023-09-19');

-- Insert data into Role_Skill table 
INSERT INTO Role_Skill (Role_Name, Skill_Name)
VALUES
    ('Software Developer', 'Web development, API integration, Debugging'),
    ('Data Analyst', 'Data analysis, SQL, Data mining'),
    ('Marketing Specialist', 'Content marketing, Branding, Public relations'),
    ('Sales Representative', 'Relationship building, Communication skills, Product knowledge');


