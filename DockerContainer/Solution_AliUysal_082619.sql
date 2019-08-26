/*
#######################################################
## Author:      Ali Uysal                            ##
## Date:        08/26/19                             ##
## Description: Solution to the assessment by Cherre ##
#######################################################
*/

-- Delete all records in the frequent_browsers table
-- This operation is required in order to display the top ten people when the script is run multiple times
delete from frequent_browsers;

-- Insert into the frequent_browsers table the top ten people who have visited the most sites
insert into frequent_browsers
select v.personId person_id, count(v.siteId) num_sites_visited
  from visits v 
  join people p 
    on v.personId = p.id
  join sites s 
    on v.siteId = s.id
 group by v.personId
 order by count(v.siteId) desc
 limit 10;
  
-- See top ten people who have visited the most sites
select * from frequent_browsers;