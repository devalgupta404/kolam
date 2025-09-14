# Test Frontend for Kolam Generator

This is a simple HTML frontend for testing the Kolam Generator API. This folder can be deleted after testing is complete.

## Features

- Interactive form to input m and n parameters
- Real-time validation of parameters
- Visual pattern generation using HTML5 Canvas
- Multiple connection styles (curves, lines, arcs)
- Quick example buttons for common patterns
- Pattern information display

## Usage

1. Make sure the backend API is running on `http://localhost:5000`
2. Open `index.html` in a web browser
3. Enter values for m (dots per arm) and n (number of arms)
4. Click "Generate Pattern" to create the Kolam design
5. Use example buttons for quick testing

## Parameters

- **m**: Number of dots per arm (must be positive integer)
- **n**: Number of arms (must be positive integer)
- **Constraint**: gcd(m,n) = 1 (parameters must be coprime)

## Example Patterns

- m=4, n=5: Simple 4-dot pattern
- m=5, n=8: Classic Hridaya Kolam
- m=6, n=7: 6-dot pattern with 7 arms
- m=8, n=9: Larger 8-dot pattern
- m=10, n=7: Complex 10-dot pattern

## Visual Features

- Red dots represent the pattern points
- Teal lines/curves show the connections
- Black center dot marks the pattern center
- Canvas automatically scales the pattern

## Notes

This is a temporary test interface. The actual frontend implementation will be handled by the frontend team member.
