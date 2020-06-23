mkdir AllRecords

#Copied all of the order records from 2012-2017 into the AllRecords folder
find . -type f -exec cp {} AllRecords/ \;

#Made VIPCustomersOrders
mkdir VIPCustomersOrders
grep -n "Michael,Davis" * > VIPCustomers/michael_davis_orders.output
grep -n "Michael,Campbell" * > VIPCustomers/michael_campbell_orders.output

cd VIPCustomersOrders/

grep -c "Michael" michael_davis_orders.output > VIPCustomerDetails.md
grep -c "Michael" michael_campbell_orders.output > VIPCustomerDetails.md