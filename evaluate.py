QUAD_BOT_X = [2, 2, 1, 1.5, 2]
QUAD_BOT_Y = [-3.5, -4, -3, -3, -4]
NEW_BOT_X = [2, 1.5, 2.5, 2.5, 3.5]
NEW_BOT_Y = [-3.5, -3.5, -3.5, -4, -4.5]
print('lower is better; perfect is 0')
quad_bot_displacement = [(QUAD_BOT_X[i] ** 2 + QUAD_BOT_Y[i] ** 2) ** 0.5 for i in range(5)]
new_bot_displacement = [(NEW_BOT_X[i] ** 2 + NEW_BOT_Y[i] ** 2) ** 0.5 for i in range(5)]
quad_bot_displacement.sort()
new_bot_displacement.sort()
print('medians:')
print('quad bot:', quad_bot_displacement[2])
print('new bot:', new_bot_displacement[2])
import statistics
print('means:')
print('quad bot:', statistics.mean(quad_bot_displacement))
print('new bot:', statistics.mean(new_bot_displacement))
