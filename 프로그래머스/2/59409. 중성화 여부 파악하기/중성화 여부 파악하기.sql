-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME, CASE WHEN SEX_UPON_INTAKE='Neutered Male' or SEX_UPON_INTAKE='Spayed Female' THEN 'O' ELSE 'X' END AS 중성화 from ANIMAL_INS order by ANIMAL_ID