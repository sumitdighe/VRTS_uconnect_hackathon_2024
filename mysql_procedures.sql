DELIMITER //
CREATE FUNCTION wait_for_three_seconds() RETURNS INT
BEGIN
  DECLARE start_time DATETIME;
  SET start_time = NOW();
  LOOP
    IF TIME_TO_SEC(TIMEDIFF(NOW(), start_time)) >=3 THEN
      RETURN 1;
    END IF;
  END LOOP;
  RETURN 1;
END //
DELIMITER ;

with recursive rnums as (
  select 1 as n
      union all
  select n+1 as n from rnums
      where n <10
  )
  select * from rnums
  ;