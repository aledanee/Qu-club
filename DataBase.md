Step 1: Define Tables

- Users Table: To store information about all users, including SKS Admins, Club Managers, and Registered Users.
- Clubs Table: To maintain details about different clubs.
- Activities Table: To store information on various activities proposed or carried out by the clubs.
- Notifications Table: To manage notifications for users based on their roles and interactions.



Commands

CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    role ENUM('SKS_ADMIN', 'CLUB_MANAGER', 'REGISTERED_USER') NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);




CREATE TABLE clubs (
    club_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);





CREATE TABLE activities (
    activity_id INT AUTO_INCREMENT PRIMARY KEY,
    club_id INT NOT NULL,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    status ENUM('PENDING', 'APPROVED', 'REJECTED') NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (club_id) REFERENCES clubs(club_id)
);





CREATE TABLE notifications (
    notification_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    message TEXT NOT NULL,
    read_status BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);





Step 3: Implement Relations

  
ALTER TABLE clubs ADD COLUMN manager_id INT NULL;
ALTER TABLE clubs ADD CONSTRAINT fk_manager_id FOREIGN KEY (manager_id) REFERENCES users(user_id);

#Activity and User Notifications: Ensure that activities can trigger notifications to the relevant users based on their roles or actions.


Step 4: Indexing


CREATE INDEX idx_users_role ON users(role);
CREATE INDEX idx_activities_status ON activities(status);



Step 5: Testing
After creating these tables, insert some test data and try out some queries to ensure everything is working as expected.
