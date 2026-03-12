# Strategy & Enterprise Migration (QRA)

This directory contains comprehensive resources and tools for Quantum Risk Assessment (QRA) and enterprise migration strategies in the context of quantum security.

## Contents

### 1. QARS_Quantum-Adjusted-Risk-Score/
Quantum-Adjusted Risk Score calculator and assessment tools for evaluating quantum security risks.

**Files:**
- `README.md` - Comprehensive framework documentation (2.3KB)
- `qars-calculator1.html` - Interactive risk calculator (70KB)
- `qars-calculator1.png` - Screenshot of calculator interface (1.3MB)
- `qars-calculator2.html` - Enhanced risk calculator with additional features (62KB)
- `qars-calculator2.png` - Screenshot of enhanced calculator (2MB)

### 2. QSRI_Quantum-Security Readiness Index_Assessment/
Quantum Security Readiness Index assessment framework for evaluating organizational preparedness.

**Files:**
- `README.md` - Assessment framework documentation (3.1KB)
- `QSRI_Quantum-Security Readiness Index_Assessment.html` - Interactive readiness assessment tool (43KB)
- `QSRI_Quantum-Security Readiness Index_Assessment.xlsx` - Excel-based assessment template (12KB)

### 3. The Architect’s Guide To Quantum Security.pdf
Comprehensive guide to quantum security architecture and implementation strategies (9.2MB).

## Purpose

This QRA section provides organizations with:
- Tools to assess quantum security risks and vulnerabilities
- Frameworks for evaluating quantum readiness
- Calculators for determining quantum-adjusted risk scores
- Guidance for enterprise migration to quantum-safe solutions

## Detailed Tool Descriptions

### Quantum-Adjusted Risk Score (QARS)

The QARS framework provides a strategic, multi-dimensional approach to evaluating post-quantum cryptography migration priorities based on the Mosca Inequality and quantum risk exposure.

**Key Features:**
- **Mosca Ratio Calculation**: Quantifies the relationship between data shelf-life, migration timeline, and threat horizon
- **Multi-dimensional Scoring**: Integrates timeline, sensitivity, and exposure risks with sector-specific weighting
- **Risk Classification**: Provides clear risk bands (Low, Medium, High, Critical) with recommended actions
- **PAREK Framework Integration**: Supports the complete PQC migration lifecycle (Post-quantum inventory, Assessment, Road-mapping, Execution, Key governance)
- **Regulatory Alignment**: Maps to DORA, NIS2, and US NSM-10 compliance requirements

**Calculation Formula:**
```
Mosca Ratio: r = (X + Y) / Z
Timeline Risk: T = 1 / (1 + exp(-3 × (r - 1)))
Sensitivity Risk: S = mapped from classification (Low: 0.1, Medium: 0.5, High: 0.8, Critical: 1.0)
Exposure Risk: E = v × q (where v = 0 for PQC, 1 for non-PQC; q = harvestability factor)
QARS = (w_T × T) + (w_S × S) + (w_E × E)
```

### Quantum Security Readiness Index (QSRI)

The QSRI provides a standardized assessment framework for evaluating organizational preparedness across eight critical dimensions.

**Assessment Dimensions:**
- **Cryptographic Inventory & Discovery** (15%): Visibility over where cryptography is used
- **Risk Assessment & Impact Analysis** (10%): Understanding quantum vulnerabilities
- **Policy & Governance** (10%): Leadership commitment and PQC strategy
- **Technology & Crypto Agility** (15%): Ability to upgrade cryptography with minimal disruption
- **Migration Planning & Execution** (20%): Defined strategy, timeline, and pilot migrations
- **Vendor & Supply Chain Readiness** (10%): Ensuring partners support PQC transition
- **Regulatory & Compliance Alignment** (10%): Alignment with national and international standards
- **Awareness & Workforce Training** (10%): Internal capacity building on quantum risks

**Maturity Framework:**
- **6-level scale** (0-5) from Unaware to Quantum-Safe Ready
- **Weighted scoring** system (0-100 total score)
- **Readiness classifications**: Unprepared (0-25), Early-stage (26-50), Progressing (51-75), Mature (76-100)

## Usage

1. **QARS Assessment**: Use the calculators to assess your organization's quantum risk exposure using the Mosca framework
2. **QSRI Evaluation**: Complete the readiness assessment to evaluate your quantum security maturity
3. **Strategic Planning**: Reference the Architect's Guide for comprehensive migration strategies
4. **Integrated Approach**: Combine QARS risk scores with QSRI maturity levels to develop a prioritized quantum security migration strategy


