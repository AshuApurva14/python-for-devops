# GUIDE.md 

Class 1: Python for DevOps + Boto3 Deep Dive

Python environment setup, virtual environments, and project structure
Data structures DevOps engineers actually use — dicts, lists, sets for parsing API responses
os and subprocess modules — running shell commands, reading system state from Python
File operations, JSON/YAML parsing
Error handling and exception management
Creating reusable Python modules and a custom CLI
Working with JSON and YAML — parsing, validating, transforming config and API responses
Python logging best practices — levels, formatters, rotating file handlers
Project: AWS Resource Audit CLI Build a production-grade Python CLI that connects to AWS via boto3, paginates through EC2, S3, and RDS resources across regions, generates a formatted report of all running resources with costs, and logs every operation. Runs on a schedule or on demand.

Class 2: Working with API’s + CRUD operations

Uses requests module to make API CRUD requests (Create, Read, Update, Delete)
Implements proper error handling for API calls
Handles API authentication and headers
Parses and validates API responses
boto3 architecture — sessions, clients vs resources, regions, profiles
Paginating through AWS APIs with get_paginator — why it matters at scale
Environment-based config management — .env, os.environ, secrets handling
Error handling and exception management for AWS API calls
Project: API CRUD Automation Script Python script using the requests module to make full CRUD operations against a REST API — proper auth headers, error handling, response validation, and structured logging for every call.