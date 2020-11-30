This project is related to price prediction of second-hand bikes using machine learning. This is end-to-end project deployed using docker and consists of the following steps:

Step1: Scraping the required data from website
	-- This is the initial step where data was collected from the site https://hamrobazaar.com/search.php?do_search=Search&searchword=&catid_search=62 for all the available brands of bikes.
	-- Web scraping was performed using scrapy and selenium. Scrapy was used since it is faster and selenium was used since the webpages were dynamic. Four fields were extracted at total.
	-- Refer to webscraping folder for the code and also the extracted .csv files.

Step2: Merging all the data into one
	-- In this step, all the separate files were merged into one with some cleaning done.
	-- Refer to mergingfiles.ipynb for the code and data.csv for the final merged file.

Step3: Make a model
	-- In this step, a model is created using sklearn. A common model is created for the brands and only those models are selected which gives a score that is greater than or equal to 0.5.
	-- Refer to hamrobazar models preparation.ipynb for the step.

Step4: Save the model
	-- The created model is then saved using pickle.
	-- Refer to bikes_price_prediction\webdevelopment_using_django\pricepredict\hamrobazar models to view the saved models.

Step5: Web development using django to implement the model
	-- To implement the model that we created, webdevelopment was performed using django. Simplified HTML file with no CSS was created.
	-- Refer to webdevelopment_using_django folder for the step.
 
Step6: Deployment of the website using docker
	-- Finally, the website was deployed using docker. For that, docker was installed at first and then Dockerfile along with requirements.txt were created to make a docker container containing all the libraries, dependencies and requirements.
	-- Refer to Dockerfile and requirements.txt for the step

Step7: Building a docker image and running it
	-- To build the docker, use the following cmd:
		docker build -t bikes_api .
	-- To run the docker, use the following cmd:
		docker run -p 8000:8000 bikes_api

In this way, a model was created to predict the price of second-hand bikes.

Note- Refer to the screenshots folder in order to view some of the results.

 
