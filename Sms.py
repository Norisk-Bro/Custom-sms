#!/usr/bin/env python3
import Freesms

if __name__ == "__main__":
    try:
        Freesms.start_app()
    except Exception as e:
        print(f"Error: {e}")
