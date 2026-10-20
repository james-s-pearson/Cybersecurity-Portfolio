"""Folder check for the Python runner (F5 in an IPython terminal).

Confirms the runner runs your script from the script's own folder.
Safe and self-contained: no input, no network. It writes one tiny file
next to itself, then deletes it.
"""

from pathlib import Path

NAME = "folder_check.tmp"
script_folder = Path(__file__).resolve().parent

print("--- Folder Check Start ---")
with open(NAME, "w") as f:  # relative path: lands in the current folder
    f.write("written with a relative path")

landed_here = (script_folder / NAME).exists()
print(f"Script folder: {script_folder.name}")
print(f"Relative file landed in the script folder: {'yes' if landed_here else 'no'}")
print("Folder Check: PASSED" if landed_here else "Folder Check: FAILED")

Path(NAME).unlink(missing_ok=True)  # clean up wherever it landed
print("--- Folder Check End ---")
