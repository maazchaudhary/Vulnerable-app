# Dark Mode Toggle Feature

## Overview

Implement a dark mode toggle that allows users to switch between light and dark themes across the Vulnerable Web Application.

## Purpose

Improve usability and accessibility by allowing users to choose a theme that matches their preference and environment.

## Functional Requirements

### FR-DM-1: Theme Toggle

* The application SHALL provide a theme toggle button on:

  * Login page
  * Signup page
  * Dashboard page

### FR-DM-2: Theme Switching

* Users SHALL be able to switch between light and dark themes without reloading the page.

### FR-DM-3: Preference Persistence

* The selected theme SHALL be stored in localStorage.
* The application SHALL restore the saved theme on subsequent visits.

### FR-DM-4: System Preference Detection

* When no saved preference exists, the application SHALL use the user's OS preference via `prefers-color-scheme`.

### FR-DM-5: Accessibility

* The toggle SHALL include an ARIA label.
* Theme colors SHALL maintain sufficient contrast for readability.

## Non-Functional Requirements

### NFR-DM-1

The theme switch SHALL complete instantly without a page refresh.

### NFR-DM-2

The selected theme SHALL remain consistent across all application pages.

## Affected Files

* frontend/static/css/styles.css
* frontend/templates/login.html
* frontend/templates/signup.html
* frontend/templates/dashboard.html
