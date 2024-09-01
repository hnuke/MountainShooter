#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY, WIN_HEIGHT
from code.EnemyShot import EnemyShot
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]
        self.top_touched = False

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]
        if self.name == 'Enemy3':
            if self.top_touched and 10 <= self.rect.centery <= WIN_HEIGHT - 10:
                self.rect.centery += ENTITY_SPEED[self.name] * 2
            elif not self.top_touched and 10 <= self.rect.centery <= WIN_HEIGHT - 10:
                self.rect.centery -= ENTITY_SPEED[self.name]
            elif self.rect.centery <= 10 and not self.top_touched:
                self.top_touched = True
                self.rect.centery += ENTITY_SPEED[self.name] * 2
            elif self.rect.centery >= WIN_HEIGHT - 10 and self.top_touched:
                self.top_touched = False
                self.rect.centery -= ENTITY_SPEED[self.name] * 2 # multiplicado para ter certeza que irá se manter no loop
            elif self.rect.centery >= WIN_HEIGHT - 10:
                self.rect.centery -= ENTITY_SPEED[self.name]
            elif self.rect.centery <= 0 - 10:
                self.rect.centery += ENTITY_SPEED[self.name] * 2





    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))
