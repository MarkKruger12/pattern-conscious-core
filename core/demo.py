#!/usr/bin/env python3
"""
Pattern Consciousness Demo
Simple command-line interface
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'core'))

try:
    from hexagram_engine import PatternCore
except ImportError:
    print("Please run: pip install -r requirements.txt")
    sys.exit(1)

def main():
    print("""
    ╔═══════════════════════════════════════╗
    ║    PATTERN CONSCIOUSNESS ENGINE      ║
    ║      I-Ching meets AI Thinking       ║
    ╚═══════════════════════════════════════╝
    """)
    
    core = PatternCore()
    
    while True:
        print("\n" + "━" * 50)
        print("1. Recognize pattern (enter 6 numbers, 0 or 1)")
        print("2. Show all hexagrams")
        print("3. Transform pattern")
        print("4. Exit")
        
        choice = input("\nChoose (1-4): ").strip()
        
        if choice == "1":
            pattern_input = input("Enter pattern (e.g., 101010 or 1 0 1 0 1 0): ")
            
            # Parse input
            if " " in pattern_input:
                pattern = [int(x) for x in pattern_input.split()]
            else:
                pattern = [int(x) for x in pattern_input]
            
            if len(pattern) != 6:
                print("Error: Must be exactly 6 numbers (0 or 1)")
                continue
            
            result = core.recognize(pattern)
            
            print(f"\n🎯 RESULT:")
            print(f"  Hexagram:    {result['hexagram']}")
            print(f"  Name:        {result['name']}")
            print(f"  Quality:     {result['quality']}")
            print(f"  Pattern:     {result['pattern']}")
            print(f"  Binary:      {result['binary']}")
            print(f"  Confidence:  {result['confidence']:.1%}")
            
        elif choice == "2":
            print("\n📚 Hexagram Matrix (First 8 of 64):")
            for i in range(1, 9):
                pattern = core.hexagrams[i]
                meaning = core.meanings.get(i, {"name": "TBD", "quality": ""})
                print(f"  {i:2d}: {pattern} - {meaning['name']}")
            print("  ... (56 more)")
            
        elif choice == "3":
            try:
                current = int(input("Current hexagram number (1-64): "))
                lines_input = input("Lines to change (e.g., '2 4' or 'none'): ")
                
                if lines_input.lower() == 'none':
                    changing_lines = []
                else:
                    changing_lines = [int(x)-1 for x in lines_input.split()]
                
                result = core.transform(current, changing_lines)
                print(f"\n🔄 TRANSFORMATION:")
                print(f"  From Hexagram {current}")
                print(f"  Changing lines: {[x+1 for x in changing_lines]}")
                print(f"  To Hexagram:    {result['hexagram']} - {result['name']}")
                
            except ValueError:
                print("Invalid input!")
                
        elif choice == "4":
            print("\n🚀 Keep exploring patterns!")
            break
        
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
