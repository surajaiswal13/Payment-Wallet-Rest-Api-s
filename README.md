# Setting up project and project Environment 

## 1. create environment
```
$ conda create -n envname python=3.7
```

## 2. Activate your Environment
```
$ conda activate EnvName
```

3. Install All Requirenments using requirements.txt

NOTE: goto to the folder when requirements.txt file is present before executing the below command.

```
$ pip freeze > requirements.txt
```

4. Configure the project

### NOTE: Make sure you are in the main project folder
```
$ python manage.py migrate
```

```
$ python manage.py makemigrations
```

```
$ python manage.py migrate
```

5. Run the Project on your Local System

```
$ pthon manage.py runserver
```


# Urls and api's to Access

## 1. Crearing account 
#### We can use navigation bar for Login and Register

## 2. Creating Wallet

#### From Form access the api
```
$ http://127.0.0.1:8000/api/create_wallet
```
Example Input: Any amount you want to deposit while creating the wallet i.e 9876

## 3. Finding User Id

#### For getting to know User Id
```
$ http://127.0.0.1:8000/api/currentid
```

## 4. Adding Money

#### Adding money through using Navigation set on create wallet page (Step no. 2)

Example Input: 
{
  "balance" : 10
}

####                    OR

#### For Adding thew money using Api
```
$ http://127.0.0.1:8000/api/add_money_to_wallet/<int:pk>
```
Note : we will need pk i.e Primary Key we can get it using (Step no. 3)

Example Input: 
{
  "balance" : 10
}

## 5. Withdrawing Money

#### Withdrawing Money using Navigation set on create wallet page (Step no. 2)

Example Input: 
{
  "balance" : 10
}

####                     OR

#### For Withdrawing the money using Api
```
$ http://127.0.0.1:8000/api/withdraw_money_from_wallet/<int:pk>
```

Example Input: 
{
  "balance" : 10
}

## 6. Check Balance

#### Checking Balance using Navigation set on create wallet page (Step no. 2)

Click on Check Balance on Create Wallet page

####                     OR

#### For Withdrawing the money using Api
```
$ http://127.0.0.1:8000/api/check_balance/<int:pk>
```

## 7. Delete Wallet

Click on Delete on Create Walet page -> Click Delete on upper right corner and click ok

####                     OR

#### For Withdrawing the money using Api
```
$ http://127.0.0.1:8000/api/delete_wallet/<int:pk>
```
Click on Delete on Create Walet page -> Click Delete on upper right corner and click ok

## Contributors <img src="https://raw.githubusercontent.com/TheDudeThatCode/TheDudeThatCode/master/Assets/Developer.gif" width=35 height=25> 

- Suraj Jaiswal