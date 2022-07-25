from flask import Flask, render_template, request, flash, redirect
import pickle
import numpy as np

model = pickle.load(open("hotel.pkl", "rb"))

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/predict", methods = ['GET', 'POST'])
def predict():
    if request.method == "POST":
        hotel = request.form["hotel"]
        if(hotel == "Resort Hotel"):
            hotel = 0
        elif(hotel == "City Hotel"):
            hotel = 1

        meal = request.form["meal"]
        if (meal == "BB"):
            meal = 0
        elif (meal == "FB"):
            meal = 1
        elif (meal == "HB"):
            meal = 2
        elif (meal == "SC"):
            meal = 3
        elif (meal == "Undefined"):
            meal = 4

        market_segment = request.form["market_segment"]
        if (market_segment == "Direct"):
            market_segment = 0
        elif (market_segment == "Corporate"):
            market_segment = 1
        elif (market_segment == "Online TA"):
            market_segment = 2
        elif (market_segment == "Offline TA/TO"):
            market_segment = 3
        elif (market_segment == "Complementary"):
            market_segment = 4
        elif (market_segment == "Groups"):
            market_segment = 5
        elif (market_segment == "Undefined"):
            market_segment = 6
        elif (market_segment == "Aviation"):
            market_segment = 7

        distribution_channel = request.form["distribution_channel"]
        if (distribution_channel == "Direct"):
            distribution_channel = 0
        elif (distribution_channel == "Corporate"):
            distribution_channel = 1
        elif (distribution_channel == "TA/TO"):
            distribution_channel = 2
        elif (distribution_channel == "Undefined"):
            distribution_channel = 3
        elif (distribution_channel == "GDS"):
            distribution_channel = 4


        reserved_room_type = request.form["reserved_room_type"]
        if (reserved_room_type == "C"):
            reserved_room_type = 0
        elif (reserved_room_type == "A"):
            reserved_room_type = 1
        elif (reserved_room_type == "D"):
            reserved_room_type = 2
        elif (reserved_room_type == "E"):
            reserved_room_type = 3
        elif (reserved_room_type == "G"):
            reserved_room_type = 4
        elif (reserved_room_type == "F"):
            reserved_room_type = 5
        elif (reserved_room_type == "H"):
            reserved_room_type = 6
        elif (reserved_room_type == "L"):
            reserved_room_type = 7
        elif (reserved_room_type == "B"):
            reserved_room_type = 8

        deposit_type = request.form["deposit_type"]
        if (deposit_type == "No Deposit"):
            deposit_type = 0
        elif (deposit_type == "Refundable"):
            deposit_type = 1
        elif (deposit_type == "Non Refund"):
            deposit_type = 2

        customer_type = request.form["customer_type"]
        if (customer_type == "Transient"):
            customer_type = 0
        elif (customer_type == "Contract"):
            customer_type = 1
        elif (customer_type == "Transient-Party"):
            customer_type = 2
        elif (customer_type == "Group"):
            customer_type = 3

        year = request.form["year"]
        if (year == "2014"):
            year = 1
        elif (year == "2015"):
            year = 0
        elif (year == "2016"):
            year = 2
        elif (year == "2017"):
            year = 3


        month = request.form["month"]
        day = request.form["day"]
        lead_time = request.form["lead_time"]
        arrival_date_week_number = request.form["arrival_date_week_number"]
        stays_in_weekend_nights = request.form["stays_in_weekend_nights"]
        stays_in_week_nights = request.form["stays_in_week_nights"]
        adults = request.form["adults"]
        children = request.form["children"]
        babies = request.form["babies"]
        is_repeated_guest = request.form["is_repeated_guest"]
        previous_cancellations = request.form["previous_cancellations"]
        previous_bookings_not_canceled = request.form["previous_bookings_not_canceled"]
        adr = request.form["adr"]
        required_car_parking_spaces = request.form["required_car_parking_spaces"]
        total_of_special_requests = request.form["total_of_special_requests"]

        lead_time = np.log(int(lead_time) + 1)
        arrival_date_week_number = np.log(int(arrival_date_week_number) + 1)
        adr = np.log(int(adr) + 1)


        prediction = model.predict([[
            hotel,
            meal,
            market_segment,
            distribution_channel,
            reserved_room_type,
            deposit_type,
            customer_type,
            year,
            month,
            day,
            lead_time,
            arrival_date_week_number,
            stays_in_weekend_nights,
            stays_in_week_nights,
            adults,
            children,
            babies,
            is_repeated_guest,
            previous_cancellations,
            previous_bookings_not_canceled,
            adr,
            required_car_parking_spaces,
            total_of_special_requests
        ]])

        if prediction == 1:
            result = "Hotel Booking will be Canceled"
        else:
            result = "Hotel Booking will Not be Cancelled"

        return render_template('home.html', prediction_text = result)


if __name__ == '__main__':
	app.run(debug = True, port = 5002)