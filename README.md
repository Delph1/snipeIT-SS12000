# SS12000 Integration with Snipe-IT

**A module for integrating SS12000 (Swedish school administration standard) with Snipe-IT (IT asset management).**

This project provides a **client** and **server** to synchronize users, groups, and licenses between **SS12000** and **Snipe-IT**. The client fetches data from the SS12000 API, and the server handles webhook notifications to keep Snipe-IT updated in real-time.

---

## 📌 Table of Contents

- [SS12000 Integration with Snipe-IT](#ss12000-integration-with-snipe-it)
  - [📌 Table of Contents](#-table-of-contents)
  - [🌟 Features](#-features)
  - [🏗 Architecture](#-architecture)
    - [Components](#components)
    - [Workflow](#workflow)
  - [📋 Prerequisites](#-prerequisites)
  - [🛠 Setup](#-setup)
    - [1. Clone the Repository](#1-clone-the-repository)

---

## 🌟 Features

- **Fetch users and groups** from the SS12000 API.
- **Register webhooks** to receive real-time updates from SS12000.
- **Synchronize data** with Snipe-IT (users, groups, and licenses).
- **JWT authentication** for secure API access.
- **Rate limiting** to prevent abuse.
- **Docker support** for easy deployment alongside Snipe-IT.

---

## 🏗 Architecture

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

## 📋 Prerequisites

- **Docker** and **Docker Compose** (for containerized deployment).
- **Python 3.9+** (for local development).
- **Snipe-IT instance** (running locally or in a container).
- **SS12000 API access** (JWT token for authentication).

---

## 🛠 Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ss12000-snipeit-integration.git
cd ss12000-snipeit-integration
