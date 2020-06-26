def is_a_valid_ip_address(word):

    digits = word.split(".")
    if len(digits) == 4:
        for digit in digits:
            if int(digit) > 255:
                # IP4 address should always be less than 255
                return False
        return True
    return False


def get_most_frequnent_ip_address():
    log = '1.1.1.1 xyz.com 2.2.2.2 howareu.com 3.3.3.3 pp.com ' \
          '1.1.1.1 kk.com 1.1.1.1 ee 2.2.2.2 ll 3.3.3.3 9.9.9.9 1.1.1.1 10.10.10.10 22.22.22.22 1.1.1.1 2.2.2.2 '
    # split on space
    log_words = log.split()
    # initiate to None
    most_frequent_ip_address = None
    max_frequency = 0
    # lets count in this dictionary
    ip_address_counter = {}
    for word in log_words:
        if is_a_valid_ip_address(word):
            if word in ip_address_counter:
                # increment count of this valid ip address
                ip_address_counter[word] += 1
            else:
                # new ip address
                ip_address_counter[word] = 1

            # let us compare the max frequency here itself
            if ip_address_counter[word] > max_frequency:
                max_frequency = ip_address_counter[word]
                most_frequent_ip_address = word
    return most_frequent_ip_address, max_frequency


print(get_most_frequnent_ip_address())
