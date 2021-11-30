from day09.class_lib.airplane import Airplane
from day09.class_lib.super_sonic_airplane import SuperSonicAirplane

sa = SuperSonicAirplane()
sa.take_off()
sa.fly()
sa.fly_mode = SuperSonicAirplane.SUPERSONIC
sa.fly()
sa.fly_mode = SuperSonicAirplane.NORMAL
sa.fly()
sa.land()