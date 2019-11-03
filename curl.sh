printf "\n\n\t\tBANK4U API SERVICE\n\n"

#request to get Token
printf "\n\nrequest to get Token\n"
curl -X GET \
    'https://bank4u.herokuapp.com/api/v1/getToken'\

#-------------------request to get branch details given the IFSC------------------------#
printf "-------------------request to get branch details given the IFSC------------------------"
#request with all correct details
printf "\n\nrequest with all correct details\n"
curl -X GET \
  'https://bank4u.herokuapp.com/api/v1/getDetails?ifsc=ABHY0065001' \
  -H 'token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NzMyNDA2NTh9.4xhUzQFLvJ5pxXXGHkO2GcOb9ti_6HW56I0-JLxAjRY' \
  -H 'Cache-Control: no-cache' \

#request with wrong token
printf "\n\nrequest with wrong token\n"
curl -X GET \
  'https://bank4u.herokuapp.com/api/v1/getDetails?ifsc=ABHY0065001' \
  -H 'token: eabceXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NzMyNDA2NTh9.4xhUzQFLvJ5pxXXGHkO2GcOb9ti_6HW56I0-JLxAjRY' \
  -H 'Cache-Control: no-cache' \

#request with wrong IFSC
printf "\n\nrequest with wrong IFSC\n"
curl -X GET \
  'https://bank4u.herokuapp.com/api/v1/getDetails?ifsc=ABHY0065601' \
  -H 'token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NzMyNDA2NTh9.4xhUzQFLvJ5pxXXGHkO2GcOb9ti_6HW56I0-JLxAjRY' \
  -H 'Cache-Control: no-cache' \


#-------------------request to get branches given bankname and city------------------------#
printf "\n\n-------------------request to get branches given bankname and city------------------------"
#request with everything correct without offset and limit
printf "\n\nrequest with everything correct without offset and limit\n"
curl -X GET \
  'https://bank4u.herokuapp.com/api/v1/getBranches?bank_name=HDFC+BANK&city=DELHI' \
  -H 'token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NzMyNDA2NTh9.4xhUzQFLvJ5pxXXGHkO2GcOb9ti_6HW56I0-JLxAjRY' \
  -H 'Cache-Control: no-cache' \
#request with everything correct with offset and limit
printf "\n\nrequest with everything correct with offset and limit\n"
curl -X GET \
  'https://bank4u.herokuapp.com/api/v1/getBranches?bank_name=HDFC+BANK&city=DELHI&offset=2&limit=5' \
  -H 'token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NzMyNDA2NTh9.4xhUzQFLvJ5pxXXGHkO2GcOb9ti_6HW56I0-JLxAjRY' \
  -H 'Cache-Control: no-cache' \
#request with wrong token
printf "\n\nrequest with wrong token\n"
curl -X GET \
  'https://bank4u.herokuapp.com/api/v1/getBranches?bank_name=HDFC+BANK&city=DELHI&offset=2&limit=5' \
  -H 'token: eabceXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NzMyNDA2NTh9.4xhUzQFLvJ5pxXXGHkO2GcOb9ti_6HW56I0-JLxAjRY' \
  -H 'Cache-Control: no-cache' \
#request with wrong bank_name
printf "\n\nrequest with wrong bank_name\n"
curl -X GET \
  'https://bank4u.herokuapp.com/api/v1/getBranches?bank_name=HDFCA+BANK&city=DELHI&offset=2&limit=5' \
  -H 'token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NzMyNDA2NTh9.4xhUzQFLvJ5pxXXGHkO2GcOb9ti_6HW56I0-JLxAjRY' \
  -H 'Cache-Control: no-cache' \
#request with wrong city
printf "\n\nrequest with wrong city\n"
curl -X GET \
  'https://bank4u.herokuapp.com/api/v1/getBranches?bank_name=HDFCA+BANK&city=CAROLINA&offset=2&limit=5' \
  -H 'token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NzMyNDA2NTh9.4xhUzQFLvJ5pxXXGHkO2GcOb9ti_6HW56I0-JLxAjRY' \
  -H 'Cache-Control: no-cache' \