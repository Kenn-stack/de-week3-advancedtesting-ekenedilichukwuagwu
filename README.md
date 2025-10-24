# 🛒 ShopLink ETL Pipeline

**ShopLinkETL** is a modular ETL (Extract–Transform–Load) pipeline designed to process e-commerce data from the `shoplink.json` dataset. It reads, validates, transforms, analyzes, and exports cleaned data in a streamlined workflow.

---

## 🚀 Features

* **Reader** → Reads raw JSON data (`shoplink.json`)
* **Validator** → Cleans and validates records for consistency and completeness
* **Transformer** → Transforms raw data into a structured, analysis-ready format
* **Analyzer** → Computes insights like total revenue, average revenue, and customer churn analysis
* **Exporter** → Saves the transformed dataset as `shoplink_cleaned.json`

---

## ⚙️ How It Works

The pipeline follows a step-by-step ETL process:

1. **Read** raw data from `shoplink.json`
2. **Validate** each record (e.g., removing duplicates or invalid entries)
3. **Transform** the cleaned data into a uniform structure
4. **Analyze** key metrics (revenue, churn, etc.)
5. **Export** the processed dataset to `shoplink_cleaned.json`

---

## 🧠 Usage

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the ETL pipeline

You can run the ETL directly from the project root:

```bash
python -m order_pipeline.pipeline
```

---

## 📊 Example Output

After running the ETL, you’ll get:

* **Raw Input** → `shoplink.json`
* **Cleaned Output** → `shoplink_cleaned.json`
* **Console Summary** → Revenue statistics and churn insights

---

## 🧾 License

This project is licensed under the **MIT License** — feel free to use, modify, and distribute it.


