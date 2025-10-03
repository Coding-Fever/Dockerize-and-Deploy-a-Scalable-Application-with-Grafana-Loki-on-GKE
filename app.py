from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "🚀 Flask Microservice running on GKE 🐳 | Containerized with Artifact Registry 🗂️ | Scalable & Monitored with Grafana 📊"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
