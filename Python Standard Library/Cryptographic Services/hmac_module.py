import hmac

# https://datatracker.ietf.org/doc/html/rfc2104.html#autoid-6
# https://www.youtube.com/watch?v=MKn3cxFNN1I&ab_channel=productioncoder


my_key = "ads54d8d9".encode()
my_message = hmac.new(key=bytes(my_key), msg="hello friend".encode(), digestmod="sha256")

other_key = "ads54d8d9".encode()
# other_key = "ads54444".encode()
other_message = hmac.new(key=bytes(other_key), msg="hello friend".encode(), digestmod="sha256")

print(my_message.hexdigest())

# #################### compare two digests ###################### #

print(hmac.compare_digest(my_message.hexdigest(), other_message.hexdigest()))  # True if the same algorithm and key

print(my_message.name)
