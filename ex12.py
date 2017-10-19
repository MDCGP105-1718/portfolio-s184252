def hotel_cost(nights):
    return 70.0 * nights

def plane_ticket_cost(city, flight_class):
    locations = {"New York": 2000,
                 "Auckland": 790,
                 "Venice": 154,
                 "Glasgow": 65}
    return locations[city] * flight_class

def rental_car_cost(days):
    if(days > 7):
        return (days * 30) - 50

    if(days > 3):
        return (days - 1) * 30

    return days * 30

def total_cost(city, days):
    price = hotel_cost(days - 1) + \
            plane_ticket_cost(city, 1) + \
            rental_car_cost(days)
            
    return price

print(total_cost("New York", 5))
