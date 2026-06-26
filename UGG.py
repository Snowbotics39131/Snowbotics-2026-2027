from QuadBotPortMap import*
#run_task(shift(gear=2))
#wait(1000)
#run_task(use_attachment(500 ,500))
drivebase.straight(-800)
drivebase.turn (-45)
run_task(shift(gear=1))

wait(1000)
drivebase.straight(-30)
run_task(use_attachment(-400, 500))
drivebase.turn(45)