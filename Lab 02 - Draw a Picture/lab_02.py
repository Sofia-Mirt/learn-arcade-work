import arcade

arcade.open_window(1000, 1000, "Camp")
arcade.set_background_color(arcade.csscolor.BLACK)
arcade.start_render()

# Draw the ground.
arcade.draw_lrtb_rectangle_filled(1, 1000, 20, 1, (8, 0, 8))
arcade.draw_lrtb_rectangle_filled(1, 1000, 40, 21, (8, 0, 8))
arcade.draw_lrtb_rectangle_filled(1, 1000, 60, 41, (8, 0, 8))
arcade.draw_lrtb_rectangle_filled(1, 1000, 80, 61, (8, 1, 8))
arcade.draw_lrtb_rectangle_filled(1, 1000, 100, 81, (8, 2, 8))
arcade.draw_lrtb_rectangle_filled(1, 1000, 120, 101, (8, 3, 8))
arcade.draw_lrtb_rectangle_filled(1, 1000, 140, 121, (8, 4, 8))
arcade.draw_lrtb_rectangle_filled(1, 1000, 160, 141, (8, 5, 8))
arcade.draw_lrtb_rectangle_filled(1, 1000, 180, 161, (8, 6, 8))
arcade.draw_lrtb_rectangle_filled(1, 1000, 200, 181, (8, 7, 8))
arcade.draw_lrtb_rectangle_filled(1, 1000, 220, 201, (8, 8, 8))
arcade.draw_lrtb_rectangle_filled(1, 1000, 240, 221, (8, 9, 8))
arcade.draw_lrtb_rectangle_filled(1, 1000, 260, 241, (8, 10, 8))
arcade.draw_lrtb_rectangle_filled(1, 1000, 280, 261, (8, 11, 8))
arcade.draw_lrtb_rectangle_filled(1, 1000, 300, 281, (8, 12, 8))
arcade.draw_lrtb_rectangle_filled(1, 1000, 320, 301, (8, 13, 8))
arcade.draw_lrtb_rectangle_filled(1, 1000, 340, 321, (8, 14, 8))
arcade.draw_lrtb_rectangle_filled(1, 1000, 360, 341, (8, 16, 8))
arcade.draw_lrtb_rectangle_filled(1, 1000, 380, 361, (8, 18, 8))
arcade.draw_lrtb_rectangle_filled(1, 1000, 400, 381, (8, 20, 8))
arcade.draw_lrtb_rectangle_filled(1, 1000, 420, 401, (8, 22, 8))
arcade.draw_lrtb_rectangle_filled(1, 1000, 440, 421, (8, 24, 8))
arcade.draw_lrtb_rectangle_filled(1, 1000, 460, 441, (8, 26, 8))
arcade.draw_lrtb_rectangle_filled(1, 1000, 480, 461, (8, 28, 8))
arcade.draw_lrtb_rectangle_filled(1, 1000, 500, 481, (8, 30, 8))

# Draw the sky.
arcade.draw_lrtb_rectangle_filled(1, 1000, 520, 501, (30, 15, 30))
arcade.draw_lrtb_rectangle_filled(1, 1000, 540, 521, (28, 15, 28))
arcade.draw_lrtb_rectangle_filled(1, 1000, 560, 541, (26, 15, 26))
arcade.draw_lrtb_rectangle_filled(1, 1000, 580, 561, (24, 15, 24))
arcade.draw_lrtb_rectangle_filled(1, 1000, 600, 581, (22, 15, 22))
arcade.draw_lrtb_rectangle_filled(1, 1000, 620, 601, (20, 15, 20))
arcade.draw_lrtb_rectangle_filled(1, 1000, 640, 621, (19, 15, 19))
arcade.draw_lrtb_rectangle_filled(1, 1000, 660, 641, (18, 15, 18))
arcade.draw_lrtb_rectangle_filled(1, 1000, 680, 661, (17, 15, 17))
arcade.draw_lrtb_rectangle_filled(1, 1000, 700, 681, (16, 15, 16))
arcade.draw_lrtb_rectangle_filled(1, 1000, 720, 701, (15, 15, 15))
arcade.draw_lrtb_rectangle_filled(1, 1000, 740, 721, (14, 15, 14))
arcade.draw_lrtb_rectangle_filled(1, 1000, 760, 741, (13, 15, 13))
arcade.draw_lrtb_rectangle_filled(1, 1000, 780, 761, (12, 15, 12))
arcade.draw_lrtb_rectangle_filled(1, 1000, 800, 781, (11, 15, 11))
arcade.draw_lrtb_rectangle_filled(1, 1000, 820, 801, (10, 15, 10))
arcade.draw_lrtb_rectangle_filled(1, 1000, 840, 821, (9, 15, 9))
arcade.draw_lrtb_rectangle_filled(1, 1000, 860, 841, (8, 15, 8))
arcade.draw_lrtb_rectangle_filled(1, 1000, 880, 861, (7, 15, 7))
arcade.draw_lrtb_rectangle_filled(1, 1000, 900, 881, (6, 15, 6))
arcade.draw_lrtb_rectangle_filled(1, 1000, 920, 901, (5, 15, 5))
arcade.draw_lrtb_rectangle_filled(1, 1000, 940, 921, (4, 15, 4))
arcade.draw_lrtb_rectangle_filled(1, 1000, 960, 941, (3, 15, 3))
arcade.draw_lrtb_rectangle_filled(1, 1000, 980, 961, (2, 15, 2))
arcade.draw_lrtb_rectangle_filled(1, 1000, 1000, 981, (1, 15, 1))

