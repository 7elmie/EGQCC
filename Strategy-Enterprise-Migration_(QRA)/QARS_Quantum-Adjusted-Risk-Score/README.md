# Quantum-Adjusted Risk Score (QARS)

A strategic framework and computational engine for evaluating and prioritizing post-quantum cryptography migration based on multi-dimensional risk analysis.

---

## Strategic Framework for the Quantum-Adjusted Risk Score (QARS)

### 1. The Quantum Cybersecurity Imperative

The emergence of quantum computing represents a systemic risk to the global architecture of digital trust. For decades, the security of the internet has rested on the mathematical difficulty of factoring large integers and computing discrete logarithms—problems that classical computers would require billions of years to solve. However, quantum computing does not merely hack faster; it rewrites the fundamental mathematics of encryption. This shift necessitates a transition from binary threat models, which view "Q-Day" as a distant switch, to a quantitative risk-scoring engine that functions as an investment prioritization tool. By moving toward a granular assessment model, organizations can achieve true algorithmic lifecycle management and maintain a defensible risk posture in the face of evolving capabilities.

The core risk involves the vulnerability of current public-key encryption standards, such as RSA and Elliptic Curve Cryptography (ECC), which are susceptible to Shor's algorithm. Shor's algorithm provides an exponential speedup for factoring, rendering contemporary asymmetric primitives obsolete once a Cryptographically Relevant Quantum Computer (CRQC) is realized. Adversaries are currently exploiting this reality through "Harvest Now, Decrypt Later" (HNDL) strategies, intercepting and stockpiling encrypted traffic today to unlock it retroactively. Conversely, symmetric encryption—specifically AES-256—demonstrates higher resilience; it is subject only to Grover's algorithm, which provides a quadratic speedup. This allows symmetric systems to remain secure simply by doubling key lengths, whereas public-key systems require a total architectural overhaul.

The transition from classical to quantum-resistant infrastructure is not a technical refresh but a strategic necessity to mitigate long-tail data persistence risks.

---

### 2. Foundations of Quantum Risk: The Mosca Inequality

Measuring quantum risk begins with understanding temporal variables. The window of organizational vulnerability is defined not by the arrival of a quantum computer alone, but by the relationship between data shelf-life, the speed of cryptographic migration, and the maturation of the threat horizon.

Dr. Michele Mosca formulated this relationship through the "Mosca Inequality," a framework used to determine if an organization has already run out of time to protect its most sensitive secrets.

**X + Y > Z**

- **X (Shelf-life)**: The duration for which the data must remain confidential (e.g., state secrets, long-term financial records, or genomic data).
- **Y (Migration Timeline)**: The time required to transition the organization's entire cryptographic infrastructure to Post-Quantum Cryptography (PQC).
- **Z (Threat Horizon)**: The predicted time until a Cryptographically Relevant Quantum Computer (CRQC) emerges.

This equation reveals the phenomenon of "Crypto-Procrastination." If X + Y exceeds Z, the organization has entered a period of retroactive exposure. Because a full cryptographic migration can take a decade or more, and certain data lifespans extend for thirty years or more, many enterprises are already in a state of "post-quantum insolvency." To quantify the severity of this mismatch, we utilize the **Mosca Ratio** (r = (X+Y)/Z) as the primary driver for our granular risk modeling.

While the Mosca Inequality provides a critical binary threshold, the QARS model translates this threshold into a prioritized execution list.

---

### 3. The QARS Model: Dimensional Analysis and Weighting

The Quantum-Adjusted Risk Score (QARS) transforms Mosca's threshold into a multi-factor, weighted index. Its objective is to move beyond simple "pass/fail" logic to provide a continuous score that enables C-suite advisors to calibrate investments based on organizational risk appetite and regulatory mandates.

The QARS model integrates three core dimensions:

