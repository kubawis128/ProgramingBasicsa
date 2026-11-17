import engine
import user_input
import verify

user_input_str = "0000"
actual_pin = engine.engine_rnd()
user_input_str = user_input.get_user_input()
while not verify.verify(user_input_str, actual_pin):
    user_input_str = user_input.get_user_input()
print("Thanks for playing")