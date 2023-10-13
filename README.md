# Bank System - DevOps Course Assignment | Felix GG

## Overview

The Bank System is a comprehensive application designed to simulate a banking environment. It is divided into a backend API, a frontend interface, and associated infrastructure configurations. The backend API is developed in Python and is responsible for handling all the business logic related to banking operations. The frontend is developed using Vue.js and provides a user interface for interacting with the bank system. The infrastructure configurations are defined using Bicep and are used to deploy the application to Azure.

Deployments to Azure are set-up so that only the production code is deployed when a new release in the `main` branch is created. On the other hand, all development code is deployed in the `dev` branch. This allows for testing of new features and bug fixes before they are deployed to production.

## Table of Contents

- [Overview](#overview)
- [Backend API](#backend-api)
- [Frontend](#frontend)
- [Infrastructure](#infrastructure)
- [Testing](#testing)
- [Deployment](#deployment)

## Backend API

### Overview

The backend is developed in Python and serves as the API for the bank system. It is responsible for handling and processing all the business logic related to banking operations.

### Structure

- `__init__.py`: Initializes the Python package for the backend.
- `models.py`: Defines the data models used in the application.
- `routes.py`: Contains the route definitions and associated handlers for the API.

### Testing

The backend includes a suite of tests to ensure its functionality:

- `conftest.py`: Provides configurations for the test suite.
- `test_routes.py`: Contains functional tests for route handlers.
- `test_model.py`: Includes unit tests for data models.

## Frontend

### Overview

The frontend is developed using Vue.js and provides a user interface for interacting with the bank system.

### Structure

- `App.vue`: The main Vue component that serves as the entry point for the application.
- `main.js`: Initializes the Vue application.
- `index.js`: Defines the routes for the Vue application.
- `AppAccounts.vue`, `HomePage.vue`, `Skull.vue`: Various Vue components used in the application.

## Infrastructure

The `app-service.bicep` file contains infrastructure-as-code configurations for deploying the application.

## Testing

The project includes a series of tests located in the `backend/tests` directory to ensure the functionality of the backend API.

## Deployment

Deployment configurations and workflows are defined in the `.github/workflows/full-stack-bank.yml` file, which sets up a CI/CD pipeline for the application using GitHub Actions,
