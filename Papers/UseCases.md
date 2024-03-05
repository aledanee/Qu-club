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





Use Case: Manage Activity Posts with Approval (Club Manager)

Actor: Club Manager

Description: The Club Manager initiates changes to activity posts, including creation, editing, or deletion. However, these changes must be approved by an SKS Admin before they go live on the system.

Preconditions:

    The Club Manager is logged into the system.
    The Club Manager has the necessary permissions to propose changes to activity posts.

Main Flow:

    The Club Manager selects the option to manage activity posts.
    The system presents options to create a new post, edit an existing post, or delete a post.
    The Club Manager submits the proposed changes for approval.
    An approval request is sent to the SKS Admin.
    The SKS Admin reviews the request and either approves, rejects, or requests further information.
    The Club Manager receives a notification regarding the decision.
    If approved, the system updates the activity post accordingly.

Alternative Flows:

    If the Club Manager decides to cancel the action before submission, no changes are made or submitted for approval.
    If the SKS Admin requests additional information, the Club Manager provides the necessary details, and the review process repeats.

Postconditions:

    If approved, the activity post is created, updated, or deleted as per the Club Manager's request and is visible in the system.
    If rejected, the proposed changes are not implemented, and the activity post remains unchanged.
