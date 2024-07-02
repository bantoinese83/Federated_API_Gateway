# 🚀 Federated API Gateway

Welcome to the Federated API Gateway project! This repository demonstrates how to set up a federated GraphQL API using Apollo Gateway and FastAPI with Graphene for Python. The project is composed of multiple subgraphs, including `users` and `posts`, that are combined into a single supergraph by the Apollo Gateway.

## 📋 Table of Contents

- [Introduction](#introduction)
- [Architecture](#architecture)
- [Getting Started](#getting-started)
- [Running the Services](#running-the-services)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## 🌟 Introduction

In this project, we build a federated GraphQL architecture with the following components:

- **Users Subgraph**: Manages user data.
- **Posts Subgraph**: Manages post data.
- **Apollo Gateway**: Combines the subgraphs into a unified API.

## 🏗️ Architecture

The architecture includes:

- **Users Service**: A FastAPI app providing user-related data.
- **Posts Service**: A FastAPI app providing post-related data.
- **Apollo Gateway**: A Node.js service combining the subgraphs into a single GraphQL API.

## 🚀 Getting Started

Follow these instructions to set up the project on your local machine.

### Prerequisites

- Python 3.8+
- Node.js 14+
- npm 6+

### Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/bantoinese83/Federated_API_Gateway.git
    cd Federated_API_Gateway
    ```

2. **Install Python dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

3. **Install Node.js dependencies**:
    ```sh
    cd gateway
    npm install
    ```

## 🏃‍♂️ Running the Services

1. **Start the Users Service**:
    ```sh
    uvicorn users_service:app --reload --port 8000
    ```

2. **Start the Posts Service**:
    ```sh
    uvicorn posts_service:app --reload --port 8001
    ```

3. **Start the Apollo Gateway**:
    ```sh
    cd gateway
    node gateway.js
    ```

## 📚 Usage

Once the services are running, you can access the federated API at `http://localhost:4000/graphql`.

### Example Queries

- **Query a user with their posts**:
    ```graphql
    {
      user(id: "1") {
        id
        username
        posts {
          id
          title
        }
      }
    }
    ```

- **Query a post with its author**:
    ```graphql
    {
      post(id: "1") {
        id
        title
        author {
          id
          username
        }
      }
    }
    ```

## 🛠️ Technologies Used

- **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python 3.6+.
- **Graphene**: A Python library for building GraphQL schemas/types fast and easily.
- **Graphene Federation**: Extends Graphene to support Apollo Federation.
- **Apollo Gateway**: A GraphQL gateway that builds a federated data graph by combining multiple subgraphs.
- **Node.js**: A JavaScript runtime built on Chrome's V8 JavaScript engine.

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add your feature'`).
5. Push to the branch (`git push origin feature/your-feature`).
6. Open a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

✨ Happy Coding! ✨
