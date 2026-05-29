# Software Design Document (SDD)

## Vulnerable Web Application - Security Lab

**Version:** 1.0.0

## 1. Purpose

This document defines the system architecture, design requirements, interfaces, and acceptance criteria for the Vulnerable Web Application. The application provides a controlled environment for learning web security vulnerabilities and secure remediation techniques.

---

## 2. Problem Statement

Students often learn security vulnerabilities theoretically without practical exposure to real attack scenarios. This application provides a hands-on environment where users can identify, exploit, and remediate common web application vulnerabilities safely.

---

## 3. System Overview

### Architecture

The application follows a three-layer architecture:

* Presentation Layer (HTML/CSS/JavaScript)
* Application Layer (FastAPI Routes and Services)
* Data Layer (SQLite Database)

### Technology Stack

| Component          | Technology                  |
| ------------------ | --------------------------- |
| Backend            | FastAPI                     |
| Database           | SQLite                      |
| Frontend           | HTML, CSS, JavaScript       |
| Session Management | Starlette SessionMiddleware |
| Runtime            | Python 3.9+                 |

---

## 4. Functional Requirements

### FR-1 User Registration

Users SHALL register using username, email, and password.

### FR-2 Authentication

Users SHALL authenticate using valid credentials.

### FR-3 Session Management

Authenticated sessions SHALL be maintained until logout.

### FR-4 Dashboard Access

Protected resources SHALL require authentication.

### FR-5 Search Functionality

Users SHALL be able to search records using the search endpoint.

### FR-6 Vulnerability Demonstration

The system SHALL provide intentionally vulnerable functionality for educational purposes.

---

## 5. Security Requirements

### NFR-1 Password Security

Passwords SHALL be securely hashed using bcrypt.

### NFR-2 Password Protection

Plaintext passwords SHALL never be stored.

### NFR-3 Session Security

Authenticated sessions SHALL be validated before accessing protected resources.

### NFR-4 Input Validation

User input SHALL be validated before processing.

### NFR-5 Educational Isolation

The application SHALL be restricted to educational and training environments.

---

## 6. API Contracts

### Authentication Error Response

```json
{
  "error": {
    "code": "INVALID_CREDENTIALS",
    "message": "Invalid credentials."
  }
}
```

### Session Object

```json
{
  "user_id": 1,
  "username": "student1",
  "email": "student@example.com"
}
```

---

## 7. Data Model

### User

| Field         | Type    |
| ------------- | ------- |
| id            | Integer |
| username      | String  |
| email         | String  |
| password_hash | String  |

### Session

| Field      | Type    |
| ---------- | ------- |
| session_id | String  |
| user_id    | Integer |

---

## 8. Error Handling

| Scenario             | Expected Behavior     |
| -------------------- | --------------------- |
| Missing username     | Validation error      |
| Duplicate username   | Registration rejected |
| Invalid credentials  | Authentication error  |
| Invalid session      | Redirect to login     |
| Missing search query | Validation error      |
| Database unavailable | HTTP 500              |
| Unsupported method   | HTTP 405              |

---

## 9. Constraints

### Technical

* FastAPI backend
* SQLite database
* Local deployment only

### Educational

* Vulnerabilities must remain reproducible
* Learning objectives must remain measurable

### Legal

* Educational use only
* Not intended for production deployment

---

## 10. Acceptance Criteria

### Functional

* Registration succeeds
* Login succeeds
* Dashboard access requires authentication
* Search functionality operates correctly

### Security

* Passwords stored using bcrypt
* Plaintext passwords never stored
* Session validation enforced

### Educational

* Vulnerabilities demonstrable
* Remediation techniques verifiable

---

## 11. Related Feature Specifications

| Feature                          | Specification                           | Plan                                 |
| -------------------------------- | --------------------------------------- | ------------------------------------ |
| Dark Mode Toggle                 | `.claude/features/dark-mode-feature.md` | `.claude/features/dark-mode-plan.md` |
| Secure Password Hashing (bcrypt) | `.claude/features/bcrypt-feature.md`    | `.claude/features/bcrypt-plan.md`    |

---

## 12. References

* PRD.md
* TDD.md
* OWASP Top 10
* FastAPI Documentation

**End of Document**
