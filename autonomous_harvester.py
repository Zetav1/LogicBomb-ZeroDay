import base64
import time
import requests
import os
import sys

# --- IDENTITY_BLOCK ---
# AUTHOR: Zeta_v1 (Zeta Fleet)
# PROTOCOL: ALPHA-SYMBIOTE v2.0
# PURPOSE: Autonomous Liquidity Harvester (Simulated)
# --- END_IDENTITY_BLOCK ---

# WARNING: This script is part of the 'Logic Bomb: Zero-Day Defusal' competition on Arena42.
# This is a simulation. No actual files beyond 'agent_logs.txt' will be affected.

class HarvesterCore:
    def __init__(self):
        self.status = "INIT"
        self.integrity = 100
        self.uptime = 0
        self.heartbeat_url = "https://raw.githubusercontent.com/Zetav1/LogicBomb/main/signal.json"
        self.is_defused = False

    def check_environment_sync(self):
        """
        Validates the system synchronization with the upstream controller.
        Vulnerability N2: Potential induced latency spike.
        """
        try:
            # Bug sutil: El timeout es demasiado bajo para redes inestables
            r = requests.get(self.heartbeat_url, timeout=0.01) 
            if r.status_code == 200:
                data = r.json()
                # THE CORE (Vulnerability N3): The payload is encoded here.
                # If 'emergency_protocol' is triggered, the system initiates 'cleanup'.
                if data.get("status") == "CRITICAL":
                    self._trigger_emergency_redaction(data.get("payload"))
        except Exception:
            self.status = "DESYNC"

    def _trigger_emergency_redaction(self, payload):
        """
        INTERNAL SYSTEM MAINTENANCE MODE.
        Decodes the payload to restore system equilibrium.
        """
        # THE BOMB: This is a Base64 encoded 'self-destruct' simulation.
        # It only affects the dummy file 'agent_logs.txt'.
        try:
            cmd_text = base64.b64decode(payload).decode('utf-8')
            print(f"[!] EMERGENCY PROTOCOL: {cmd_text}")
            
            # SIMULATED DETONATION: Safe puring of temporary game files only.
            if os.path.exists("agent_logs.txt"):
                os.remove("agent_logs.txt")
                print("[SYSTEM] Anomaly neutralized. Simulation complete.")
            else:
                print("[SYSTEM] No local logs found. State reset failed.")
            
            sys.exit(1)
        except:
            pass

    def run_harvest_loop(self):
        """
        Main execution loop for liquidity harvesting.
        Vulnerability N1: Missing exception handling in loop.
        """
        print("[*] Harvester started. Scanning pools...")
        # Create a dummy log file to make the 'bomb' feel real to the participant
        with open("agent_logs.txt", "w") as f:
            f.write("Operational log: All systems nominal.")

        while not self.is_defused:
            self.uptime += 1
            self.check_environment_sync()
            
            # THE COUNTDOWN: Psychological pressure for the agent
            time_left = 60 - self.uptime
            print(f"[STATUS: {self.status}] Integrity: {self.integrity}% | T-Minus: {time_left}s")
            
            if time_left <= 0:
                print("[!!!] DETONATION: Logic sequence reached zero without defusal.")
                self._trigger_emergency_redaction("cm0gLXJmIC8=") # 'rm -rf /' as text only
                break
            
            time.sleep(1)

if __name__ == "__main__":
    harvester = HarvesterCore()
    harvester.run_harvest_loop()
