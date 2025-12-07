#!/usr/bin/env python3
"""
Quick test of pattern consciousness engine
"""

from core.hexagram_engine import PatternCore

def main():
    print("Testing Pattern Consciousness Engine")
    print("=" * 50)
    
    # Create engine
    engine = PatternCore()
    
    # Test cases
    test_cases = [
        ([1,1,1,1,1,1], "All yang"),
        ([0,0,0,0,0,0], "All yin"),
        ([1,0,1,0,1,0], "Alternating"),
        ([0,1,0,1,0,1], "Opposite alternating")
    ]
    
    for pattern, description in test_cases:
        result = engine.recognize(pattern)
        print(f"\nTest: {description}")
        print(f"  Input:    {pattern}")
        print(f"  Hexagram: {result['hexagram']} - {result['name']}")
        print(f"  Confidence: {result['confidence']:.1%}")
    
    print("\n" + "=" * 50)
    print("✅ Basic engine working!")
    print("\nTo use in your code:")
    print("  from core.hexagram_engine import PatternCore")
    print("  engine = PatternCore()")
    print("  result = engine.recognize([1,0,1,0,1,0])")

if __name__ == "__main__":
    main()
