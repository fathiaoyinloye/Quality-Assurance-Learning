Register


[Missing]
Is email verification mandatory?
a. what fields are needed to register?
b. what is the minimum or maximum characters of password?
c. what letter combination does the password takes
d. What password rules are required?
e. can the same email be use to register twice
f. can a user register more than once
g.how is the email verified
h. via what is it sent, is it through mail 
i. does a phone nummber need to be verify too
j. what age can register
k. What happens if verification fails?

[Ambiguous]
 The requirement says "strong password".
l.  What does strong mean?
m.  what combinaion of characters does it need to be strong
n.  what min or mx length does it needs to be strong
    The requirement says fast login
o.  how many seconds does it takes 95% of users to login
    The requirement says "email shold be verifed ".
p.  how would it be verified
q.  how long does the verification links takes before it expires
r.  will otp be sent for verification? 
s.  how many seconds does it takes the otp to get to the user

[Contradictory]
t.  Requirement A says email is optional.
    Requirement B says verification email is required.
u.  Requirement A says password at least 8 characters is optional.
    Requirement B says password must be 10 characters.
v.  Requirement A says for 22 above.
    Requirement B says must be an adult.


Login
[Missing]
a. what fields are needed for login?
b. what is the minimum or maximum characters?
c. what letter combination does it takes
d. how long can a user stays logged in on a device
e. what happen if there us a network gliche
e. does the system remembers a user once logged in on a device
f. can a user forget password
g.  what do you mean when
h.

[Ambiguous]
    requirement says lock account after multiple trials
i.  what do you mean by lock account after multiple trials
j.  does multiple trials means once or twice or trials?
k.  those the lock account comes open after some minutes?
l.  if yes how many minutes?

m. The requirement says Notify the user if credentials are incorrect. 
n. Does this mean we should tell them exactly or use a generic message ("Invalid email or password") for security reason
o. What happens if a user tries to log in, but their account was previously suspended by an admin?

[Contradictory]
p.  Requirement A says login with email.
    Requirement B says login with username.
q.  Requirement A says user can only stay login for at most thirty minutes.
    Requirement A says user can only stay login for at  twenty minutes.
r.  Requirement A says Usernames must be exactly 8 characters long for login.
    Requirement B: says Users must use their Email Address as their username for login





Password Reset
[Missing]
a. how would the password be reser?
b. is it an otp?
c. is it email?
d. how long will it takefor the link to expire?
e. how long will it take the otp to expire
f. when pasword is reset will it still stay logged in on other devices
g.what happen if there is a network outage while waiting for the otp
h. via what is it sent, is it through mail 
i. does a phone nummber need to be verify too
j. What happens if otp or email fails?

[Ambiguous]
 The requirement says user have to prove they own the account.
k.  What does that mean?
l.  does it mean there would have been some question before hand like favorite food or color
m.  what do you mean by reset password through a friend, those it mean a friend have already been registed or invited to be  a third party it securing your account
n. 
[Contradictory]
o.  Requirement A says otp should be sent to mail.
    Requirement B says otp should be sent to phonenumber.
p.  Requirement A says cannot reset password maximum twice in a day.
    Requirement B says password reset can only be allowed once a day.

Daily Reflection
I learnt that while testing happens even before development, it is important to note that a clear unambiquous requirement document can also help in making it better and preventing bugs.
A requirement document could even be a source of defect to the system that is why we have to catch it before it even get to the developer.


Summary
Today I learned that QA starts before development begins. Requirements themselves can contain defects in the form of missing information, ambiguity, or contradictions. Before designing test cases, I should first review requirements and ask clarification questions. I learned that a good QA engineer challenges assumptions and identifies gaps that could cause developers to build the wrong functionality. During the exercise, I reviewed Login, Registration, and Password Reset requirements and discovered many unanswered questions related to validation rules, verification processes, session management, and failure scenarios. I also learned that requirement defects can eventually become software defects if they are not identified early.