# Draw a tree.
arcade.draw_rectangle_filled(240, 560, 30, 160, (61, 36, 3))
arcade.draw_parabola_filled(200, 320, 280, 300, (3, 30, 31), 300)
arcade.draw_parabola_filled(280, 320, 200, 300, (3, 30, 31), 60)
arcade.draw_parabola_filled(200, 420, 280, 260, (3, 30, 31), 305)
arcade.draw_parabola_filled(280, 420, 200, 260, (3, 30, 31), 55)
arcade.draw_parabola_filled(200, 540, 270, 200, (3, 30, 31), 310)
arcade.draw_parabola_filled(280, 540, 210, 200, (3, 30, 31), 50)
arcade.draw_arc_filled(240, 750, 70, 180, (3, 30, 31), 0, 180)
arcade.draw_circle_filled(240, 620, 40, (3, 30, 31))
arcade.draw_circle_filled(240, 700, 40, (3, 30, 31))


# Draw a bush.
arcade.draw_circle_filled(200, 380, 30, (3, 36, 30))
arcade.draw_circle_filled(215, 415, 30, (3, 36, 30))
arcade.draw_circle_filled(185, 440, 30, (3, 36, 30))
arcade.draw_circle_filled(150, 445, 30, (3, 36, 30))
arcade.draw_circle_filled(125, 410, 30, (3, 36, 30))
arcade.draw_circle_filled(150, 385, 30, (3, 36, 30))
arcade.draw_circle_filled(180, 425, 30, (3, 36, 30))

# Draw second bush.
arcade.draw_circle_filled(290, 355, 30, (4, 41, 35))
arcade.draw_circle_filled(315, 370, 30, (4, 41, 35))
arcade.draw_circle_filled(285, 410, 30, (4, 41, 35))
arcade.draw_circle_filled(250, 415, 30, (4, 41, 35))
arcade.draw_circle_filled(225, 380, 30, (4, 41, 35))
arcade.draw_circle_filled(250, 355, 30, (4, 41, 35))
arcade.draw_circle_filled(280, 395, 30, (4, 41, 35))

# Draw a tent.
arcade.draw_triangle_filled(440, 470, 500, 500, 470, 600, (106, 48, 16))
arcade.draw_polygon_filled(((440, 470),
                            (470, 600),
                            (350, 601),
                            (310, 477)
                            ),
                           (78, 31, 5))
arcade.draw_line(470, 600, 470, 485, (64, 32, 15), 2)

# Draw a fire.
arcade.draw_line(570, 510, 590, 480, (86, 37, 10), 5)
arcade.draw_line(570, 510, 550, 480, (86, 37, 10), 5)
arcade.draw_line(570, 510, 570, 475, (86, 37, 10), 5)
arcade.draw_line(570, 510, 580, 477, (86, 37, 10), 5)
arcade.draw_line(570, 510, 560, 477, (86, 37, 10), 5)
arcade.draw_polygon_filled(((570, 500),
                            (560, 510),
                            (565, 525),
                            (570, 530),
                            (572, 525),
                            (575, 538),
                            (578, 530),
                            (580, 520),
                            (575, 540),
                            (580, 505)
                            ),
                           arcade.csscolor.ORANGE)

# Draw a light from the fire.
arcade.draw_arc_filled(570, 500, 60, 80, (255, 188, 3, 30), 0, 180)
arcade.draw_arc_filled(570, 500, 60, 40, (255, 188, 3, 20), 180, 360)
arcade.draw_arc_filled(570, 500, 120, 140, (255, 188, 3, 20), 0, 180)
arcade.draw_arc_filled(570, 500, 120, 80, (255, 188, 3, 15), 180, 360)
arcade.draw_arc_filled(570, 500, 200, 220, (255, 188, 3, 15), 0, 180)
arcade.draw_arc_filled(570, 500, 200, 150, (255, 188, 3, 10), 180, 360)
arcade.draw_arc_filled(570, 500, 350, 370, (255, 188, 3, 10), 0, 180)
arcade.draw_arc_filled(570, 500, 350, 280, (255, 188, 3, 10), 180, 360)

# Draw the moon.
arcade.draw_circle_filled(150, 950, 30, arcade.csscolor.SEASHELL)
arcade.draw_circle_filled(170, 950, 25, (4, 15, 4))

# Draw stars.
arcade.draw_circle_filled(850, 980, 2, arcade.csscolor.SEASHELL)
arcade.draw_circle_filled(963, 648, 2, arcade.csscolor.SEASHELL)
arcade.draw_circle_filled(60, 860, 2, arcade.csscolor.SEASHELL)
arcade.draw_circle_filled(30, 530, 2, arcade.csscolor.SEASHELL)
arcade.draw_circle_filled(450, 930, 2, arcade.csscolor.SEASHELL)
arcade.draw_circle_filled(856, 526, 2, arcade.csscolor.SEASHELL)
arcade.draw_circle_filled(496, 759, 2, arcade.csscolor.SEASHELL)
arcade.draw_circle_filled(753, 736, 2, arcade.csscolor.SEASHELL)


arcade.finish_render()
arcade.run()
