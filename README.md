# AI-Assisted Text Classification System
### BERT-Powered Complaint vs. Feedback Classifier

This project is a microservice-based application that classifies user input into **Complaints**, **Queries**, or **Feedback**. It leverages a **BERT (Bidirectional Encoder Representations from Transformers)** model for Natural Language Processing, served via a **FastAPI** backend, and integrated into a **Node.js** gateway.

---

## 🏗 System Architecture

The application is split into two specialized services to ensure scalability and separation of concerns:

1.  **AI Inference Engine (Python/FastAPI):** Loads the BERT model and performs text classification.
2.  **Gateway API (Node.js/Express):** Acts as the primary entry point for users, handling requests and communicating with the AI service.



---

## 🚀 Tech Stack

* **Language:** Python 3.9, Node.js 18
* **AI/ML:** Hugging Face Transformers, PyTorch, BERT
* **API Frameworks:** FastAPI (Python), Express (Node.js)
* **Containerization:** Docker, Docker Compose
* **Communication:** RESTful API (Axios/Uvicorn)

---

## 🛠 Installation & Setup

### Prerequisites
* [Docker Desktop](https://www.docker.com/products/docker-desktop/) (recommended)
* Git

### Running with Docker (Recommended)
This is the easiest way to get the entire system running in seconds.

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/bert-microservice.git](https://github.com/YOUR_USERNAME/bert-microservice.git)
    cd bert-microservice
    ```

2.  **Build and Start the containers:**
    ```bash
    docker-compose up --build
    ```

3.  **Access the services:**
    * **Node.js Gateway:** `http://localhost:3000`
    * **FastAPI Docs:** `http://localhost:8000/docs`

---

## 📡 API Usage

### Classify Text
**Endpoint:** `POST /classify` (via Node.js Gateway)

**Request Body:**
```json
{
  "text": "The delivery was delayed by three days and the package was damaged."
}
