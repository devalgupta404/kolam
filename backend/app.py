from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import math
import json
import os

app = Flask(__name__)
CORS(app)

class KolamGenerator:
    def __init__(self):
        pass
    
    def generate_generator_sequence(self, m, n):
        if math.gcd(m, n) != 1:
            raise ValueError(f"m={m} and n={n} must be coprime (gcd(m,n)=1)")
        
        S = []
        for k in range(m):
            if k == 0:
                a_k = m
            else:
                a_k = (k * n) % m
            S.append(a_k)
        return S
    
    def generate_extended_sequence(self, S, n):
        S_prime = S * n
        return S_prime
    
    def generate_polar_coordinates(self, m, n):
        delta_theta = 2 * math.pi / n
        S = self.generate_generator_sequence(m, n)
        S_prime = self.generate_extended_sequence(S, n)
        C = []
        for i in range(len(S_prime)):
            theta_i = (i % n) * delta_theta
            r_i = S_prime[i]
            C.append({
                'r': r_i,
                'theta': theta_i,
                'x': r_i * math.cos(theta_i),
                'y': r_i * math.sin(theta_i)
            })
        if C:
            C.append(C[0].copy())
        return C, S, S_prime
    
    def generate_pattern(self, m, n, connection_style="curves"):
        try:
            S = self.generate_generator_sequence(m, n)
            S_prime = self.generate_extended_sequence(S, n)
            dots = self.generate_reference_dots(m, n)
            connections = []
            
            for i in range(len(S_prime)):
                current_arm = i % n
                current_dot_level = S_prime[i] - 1
                next_arm = (i + 1) % n
                next_dot_level = S_prime[(i + 1) % len(S_prime)] - 1
                current_dot = dots[current_arm][current_dot_level]
                next_dot = dots[next_arm][next_dot_level]
                
                connections.append({
                    'from': {
                        'x': current_dot['x'],
                        'y': current_dot['y'],
                        'arm': current_arm,
                        'dot': current_dot_level,
                        'radius': S_prime[i]
                    },
                    'to': {
                        'x': next_dot['x'],
                        'y': next_dot['y'],
                        'arm': next_arm,
                        'dot': next_dot_level,
                        'radius': S_prime[(i + 1) % len(S_prime)]
                    },
                    'style': connection_style
                })
            
            return {
                'm': m,
                'n': n,
                'generator_sequence': S,
                'extended_sequence': S_prime,
                'connections': connections,
                'dots': dots,
                'center': {'x': 0, 'y': 0},
                'algorithm': 'Algorithm 1 - Traditional Kolam Connection'
            }
            
        except Exception as e:
            raise ValueError(f"Error generating pattern: {str(e)}")
    
    def generate_reference_dots(self, m, n, radius=200):
        dots = []
        angle_step = 2 * math.pi / n
        
        for arm in range(n):
            arm_angle = arm * angle_step
            arm_dots = []
            for dot in range(m):
                dot_radius = radius * (dot + 1) / m
                x = dot_radius * math.cos(arm_angle)
                y = dot_radius * math.sin(arm_angle)
                arm_dots.append({
                    'x': x,
                    'y': y,
                    'arm': arm,
                    'dot': dot
                })
            dots.append(arm_dots)
        return dots

kolam_gen = KolamGenerator()

@app.route('/')
def home():
    return jsonify({
        'message': 'Kolam Generator API',
        'version': '1.0.0',
        'endpoints': {
            'generate': '/api/generate',
            'health': '/api/health'
        }
    })

@app.route('/api/health')
def health():
    return jsonify({'status': 'healthy'})

@app.route('/api/generate', methods=['POST'])
def generate_kolam():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No JSON data provided'}), 400
        
        m = data.get('m')
        n = data.get('n')
        connection_style = data.get('style', 'curves')
        
        if m is None or n is None:
            return jsonify({'error': 'Both m and n parameters are required'}), 400
        if not isinstance(m, int) or not isinstance(n, int):
            return jsonify({'error': 'm and n must be integers'}), 400
        if m <= 0 or n <= 0:
            return jsonify({'error': 'm and n must be positive integers'}), 400
        
        pattern = kolam_gen.generate_pattern(m, n, connection_style)
        return jsonify({
            'success': True,
            'pattern': pattern
        })
        
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': f'Internal server error: {str(e)}'}), 500

@app.route('/api/validate', methods=['POST'])
def validate_parameters():
    try:
        data = request.get_json()
        m = data.get('m')
        n = data.get('n')
        
        if m is None or n is None:
            return jsonify({'valid': False, 'error': 'Both m and n parameters are required'})
        if not isinstance(m, int) or not isinstance(n, int):
            return jsonify({'valid': False, 'error': 'm and n must be integers'})
        if m <= 0 or n <= 0:
            return jsonify({'valid': False, 'error': 'm and n must be positive integers'})
        
        is_coprime = math.gcd(m, n) == 1
        return jsonify({
            'valid': is_coprime,
            'm': m,
            'n': n,
            'gcd': math.gcd(m, n),
            'error': None if is_coprime else f'm={m} and n={n} must be coprime (gcd(m,n)=1)'
        })
        
    except Exception as e:
        return jsonify({'valid': False, 'error': f'Validation error: {str(e)}'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
