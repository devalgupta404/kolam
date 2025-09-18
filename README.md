# Kolam Pattern Generator

A comprehensive mathematical Kolam pattern generator implementing multiple algorithms based on research papers and traditional mathematical foundations.

## Project Structure

```
kolam/
├── backend/                 # Flask API backend
│   ├── app.py              # Main application
│   ├── requirements.txt    # Python dependencies
│   └── README.md          # Backend documentation
├── test-frontend/          # Temporary test frontend (delete after testing)
│   ├── index.html         # Test HTML interface
│   └── README.md          # Frontend test documentation
├── run_backend.bat        # Windows batch file to start backend
└── README.md              # This file
```

## Mathematical Foundation

The Kolam generator implements multiple algorithms based on research papers:

- **Algorithm 1**: Hridaya Kolam (Chakraborty & Manna, 2025)
- **Algorithm 2**: Pulli Kolam (Traditional dot-grid patterns)
- **Algorithm 3**: Rangoli Kolam (Artistic flowing patterns)
- **Algorithm 4**: Muggulu Kolam (Telugu geometric designs)
- **Algorithm 5**: Alpana Kolam (Bengali floral motifs)
- **Algorithm 6**: Kolam Classification (KolamNetV2 inspired)

### Core Parameters

- **m**: Number of dots per arm
- **n**: Number of arms
- **Constraint**: gcd(m,n) = 1 (parameters must be coprime)
- **Type**: Kolam style selection (hridaya, pulli, rangoli, muggulu, alpana)

## 🔢 Algorithm Details

### Algorithm 1: Hridaya Kolam Generation

**Source**: Chakraborty & Manna (2025) - Algorithm 1

**Mathematical Foundation**:

- **Input**: m (number of radial dots), n (number of arms) where gcd(m,n) = 1
- **Output**: Set of polar coordinates (r, θ) for closed Kolam pattern

**Algorithm Steps**:

1. **Initialize angle step**: Δθ = 2π/n
2. **Generate sequence S**:
   ```
   for k = 0 to m-1:
       if k == 0:
           a_k = m
       else:
           a_k = (k × n) mod m
       Append a_k to S
   ```
3. **Form extended sequence S'**: Repeat S exactly n times
4. **Generate coordinates**:
   ```
   for i = 0 to length(S')-1:
       θ_i = (i mod n) × Δθ
       r_i = S'[i]
       Append point (r_i, θ_i) to C
   ```
5. **Close the loop**: Append initial point C[0] at the end

### Algorithm 2: Pulli Kolam Generation

**Source**: Traditional dot-grid patterns

**Characteristics**: Simple geometric connections, grid-based, linear connections

**Algorithm**:

1. Generate dot positions: Create radial dot grid
2. Connect consecutive dots: Linear connections within each arm
3. Connect arms: Circular connections between outer dots

### Algorithm 3: Rangoli Kolam Generation

**Source**: Artistic flowing patterns

**Characteristics**: Flower-like artistic connections, flowing curves, organic shapes

**Algorithm**:

1. Generate dot positions: Create radial dot grid
2. Create center connections: Connect center dots in flower pattern
3. Add outer ring: Connect consecutive dots in each arm

### Algorithm 4: Muggulu Kolam Generation

**Source**: Telugu geometric patterns

**Characteristics**: Intricate geometric designs, diamond/square patterns, symmetric connections

**Algorithm**:

1. Generate dot positions: Create radial dot grid
2. Create geometric patterns: Connect opposite arms in pairs
3. Form diamond shapes: Connect dots in symmetric patterns

### Algorithm 5: Alpana Kolam Generation

**Source**: Bengali floral motifs

**Characteristics**: Floral, organic patterns, petal-like connections, radial symmetry

**Algorithm**:

1. Generate dot positions: Create radial dot grid
2. Create petal connections: Connect center to outer dots
3. Form circular pattern: Connect outer dots in circular fashion

### Algorithm 6: Kolam Classification (KolamNetV2 Inspired)

**Source**: Sasithradevi et al. (2024) - KolamNetV2

**Classification Rules**:

```python
def classify_kolam(m, n):
    if m <= 3:
        return 'pulli', 0.85
    elif m <= 6:
        return 'hridaya', 0.90
    elif m <= 8:
        return 'rangoli', 0.80
    else:
        return 'muggulu', 0.75
```

