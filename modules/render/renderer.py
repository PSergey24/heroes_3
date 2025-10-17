import os
import pygame

from modules.settings import Settings
from modules.render.unit_renderer import UnitRenderer


class BattleRenderer:

    def __init__(self, screen):
        self.screen = screen
        self.bg_surface = None
        self.clock = pygame.time.Clock()
        self.anim_accumulator_ms = 0
        self.anim_base_frame_ms = 120
        self.anim_speed_multiplier = 8
        self.on_unit_move_complete = None

    def load_background(self, filename):
        window_size = (Settings.width, Settings.height)
        self.bg_surface = pygame.transform.scale(
            pygame.image.load(os.path.join("data/bg", filename)), window_size
        )

    def draw_background(self):
        if self.bg_surface is not None:
            self.screen.blit(self.bg_surface, (0, 0))

    def draw_field(self, field):
        field.draw(self.screen)

    def draw_units(self, units):
        for item in sorted(units, key=lambda x: x.hex[0][0], reverse=False):
            UnitRenderer.draw_unit(self.screen, item)

    # animation timing utilities
    def tick(self, fps=60):
        return self.clock.tick(fps)

    def advance_unit_animations(self, units, dt_ms):
        self.anim_accumulator_ms += dt_ms
        effective_frame_ms = max(1, self.anim_base_frame_ms / max(1, self.anim_speed_multiplier))
        if self.anim_accumulator_ms < effective_frame_ms:
            return

        frames_to_advance = int(self.anim_accumulator_ms / effective_frame_ms)
        self.anim_accumulator_ms = self.anim_accumulator_ms % effective_frame_ms

        for _ in range(frames_to_advance):
            for unit_ in units:
                # cycle frames for standing and moving
                if len(getattr(unit_, 'current_animation_images', [])) > 0:
                    current_image = unit_.current_animation_images.pop(0)
                    unit_.current_animation_images.append(current_image)

                # advance position if moving
                if getattr(unit_, 'current_animation', None) == "moving":
                    if len(getattr(unit_, 'current_animation_points', [])) > 0:
                        unit_.position = unit_.current_animation_points.pop(0)
                    if len(getattr(unit_, 'current_animation_points', [])) == 0:
                        # finalize movement: lock on destination, switch to standing
                        if hasattr(unit_, '_pending_destination'):
                            dest_r, dest_c = unit_._pending_destination
                            unit_.i, unit_.j = dest_r, dest_c
                            # refresh field occupancy and hex
                            try:
                                unit_.reset_field()
                                unit_.init_hex()
                                unit_.init_field()
                                delattr(unit_, '_pending_destination')
                            except Exception:
                                pass
                        unit_.current_animation = "standing"
                        if hasattr(unit_, 'animations') and 'standing' in unit_.animations:
                            unit_.current_animation_images = [unit_.get_surface(img) for img in unit_.animations['standing'] for _ in range(6)]
                        # notify game to recompute reachability
                        if callable(self.on_unit_move_complete):
                            try:
                                self.on_unit_move_complete()
                            except Exception:
                                pass


