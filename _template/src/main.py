# Main application file
# This is a template - customize for your tutorial

import os
from dotenv import load_dotenv

def main():
    """Main function example."""
    load_dotenv()  # Load environment variables
    
    print("🚀 Hello from Impact Learning Lab!")
    print(f"Debug mode: {os.getenv('DEBUG', 'False')}")
    
    # Add your tutorial code here
    
if __name__ == "__main__":
    main()