## Quick Start

### Backend Setup

1. Navigate to the backend directory:

```bash
cd backend
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the Flask server:

```bash
python app.py
```

The API will be available at `http://localhost:5000`

### Testing with Frontend

1. Open `test-frontend/index.html` in a web browser
2. Set Density (controls m,n under the hood as a coprime pair)
3. Select Kolam Type and Connection Style (curves/lines)
4. (Optional) Keep "Animated Generation" checked for step-by-step drawing
5. Click "Generate Pattern" to visualize

## API (overview only)

This project exposes a small Flask API used by the test frontend. Refer to `backend/app.py` for the exact routes currently implemented. The test-frontend calls the API via `fetch` and renders results on an HTML5 Canvas. Detailed route documentation has been intentionally omitted here to keep the README concise and aligned with the current codebase.

## Example Patterns

Based on the research papers, here are some valid pattern combinations:

- **m=4, n=5**: Simple 4-dot pattern (Pulli style)
- **m=5, n=8**: Classic Hridaya Kolam (Heart-shaped)
- **m=6, n=7**: 6-dot pattern (Rangoli style)
- **m=8, n=9**: 8-dot pattern (Muggulu style)
- **m=10, n=7**: Complex 10-dot pattern (Alpana style)
- **m=12, n=5**: 12-dot pattern with 5 arms

## Key Features

- ✅ **Multiple Kolam Types**: 5 different traditional styles
- ✅ **Research-Based Algorithms**: Based on academic papers
- ✅ **Pattern Classification**: KolamNetV2 inspired classification
- ✅ **Modular Arithmetic**: Algorithm 1 implementation
- ✅ **Parameter Validation**: Coprime constraint checking
- ✅ **Multiple Connection Styles**: Curves, lines
- ✅ **RESTful API Design**: Clean, documented endpoints
- ✅ **Interactive Test Frontend**: Real-time pattern generation
- ✅ **Mathematical Foundation**: Traditional and modern approaches

## Mathematical Properties

### Coprime Constraint

- **Requirement**: gcd(m, n) = 1
- **Purpose**: Ensures proper sequence generation and pattern closure
- **Validation**: `math.gcd(m, n) == 1`

### Sequence Properties

- **Generator Sequence S**: Length = m
- **Extended Sequence S'**: Length = m × n
- **Pattern Closure**: S'[0] = S'[m×n] (circular)

### Geometric Properties

- **Radial Symmetry**: n-fold rotational symmetry
- **Scale Invariance**: Patterns scale with radius parameter
- **Connectivity**: Each pattern forms closed loops

## Algorithm Selection Guide

| **Kolam Type** | **Best For**         | **Characteristics**                    | **Complexity** |
| -------------- | -------------------- | -------------------------------------- | -------------- |
| **Hridaya**    | Traditional patterns | Complex curves, mathematical precision | High           |
| **Pulli**      | Simple designs       | Grid-based, linear connections         | Low            |
| **Rangoli**    | Artistic patterns    | Flowing curves, organic shapes         | Medium         |
| **Muggulu**    | Geometric designs    | Symmetric patterns, angular lines      | Medium         |
| **Alpana**     | Floral motifs        | Petal-like, radial connections         | Medium         |

## Next Steps

1. Test the backend API with the provided frontend
2. Integrate with the main frontend application
3. Add more visualization options
4. Implement pattern export functionality
5. Add pattern history and favorites

## Research References

1. **Chakraborty, S. K., & Manna, A. (2025)**. Extending Hridaya Kolam to Even-Ordered Dot Patterns and Their Applications. arXiv preprint arXiv:2507.02874.

2. **Sasithradevi, A., Sabarinathan, S. Shoba, et al. (2024)**. KolamNetV2: efficient attention-based deep learning network for tamil heritage art-kolam classification. Heritage Science, 12, 60.

3. **ResearchGate Publication**. Generation of Kolam-Designs Based on Contextual Array P Systems.

## Frontend Usage (brief)

- Open `test-frontend/index.html`
- Configure Density, Type, and Style
- Click Generate (optionally enable Animated Generation)
- The Canvas renders the dots and connections from API output

---

**Note**: The `test-frontend` folder is temporary and should be deleted after testing is complete.
