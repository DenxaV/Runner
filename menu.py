import pygame
from sys import exit

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 50)
        self.title_font = pygame.font.Font(None, 80)
        
        # Colors
        self.BG_COLOR = (30, 30, 40)
        self.TEXT_COLOR = (255, 255, 255)
        self.HIGHLIGHT_COLOR = (255, 200, 0)
        
        # Menu items
        self.options = ["Start Game", "Quit"]
        self.selected_option = 0
        
        # Load background if you want
        try:
            self.background = pygame.image.load('sprites/woods.png').convert()
            self.background = pygame.transform.scale(self.background, (800, 400))
        except:
            self.background = None
    
    def draw(self):
        # Draw background
        if self.background:
            self.screen.blit(self.background, (0, 0))
        else:
            self.screen.fill(self.BG_COLOR)
        
        # Draw title
        title_text = self.title_font.render("GHOST RUNNER", True, self.TEXT_COLOR)
        title_rect = title_text.get_rect(center=(400, 100))
        self.screen.blit(title_text, title_rect)
        
        # Draw menu options
        for i, option in enumerate(self.options):
            color = self.HIGHLIGHT_COLOR if i == self.selected_option else self.TEXT_COLOR
            text = self.font.render(option, True, color)
            rect = text.get_rect(center=(400, 200 + i * 60))
            self.screen.blit(text, rect)
        
        pygame.display.update()
    
    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.selected_option = (self.selected_option + 1) % len(self.options)
                elif event.key == pygame.K_UP:
                    self.selected_option = (self.selected_option - 1) % len(self.options)
                elif event.key == pygame.K_RETURN:
                    return self.selected_option
        
        return None
    
    def run(self):
        while True:
            selection = self.handle_input()
            if selection is not None:
                return selection
            
            self.draw()
            self.clock.tick(60)

# Example usage in your main game file:
# from menu import Menu
# 
# pygame.init()
# screen = pygame.display.set_mode((800, 400))
# menu = Menu(screen)
# selected = menu.run()
# 
# if selected == 0:  # Start Game
#     # Run your game
# elif selected == 1:  # Quit
#     pygame.quit()
#     exit()