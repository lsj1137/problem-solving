-- 코드를 작성해주세요
SELECT COUNT(*) as COUNT from ECOLI_DATA where     -- 2번 비트가 0
    (GENOTYPE & 2) = 0
    AND
    -- 1번 비트가 1 또는 3번 비트가 1
    (
      (GENOTYPE & 1) = 1    -- 1번 비트 체크
      OR
      (GENOTYPE & 4) = 4    -- 3번 비트 체크 (2^2 = 4)
    );