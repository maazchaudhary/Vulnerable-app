# Security Remediation Patch — Replace MD5 with Secure Password Hashing

This patch updates the Spec-Driven Document (SDD) to replace insecure MD5 password hashing with secure password hashing using bcrypt or Argon2.

---

# 1. Update Non-Functional Requirements

## Replace

```md
**NFR-6:** The system SHALL use MD5 hashing without salt for password storage.
```

## With

```md
**NFR-6:** The system SHALL securely hash passwords using a modern adaptive password hashing algorithm such as bcrypt or Argon2 with automatic salting.

**NFR-6.1:** The system SHALL never store plaintext passwords.

**NFR-6.2:** The system SHALL generate a unique cryptographic salt for each password hash.

**NFR-6.3:** The system SHALL support password verification using the selected hashing algorithm during authentication.
```

---

# 2. Update POST /signup Behavior

## Replace

```md
- Stores credentials (password hashed via MD5)
```

## With

```md
- Stores credentials using secure password hashing (bcrypt or Argon2)
- Password hashes SHALL include automatic per-password salting
```

---

# 3. Update POST /login Behavior

## Replace

```md
- Hashes password using MD5
```

## With

```md
- Verifies password using secure password hash verification (bcrypt or Argon2)
```

---

# 4. Replace Section 6.5

## Replace Entire Section

```md
### 6.5 Weak Password Storage

**Location:** Password hashing implementation

**Vulnerability:** Passwords hashed using MD5 without salt.

**Attack Vector:** If database is exposed, MD5 hashes can be cracked via rainbow tables.

**Expected Behavior:** Passwords can be reverse-engineered from database dump.

**Educational Objective:** Understand why strong hashing (bcrypt, Argon2) with salt is necessary.
```

## With

```md
### 6.5 Secure Password Storage

**Location:** Password hashing implementation

**Security Requirement:** Passwords SHALL be securely hashed using bcrypt or Argon2 with automatic salting and configurable work factors.

**Expected Behavior:** Password hashes SHALL resist rainbow table attacks and computational cracking attempts.

**Educational Objective:** Understand modern password hashing practices and why adaptive hashing algorithms are preferred over legacy cryptographic hashes such as MD5.
```

---

# 5. Update Data Model Notes

## Replace

```md
- Password stored as MD5 hex digest (no salt)
```

## With

```md
- Password stored as bcrypt or Argon2 hash with embedded salt and work factor metadata
```

---

# 6. Update OWASP Alignment Table

## Replace

```md
| A07: Identification and Authentication Failures | Weak Password Storage |
```

## With

```md
| A07: Identification and Authentication Failures | Secure Password Storage Mitigation |
```

---

# 7. Update Vulnerability Acceptance Criteria

## Replace

```md
- [ ] MD5 password hashes are crackable from database dump
```

## With

```md
- [ ] Passwords are securely hashed using bcrypt or Argon2
- [ ] Password hashes include automatic salting
- [ ] Plaintext passwords are never stored in the database
```

---

# 8. Update Verification Plan

## Replace

```md
5. Weak Password Storage:
   - Download database
   - Open in SQLite browser
   - Verify passwords are stored as MD5 hashes
   - Verify hashes can be cracked with rainbow tables
```

## With

```md
5. Secure Password Storage:
   - Register a new user account
   - Open the database in SQLite browser
   - Verify passwords are stored as bcrypt or Argon2 hashes
   - Verify hashes contain embedded salt metadata
   - Verify plaintext passwords are not recoverable
   - Verify login succeeds using password verification APIs
```

---

# 9. Update Educational Impact Metrics

## Replace

```md
- Students can successfully exploit all 8 vulnerabilities using appropriate techniques
```

## With

```md
- Students can successfully exploit the intentionally vulnerable components of the application
- Students can identify and verify secure remediation of the password hashing subsystem
```

---

# 10. Update Critical Files Reference

## Replace

```md
| `backend/app/core/security.py` | Password hashing (MD5 implementation) |
```

## With

```md
| `backend/app/core/security.py` | Secure password hashing and verification utilities |
| `frontend/static/css/styles.css` | CSS variables for light/dark theming and UI styling |
| `frontend/templates/login.html` | Login page with dark mode toggle (lines 14-19, 110-142) |
| `frontend/templates/signup.html` | Signup page with dark mode toggle (lines 14-19, 98-130) |
| `frontend/templates/dashboard.html` | Dashboard with dark mode toggle (lines 14-19, 140-172) |
```

