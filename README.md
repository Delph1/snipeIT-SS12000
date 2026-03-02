# SS12000 Integration with Snipe-IT

**A module for integrating SS12000 (Swedish school administration standard) with Snipe-IT (IT asset management).**

This project provides a **client** and **server** to synchronize users, groups, and licenses between **SS12000** and **Snipe-IT**. The client fetches data from the SS12000 API, and the server handles webhook notifications to keep Snipe-IT updated in real-time.

---

## Table of Contents

- [Features](#features)
- [Architecture](#architecture)
- [Prerequisites](#prerequisites)
- [Setup](#setup)

---

## Features

- **Fetch users and groups** from the SS12000 API.
- **Manage Licenses** using the BOL API (v1.2) for orders, assignments, and returns.
- **Register webhooks** to receive real-time updates from SS12000.
- **Synchronize data** with Snipe-IT (users, groups, and licenses).
- **JWT authentication** for secure API access.
- **Rate limiting** to prevent abuse.
- **Docker support** for easy deployment alongside Snipe-IT.

---

## Architecture

### Components

| Component               | Description                                                                                     |
|-------------------------|-------------------------------------------------------------------------------------------------|
| **SS12000 Client**       | Fetches users, groups, and registers webhooks with the SS12000 API.                              |
| **SS12000 Server**       | Receives webhook notifications, fetches updated data, and synchronizes with Snipe-IT.          |
| **Snipe-IT**             | IT asset management system where users, groups, and licenses are synchronized.               |
| **Docker**              | Containerizes the client and server to run alongside Snipe-IT.                                 |
| **JWT & Rate Limiting**  | Secures the API and prevents abuse.                                                            |

### Workflow

1. **SS12000 Client** fetches users and groups from the SS12000 API.
2. **SS12000 Client** registers a webhook with the SS12000 API.
3. **SS12000 Server** receives webhook notifications when data changes.
4. **SS12000 Server** fetches updated data from the SS12000 API.
5. **SS12000 Server** synchronizes the updated data with Snipe-IT.

---

## Prerequisites

- **Docker** and **Docker Compose** (for containerized deployment).
- **Python 3.9+** (for local development).
- **Snipe-IT instance** (running locally or in a container).
- **SS12000 API access** (JWT token for authentication).

---

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Delph1/snipeIT-SS12000.git
cd snipeIT-SS12000
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a .env file in the project root:

```bash
touch .env

# SS12000 API
SS12000_JWT_TOKEN=your_ss12000_jwt_token
WEBHOOK_SECRET=your_webhook_secret

# Snipe-IT API
SNIPEIT_API_TOKEN=your_snipeit_api_token

# JWT
JWT_SECRET_KEY=your_jwt_secret_key
```