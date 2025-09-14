# Kolam Generator Backend

This backend API generates Kolam patterns based on the research paper "Extending Hridaya Kolam to Even-Ordered Dot Patterns and Their Applications".

## Features

- Generate Kolam patterns using modular arithmetic
- Support for both even and odd number of dots (m)
- Validation of coprime parameters (gcd(m,n) = 1)
- Multiple connection styles (curves, lines, etc.)

## Installation

1. Install Python dependencies:

```bash
pip install -r requirements.txt
```

2. Run the Flask application:

```bash
python app.py
```

The API will be available at `http://localhost:5000`

## API Endpoints

### POST /api/generate

Generate a Kolam pattern based on m and n parameters.

**Request Body:**

```json
{
  "m": 5,
  "n": 8,
  "style": "curves"
}
```

**Response:**

```json
{
    "success": true,
    "pattern": {
        "m": 5,
        "n": 8,
        "sequence": [0, 3, 1, 4, 2],
        "dots": [...],
        "connections": [...],
        "center": {"x": 0, "y": 0}
    }
}
```

### POST /api/validate

Validate if given m,n parameters are valid for Kolam generation.

**Request Body:**

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

## Parameters

- `m`: Number of dots per arm (must be positive integer)
- `n`: Number of arms (must be positive integer)
- `style`: Connection style ("curves", "lines", etc.)

## Mathematical Foundation

The algorithm uses modular arithmetic to generate sequences where:

- gcd(m, n) = 1 (parameters must be coprime)
- Sequence generation: current = (current + n) % m
- Each sequence represents an Eulerian circuit in the Kolam graph
