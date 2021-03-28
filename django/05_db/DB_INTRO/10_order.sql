-- 나이순 오름차순 정렬해서 상위 10개만
-- SELECT * FROM users
-- ORDER BY age ASC LIMIT 10;

-- 나이순, 성순 으로 오름차순 정렬해 상위 10개?
SELECT * FROM users
ORDER BY last_name, age LIMIT 10; -- 가나다 정렬 하고 나이 어린 10명
-- ORDER BY last_name, age LIMIT 10; -- 나이 어린 10명 중에서 가나다 정렬

-- 계좌잔액순 내림차순 정렬해서 그 10명 성과 이름(부자 10명 성,이름)
SELECT last_name, first_name From users
ORDER BY balance DESC LIMIT 10;

-- 제일 부자 10명 평균나이
SELECT AVG(age) From (SELECT * FROM users ORDER BY balance DESC LIMIT 10);