1. **Timeline Risk (T)**: This dimension maps the Mosca ratio r into a [0, 1] interval using a logistic scaling function. As the migration window (Y) and data shelf-life (X) consume the remaining time in the threat horizon (Z), the score rises sharply to reflect the escalating urgency of "Harvest Now, Decrypt Later" exposure.
2. **Sensitivity Risk (S)**: This maps qualitative data labels (Low to Critical) to numeric values, explicitly incorporating regulatory mandates like GDPR, HIPAA, and DORA. This ensures the potential impact of a confidentiality breach—including legal, financial, and reputational damage—is mathematically weighted.
3. **Exposure Risk (E)**: This factor quantifies the practical ability of an adversary to intercept ciphertext. It is calculated as the product of Cryptographic Visibility (v) and Operational Harvestability (q). Crucially, v=0 for PQC-protected assets, as quantum-resistant algorithms negate the efficacy of Shor's algorithm, rendering "harvesting" moot for quantum adversaries.

#### Sector-Specific Weighting Profiles

The QARS model utilizes adjustable weights (w_T, w_S, w_E) to allow for precise risk calibration.

| Sector Profile   | Timeline (w_T) | Sensitivity (w_S) | Exposure (w_E) | Strategic Focus                                               |
| ---------------- | -------------- | ----------------- | -------------- | ------------------------------------------------------------- |
| Finance          | 0.4            | 0.4               | 0.2            | Mitigating long-tail data persistence and regulatory risk.    |
| IoT / Embedded   | 0.5            | 0.2               | 0.3            | Managing constrained upgrade cycles and device longevity.     |
| Cloud Services   | 0.3            | 0.2               | 0.5            | Reducing automated data harvesting and multi-tenant exposure. |
| General Baseline | 0.33           | 0.33              | 0.33           | Balanced prioritization for standard enterprise assets.       |

Adjusting these weights ensures that the QARS output remains an actionable analytical kernel for roadmap prioritization.

---

### 4. Calculation Methodology and Asset Scoring Examples

Applying QARS to a cryptographic inventory enables the triage of assets based on objective mathematical urgency. This section demonstrates the step-by-step application of the QARS formula using a "General Baseline" weighting where each factor weight is 0.33.

#### Risk Scoring Calculations

**Asset A: Confidential Document Archive**

- **Inputs**: Shelf-life (X) = 15 years; Migration time (Y) = 5 years; Threat Horizon (Z) = 12 years.
- **Factor Scores**: Timeline Risk (T) = 1.0 (since X+Y > Z); Sensitivity (S) = 0.90; Exposure (E) = 0.30.
- **Step-by-Step Calculation**:
  - QARS = (w_T × T) + (w_S × S) + (w_E × E)
  - QARS = (0.33 × 1.0) + (0.33 × 0.90) + (0.33 × 0.30)
  - QARS = 0.33 + 0.297 + 0.099 = **0.726**
- **Result**: High Risk

**Asset B: Short-lived Web Service**

- **Inputs**: Shelf-life (X) = 1 year; Migration time (Y) = 2 years; Threat Horizon (Z) = 12 years.
- **Factor Scores**: Timeline Risk (T) = 0.25 (since X+Y << Z); Sensitivity (S) = 0.10; Exposure (E) = 0.80.
- **Step-by-Step Calculation**:
  - QARS = (0.33 × 0.25) + (0.33 × 0.10) + (0.33 × 0.80)
  - QARS = 0.0825 + 0.033 + 0.264 = **0.3795**
- **Result**: Medium-Low Risk

#### Qualitative Risk Bands

| Risk Level | Score Range | Recommended Action                                                                              |
| ---------- | ----------- | ----------------------------------------------------------------------------------------------- |
| Low        | < 0.30      | Migration during routine tech refreshes.                                                        |
| Medium     | 0.30 – 0.60 | Scheduled migration; quarterly monitoring of quantum milestones.                                |
| High       | > 0.60      | Immediate PQC roadmap development; priority for architectural hardening.                        |
| Critical   | > 0.85      | Asset is in the "post-quantum insolvency" zone; requires urgent hybrid encryption or isolation. |

---

### 5. Implementation Lifecycle: The PAREK Framework and CBOM

The QARS model serves as the analytical core of the PAREK Framework, which provides a structured lifecycle for the transition to quantum resilience:

