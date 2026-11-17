import engine
import user_input
import verify

user_input = "0000"
actual_pin =  engine.engine_rnd()
user_inp = ""
while not verify.verify(user_inp):
    user_inp = user_input.get_user_input()
print("Thanks for playing")