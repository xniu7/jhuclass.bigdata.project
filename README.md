##Bigdata_Project

Team: Ruilong He, Yao Huang, Xiang Niu

Our genome website is builded by django.

= 
Directories:
* Admin, localhost directories include lots of web schema like css files.

* Downfile directory, which is the most importance part of django framework, includes the interfaces (view.py) to our backend (computation part) and frontend (display part)

* Hadoop directory is an individual part of computation. We can use this to compute suffix array by mapreduce.

* Statistic directory contains almost all of the computation scripts. All statistic features and genome assembly scripts are included.

* ucscSQL directory is the SQL connection to uscs, which is already abandoned.

* utility directory contains all of libraries and tools we need.

Files:
* index.html is the main page.

* manage.py is the webserver mangement script. Please using python manage.py 0.0.0.0:8080 to start the server.


