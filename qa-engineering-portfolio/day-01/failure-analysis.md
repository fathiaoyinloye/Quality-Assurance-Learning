## Application

LinkedIn

## 50 Possible Failure Scenarios

Authentication

1. User cannot login with valid credentials.
2. User cannot reset password
3. user have to login for everytime app is use on the same device
4. user cannot change email if one is no longer available
5. Notifications do not appear.
6. User suddenly logged out while on the app
7. Logged into an account without verification
8. log out and logged in on same device, verification was needed
9.  password changes was not effective
10. Password reset email never arrives.



Registration / Account Creation
10. User can register with an unexisting email
11. User can set up weak password
12. User can create account with a username that already exist
13. OTP was never sent to verify email or phone number
14. incorrect verify you are human with correct answers
15. User can have a username with just spaces
16. User receive otp but it says expires within given timefrane



Profile Management
17. Profile picture upload fails.
18. username cannot be changed
19. User cannot add Education because school is not listed
20. Skills update fails
21. Uploaded profile image disappears after refresh.
22. Cover image upload fails.
23. unable to add working experience

Search
24. Incorrect results
25. Slow response
26. No pagination
27. Search returns no results even when matching records exist.



Messaging
28. All messages lost
29. deleted messages seen
30. message marked as devilered but didnt get to the receiver
31 Message duplicated
32 Message not delivered
33 Empty message accepted
34 Receiver can delete sender message




Feed / Posts
35. deleted post seen
36. friend's post was never seen
37. unable to like post
38. user is unable to create post
39. post created  cannot be edited
40. post created cannot be deleted
41. liked on a post never increase even though it was liked countless time


Notifications
42. Connection Request Notification was never gotten
43. Notification for a message not sent
44. Notification for job was never sent
45. User didnt get notify of a new comment on his/her post
46. User didnt get notification for an email change.

Jobs
47. unable to apply for job
48. job for 18 above can be seen and apply for by under 18
49. System fails to detect fraudulent job postings.
50. job position already occupied but it still in the job search for application

## Exploratory Testing Notes

- Tested login.
- Tested search.
- Tested profile editing.
- Tested messaging.
- Tested post
- Tested authentication
- Tested registration
- Tested Profile management

## Assumptions I Made

1. Search results are accurate.
2. Messages are delivered.
3. Profile updates are saved.
4. Notifications are timely.
5. Password changes take effect.
6. Cover image updates are saved.
7. All jobs shown are still open.
8. Connection requests are actually delivered.
9. Deleted posts are permanently removed.
10. Logout clears the session.

## Reflection

What did I test today?

I explored LinkedIn's login, messaging, search and profile features.

What did I learn?

I realized I often assume features are working without consciously verifying them.

## Summary

Today I learned that QA is different from simply testing whether a feature works. QA is about identifying what could break, challenging assumptions, and thinking about risks before users encounter problems. I practiced this by analyzing LinkedIn features and creating failure scenarios for authentication, registration, messaging, search, notifications, jobs, and posts. I also learned that just because something appears to work—such as deleting a post—does not mean it is actually working correctly throughout the entire system. I need to verify assumptions like whether data is really deleted, whether other users can still see it, and whether related features are affected.