import pygame as pg


def collide_hit_rect(one, two):
    return one.hit_rect.colliderect(two.rect)


def collide_with_walls(sprite, group, dir, k=2):
    if dir == 'x':
        hits = pg.sprite.spritecollide(sprite, group, False, collide_hit_rect)
        if hits:
            if hits[0].rect.centerx > sprite.hit_rect.centerx:
                sprite.pos.x = hits[0].rect.left - sprite.hit_rect.width / k
            if hits[0].rect.centerx < sprite.hit_rect.centerx:
                sprite.pos.x = hits[0].rect.right + sprite.hit_rect.width / k
            sprite.vel.x = 0
            sprite.hit_rect.centerx = sprite.pos.x
    if dir == 'y':
        hits = pg.sprite.spritecollide(sprite, group, False, collide_hit_rect)
        if hits:
            if hits[0].rect.centery > sprite.hit_rect.centery:
                sprite.pos.y = hits[0].rect.top - sprite.hit_rect.height / k
            if hits[0].rect.centery < sprite.hit_rect.centery:
                sprite.pos.y = hits[0].rect.bottom + sprite.hit_rect.height / k
            sprite.vel.y = 0
            sprite.hit_rect.centery = sprite.pos.y

''' to do - collisions reaper with people (deleting people?)
def collide_with_people(sprite, group, dir, k=2):
    k = sprite.pos
    if dir == 'x':
        hits = pg.sprite.spritecollide(sprite, group, True, collide_hit_rect)
        if hits:
            print(k)
            print(sprite.pos)
            #if hits[0].rect.centerx > sprite.hit_rect.centerx:
                #sprite.pos.x = hits[0].rect.left - sprite.hit_rect.width / k
            #if hits[0].rect.centerx < sprite.hit_rect.centerx:
                #sprite.pos.x = hits[0].rect.right + sprite.hit_rect.width / k
            #sprite.vel.x = 0
            #sprite.hit_rect.centerx = sprite.pos.x
            #sprite.pos = k
            print(k)
            return True
    if dir == 'y':
        hits = pg.sprite.spritecollide(sprite, group, True, collide_hit_rect)
        if hits:
            #if hits[0].rect.centery > sprite.hit_rect.centery:
                #sprite.pos.y = hits[0].rect.top - sprite.hit_rect.height / k
            #if hits[0].rect.centery < sprite.hit_rect.centery:
                #sprite.pos.y = hits[0].rect.bottom + sprite.hit_rect.height / k
            #sprite.vel.y = 0
            #sprite.hit_rect.centery = sprite.pos.y
            sprite.pos = k
            return True
    return False'''
