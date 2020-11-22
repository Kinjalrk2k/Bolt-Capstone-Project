# Bolt-Capstone-Project

## Project Objectives:

The pharmaceutical companies use a cooling chamber which is similar to a refrigerator to keep the tablets and maintain the temperature in the required limits. However, since you most probably don’t have a cooling chamber which can maintain a temperature in the range, of -40 to -30 degrees Celcius, you can instead use a regular refrigerator at your home for this project.

_The objectives of the Capstone project are as follows._

**A.** Build the circuit for temperature monitoring system, using the Bolt and LM35 sensor. NOTE: You have already learned how to do this in Module 3 of the course, you can repeat the circuit connection for the system.

**B.** Create a product on the Bolt Cloud, to monitor the data from the LM35, and link it to your Bolt.

**C.** Write the product code, required to run the polynomial regression algorithm on the data sent by the Bolt.

With this objective in mind, Mr. Nigel managed to satisfy the first condition set by the Government. Using the prediction data, he was able to take early action, whenever the graph predicted that the temperature would be maintained within the -33 and -30 degrees Celsius range for longer than 20 minutes.

**D.** Keep the temperature monitoring circuit inside your fridge with the door of the fridge closed, and let the system record the temperature readings for about 2 hours.

**E.** Using the reading that you received in the 2 hours, set boundaries for the temperature within the fridge.

**F.** Write a python code which will fetch the temperature data, every 10 seconds, and send out an email alert, if the temperature goes beyond the temperature thresholds you decided on in objective "E".

**G.** Modify the python code, to also do a Z-score analysis and print the line “Someone has opened the fridge door” when an anomaly is detected.

**H.** Tune the Z-score analysis code, such that, it detects an anomaly when someone opens the door of the fridge.

As you may have guessed, this objective helped Mr. Nigel set up a system which knew that the fridge door was open, without any extra hardware. Remember that in your case, you might have to keep the door open for about 10 seconds to see the results.
