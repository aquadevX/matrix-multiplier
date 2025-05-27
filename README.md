# ⚙️ Advanced Matrix Multiplier (CPU Only)

An advanced Python project that benchmarks matrix multiplication using:
- ✅ Pure Python (nested loops)
- ✅ NumPy (C-optimized)
- ✅ Multiprocessing (parallel CPU execution)

---

## 🧪 Benchmark Results

Sample output for matrix sizes:

Matrix Size | Python Time (s) | NumPy Time (s) | Parallel Time (s)
10 | 0.00012 | 0.00001 | 0.08040
100 | 0.16129 | 0.00208 | 0.31324
200 | 1.27561 | 0.00736 | 0.74819
300 | 3.83211 | 0.02284 | 1.54211


---

## 🏗️ Project Structure

matrix-multiplier/
├── benchmarks/
│ └── benchmark.py
├── src/
│ ├── numpy_version.py
│ ├── parrallel_python.py
│ └── pure_python.py
└── README.md


---

## ▶️ Run It

```bash
python benchmarks/benchmark.py

## Requirements
pip install numpy

💡 Learnings
Clean code structuring

Benchmarking techniques

Optimizing with parallel computing

NumPy's raw speed 🔥