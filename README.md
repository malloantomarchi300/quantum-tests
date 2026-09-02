# Quantum Random Number Generator (QRNG)

A personal quantum computing project built with [Qiskit](https://qiskit.org/). This is the starting point of a codebase I intend to keep building on over time, exploring quantum circuits and algorithms.

The first piece of functionality is a quantum random number generator: a single qubit is put into superposition with a Hadamard gate and then measured, producing an outcome that is genuinely random rather than pseudo-random like `random.random()`.

Every run is effectively a "quantum coin flip": measuring the qubit in superposition collapses it to `0` or `1` with an exact 50/50 probability.

## Status

Early stage — currently contains a single working example. Expect the structure and scope to evolve as I add more quantum experiments, abstractions, and tooling.

## How it works

The circuit in `qrng.py` consists of three steps:

1. **Initialize** — a 1-qubit / 1-classical-bit circuit is created.
2. **Superposition** — a Hadamard (`H`) gate is applied to the qubit, putting it into an equal 50/50 superposition of `|0⟩` and `|1⟩`.
3. **Measure** — the qubit is measured, collapsing the superposition and storing the result (`0` or `1`) in the classical bit.

The circuit is then run 100 times ("shots") on Qiskit's local `AerSimulator` to show the statistical breakdown, and an optional histogram of the results is plotted with Matplotlib.

## Requirements

- Python 3.8+
- Dependencies listed in [`requirements.txt`](requirements.txt):
  - [Qiskit](https://pypi.org/project/qiskit/) (`qiskit`)
  - [Qiskit Aer](https://pypi.org/project/qiskit-aer/) (`qiskit-aer`)
  - [Matplotlib](https://pypi.org/project/matplotlib/) (`matplotlib`)

## Installation

Create and activate a virtual environment, then install the dependencies:

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

> Note: `.venv/`, `venv/`, and `env/` are already ignored via `.gitignore`.

## Usage

Run the script:

```bash
python qrng.py
```

You'll see the circuit diagram, followed by the results of 100 quantum coin flips, for example:

```
Our Quantum Circuit:
     ┌───┐┌─┐
  q: ┤ H ├┤M├
     └───┘└╥┘
 c: 1/═════╩═
           0

Results of 100 quantum coin flips: {'0': 51, '1': 49}
```

Because the outcomes are genuinely random, the exact counts will differ on every run — though with enough shots they will always hover close to a 50/50 split.

If a window doesn't appear when the histogram code runs, your backend may not support interactive plots. You can instead save the figure by replacing `plt.show()` with:

```python
plt.savefig("histogram.png")
```

## Project structure

```
quantum-project/
├── .gitignore        # Python virtual environment ignores
├── qrng.py           # The quantum random number generator
├── README.md         # This file
└── requirements.txt  # Python dependencies
```

## License

[Apache License 2.0](LICENSE)
