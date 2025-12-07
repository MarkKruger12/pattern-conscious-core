"""
Pattern Consciousness Core Engine
Based on I-Ching 64 hexagram mathematics
"""

import numpy as np

class PatternCore:
    """Core pattern recognition engine"""
    
    def __init__(self):
        self.hexagrams = self._create_hexagram_matrix()
        self.meanings = self._load_meanings()
    
    def _create_hexagram_matrix(self):
        """Create 64 hexagrams (6-bit patterns)"""
        hexagrams = {}
        for i in range(64):
            # Binary representation with 6 bits
            pattern = [(i >> (5 - bit)) & 1 for bit in range(6)]
            hexagrams[i + 1] = pattern  # Hexagrams numbered 1-64
        return hexagrams
    
    def _load_meanings(self):
        """Basic hexagram meanings"""
        return {
            1: {"name": "The Creative", "quality": "Strength, Creativity"},
            2: {"name": "The Receptive", "quality": "Devotion, Yielding"},
            63: {"name": "After Completion", "quality": "Clarity after difficulty"},
            64: {"name": "Before Completion", "quality": "Transition, Not yet finished"}
        }
    
    def recognize(self, input_pattern):
        """Find closest hexagram match"""
        if len(input_pattern) != 6:
            raise ValueError("Pattern must be 6 elements (yin=0, yang=1)")
        
        best_match = 1
        best_similarity = -1
        
        for num, hexagram in self.hexagrams.items():
            similarity = np.dot(input_pattern, hexagram)
            if similarity > best_similarity:
                best_similarity = similarity
                best_match = num
        
        return {
            "hexagram": best_match,
            "name": self.meanings.get(best_match, {}).get("name", "Unknown"),
            "quality": self.meanings.get(best_match, {}).get("quality", ""),
            "pattern": self.hexagrams[best_match],
            "confidence": best_similarity / 6.0,
            "binary": ''.join(str(bit) for bit in self.hexagrams[best_match])
        }
    
    def transform(self, current_hexagram, changing_lines=None):
        """Apply I-Ching transformation rules"""
        if changing_lines is None:
            changing_lines = []
        
        current_pattern = self.hexagrams[current_hexagram].copy()
        
        # Flip changing lines (yin↔yang)
        for line in changing_lines:
            if 0 <= line < 6:
                current_pattern[line] = 1 - current_pattern[line]
        
        return self.recognize(current_pattern)

# Quick test
if __name__ == "__main__":
    print("🧠 Pattern Consciousness Engine Test")
    print("=" * 40)
    
    core = PatternCore()
    
    # Test pattern
    test_input = [1, 0, 1, 0, 1, 0]  # Alternating yin/yang
    
    result = core.recognize(test_input)
    
    print(f"Input pattern:    {test_input}")
    print(f"Matched hexagram: {result['hexagram']} - {result['name']}")
    print(f"Quality:          {result['quality']}")
    print(f"Confidence:       {result['confidence']:.1%}")
    print(f"Binary:           {result['binary']}")
    
    # Test transformation
    print("\n" + "=" * 40)
    print("Transformation test:")
    new_result = core.transform(result['hexagram'], changing_lines=[2, 4])
    print(f"If lines 2 and 4 change → Hexagram {new_result['hexagram']}")
