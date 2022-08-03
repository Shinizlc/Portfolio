select distinct userid from zportal.users u where brandid = 7010 and privilegeid <> 2 and exists
(select * from zportal.phonelines pl where pl.userid = u.userid and phonelinetype = 1 and defaultareacode = 077 and
 (select devicetype from zportal.agentinstances where userid = pl.userid and instanceid = pl.instanceid and removed is null) > 0)
 order by userid;