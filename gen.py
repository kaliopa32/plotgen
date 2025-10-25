import random
import csv


# loop logic (100 iterations)


with open("res.csv", "w", newline="") as f:
    writer = csv.writer(f)

    # header row
    writer.writerow(["iteration","whole","head","tail"])

    for i in range(100):
        whole = round(random.uniform(0,10), 7) # generate a float between 0-10, with 7 rounding places
        tail = round(whole % 1, 7)
        head = int(whole)
        
        # these two need to have their format specific otherwise they will use scientific notation and / or remove trailing 0s
        whole_str = f"{whole:.7f}"
        tail_str = f"{tail:.7f}"


        # data row (loops range times)
        writer.writerow([i,whole_str,head,tail_str])

        # debug print
        #print(f"head {i+1} = {head} && tail {i+1} = {tail:07f}") # prints out head and tail (with iteration)
        

print("results written to res.csv")

