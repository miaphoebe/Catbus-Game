import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

bus_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
speed = 300

bus_shape = [
    # --- belly (front -> back) ---
    (-120,  38),
    (-95,   46),
    (-60,   52),
    (-20,   55),
    ( 25,   54),
    ( 70,   52),
    (105,   48),
    (125,   40),

    # --- back / rump up ---
    (135,   30),
    (138,   15),
    (136,    0),
    (130,  -12),

    # --- roof dome (back -> front) ---
    (115,  -28),
    ( 85,  -42),
    ( 40,  -50),
    ( -5,  -50),
    (-45,  -44),
    (-75,  -34),

    # --- head / snout bump (front top -> front bottom) ---
    (-98,  -22),
    (-112, -10),
    (-120,   5),

    # --- return to belly front ---
    (-122,  22),
]


leg_offsets = [(-80, 40), (-40, 40), (0, 40), (40, 40), (80, 40)]
# wheel_width = 20
# wheel_height = 80

while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        bus_pos.y -= speed * dt
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        bus_pos.y += speed * dt
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        bus_pos.x -= speed * dt
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        bus_pos.x += speed * dt

    screen.fill((250, 245, 220))

    bus_points = [(bus_pos.x + x, bus_pos.y + y) for (x, y) in bus_shape]

    pygame.draw.polygon(screen, (140, 90, 40), bus_points)
    pygame.draw.polygon(screen, (60, 35, 10), bus_points, 4)

        # --- Simple cat head (ellipse + ears) ---
    hx = bus_pos.x + 100
    hy = bus_pos.y - 35
    # Head ellipse
    head_rect = pygame.Rect(
        hx,  # x
        hy,   # y
        100,               # width
        80                # height
    )

    pygame.draw.ellipse(screen, (140, 90, 40), head_rect)

    # Left ear
    left_ear = [
        (hx + 10, hy + 10),
        (hx + 30, hy - 25),
        (hx + 50, hy + 10),
    ]

    # Right ear
    right_ear = [
        (hx + 45, hy + 10),
        (hx + 65, hy - 25),
        (hx + 85, hy + 10),
    ]

    pygame.draw.polygon(screen, (140, 90, 40), left_ear)

    pygame.draw.polygon(screen, (140, 90, 40), right_ear)

    
    # cat tail
    tw, th = 50, 150
    tail_surf = pygame.Surface((tw, th), pygame.SRCALPHA)

    # ellipse in tail_surf
    pygame.draw.ellipse(tail_surf, (140, 90, 40), (0, 0, tw, th))

    # rotate 
    tail_surf = pygame.transform.rotate(tail_surf, -75)

    # position on screen 
    tail_pos = (bus_pos.x - 200, bus_pos.y - 30)

    # blit to screen
    screen.blit(tail_surf, tail_pos)



    # Draw legs as ellipses 
    for ox, oy in leg_offsets:
        cx = int(bus_pos.x + ox)
        cy = int(bus_pos.y + oy)

        
        leg_points = [
            # start (back/top of leg at body)
            (cx - 8,  cy),

            # slight forward bulge (thigh)
            (cx - 2,  cy + 2),
            (cx + 6,  cy + 4),

            # your original front/top
            (cx + 16, cy),

            # shin slope (your original)
            (cx + 28, cy + 25),

            # knee/ankle taper before paw
            (cx + 34, cy + 30),
            (cx + 36, cy + 35),   # your original

            # paw front + toes
            (cx + 33, cy + 38),
            (cx + 27, cy + 40),
            (cx + 22, cy + 41),
            (cx + 18, cy + 41),
            (cx + 15, cy + 41),

            # your originals (paw/base/back)
            (cx + 20, cy + 39),
            (cx + 12, cy + 41),

            # heel bump + back of paw up toward leg
            (cx + 6,  cy + 40),
            (cx + 2,  cy + 37),
            (cx + 0,  cy + 33),
            (cx - 2,  cy + 28),
            (cx - 4,  cy + 22),
            (cx - 6,  cy + 14),
        ]

        # foot_points = [(bus_pos.x + x, bus_pos.y + y) for (x, y) in foot_shape]
        # hub_rect = pygame.Rect(cx - 6, cy + 20, 40, 40)
        # pygame.draw.ellipse(screen, (100, 50, 10), hub_rect)
        pygame.draw.polygon(screen, (140, 90, 40), leg_points)
        

    pygame.display.flip()

pygame.quit()
