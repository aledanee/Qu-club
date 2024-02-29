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





testing
-- Insert Users
INSERT INTO users (username, email, password_hash, role) VALUES
('admin1', 'admin1@sks.com', 'hash1', 'SKS_ADMIN'),
('manager1', 'manager1@club.com', 'hash2', 'CLUB_MANAGER'),
('user1', 'user1@site.com', 'hash3', 'REGISTERED_USER');

-- Insert Clubs
INSERT INTO clubs (name, description, manager_id) VALUES
('Chess Club', 'A club for chess enthusiasts.', (SELECT user_id FROM users WHERE username = 'manager1')),
('Book Club', 'A club for people who love reading.', NULL);

-- Insert Activities
INSERT INTO activities (club_id, title, description, status) VALUES
((SELECT club_id FROM clubs WHERE name = 'Chess Club'), 'Weekly Chess Tournament', 'A tournament for all members.', 'APPROVED'),
((SELECT club_id FROM clubs WHERE name = 'Book Club'), 'Monthly Book Discussion', 'Discussion on the selected book of the month.', 'PENDING');

-- Insert Notifications
INSERT INTO notifications (user_id, message, read_status) VALUES
((SELECT user_id FROM users WHERE username = 'user1'), 'Welcome to the platform!', FALSE);


Test Queries

Retrieve all activities of a specific club:
SELECT a.title, a.description
FROM activities a
JOIN clubs c ON a.club_id = c.club_id
WHERE c.name = 'Chess Club';


Find all notifications for a specific user:
SELECT n.message, n.read_status
FROM notifications n
JOIN users u ON n.user_id = u.user_id
WHERE u.username = 'user1';

Check the role-based data retrieval (e.g., fetching all CLUB_MANAGERs):
SELECT username, email
FROM users
WHERE role = 'CLUB_MANAGER';


Verify indexing efficiency (this doesn't return a result but should run efficiently due to the index on status):
EXPLAIN SELECT * FROM activities WHERE status = 'APPROVED';


Update a club manager and observe the cascading effects (no actual effect in this schema, but good to understand the structure):
UPDATE clubs SET manager_id = (SELECT user_id FROM users WHERE username = 'admin1') WHERE name = 'Book Club';




