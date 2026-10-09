import pygame
import random
import math
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Colors (RGB)
BG_COLOR = (18, 18, 24)
PLAYER_COLOR = (0, 245, 255)
ORB_COLOR = (50, 255, 100)
HAZARD_COLOR = (255, 60, 90)
TEXT_COLOR = (240, 240, 250)

# Setup Screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Orb Catcher - Satisfying Arcade Game")
clock = pygame.time.Clock()

class Particle:
    """Creates satisfying visual pop effects when collecting items."""
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        angle = random.uniform(0, 2 * math.pi)
        speed = random.uniform(2, 6)
        self.vx = math.cos(angle) * speed
        self.vy = math.sin(angle) * speed
        self.life = 1.0 # Alpha/lifetime tracker
        self.decay = random.uniform(0.02, 0.05)

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.life -= self.decay

    def draw(self, surface):
        if self.life > 0:
            alpha_color = (
                int(self.color[0]),
                int(self.color[1]),
                int(self.color[2])
            )
            pygame.draw.circle(surface, alpha_color, (int(self.x), int(self.y)), int(self.life * 4))

class Player:
    def __init__(self):
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT // 2
        self.radius = 20
        self.speed = 6
        self.scale_timer = 0 # Used for squish/stretch satisfaction feedback

    def handle_input(self):
        keys = pygame.key.get_pressed()
        dx, dy = 0, 0
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            dx = -1
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            dx = 1
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            dy = -1
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            dy = 1

        # Normalize diagonal movement
        if dx != 0 and dy != 0:
            dx *= 0.7071
            dy *= 0.7071

        self.x += dx * self.speed
        self.y += dy * self.speed

        # Keep player inside screen boundaries
        self.x = max(self.radius, min(SCREEN_WIDTH - self.radius, self.x))
        self.y = max(self.radius, min(SCREEN_HEIGHT - self.radius, self.y))

        if self.scale_timer > 0:
            self.scale_timer -= 1

    def draw(self, surface):
        # Scale effect for tactile feedback when picking up items
        current_radius = self.radius + (4 if self.scale_timer > 0 else 0)
        pygame.draw.circle(surface, PLAYER_COLOR, (int(self.x), int(self.y)), int(current_radius))
        # Inner core glow
        pygame.draw.circle(surface, (255, 255, 255), (int(self.x), int(self.y)), int(current_radius * 0.4))

class GameObject:
    def __init__(self, color, radius):
        self.radius = radius
        self.color = color
        self.respawn()

    def respawn(self):
        self.x = random.randint(50, SCREEN_WIDTH - 50)
        self.y = random.randint(50, SCREEN_HEIGHT - 50)

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.radius)

def main():
    player = Player()
    orb = GameObject(ORB_COLOR, 12)
    hazards = [GameObject(HAZARD_COLOR, 16) for _ in range(3)]
    
    particles = []
    score = 0
    game_over = False

    font = pygame.font.SysFont("Arial", 28)
    large_font = pygame.font.SysFont("Arial", 48, bold=True)

    while True:
        # Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if game_over and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    # Restart game
                    main()
                    return

        if not game_over:
            player.handle_input()

            # Check collection of the target orb
            distance_to_orb = math.hypot(player.x - orb.x, player.y - orb.y)
            if distance_to_orb < player.radius + orb.radius:
                score += 1
                player.scale_timer = 10 # Trigger visual pop feedback
                # Create particle burst
                for _ in range(15):
                    particles.append(Particle(orb.x, orb.y, ORB_COLOR))
                orb.respawn()
                
                # Add a new hazard every 5 points to scale difficulty smoothly
                if score % 5 == 0 and len(hazards) < 8:
                    hazards.append(GameObject(HAZARD_COLOR, 16))

            # Check collision with hazards
            for hazard in hazards:
                # Slowly move hazards slightly toward the player for added dynamic tension
                angle = math.atan2(player.y - hazard.y, player.x - hazard.x)
                hazard.x += math.cos(angle) * 1.2
                hazard.y += math.sin(angle) * 1.2

                distance_to_hazard = math.hypot(player.x - hazard.x, player.y - hazard.y)
                if distance_to_hazard < player.radius + hazard.radius:
                    game_over = True
                    for _ in range(25):
                        particles.append(Particle(player.x, player.y, HAZARD_COLOR))

        # Update Particles
        for p in particles[:]:
            p.update()
            if p.life <= 0:
                particles.remove(p)

        # Drawing
        screen.fill(BG_COLOR)

        # Draw game elements
        for p in particles:
            p.draw(screen)

        if not game_over:
            player.draw(screen)
            orb.draw(screen)
            for hazard in hazards:
                hazard.draw(screen)

        # Render Score HUD
        score_surface = font.render(f"Score: {score}", True, TEXT_COLOR)
        screen.blit(score_surface, (20, 20))

        if game_over:
            game_over_surface = large_font.render("GAME OVER", True, HAZARD_COLOR)
            restart_surface = font.render("Press 'R' to Restart", True, TEXT_COLOR)
            
            screen.blit(game_over_surface, (SCREEN_WIDTH // 2 - game_over_surface.get_width() // 2, SCREEN_HEIGHT // 2 - 50))
            screen.blit(restart_surface, (SCREEN_WIDTH // 2 - restart_surface.get_width() // 2, SCREEN_HEIGHT // 2 + 10))

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
