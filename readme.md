bank4u

Banks Branch details API service.
Changes Have been made to the SQL script to be able to accomodate 10000 rows in Heroku by creating a Trigger.

Endpoints:

/api/v1/getToken
        Desceription : Endpoint to get the token WHICH is valid for only 5 days.
        Accepts POST/GET request.
        Params : Expects Nothing.
        Returns : a JWT in JSON.


/api/v1/getDetails
        Desceription : Endpoint to get the bank details given the IFSC.
        Accepts GET request.
        Params : Expects JWT in header and IFSC in param.
        Returns : bank details if IFSC exists in Database otherwise an error message in JSON Format.


/api/v1/getBranches
        Desceription : Endpoint to fetch all details of branches, given bank name and a city. This API should also support limit and offset parameters.
        Accepts GET request.
        Params : Expects JWT in header and bank name, city, offset(optional), limit(optional) in params.
        Returns : branches details if bank name & city exists in Database otherwise an error message in JSON Format.
        Default values: offset=1, limit=10

cURL script is included you can play around.

Also it has been deployed at - https://bank4u.herokuapp.com/ + <API_ENDPOINT>