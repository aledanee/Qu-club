Use Cases for Student Club Management System (SCMS)
1. Use Case: Manage Club Pages (SKS Admin)

Actor: SKS Admin

Description: The SKS Admin creates, assigns managers to, and deletes club pages.

Preconditions:

    The SKS Admin is logged into the system.

Main Flow:

    The SKS Admin selects the option to manage club pages.
    The system presents options to create a new club page, assign a club manager, or delete an existing club page.
    The SKS Admin performs the desired action.
    The system updates accordingly and confirms the action to the SKS Admin.

Alternative Flows:

    The SKS Admin decides to cancel the action, and no changes are made.

Postconditions:

    The club page is created, updated, or deleted as requested.

2. Use Case: Approve/Reject Activity Form (SKS Admin)

Actor: SKS Admin

Description: The SKS Admin reviews and approves or rejects activity forms submitted by Club Managers.

Preconditions:

    An activity form is submitted for approval.

Main Flow:

    The SKS Admin receives a notification of a submitted activity form.
    The SKS Admin reviews the form details.
    The SKS Admin approves or rejects the form.
    The Club Manager receives a notification regarding the approval status.

Alternative Flows:

    The SKS Admin requests additional information before making a decision.

Postconditions:

    The activity form is either approved and published or rejected.

3. Use Case: Search and View Club Information (Registered User)

Actor: Registered User

Description: The Registered User searches for clubs and views their pages and weekly activities.

Preconditions:

    The Registered User is logged into the system.

Main Flow:

    The Registered User inputs a search query to find a specific club.
    The system displays the search results.
    The Registered User selects a club to view its main page and weekly activity table.
    The system displays the selected club's information and activities.

Alternative Flows:

    No results are found, and the user modifies the search query.

Postconditions:

    The Registered User accesses the club's information and activities.

4. Use Case: Manage Activity Posts (Club Manager)

Actor: Club Manager

Description: The Club Manager creates, edits, or deletes activity posts after getting approval.

Preconditions:

    The Club Manager is logged into the system.

Main Flow:

    The Club Manager selects the option to manage activity posts.
    The system presents options to create a new post, edit an existing post, or delete a post.
    The Club Manager performs the desired action.
    The system updates and confirms the action.

Alternative Flows:

    The Club Manager decides to cancel the action, and no changes are made.

Postconditions:

    The activity post is created, updated, or deleted as requested.
