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
2. Enter m and n values (e.g., m=5, n=8)
3. Select Kolam type from dropdown
4. Click "Generate Pattern" to see the Kolam design
5. Try different examples using the quick buttons

## API Endpoints

### POST /api/generate

Generate a Kolam pattern.

**Request:**

```json
{
  "m": 5,
  "n": 8,
  "style": "curves",
  "type": "hridaya"
}
```

**Response:**

```json
{
  "success": true,
  "pattern": {
    "m": 5,
    "n": 8,
    "kolam_type": "hridaya",
    "kolam_name": "Hridaya Kolam",
    "description": "Heart-shaped traditional Kolam with radial symmetry",
    "generator_sequence": [5, 3, 1, 4, 2],
    "extended_sequence": [5, 3, 1, 4, 2, 5, 3, 1, 4, 2, ...],
    "connections": [...],
    "dots": [...],
    "center": {"x": 0, "y": 0},
    "algorithm": "Algorithm 1 - Hridaya Kolam"
  }
}
```

### POST /api/validate

Validate parameters before generation.

**Request:**

```json
{
  "m": 5,
  "n": 8
}
```

**Response:**

```json
{
  "valid": true,
  "m": 5,
  "n": 8,
  "gcd": 1,
  "error": null
}
```

### GET /api/types

Get all available Kolam types.

**Response:**

```json
{
  "success": true,
  "types": {
    "hridaya": {
      "name": "Hridaya Kolam",
      "description": "Heart-shaped traditional Kolam with radial symmetry",
      "algorithm": "algorithm_1"
    },
    "pulli": {
      "name": "Pulli Kolam",
      "description": "Dot-based Kolam with geometric patterns",
      "algorithm": "pulli_algorithm"
    }
  }
}
```

### POST /api/classify

Classify a Kolam pattern (KolamNetV2 inspired).

**Request:**

```json
{
  "m": 5,
  "n": 8
}
```

**Response:**

```json
{
  "success": true,
  "predicted_type": "hridaya",
  "confidence": 0.9,
  "type_info": {
    "name": "Hridaya Kolam",
    "description": "Heart-shaped traditional Kolam with radial symmetry"
  }
}
```

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

## Usage for Frontend Engineers

### API Integration

```javascript
// Generate different Kolam types
fetch("/api/generate", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    m: 5,
    n: 8,
    style: "curves",
    type: "hridaya", // Choose from: hridaya, pulli, rangoli, muggulu, alpana
  }),
})
  .then((response) => response.json())
  .then((data) => {
    if (data.success) {
      // Use data.pattern.connections to draw the Kolam
      drawKolam(data.pattern.connections);
    }
  });
```

### Response Data Structure

- **connections**: Array of line segments to draw the pattern
- **dots**: Reference dot positions (for visualization)
- **generator_sequence**: The mathematical sequence S
- **extended_sequence**: The repeated sequence S' used for connections
- **kolam_type**: Type of Kolam generated
- **algorithm**: Algorithm used for generation

---

**Note**: The `test-frontend` folder is temporary and should be deleted after testing is complete.
