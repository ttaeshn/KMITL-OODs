def hell(now_step, all_step, thorn, max_stamina, now_stamina, tiredness:dict,hit_thorn = 0):
    ways = []
    if now_stamina > max_stamina:
        # print(f"now_stamina, max_stamina = {now_stamina, max_stamina} Bye")
        return [False]

    if now_step != 0 and str(now_step) in thorn:
        # print(f"now, thorn = {now_step, thorn[0]} Bye")
        return [False]

    if now_step >= all_step:
        # print(f"now_stamina, max_stamina, now_step, all_step = {now_stamina, max_stamina, now_step, all_step}")
        if now_stamina > max_stamina or now_step > all_step:
            # print("Bye")
            return [False]
        else:
            # print("Yay")
            return [True]

    for next_step in range(1,4):
        # print(f"next_step is {next_step + now_step}")
        ways.extend(hell(
            now_step = now_step + next_step,
            all_step = all_step,
            thorn = thorn,
            max_stamina = max_stamina,
            now_stamina = now_stamina + tiredness[next_step],
            tiredness = tiredness))
    
    return ways

inp = input("Creating a simulated hell scenario: ").split("/")
thorn = list(inp[1].split(","))
step = inp[-1].split(",")
print("Height: " + inp[0])
print("thorn At:",end=" ")
print(thorn)
print("Max Tiredness: " + str(float(inp[2])))
tiredness_dict = {}
num = 0
# print(step != [''])
if len(step) == 0:
    pass

elif len(step) == 1 and step != ['']:
    for i in range(0,3):
        tiredness_dict[i+1] = float(step[0])

elif len(step) > 1:   
    for i in range(0,3):
        if i < len(step):
            tiredness_dict[i+1] = float(step[i])
        else:
            tiredness_dict[i+1] = 0


print("Tiredness Values:",end=" ")
print(tiredness_dict)
print("--------------------------------------------------")
if len(step) >= 1 and step != ['']:
    all_ways = sum(1 for i in hell(0,int(inp[0]),thorn,float(inp[2]),0.0,tiredness_dict) if i is True)
    print(f"The ways to escape is/are {all_ways} ways")