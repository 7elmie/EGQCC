# Strategy & Enterprise Migration (QRA)

This directory contains comprehensive resources and tools for Quantum Risk Assessment (QRA) and enterprise migration strategies in the context of quantum security.

## Contents

### 1. QARS_Quantum-Adjusted-Risk-Score/
Quantum-Adjusted Risk Score calculator and assessment tools for evaluating quantum security risks.

**Files:**
- `README.md` - Comprehensive framework documentation 
- `QARS_Quantum-Adjusted-Risk-Score.html` - Interactive risk calculator 

**Key Features:**
- **Strategic Framework**: Multi-dimensional approach to evaluating post-quantum cryptography migration priorities
- **Mosca Inequality Integration**: Quantifies the relationship between data shelf-life, migration timeline, and threat horizon
- **Real-time Calculations**: Dynamic risk scoring with visual feedback and progress tracking
- **Sector-specific Weighting**: Finance, IoT/Embedded, Cloud Services, and General baseline profiles
- **PAREK Framework**: Complete PQC migration lifecycle support (Post-quantum inventory, Assessment, Road-mapping, Execution, Key governance)
- **Regulatory Compliance**: Maps to DORA, NIS2, and US NSM-10 requirements
- **Interactive Dashboard**: Asset management, risk visualization, and export capabilities

**Calculation Formula:**
```
Mosca Ratio: r = (X + Y) / Z
Timeline Risk: T = 1 / (1 + exp(-3 × (r - 1)))
Sensitivity Risk: S = mapped from classification (Low: 0.1, Medium: 0.5, High: 0.8, Critical: 1.0)
Exposure Risk: E = v × q (where v = 0 for PQC, 1 for non-PQC; q = harvestability factor)
QARS = (w_T × T) + (w_S × S) + (w_E × E)
```

### 2. QSRI_Quantum-Security-Readiness-Index/
Quantum Security Readiness Index assessment framework for evaluating organizational preparedness.

**Files:**
- `README.md` - Assessment framework documentation 
- `QSRI_Quantum-Security-Readiness-Index.html` - Interactive readiness assessment tool 
- `QSRI_Quantum-Security-Readiness-Index.xlsx` - Excel-based assessment template 

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
- **Interactive Features**: Real-time scoring, visual radar chart, progress tracking, and PDF export

### 3. The Architect’s Guide To Quantum Security.pdf
Comprehensive guide to quantum security architecture and implementation strategies.

## Purpose

This QRA section provides organizations with:
- **Risk Assessment Tools**: Quantify quantum security risks and vulnerabilities using mathematical frameworks
- **Readiness Evaluation**: Benchmark organizational preparedness against industry standards
- **Migration Planning**: Strategic frameworks for prioritizing and executing quantum-safe transitions
- **Compliance Mapping**: Alignment with regulatory requirements and best practices
- **Interactive Dashboards**: Real-time visualization and tracking of quantum security posture

## Detailed Tool Descriptions

### Quantum-Adjusted Risk Score (QARS) Framework

The QARS framework provides a strategic, multi-dimensional approach to evaluating post-quantum cryptography migration priorities based on the Mosca Inequality and quantum risk exposure.

**Core Components:**
1. **Asset Configuration**: Input data shelf-life, migration timeline, threat horizon, and sensitivity levels
2. **Risk Classification**: Automatic calculation of timeline, sensitivity, and exposure risks
3. **Sector Profiles**: Pre-configured weightings for Finance (wT=0.4, wS=0.4, wE=0.2), IoT/Embedded (wT=0.5, wS=0.2, wE=0.3), Cloud Services (wT=0.3, wS=0.2, wE=0.5), and General baseline (wT=0.33, wS=0.33, wE=0.34)
4. **PAREK Workflow**: Visual representation of the complete migration lifecycle
5. **Cryptographic Bill of Materials (CBOM)**: Asset-specific cryptographic inventory tracking
6. **Regulatory Compliance**: Real-time compliance status for DORA, NIS2, and NIST standards

**Risk Bands:**
- **Low** (< 0.30): Migration during routine tech refreshes
- **Medium** (0.30–0.60): Scheduled migration with quarterly monitoring
- **High** (> 0.60): Immediate PQC roadmap development required
- **Critical** (> 0.85): Asset in "post-quantum insolvency" zone requiring urgent action

### Quantum Security Readiness Index (QSRI) Assessment

The QSRI provides a standardized assessment framework for evaluating organizational preparedness across eight critical dimensions.

**Maturity Levels:**
- **Level 0 (Unaware)**: No awareness of quantum threats; no action taken
- **Level 1 (Aware)**: Basic awareness; no formal program or inventory
- **Level 2 (Initiating)**: Initial assessments or inventories in progress
- **Level 3 (Planning)**: Roadmaps, governance, and testbeds defined
- **Level 4 (Migrating)**: Pilot PQC/hybrid crypto deployments in production
- **Level 5 (Quantum-Safe Ready)**: Full cryptographic agility and PQC adoption

**Scoring Interpretation:**
- **0–25 (Unprepared)**: Critical risk; no quantum defense strategy
- **26–50 (Early-stage)**: Awareness stage; significant work required
- **51–75 (Progressing)**: Partial readiness with some implementation
- **76–100 (Mature)**: Quantum-safe ready with strong governance

## Usage

1. **QARS Assessment**: Use the interactive calculator to assess your organization's quantum risk exposure using the Mosca framework. Configure assets, select sector profiles, and generate prioritized migration roadmaps.

2. **QSRI Evaluation**: Complete the readiness assessment to evaluate your quantum security maturity across all eight dimensions. Track progress over time and identify specific areas for improvement.

3. **Strategic Planning**: Reference the Architect's Guide for comprehensive migration strategies, implementation best practices, and architectural patterns.

4. **Integrated Approach**: Combine QARS risk scores with QSRI maturity levels to develop a prioritized quantum security migration strategy that addresses both technical and organizational readiness.

5. **Compliance Reporting**: Generate reports for regulatory compliance, executive briefings, and stakeholder communication using the built-in export functionality.

## Implementation Workflow

1. **Assessment Phase**: Use QSRI to establish baseline maturity across all dimensions
2. **Risk Analysis**: Apply QARS to identify high-priority assets and vulnerabilities
3. **Strategy Development**: Create migration roadmaps based on combined QARS/QSRI insights
4. **Execution Tracking**: Monitor progress through the PAREK framework stages
5. **Continuous Improvement**: Regular reassessment and adjustment of strategies based on evolving threats and capabilities

This integrated approach ensures organizations can systematically address quantum security challenges while maintaining operational resilience and regulatory compliance.


