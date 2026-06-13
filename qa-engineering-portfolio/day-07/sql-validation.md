Section 1 — Database Validation Notes
Using SwiftBank:

Registration Validation

Requirement:

Every registered user must:
- Exist in users table
- Have exactly one account
- Have an audit log

Verification Strategy:

SELECT *
FROM users
WHERE email = 'user@email.com';
SELECT *
FROM accounts
WHERE user_id = ?;
SELECT *
FROM audit_logs
WHERE user_id = ?;
Section 2 — Data Integrity Checks
Check for Duplicate Emails
SELECT
email,
COUNT(*)
FROM users
GROUP BY email
HAVING COUNT(*) > 1;

Expected:

No rows returned
Check for Users with No Accounts
SELECT *
FROM users u
LEFT JOIN accounts a
ON u.user_id = a.user_id
WHERE a.user_id IS NULL;

Expected:

No rows returned
Check for Multiple Accounts
SELECT
user_id,
COUNT(*)
FROM accounts
GROUP BY user_id
HAVING COUNT(*) > 1;

Expected:

No rows returned
Section 3 — Transfer Investigation

Requirement:

Transfer should:
- Debit sender
- Credit receiver
- Create transaction record
- Create audit log

Investigation Plan:

Verify sender balance.
Verify receiver balance.
Verify transaction record exists.
Verify audit log exists.
Verify transfer was not duplicated.

