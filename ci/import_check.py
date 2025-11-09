#!/usr/bin/env python3
"""Minimal import checker (from issue):
- Puts `src` at the front of sys.path so local imports resolve
- Tries to import `manager` and `inventhory`
- Exits non-zero if imports fail so CI marks the build as failed

Usage: python ci/import_check.py
"""

import sys
import traceback

# Put src at the front so local imports resolve
sys.path.insert(0, 'src')

try:
    import manager
    import inventhory
    print('Import OK: manager, inventhory')
except Exception as e:
    print('Import FAILED:', repr(e))
    traceback.print_exc()
    # Exit with error so CI marks the build as failed
    sys.exit(1)

# If we reach here, critical imports succeeded
print('Critical imports passed.')
sys.exit(0)
