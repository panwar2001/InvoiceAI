# 🧾 InvoiceAI: Local GLM-OCR Pipeline

Enterprise-grade local OCR pipeline for extracting structured JSON data from invoices using the **GLM-4V** architecture optimized for Apple Silicon (MLX).

![Invoice AI Banner](https://img.shields.io/badge/OCR-GLM--4V-blue?style=for-the-badge&logo=ai)
![MLX Optimized](https://img.shields.io/badge/Optimization-MLX-orange?style=for-the-badge&logo=apple)
![JSON Output](https://img.shields.io/badge/Format-JSON-green?style=for-the-badge&logo=json)

## 🌟 Features
- **Local Execution**: Keep your sensitive financial data private by running everything on-device.
- **MLX Optimized**: Specifically tuned for high-performance inference on Mac with Apple Silicon (M1/M2/M3/M4).
- **Structured Extraction**: Automatically parses total amounts, dates, and addresses into clean JSON.
- **Batch Processing**: Capable of analyzing multiple invoices in a single run.

## 🚀 Getting Started

### 1. Environment Setup
Create a dedicated virtual environment and install the necessary dependencies:

```bash
# Create and activate environment
python3 -m venv glm-ocr-env
source ./glm-ocr-env/bin/activate

# Install requirements
pip3 install mlx-lm mlx-vlm
```

### 2. Download Model Weights
Download the quantized GLM-OCR weights (6-bit) to your local machine:

```bash
python3 download_glmocr_weights.py
```

### 3. Run Extraction
Execute the pipeline to process the sample invoices in the `./data` directory:

```bash
python3 index.py
```

## 📊 Sample Output
The pipeline extracts data into the following format:

```json
{
  "amount": "$1,250.50",
  "date": "October 12, 2025",
  "from_address": "TechFlow Solutions, 123 Innovation Drive, San Francisco, CA",
  "to_address": "Global Logistics Inc, 456 Supply Chain Road, New York, NY",
  "amount": "100.00"  
}
```

## 📂 Project Structure
- `index.py`: Main entry point for OCR extraction.
- `download_glmocr_weights.py`: Utility to fetch model weights from Hugging Face.
- `/data`: Directory containing invoice images (PNG/JPG).
- `/models`: Local storage for the GLM-OCR model.

## 📝 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
