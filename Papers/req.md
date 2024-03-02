SKS Admin
-Create Club Page
-Delete Club Page
-Assign Club Manager
-Approve/Reject Activity Form
-Receive Notification (whenever a change occured in club page)
-Delete Activity (If something inappropria te is shared on the club page, deletion will be done by SKS.)
-Search Club Page
-Announce All Activities (On the main page will be displayed)



Registered user
-SEARCH CLUBS
-DISPLAY WEEKLY ACTIVITY TABLE
-DISPLAY CLUB MAIN PAGE


Club Manager
-Fill activity form
-Publish Activity Post
-Edit/Delete Activity Post
-Receive Notification (whenever a change occured in club page by SKS)


For structuring a system with FastAPI to accommodate the roles and functionalities you've outlined, you would need to design models, API endpoints, and access control mechanisms for each role and action. Here's a breakdown of how you can structure your FastAPI application for each role:

1. SKS Admin
Endpoints:

POST /clubs: Create a club page.
DELETE /clubs/{club_id}: Delete a club page.
POST /clubs/{club_id}/assign_manager: Assign a club manager.
PUT /activities/{activity_id}/approve: Approve an activity form.
PUT /activities/{activity_id}/reject: Reject an activity form.
GET /notifications: Receive notifications on changes.
DELETE /activities/{activity_id}: Delete inappropriate activities.
GET /clubs/search: Search club pages.
POST /activities/announce: Announce all activities.


2. Registered User
Endpoints:

GET /clubs/search: Search clubs.
GET /activities/weekly: Display weekly activity table.
GET /clubs/{club_id}: Display club main page.


3. Club Manager
Endpoints:

POST /activities: Fill and submit an activity form.
POST /activities/{activity_id}/publish: Publish an activity post.
PUT /activities/{activity_id}: Edit an activity post.
DELETE /activities/{activity_id}: Delete an activity post.
GET /notifications: Receive notifications.


Models:

Club: Represents the club information (e.g., name, description).
Activity: Represents an activity's details (e.g., name, description, status).
User: Represents users, with roles (e.g., SKS Admin, Registered User, Club Manager).
Access Control:

Implement role-based access control (RBAC) to ensure that endpoints are accessible only to users with the appropriate roles.
For notifications, you can use WebSockets or Server-Sent Events (SSE) to update clients in real-time.
Additional Considerations:

Database Design: Design your database schema to support these operations efficiently, considering relationships between clubs, users, and activities.
Authentication & Authorization: Implement JWT or OAuth for secure authentication and authorization.
Validation: Ensure to validate data for each endpoint, especially for creation and update operations.
Error Handling: Implement proper error handling to respond with appropriate error messages and status codes.


Phase 1: Requirements Gathering and Planning
Define Detailed Requirements:

Gather all the detailed functional and non-functional requirements for each role (SKS Admin, Club Manager, and Registered User).
Define the specific features, user stories, and expected behaviors within the system.
System Architecture Design:

Plan the overall system architecture, deciding on how the frontend and backend will communicate, the structure of your database, and how you'll manage user authentication and authorization.
Technology Stack Confirmation:

Confirm that FastAPI for the backend, MySQL for the database, and Figma for frontend design are the best choices based on your requirements. Also, decide on the frontend technology you will use to implement the Figma designs.

Phase 2: Backend Development
Setup Development Environment:

Prepare your development environment with all necessary installations (e.g., FastAPI, database server, any development tools).
API Development:

Develop the API endpoints required for all functionalities using FastAPI.
Implement authentication and authorization to handle different roles and permissions.
Database Integration:

Design and implement your MySQL database schema.
Integrate the database with your FastAPI backend to ensure data persistence and retrieval.


Phase 3: Frontend Development
Figma Design Implementation:

Convert your Figma designs into actual code using your chosen frontend technology.
Ensure that the designs are responsive and user-friendly.
Frontend Integration:

Connect your frontend with the FastAPI backend, ensuring that the frontend can consume the API endpoints effectively.
Implement dynamic data rendering, form submissions, and interactive UI elements based on your requirements.


Phase 4: Testing
Unit and Integration Testing:

Conduct thorough testing for each component and service, ensuring they work as expected in isolation and when integrated.
Cover backend logic, API endpoints, database integrity, and frontend functionality.
User Acceptance Testing (UAT):

Involve stakeholders or potential users to test the system in a staging environment.
Gather feedback and make any necessary adjustments.


Phase 5: Deployment and Maintenance
Deployment:

Deploy your backend and frontend to production, ensuring secure and scalable hosting environments.
Set up monitoring and logging to track the system's health and user activities.
Maintenance and Updates:

Regularly update the system with patches, security updates, and feature enhancements.
Monitor user feedback and system performance to plan future improvements.
