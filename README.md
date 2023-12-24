**Pacakages used**

    asgiref==3.7.2
    Django==5.0
    django-rest-framework==0.1.0
    djangorestframework==3.14.0
    Faker==21.0.0
    python-dateutil==2.8.2
    pytz==2023.3.post1
    six==1.16.0
    sqlparse==0.4.4
    tzdata==2023.3

1. Clone repository 
  > git clone  https://github.com/Vidit-Kumar/DjangoForLims.git

2. Goto folder "DjangoForLims and create virtual environment
   > py -m venv yourenvnamehere
   
   yourenvnamehere>\Scripts\activate.bat
    (It will prompt envirnment folder as (envname) C:\Users\Your Name>)

3. Install package for custome environment
   >py -m pip install -r requirements.txt

4. Navigate to \DjangoForLims\projectlims folder

5. Initialize migrate

   >py manage.py makemigrations library
   
   >py manage.py migrate

6. On running server first time 
     
     a) 200 records will be added in db
     
     b) Two users will be provisioned with new accounts.
   
		userid= lims_user; pwd=lims   **(Normal user)**
	  
   		userid= lims_admin; pwd=admin **(Admin user**)


**URI INTERFACES**

	http://127.0.0.1:8000/books/
  
	http://127.0.0.1:8000/adminview/ [user datamodel] **(NOTE: pending access to admin only)**


**REST API**
	
 	http://127.0.0.1:8000/api/books/	

	http://127.0.0.1:8000/api/books/?Limit=10

 	http://127.0.0.1:8000/api/checkout/
	{
	 "book_id":20
	} 
