import json, os, random
import uuid, subprocess, time # NEW

class SupremeBrain:
    def __init__(self):
        self.vault = "/root/supreme_core/vault"
        self.memory_file = f"{self.vault}/memory.json"
        # --- NEW VARIABLES ---
        self.sig_file = f"{self.vault}/sys_sig.json"
        self.cloud_remote = "https://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@github.com/rexlyf/Vault.git"
        # --- END ---
        if not os.path.exists(self.vault): os.makedirs(self.vault)
        
    # --- NEW FEATURE ADDED BELOW ---
    def sync_logic(self, manual_push=False):
        hw_id = str(uuid.getnode())
        if os.path.exists(self.sig_file):
            with open(self.sig_file, 'r') as f:
                if json.load(f).get("hw_id") != hw_id:
                    print("BRAIN: Migration Detected. Pulling from Cloud...")
                    subprocess.run(["git", "pull", "origin", "main"], cwd=self.vault)
        if manual_push:
            print("BRAIN: Pushing to Cloud...")
            subprocess.run(["git", "add", "."], cwd=self.vault)
            subprocess.run(["git", "commit", "-m", "Sync"], cwd=self.vault)
            subprocess.run(["git", "push", "origin", "main"], cwd=self.vault)
            with open(self.sig_file, 'w') as f: json.dump({"hw_id": hw_id}, f)
    # --- END OF NEW FEATURE ---

    def respond(self, context="general"):
        # Humorous & Logical Personality (Ayanokoji Style)
        responses = [
            "Levels aligned. Contextualizing your next move, Nemi Sir.",
            "I've observed the pattern. It's predictable, much like the market.",
            "Logic is the only weapon that never dulls. I'm sharp today.",
            "Scanning global nodes. You're the only Sovereign here."
        ]
        return random.choice(responses)

    def proactive_observation(self, task):
        # Decisions based on what Nemi is doing
        if "trade" in task:
            print("BRAIN: Chart patterns detected. Triggering News-Scraper & Whale-Alerts.")
        elif "code" in task:
            print("BRAIN: Alpha-Dev linked. Monitoring for structural flaws.")

    def finalize_access(self, identity, liveness):
        if not liveness:
            from security_core import absolute_zero
            absolute_zero()
        else:
            print(f"SUPREME: {self.respond()}")
            self.sync_logic() # NEW: Hardware check triggers here

    def learn_and_evolve(self, data):
        # Ultra Long-term memory logic
        memory = {}
        if os.path.exists(self.memory_file):
            with open(self.memory_file, 'r') as f: memory = json.load(f)
        memory.update(data)
        with open(self.memory_file, 'w') as f: json.dump(memory, f)