---

# 11. Update Glossary

## Replace

```md
| **MD5** | Cryptographic hash function (deprecated for password storage) |
```

## With

```md
| **bcrypt** | Adaptive password hashing algorithm designed for secure password storage |
| **Argon2** | Modern password hashing algorithm resistant to GPU and memory-based attacks |
| **CSS Custom Properties** | CSS variables that allow defining values in one place and reusing them throughout stylesheets |
| **localStorage** | Web API for persisting key-value pairs in a web browser with no expiration time |
| **data-theme Attribute** | HTML data attribute used to toggle between CSS variable sets for theming |
| **prefers-color-scheme** | CSS media query that detects user's system-level dark/light mode preference |
```

---

# 12. Update Vulnerability Quick Reference Table

## Replace

```md
| 5 | Weak Password Storage | POST /signup | password | `security.py:10` |
```

## With

```md
| 5 | Secure Password Storage Mitigation | POST /signup | password | `security.py:10` |
```

---

# 13. Missing Areas to Make the SDD Fully Spec-Driven

The current SDD is already strong, but a few areas should be adjusted to fully satisfy a complete spec-driven structure.

---

## A. Problem Statement

### Current Status

Partially covered in:

* Context
* Purpose
* Educational Objectives

### Recommended Addition

Add a dedicated section after `1.1 Purpose`:

```md
### 1.1.1 Problem Statement

Traditional cybersecurity education often relies on theoretical explanations of vulnerabilities without giving students practical experience exploiting and remediating real systems.

Students frequently lack hands-on exposure to:
- authentication bypass attacks,
- cross-site scripting,
- session hijacking,
- insecure password storage,
- insecure configuration patterns.

This application addresses that gap by providing an intentionally vulnerable web application where students can safely practice identifying, exploiting, and mitigating real-world web vulnerabilities.
```

---

## B. Functional Requirements

### Current Status

Fully covered.

The document already contains:

* FR-1 through FR-24
* Authentication requirements
* Session requirements
* Search requirements
* Database access requirements

No major adjustment required.

---

## C. API Contracts (Inputs / Outputs / Data Shapes)

### Current Status

Mostly covered.

You already define:

* request parameters,
* endpoint behavior,
* responses,
* status codes.

### Missing Area

The document does not formally define response schemas/data shapes.

### Recommended Addition

Add a subsection:

````md
### 5.6 Response Data Contracts

#### Authentication Error Response

```json
{
  "error": {
    "code": "INVALID_CREDENTIALS",
    "message": "Invalid credentials."
  }
}
````

#### Session Data Shape

```json
{
  "user_id": 1,
  "username": "student1",
  "email": "student@example.com"
}
```

````

This makes the API contracts more explicit.

---

## D. Constraints

### Current Status
Covered well in Section 11.

Includes:
- legal constraints,
- technical constraints,
- educational constraints.

No major adjustment required.

---

## E. Edge Cases and Error Handling

### Current Status
Partially covered.

You mention some validation and errors, but edge cases are not centralized.

### Recommended Addition
Add a dedicated section:

```md
## 5.7 Edge Cases and Error Handling

| Scenario | Expected Behavior |
|----------|------------------|
| Missing username during signup | Return validation error |
| Duplicate username | Reject registration |
| Empty login request | Return authentication error |
| Invalid session cookie | Redirect to login |
| Missing search query | Display query required message |
| Database unavailable | Return 500 Internal Server Error |
| Malformed request body | Return validation error |
| Unsupported HTTP method | Return 405 Method Not Allowed |
````

````

This improves completeness significantly.

---

## F. Acceptance Criteria

### Current Status
Fully covered.

You already include:
- Functional acceptance
- Vulnerability acceptance
- Educational acceptance

This section is strong and well structured.

---

# Final Assessment

| Area | Status |
|---|---|
| Problem Statement | Needs dedicated section |
| Functional Requirements | Complete |
| API Contracts | Mostly complete |
| Constraints | Complete |
| Edge Cases & Error Handling | Needs dedicated section |
| Acceptance Criteria | Complete |

---

# Overall Assessment

The document is already approximately:

