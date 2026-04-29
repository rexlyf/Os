import pygame, threading, time, random, os
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from eyes import SovereignEyes
from brain import SupremeBrain
from alpha_dev import AlphaDev
from supreme_bot import SupremeExchangeBot
from hands import SovereignHands # NEW

class SupremeOS:
    def __init__(self):
        pygame.init()
        self.display = (1920, 1080)
        pygame.display.set_mode(self.display, DOUBLEBUF | OPENGL | FULLSCREEN)
        gluPerspective(45, (16/9), 0.1, 50.0)
        glTranslatef(0.0, 0.0, -10)
        self.eyes = SovereignEyes()
        self.brain = SupremeBrain()
        self.alpha = AlphaDev()
        self.bot = SupremeExchangeBot()
        self.hands = SovereignHands() # NEW
        self.atoms = [[random.uniform(-7, 7) for _ in range(3)] for _ in range(2500)]

    def atoms_to_vortex(self):
        for i in range(150):
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            glBegin(GL_POINTS)
            for a in self.atoms:
                if self.eyes.threat_level == "CRITICAL": glColor3f(1.0, 0.0, 0.0)
                else: glColor3f(1.0, 0.85, 0.0)
                glVertex3fv(a)
                a[0]*=0.96; a[1]*=0.96; a[2]*=0.96
            glEnd()
            pygame.display.flip()
            pygame.time.wait(10)

    def ignite(self):
        # Genesis Check
        if not os.path.exists("/root/supreme_core/vault/creator.json"):
            pygame.display.quit()
            from genesis import start_genesis
            if start_genesis(): os.system("python main.py")
            return

        self.hands.overdrive() # NEW: Activates your i3 performance tuning

        # Parallel Cognitive Processing
        # (Using your exact logic below, modifying to call your optical_intelligence function)
        scan_thread = threading.Thread(target=self.eyes.optical_intelligence)
        scan_thread.start()
        self.atoms_to_vortex()
        scan_thread.join()

        # Decision & Access
        # Using liveness directly based on how you wrote it in optical_intelligence
        liveness_status = getattr(self.eyes, 'liveness', False) 
        self.brain.finalize_access(self.eyes.identity, liveness_status)
        
        # Start Proactive Observer
        self.brain.proactive_observation("trading")

if __name__ == "__main__":
    SupremeOS().ignite()
