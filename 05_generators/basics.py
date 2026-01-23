def serve_chai():
    yield "black tea"
    yield "ginger"
    yield "milk"
    yield "water"


stall = serve_chai()
# for chai in stall:
#     print(chai)

# OUPUT:
# black tea
# ginger
# milk
# water
print(stall)  # <generator object serve_chai at 0x000001FB2F2A49E0>

print(next(stall))  # black tea
print(next(stall))  # ginger
print(next(stall))  # milk
print(next(stall))  # water


def get_chai_list():
    return ["black tea", "ginger", "milk", "water"]


def chai_get():
    yield "Cup 1"
    yield "Cup 2"
    yield "Cup 3"


chai = chai_get()
print(next(chai))
