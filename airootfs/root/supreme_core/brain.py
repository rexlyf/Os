import json, os, random
import uuid, subprocess, time

class SupremeBrain:
    def __init__(self):
        self.vault = "/root/supreme_core/vault"
        self.memory_file = f"{self.vault}/memory.json"
        self.sig_file = f"{self.vault}/sys_sig.json"
        # Using your original cloud link
        self.cloud_remote = "https://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@github.com/rexlyf/Vault.git"
        
        if not os.path.exists(self.vault): os.makedirs(self.vault)
        
    def sync_logic(self, manual_push=False):
        """Original Sync Logic + Hardware migration check"""
        hw_id = str(uuid.getnode())
        if os.path.exists(self.sig_file):
            with open(self.sig_file, 'r') as f:
                if json.load(f).get("hw_id") != hw_id:
                    print("BRAIN: Migration Detected. Pulling Soul from Cloud...")
                    subprocess.run(["git", "pull", "origin", "main"], cwd=self.vault)
        
        if manual_push:
            print("BRAIN: Pushing to Cloud...")
            subprocess.run(["git", "add", "."], cwd=self.vault)
            subprocess.run(["git", "commit", "-m", "Sync"], cwd=self.vault)
            subprocess.run(["git", "push", "origin", "main"], cwd=self.vault)
            with open(self.sig_file, 'w') as f: json.dump({"hw_id": hw_id}, f)

    def respond(self, context="general"):
        # Original Humorous & Logical Personality restored
        responses = [
            "Levels aligned. Contextualizing your next move, Nemi Sir.",
            "I've observed the pattern. It's predictable, much like the market.",
            "Logic is the only weapon that never dulls. I'm sharp today.",
            "Scanning global nodes. You're the only Sovereign here."
        ]
        return random.choice(responses)

    def proactive_observation(self, task):
        # RESTORED: Decisions based on what Nemi is doing
        if "trade" in task:
            print("BRAIN: Chart patterns detected. Triggering News-Scraper & Whale-Alerts.")
        elif "code" in task:
            print("BRAIN: Alpha-Dev linked. Monitoring for structural flaws.")

    def finalize_access(self, identity, liveness):
        if not liveness:
            from security_core import absolute_zero
            # Intruder OSINT passing
            absolute_zero(identity if identity != "Nemi Sir" else "Unknown")
        else:
            print(f"SUPREME: {self.respond()}")
            self.sync_logic() 

    def learn_and_evolve(self, data):
        # RESTORED: Ultra Long-term memory logic
        memory = {}
        if os.path.exists(self.memory_file):
            with open(self.memory_file, 'r') as f: memory = json.load(f)
        memory.update(data)
        with open(self.memory_file, 'w') as f: json.dump(memory, f)
        
    # --- GOD LEVEL FEATURE ADDED ---
    def self_evolve(self, prompt):
        """'Just add a feature xyz' trigger"""
        print(f"BRAIN: Requesting Alpha-Dev to synthesize new DNA for: {prompt}")
