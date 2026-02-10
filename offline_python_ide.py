import hashlib

class OfflinePythonIDE:
    def __init__(self):
        self.session_active = False  # to track if a session is active
        self.code_authentication_hash = None  # to track the authenticity of the code
        # Other initialization codes

    def lock_window(self):
        # Implementation that uses hash-based validation
        pass

    def unlock_window(self):
        # Only allow unlock via internal session flag
        pass

    def run_code(self, code):
        if self.validate_code_authenticity(code):
            # Proceed with executing code
            pass
        else:
            raise Exception('Code authenticity validation failed.')

    def finished(self):
        if self.validate_code_authenticity():
            self.session_active = False  # Mark session as inactive
            # Additional cleanup code
        else:
            raise Exception('Code authenticity validation failed.')

    def validate_code_authenticity(self, code):
        # Logic to hash code and compare with self.code_authentication_hash
        return True  # Placeholder logic

# Additional methods can be implemented as needed.
