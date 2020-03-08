# "Pet Search Party" App 
Finding Missing Pets with a Geolocation Based App -- A ChiPy Mentorship Project 

This web app help pet owners look for missing pets as they physically search for them on the street. Because it uses the geolocation ability of the browser, there's nothing to download like in an Android or iOS app. The app is meant to be used by opening up a browser on a smartphone and visiting a live site that hosts the app.

Use Case: After signing up, the owner creates a profile for their missing pet. The app tracks the path of the pet owner in real time and shows it on a map. Other people, who want to help search for that pet, can join the search party. Their path is tracked and shows up in the same map. Since it shows everybody's path on the same map, one can tell where people have searched already. Thus, they can make a decision where to search next, which will be in one of the unsearched areas.

The tech stack for the app is:
 - HTML, CSS, JavaScript, Bootstrap (front-end)
 - Django, Python, Postgres with PostGIS (back-end)
 - WebSockets from Django's Channels library (real-time tracking)
 - MapBox (map visualization)
 
 Visit  https://www.youtube.com/watch?v=nhn0cJU1mFs for a video demo of the app.
 To find more about the making of the app, visit the blog at https://sophanmien.com/blog/
