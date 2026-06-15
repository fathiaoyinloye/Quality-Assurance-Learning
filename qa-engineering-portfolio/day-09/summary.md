What I Tested Today
Authentication
Registration validation
Budget creation validation
API error handling
HTTP response codes
What I Learned
APIs should return validation errors (400), not server errors (500/501), when users submit invalid input.
Missing validation annotations can allow invalid data into the system.
A successful API call is not enough; the returned status code must also be verified.
Real QA work involves discovering requirements from the system and proving where behavior differs from expected behavior.
##