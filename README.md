# globe-guard-ai-disaster-forecaster
# GlobeGuard – AI-Powered Geo-Disaster Impact Forecaster

GlobeGuard is a serverless application built with AWS Lambda and Amazon Bedrock that delivers location-based natural disaster impact forecasts in real time. It transforms raw disaster alerts into clear, human-readable summaries to help individuals and communities take timely action.

---

## 🚀 How It Works

1. **User Input (via API Gateway)**  
   Users submit their city or geographic location.

2. **Disaster Alert Trigger (via EventBridge)**  
   Scheduled or simulated disaster events (e.g., earthquake, flood) are fetched and trigger AWS Lambda.

3. **Forecast Generation (via Lambda + Bedrock)**  
   AWS Lambda formats the disaster event and user location into a prompt. It then invokes Amazon Bedrock (Claude) to generate a natural-language impact forecast.

4. **Delivery**  
   The forecast is:
   - Emailed to users via Amazon SES, and/or
   - Stored in Amazon S3 for later access.

---

## 🧠 How AWS Lambda Was Used

AWS Lambda is the backbone of the GlobeGuard architecture. It performs all key logic in the forecasting pipeline:

- **Processes disaster event data** triggered by Amazon EventBridge.
- **Receives user input** through Amazon API Gateway and connects it to relevant alerts.
- **Invokes Amazon Bedrock (Claude)** using Python and Boto3 to generate summaries.
- **Sends output** via Amazon SES or stores it in Amazon S3.
- **Runs serverless**, making it highly scalable and cost-efficient.

All Lambda executions are securely managed using IAM and monitored using CloudWatch.

---

## 📦 Built With

- AWS Lambda
- Amazon API Gateway
- Amazon EventBridge
- Amazon Bedrock (Claude)
- Amazon SES
- Amazon S3
- AWS IAM
- Amazon CloudWatch
- Python (Boto3)

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.
