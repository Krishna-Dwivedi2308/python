def infinite_chais():
    count=1
    while True:
        yield f"Refill {count} done"
        count+=1

refill_user1=infinite_chais() #one object for user 1 
refill_user2=infinite_chais() #and another for user 2
# now this is the part where we are actually putting a limit or control over the generator.
for i in range(5):
    print('user 1 ',next(refill_user1))
for i in range(5):
    print('user 2 ',next(refill_user2))

# OUTPUT:
# user 1  Refill 1 done
# user 1  Refill 2 done
# user 1  Refill 3 done
# user 1  Refill 4 done
# user 1  Refill 5 done
# user 2  Refill 1 done
# user 2  Refill 2 done
# user 2  Refill 3 done
# user 2  Refill 4 done
# user 2  Refill 5 done