1. **P (Post-quantum inventory)**: Identifying all cryptographic assets across the enterprise.
2. **A (Asset/Algorithm assessment)**: Quantifying vulnerability using the QARS scoring model.
3. **R (Road-mapping)**: Transforming QARS data into a prioritized execution schedule.
4. **E (Execution)**: Implementing NIST-standardized PQC (FIPS 203, 204, and 205).
5. **K (Key governance)**: Establishing long-term crypto-agility—the ability to swap algorithms without significant infrastructure overhaul.

To achieve QARS accuracy, the organization must maintain a **Cryptographic Bill of Materials (CBOM)**. A CBOM provides the granular hygiene data required for strategic assessments by capturing:

1. **Algorithms**: Specific primitives and their respective classical vs. quantum security levels.
2. **Key Material**: Key types, sizes, and specific Object Identifiers (OIDs) for precise identification.
3. **Certificates**: X.509 details, issuers, and lifespan/rotation dates to manage operational risk.
4. **Protocols**: Usage context, such as TLS 1.3 or IPsec configurations and enabled cipher suites.

Integrating CBOM data into the QARS model allows for automated detection of weak cryptography and continuous risk adjustment.

---

### 6. Regulatory Alignment and Compliance Mapping

Quantum readiness has shifted from a best practice to an audit-ready mandate. Regulatory frameworks now require organizations to demonstrate a "state-of-the-art" posture that includes quantum risk management.

- **DORA (Digital Operational Resilience Act)**: Applies to 21 entity types in the European financial sector. It introduces Regulatory Technical Standards (RTS) on ICT Risk Management, mandating comprehensive cryptographic inventories and proactive monitoring of quantum threats.
- **NIS2 Directive**: Emphasizes crypto-agility as a core requirement for essential entities. Implementing Regulation (EU) 2024/2690 specifically mandates the ability to rapidly replace vulnerable algorithms for digital service providers.
- **US National Security Memorandum 10 (NSM-10)**: Directs federal agencies to migrate to NIST standards, specifically FIPS 203 (ML-KEM), FIPS 204 (ML-DSA), and FIPS 205 (SLH-DSA).

The strategic "So What?" for the CISO is found in the economic scale of the threat. The January 2026 Citi Institute report estimates that a single quantum-enabled attack on payment systems could put $2 trillion to $3.3 trillion of GDP at risk. Using QARS provides a defensible, mathematically grounded justification for PQC investment, moving the organization from observation to the action necessary to ensure long-term digital resilience.


## Getting Started

### Quick Start

1. Open `QARS_Quantum-Adjusted-Risk-Score.html` in any modern web browser
2. Enter asset information including:
   - Asset name and description
   - Data shelf-life requirements (X)
   - Migration timeline estimate (Y)
   - Threat horizon projection (Z)
   - Data sensitivity classification
   - Cryptographic exposure factors
3. Select a sector profile or customize weights
4. Click "Calculate QARS" to generate the risk score

### Understanding Your Results

- **QARS Score (0-1)**: A normalized risk score where higher values indicate greater quantum vulnerability
- **Timeline Risk**: Reflects how close you are to "crypto-procrastination" territory
- **Sensitivity Risk**: Weighted by regulatory requirements and data criticality
- **Exposure Risk**: Accounts for practical attack surface and harvestability

---

## Technical Details

### Calculation Formulas

```
Mosca Ratio: r = (X + Y) / Z
Timeline Risk: T = 1 / (1 + exp(-3 × (r - 1)))
Sensitivity Risk: S = mapped from classification (Low: 0.1, Medium: 0.5, High: 0.8, Critical: 1.0)
Exposure Risk: E = v × q (where v = 0 for PQC, 1 for non-PQC; q = harvestability factor)
QARS = (w_T × T) + (w_S × S) + (w_E × E)
```

### NIST PQC Standards

The framework supports assessment against NIST-approved post-quantum cryptographic standards:

- **FIPS 203**: ML-KEM (Key Encapsulation Mechanism)
- **FIPS 204**: ML-DSA (Digital Signature Algorithm)
- **FIPS 205**: SLH-DSA (Stateless Hash-Based Digital Signature Algorithm)

---

