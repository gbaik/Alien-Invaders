import pygame
import game_functions as gf

from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from alien import Alien

def run_game():
  pygame.init()
  ai_settings = Settings()
  screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
  pygame.display.set_caption("Alien Invasion")

  play_button = Button(ai_settings, screen, "Play")

  stats = GameStats(ai_settings)
  scoreboard = Scoreboard(ai_settings, screen, stats)

  ship = Ship(ai_settings, screen)
  bullets = Group()
  aliens = Group()

  gf.create_fleet(ai_settings, screen, ship, aliens)

  while True:
    gf.check_events(ai_settings, screen, stats, scoreboard, play_button, ship, bullets, aliens)
    if stats.game_active:
      ship.update()
      gf.update_bullets(ai_settings, screen, stats, scoreboard, ship, bullets, aliens)
      gf.update_aliens(ai_settings, screen, stats, scoreboard, ship, bullets, aliens)
    gf.update_screen(ai_settings, screen, stats, play_button, scoreboard, ship, bullets, aliens)

run_game()

