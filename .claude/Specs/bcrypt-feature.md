# Secure Password Hashing (bcrypt) Feature

## Overview

Replace insecure MD5 password hashing with bcrypt-based password hashing to improve authentication security and align with modern security practices.

## Purpose

Protect user credentials against rainbow table attacks, brute-force attacks, and database compromise scenarios.

## Functional Requirements

### FR-BCRYPT-1

The system SHALL hash all newly created passwords using bcrypt.

### FR-BCRYPT-2

The system SHALL never store plaintext passwords.

### FR-BCRYPT-3

The system SHALL use bcrypt's automatic per-password salt generation.

### FR-BCRYPT-4

The system SHALL verify passwords using bcrypt verification APIs during authentication.

### FR-BCRYPT-5

Legacy MD5 hashes SHALL be considered unsupported and migrated or reset.

## Non-Functional Requirements

### NFR-BCRYPT-1

Password hashes SHALL include embedded salt and cost-factor metadata.

### NFR-BCRYPT-2

Password verification SHALL use bcrypt's secure comparison mechanisms.

### NFR-BCRYPT-3

The hashing implementation SHALL be centralized in `backend/app/core/security.py`.

## Affected Files

* backend/app/core/security.py
* backend/app/services/auth_service.py
* backend/app/api/routes/auth.py
* backend/app/db/session.py
