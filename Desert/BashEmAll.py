# https://codecombat.com/play/level/bash-em-all?
# Будь осторожен с ограми .
# Это специально обученные, обезжиренное убер-огры. Они очень сильны.
# Ключевое слово: "обезжиренные"
while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        if (hero.isReady('bash')):
            hero.bash(enemy)
        else:
            hero.moveXY(40, 34)
    else:
        item = hero.findNearestItem()
        if item:
            hero.moveXY(item.pos.x, item.pos.y)
            hero.moveXY(40, 34)
