# IR Project Instructions

Step 1 : To create virtual Environment ( only once it need to be executed )

<code>py -3 -m venv venv </code>

Step 2 : activate virtual Environment ( everytime when opening new project )

<code> venv\Scripts\activate </code>

<!-- command for creating  requirements file not needed until and unless your adding more packages  -->

<!-- <code>pip freeze > requirements.txt <code> -->

Step 3: Installing packages from requirements file

<code> pip install -r requirements.txt </code>

Step 4 : Run flask app

<code> set FLASK_APP=run </code> <!-- to set flask app -->
<code> flask run --debug </code> <!-- to run flask app -->

## Note

Don't Forget to Download NLTK packages
( only once it need to be used ) -->

<code> import nltk </code>

<code> nltk.download() </code>
