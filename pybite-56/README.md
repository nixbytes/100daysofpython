Complete create_parser below so that our BMI program can be called like this:

    $ python bmi.py -h
    usage: bmi.py [-h] [-w WEIGHT] [-l LENGTH]

    Calculate your BMI.

    optional arguments:
      -h, --help            show this help message and exit
      -w WEIGHT, --weight WEIGHT
                            Your weight in kg
      -l LENGTH, --length LENGTH
                            Your length in cm

    $ python bmi.py -w 80 -l 187
    Your BMI is: 22.88

Please note that calc_bmi and handle_args are given, you only need to code create_parser!

We have two more Bites to practice argparse: 57 and 58.

