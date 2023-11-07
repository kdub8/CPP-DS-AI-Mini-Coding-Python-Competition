def squirrel_play(temperature, is_summer):
    if temperature >= 60 and temperature <= 90 and is_summer == False:
        print(True)
        return True
    elif temperature >= 60 and temperature <= 100 and is_summer == True:
        print(True)
        return True
    else:
        print(False)
        return False


squirrel_play(70, False)
squirrel_play(90, True)
squirrel_play(100, True)
squirrel_play(100, False)
squirrel_play(40, False)
squirrel_play(40,True)