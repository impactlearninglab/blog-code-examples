"""
Hello Blog - First Example Script
Demonstrates basic Python project structure.
"""

import os
import sys
from datetime import datetime
from dotenv import load_dotenv

def load_configuration():
    """Load environment configuration."""
    load_dotenv()  # Load from .env file
    
    config = {
        'debug': os.getenv('DEBUG', 'False').lower() == 'true',
        'app_name': os.getenv('APP_NAME', 'HelloBlog'),
        'version': os.getenv('VERSION', '1.0.0')
    }
    return config

def main():
    """Main function."""
    print("=" * 50)
    print("HELLO BLOG - IMPACT LEARNING LAB")
    print("=" * 50)
    
    # Load configuration
    config = load_configuration()
    
    print(f"\n📱 App: {config['app_name']} v{config['version']}")
    print(f"🐍 Python: {sys.version.split()[0]}")
    print(f"📅 Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"🔧 Debug Mode: {config['debug']}")
    
    # Example functionality
    print("\n🎯 Example Operations:")
    print("1. Environment variables loaded ✓")
    print("2. Basic Python syntax ✓")
    print("3. Project structure ✓")
    
    print("\n" + "=" * 50)
    print("✅ Tutorial completed successfully!")
    print("Check out more at: https://impactlearninglab.io")
    print("=" * 50)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)