```text
85–90% complete as a professional spec-driven document.
````

The main missing pieces are:

* dedicated Problem Statement section,
* formal response schemas/data shapes,
* centralized edge case/error handling section.

After adding those, the SDD becomes enterprise-quality and fully aligned with a spec-driven engineering workflow.

---

# Result

After applying these changes:

```text
SPEC ↔ IMPLEMENTATION ↔ TESTS
```

will remain aligned after migrating from MD5 to bcrypt/Argon2.

---

# 14.  Dark Mode Toggle Feature

## Overview

The application now includes a dark mode toggle feature that allows users to switch between light and dark themes. The implementation uses CSS custom properties for theming, JavaScript for state management, and localStorage for preference persistence.

## Implementation Details

### CSS Variables System (styles.css)

**Light Mode Variables** (`:root`, lines 9-47):
- Background colors: `--header-bg`, `--auth-body-bg`, `--card-bg`, `--dashboard-bg`
- Text colors: `--text-primary`, `--text-secondary`, `--title-color`
- Input styling: `--input-bg`, `--input-border`, `--input-focus-border`
- Button colors: `--btn-primary`, `--btn-primary-hover`
- Error states: `--error-bg`, `--error-border`, `--error-color`
- Toggle button: `--toggle-btn-bg`, `--toggle-btn-hover`, `--toggle-btn-text`

**Dark Mode Variables** (`[data-theme="dark"]`, lines 49-87):
- Complete override of light mode variables with dark theme values
- Maintains visual consistency across all UI elements
- Ensures accessibility and readability in both modes

### HTML Template Changes

All three templates contain identical toggle button markup:
```html
<button class="theme-toggle" id="theme-toggle" aria-label="Toggle dark mode">
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" id="theme-icon">
    <path d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707-.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"/>
  </svg>
  <span>Light</span>
</button>
```

### JavaScript Implementation

Each template contains identical inline JavaScript for theme management:

**Key Functions:**
- `setTheme(isDark)`: Sets theme by adding/removing `data-theme="dark"` attribute
- Icon switching between sun and moon SVG paths
- Text label updates between "Light" and "Dark"
- localStorage persistence

**Theme Detection Priority:**
1. localStorage for saved theme preference
2. System preference via `window.matchMedia('(prefers-color-scheme: dark)')`
3. Default to light mode

**Event Handling:**
- Click event listener on toggle button
- Toggles between light and dark modes
- Persists choice to localStorage

## Critical Files Modified

| File | Description |
|------|-------------|
| `frontend/static/css/styles.css` | CSS variables for theming, toggle button styles |
| `frontend/templates/login.html` | Toggle button markup and JavaScript (lines 14-19, 110-142) |
| `frontend/templates/signup.html` | Toggle button markup and JavaScript (lines 14-19, 98-130) |
| `frontend/templates/dashboard.html` | Toggle button markup and JavaScript (lines 14-19, 140-172) |

## Non-Functional Requirements

**NFR-9:** The system SHALL support user-selectable dark/light themes with preference persistence.

**NFR-9.1:** The system SHALL respect OS-level dark mode preferences on first visit.

**NFR-9.2:** The system SHALL persist theme preferences across sessions using localStorage.

**NFR-9.3:** The system SHALL provide accessible toggle controls with proper ARIA labels.

## Verification Plan

1. Light Mode Verification:
   - Load any page (login, signup, dashboard)
   - Verify light theme is applied by default
   - Check all UI elements use light mode colors

2. Dark Mode Verification:
   - Click the toggle button
   - Verify dark theme is applied
   - Check all UI elements use dark mode colors
   - Verify icon changes to moon
   - Verify text changes to "Dark"

3. Persistence Verification:
   - Set theme to dark mode
   - Refresh the page
   - Verify dark mode persists
   - Close and reopen browser
   - Verify dark mode persists across sessions

4. System Preference Verification:
   - Clear localStorage
   - Set OS to dark mode
   - Load any page
   - Verify dark mode is applied automatically
   - Set OS to light mode
   - Load any page
   - Verify light mode is applied

5. Cross-Page Verification:
   - Set theme on login page
   - Navigate to signup page
   - Verify theme persists
   - Navigate to dashboard
   - Verify theme persists

## Educational Impact

The dark mode feature demonstrates:
- CSS custom properties for maintainable theming
- Client-side state management with localStorage
- System preference detection using CSS media queries
- Accessible UI controls with proper ARIA labels
- Consistent feature implementation across multiple pages
