# Test Case Execution Report

| TC ID | Test Description | Request Body | Expected Result | Actual Result | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **TC-001** | Create budget without login | `{"name":"June Budget", "period":"MONTHLY"}` | 401 Unauthorized | 401 Unauthorized - "Invalid, expired or malformed token." | **PASS** |
| **TC-002** | Create budget with valid token. | `{"name":"June Budget", "period":"MONTHLY"}` | 201 Created | 201 Created | **PASS** |
| **TC-003** | Sign Up with an existing username | `{"email": "fathiaoyinloye21@gmail.com", "firstName": "Fathia", "lastName": "Oyinloye", "password": "fathiaoyinloye21", "username": "haliyahkareem"}` | 400 Bad Request | 400 Bad Request <br>`{"message": "Username not available"}` | **PASS** |
| **TC-004** | Sign Up with valid details | `{"email": "fathiaoyinloye@gmail.com", "firstName": "Fathia", "lastName": "Oyinloye", "password": "fathiaoyinloye", "username": "fathiaoyinloye"}` | 201 Created | 201 Created | **PASS** |
| **TC-005** | Create budget with valid token. | `{"name":"June Budget", "period":"MONTHLY"}` | 201 Created | 202 Created | **PASS** |
| **TC-006** | Create budget with empty name. | `{"name": " ", "period": "MONTHLY"}` | 400 Bad Request | 201 Created | **FAIL** |
| **TC-007** | Create budget with empty body. | `{}` | 400 Bad Request | 500 Internal Server Error | **FAIL** |
| **TC-008** | Create budget with invalid period. | `{"name": "June Budget", "period": "INVALID"}` | 400 Bad Request | 400 Bad Request | **PASS** |
| **TC-009** | Create budget with space as name | `{"name": " ", "period": "MONTHLY"}` | 400 Bad Request | 201 Created | **FAIL** |
| **TC-010** | create budget with empty period | `{"name": "June Budget", "period": " "}` | 400 Bad Request | 400 Bad Request | **PASS** |
| **TC-011** | Sign Up with an empty username | `{"email": "fathiaoyinloye21@gmail.com", "firstName": "Fathia", "lastName": "Oyinloye", "password": "fathiaoyinloye21", "username": ""}` | 400 Bad Request | 400 Bad Request | **PASS** |
| **TC-012** | Sign Up with an empty email | `{"email": "", "firstName": "Fathia", "lastName": "Oyinloye", "password": "fathiaoyinloye21", "username": "haliyahkareem"}` | 400 Bad Request | 501 Internal Server Error | **FAIL** |
| **TC-013** | Sign Up with space as password | `{"email": "fathiaoyinloye21@gmail.com", "firstName": "Fathia", "lastName": "Oyinloye", "password": " ", "username": "haliyahkareem"}` | 400 Bad Request | 400 Bad Request | **PASS** |