-- 각 성씨가 몇명씩 있는지?
SELECT last_name, COUNT(*) FROM users
GROUP BY last_name; -- last_name 같은 사람들만 select 진행하고 다음 진행하고 .. 가나다 순서

-- SELECT DISTINCT last_name FROM users; -- 발견한 순서대로
