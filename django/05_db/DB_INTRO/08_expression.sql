-- users 레코드의 개수
SELECT COUNT(*) FROM users;

-- 30살 이상인 사람들의 평균나이?
SELECT AVG(age) FROM users
WHERE age >= 30;

-- users에서 계좌 잔액(balance)이 가장 높은 사람이름과 액수는?
SELECT first_name, MAX(balance) FROM users;

-- 잔액 가장 높은사람 이름만
SELECT first_name FROM (SELECT first_name, MAX(balance)  FROM users);


-- 30이상인 사람의 계좌 평균 잔액?
SELECT AVG(balance) FROM users
WHERE age >= 30;

-- 전체 계좌 잔액
SELECT SUM(balance) FROM users;