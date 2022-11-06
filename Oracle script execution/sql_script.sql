set long 10000
set pagesize 10000
set linesize 10000
alter session set current_schema=ZPORTAL;
select count(*) from ZPORTAL.USERS where servicelevel = 9020;