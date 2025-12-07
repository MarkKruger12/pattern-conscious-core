"""
Pattern Consciousness Engine v0.1
Minimal viable hexagram recognition
"""

class PatternCore:
    """Simplest possible pattern recognizer"""
    
    def __init__(self):
        # Just 4 hexagrams for MVP
        self.hexagrams = {
            1: [1,1,1,1,1,1],  # All yang
            2: [0,0,0,0,0,0],  # All yin
            63: [1,0,1,0,1,0], # After completion
            64: [0,1,0,1,0,1]  # Before completion
        }
        self.names = {
            1: "The Creative",
            2: "The Receptive", 
            63: "After Completion",
            64: "Before Completion"
        }
    
    def recognize(self, pattern):
        """Simple pattern matching"""
        if len(pattern) != 6:
            return {"error": "Pattern must be 6 numbers (0 or 1)"}
        
        # Find closest match
        best_match = None
        best_score = -1
        
        for num, hexagram in self.hexagrams.items():
            score = sum(1 for a,b in zip(pattern, hexagram) if a == b)
            if score > best_score:
                best_score = score
                best_match = num
        
        return {
            "hexagram": best_match,
            "name": self.names.get(best_match, "Unknown"),
            "match_score": best_score,
            "confidence": best_score / 6.0
        }
    
    def demo(self):
        """Run a quick demo"""
        test_pattern = [1,0,1,0,1,0]
        result = self.recognize(test_pattern)
        print("🧠 Pattern Consciousness Demo")
        print("=" * 40)
        print(f"Test pattern:  {test_pattern}")
        print(f"Hexagram:      {result['hexagram']}")
        print(f"Name:          {result['name']}")
        print(f"Confidence:    {result['confidence']:.1%}")
        return result

if __name__ == "__main__":
    # Quick test when run directly
    engine = PatternCore()
    engine.demo()
