--전체 조회
SELECT * FROM classmatess;


-- 컬럼 지정 조회
SELECT name, address FROM classmatess;

-- 개수 제한 (지정)
SELECT id, name FROM classmatess LIMIT 1;

-- from N to M
-- OFFSET 뒤부터 ,  LIMIT 개
SELECT id, name FROM classmatess LIMIT 1 OFFSET 2;