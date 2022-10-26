set long 10000
set pagesize 10000
set linesize 10000
--alter session set current_schema=ZPORTAL;
select userid, sum (Nummessages) CntE2f , max(DaysUsed) NumbeofdaysE2F  from
(select folderid, count(distinct trunc(received)) DaysUsed, count(1) NumMessages
from ZPORTAL.MESSAGE where messagetype = 2 and fromaddr like '%@%' and received > current_date - 180
group by folderid) tt join zportal.folder f on f.folderid=tt.folderid
join zportal.mailboxes m on f.mailboxid =m.mailboxid
group by userid
order by 2 desc;