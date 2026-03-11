import os
import time
from flask import Flask, request, jsonify, render_template
from transformers import pipeline

app = Flask(__name__)

MODEL_NAME = "SamLowe/roberta-base-go_emotions"
THRESHOLD = 0.5

classifier = pipeline(
    "text-classification",
    model=MODEL_NAME,
    top_k=None
)

last_prediction = None
last_latency_ms = 0.0
request_count = 0
error_count = 0
total_latency_ms = 0.0


def analyze_text(text: str):
    """
    Returns:
    - top_5: top 5 labels sorted by score desc
    - predicted: labels with score >= THRESHOLD
    """
    raw_results = classifier(text)[0]
    sorted_results = sorted(raw_results, key=lambda x: x["score"], reverse=True)

    top_5 = sorted_results[:5]
    predicted = [item for item in sorted_results if item["score"] >= THRESHOLD]

    # Fallback so the UI/API always has something meaningful to show
    if not predicted and sorted_results:
        predicted = [sorted_results[0]]

    return top_5, predicted


@app.route("/")
def index():
    return render_template(
        "index.html",
        text="",
        error=None,
        top_5=None,
        predicted=None,
        threshold=THRESHOLD
    )


@app.route("/predict_ui", methods=["POST"])
def predict_ui():
    global last_prediction, request_count, error_count, total_latency_ms, last_latency_ms

    start_time = time.time()

    try:
        text = request.form.get("text", "").strip()

        if not text:
            error_count += 1
            return render_template(
                "index.html",
                text="",
                error="Please enter some text.",
                top_5=None,
                predicted=None,
                threshold=THRESHOLD
            )

        top_5, predicted = analyze_text(text)

        latency_ms = (time.time() - start_time) * 1000
        last_latency_ms = latency_ms
        total_latency_ms += latency_ms
        request_count += 1

        last_prediction = {
            "text": text,
            "top_5": top_5,
            "predicted": predicted
        }

        return render_template(
            "index.html",
            text=text,
            error=None,
            top_5=top_5,
            predicted=predicted,
            threshold=THRESHOLD
        )

    except Exception as e:
        error_count += 1
        return render_template(
            "index.html",
            text=request.form.get("text", ""),
            error=f"Prediction failed: {str(e)}",
            top_5=None,
            predicted=None,
            threshold=THRESHOLD
        )


@app.route("/predict", methods=["POST"])
def predict():
    global last_prediction, request_count, error_count, total_latency_ms, last_latency_ms

    start_time = time.time()

    try:
        data = request.get_json()

        if not data or "text" not in data:
            error_count += 1
            return jsonify({"error": "Missing 'text' in request body"}), 400

        text = str(data["text"]).strip()

        if not text:
            error_count += 1
            return jsonify({"error": "'text' cannot be empty"}), 400

        top_5, predicted = analyze_text(text)

        latency_ms = (time.time() - start_time) * 1000
        last_latency_ms = latency_ms
        total_latency_ms += latency_ms
        request_count += 1

        last_prediction = {
            "text": text,
            "top_5": top_5,
            "predicted": predicted
        }

        return jsonify({
            "model": MODEL_NAME,
            "threshold": THRESHOLD,
            "input": text,
            "predicted_emotions": predicted,
            "top_5_emotions": top_5,
            "latency_ms": round(latency_ms, 2)
        })

    except Exception as e:
        error_count += 1
        return jsonify({"error": str(e)}), 500


@app.route("/monitor")
def monitor():
    avg_latency_ms = total_latency_ms / request_count if request_count > 0 else 0.0
    total_attempts = request_count + error_count
    error_rate = (error_count / total_attempts * 100) if total_attempts > 0 else 0.0

    return render_template(
        "monitor.html",
        status="Running",
        model_name=MODEL_NAME,
        threshold=THRESHOLD,
        requests=request_count,
        errors=error_count,
        avg_latency_ms=round(avg_latency_ms, 2),
        last_latency_ms=round(last_latency_ms, 2),
        error_rate=round(error_rate, 2),
        last_prediction=last_prediction
    )


@app.route("/health")
def health():
    return jsonify({
        "status": "running",
        "model": MODEL_NAME
    }), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))