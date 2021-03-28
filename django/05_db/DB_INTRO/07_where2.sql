-- -- users에서 age 30 이상
-- SELECT * FROM users
-- WHERE age >= 30;

-- -- users 에서 age 30이상인사람 이름만?
-- SELECT first_name FROM users
-- WHERE age >= 30;

--30이상, 성이 김인 사람인 사람의 성과 나이만 가져오기?
SELECT last_name, first_name FROM users
WHERE age >= 30 AND last_name='김';