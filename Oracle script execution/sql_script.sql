set long 10000
set pagesize 10000
set linesize 10000
alter session set current_schema=ZPORTAL;
SELECT  parameter,value,SERVICELEVEL,BRANDID FROM SERVICES WHERE PARAMETER in (136,259,812)
order by BRANDID asc;