# sber_api_django
 Тестовое задание СБЕР
 
 
### Task:

We're building a website for an electric utility company.
Below is the view we use to retrieve various data related to our clients.
Some specs:
- This view is available via `POST /api/clients/{id}/data/{type}`; see arguments below.
- Requires authentication: admin users may view information related to any client,
general users can only view their own data;
- Arguments:
  - path:
    - `id` must correspond to existing Client record in the database
    - `type` is a type of data to return: either "payments", "charges" or "measurements"
  - body:
    - `start` - start of the period to fetch data for;
    - `end` - end of the period to fetch data for.
- All three PaymentsData, BillsData and MeasurementsData functions return dictionaries of following format:
  - 'count' (int): number of records returned;
  - 'data' (list): records for given period.

