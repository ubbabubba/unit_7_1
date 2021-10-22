from car import car_7_1
from pytest import mark


def test_say_speed():
    #test the object returns speed message
    #arrange
    car_object =car_7_1.Car()
    return_speed = car_object.say_speed()
    #assert
    assert return_speed == 0


def test_say_odometer():
    #test that the object returns odometer reading
    #arrange
    car_object = car_7_1.Car()
    return_odometer = car_object.say_odometer()
    assert return_odometer == 0



def test_say_time():
    #arrange
    car_object = car_7_1.Car()
    #act
    return_time = car_object.say_time()
    #assert
    assert return_time ==0


def test_accelerate():
    car_object =car_7_1.Car()
    car_object.accelerate()
    assert car_object.say_speed() ==5

@mark.parametrize("speed,expected", [(30,25), (0,0)])
def test_brake(speed, expected):
    car_object =car_7_1.Car(speed=speed)
    car_object.brake()
    assert car_object.say_speed() == expected



def test_step():
    car_object =car_7_1.Car()
    car_object.step()
    odom_read = car_object.say_odometer()
    time_read = car_object.say_time()

    assert odom_read == 0 and time_read == 1

@mark.parametrize("odometerp,timep,expected_speed", [(0,0,0), (100,5,20)])
def test_average_speed(odometerp,timep,expected_speed):
    car_object =car_7_1.Car(odometer=odometerp, time=timep)
    avg_speed = car_object.average_speed()
    assert avg_speed == expected_speed
