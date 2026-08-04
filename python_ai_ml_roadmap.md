# Python for AI / ML Development — Learning Roadmap

---

## 1. Python Foundations

- Variables, data types, and operators
- Control flow: conditionals and loops
- Functions, `*args`, `**kwargs`, and closures
- Modules, packages, and virtual environments
- File I/O and exception handling
- Comprehensions and generators
- Object-oriented programming: classes, inheritance, dunder methods
- Type hints and `mypy` static analysis

---

## 2. Scientific Python Stack

- **NumPy** — arrays, broadcasting, vectorized operations, linear algebra
- **Pandas** — DataFrames, indexing, groupby, merging, time series
- **Matplotlib / Seaborn** — line/bar/scatter plots, heatmaps, figure composition
- **SciPy** — optimization, statistics, signal processing, sparse matrices
- **Jupyter Notebooks** — interactive development, magic commands, reproducible reports

---

## 3. Mathematics for ML

- Linear algebra — vectors, matrices, eigenvalues, SVD
- Calculus — gradients, partial derivatives, chain rule, Jacobians
- Probability and statistics — distributions, Bayes' theorem, MLE
- Optimization — gradient descent variants (SGD, Adam), convexity, learning rate schedules
- Information theory — entropy, KL divergence, cross-entropy loss

---

## 4. Classical Machine Learning

- **Supervised learning** — linear/logistic regression, SVMs, decision trees, random forests, gradient boosting (XGBoost, LightGBM)
- **Unsupervised learning** — k-means, DBSCAN, PCA, t-SNE, autoencoders
- **Model evaluation** — train/val/test splits, cross-validation, precision/recall/F1, ROC-AUC
- **Feature engineering** — encoding, scaling, imputation, selection
- **Scikit-learn** — pipelines, `ColumnTransformer`, `GridSearchCV`, custom estimators
- **Imbalanced data** — SMOTE, class weights, threshold tuning

---

## 5. Deep Learning

- **Neural network fundamentals** — forward pass, backpropagation, activation functions
- **PyTorch** — tensors, `nn.Module`, `DataLoader`, custom training loops, `autograd`
- **TensorFlow / Keras** — `Sequential` and functional APIs, `tf.data`, callbacks
- **CNNs** — convolutions, pooling, batch norm, transfer learning (ResNet, EfficientNet)
- **RNNs / LSTMs / GRUs** — sequence modeling, vanishing gradients, teacher forcing
- **Training best practices** — regularization (dropout, weight decay), learning rate warmup, mixed precision (`torch.amp`)
- **GPU programming** — CUDA setup, multi-GPU with `DistributedDataParallel`, profiling

---

## 6. Natural Language Processing

- **Text preprocessing** — tokenization, stemming, lemmatization, stopwords
- **Classical NLP** — TF-IDF, n-grams, Naive Bayes, topic modeling (LDA)
- **Word embeddings** — Word2Vec, GloVe, FastText
- **Transformer architecture** — attention mechanism, positional encoding, encoder/decoder
- **HuggingFace ecosystem** — `transformers`, `datasets`, `tokenizers`, `PEFT` fine-tuning
- **Fine-tuning LLMs** — full fine-tune, LoRA/QLoRA, instruction tuning, RLHF concepts
- **Evaluation** — BLEU, ROUGE, perplexity, BERTScore

---

## 7. Large Language Model (LLM) Engineering

- **Prompt engineering** — zero/few-shot, chain-of-thought, structured output
- **RAG (Retrieval-Augmented Generation)** — chunking strategies, vector stores, re-ranking
- **Embeddings and semantic search** — `sentence-transformers`, cosine similarity, ANN indexes (FAISS, Hnswlib)
- **LLM APIs** — Anthropic Claude SDK, OpenAI API, streaming, function/tool calling
- **Frameworks** — LangChain, LlamaIndex, DSPy
- **Agents and multi-agent systems** — ReAct pattern, tool use, memory, agent orchestration
- **Evaluation and observability** — LLM-as-judge, tracing with LangSmith / Weave / Arize

---

## 8. MLOps and Production

- **Experiment tracking** — MLflow, Weights & Biases (W&B)
- **Data versioning** — DVC, LakeFS
- **Model packaging** — `pickle`, `joblib`, `torch.save`, ONNX export
- **Serving** — FastAPI / Flask, TorchServe, Triton Inference Server, BentoML
- **Containerization** — Docker, Docker Compose, multi-stage builds for ML images
- **CI/CD for ML** — GitHub Actions pipelines, automated retraining triggers
- **Monitoring** — data drift detection, model performance dashboards, alerting

---

## 9. Data Engineering for ML

- **SQL and databases** — window functions, CTEs, query optimization, PostgreSQL
- **Big data tools** — PySpark, Dask, Polars for large-scale data processing
- **Data pipelines** — Apache Airflow, Prefect, Dagster
- **Feature stores** — Feast, Hopsworks, offline vs. online features
- **Cloud data warehouses** — BigQuery, Snowflake, Redshift integration with Python
- **Streaming** — Kafka, Kinesis, real-time feature computation

---

## 10. Specialized Domains (choose by focus)

- **Computer Vision** — object detection (YOLO, DETR), segmentation, OpenCV, video understanding
- **Time Series** — forecasting (Prophet, N-BEATS, PatchTST), anomaly detection, feature extraction
- **Reinforcement Learning** — Gym/Gymnasium, Q-learning, PPO, model-based RL
- **Graph ML** — PyTorch Geometric, node classification, link prediction, GNNs
- **Multimodal AI** — vision-language models (CLIP, LLaVA), speech (Whisper), image generation (Diffusers)

---

## Suggested Progression

```
Foundations → Scientific Stack + Math → Classical ML → Deep Learning
      ↓                                                       ↓
NLP / LLM Engineering ←————————————————— Specialized Domains
      ↓
MLOps + Data Engineering (run in parallel once models are working)
```

> **Tip:** Build a project at the end of each section — projects compound your learning faster than courses alone.
