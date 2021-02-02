-- Tạo cơ sở dũ liệu

CREATE TABLE house1(
    STT int PRIMARY KEY AUTO_INCREMENT NOT NULL,
    TEMP DECIMAL(4, 2),
    HUMI DECIMAL(4, 2),
    LIGHT DECIMAL(4, 2),
    RAIN DECIMAL(4, 2),
    TIME TIMESTAMP -- kiểu dữ liệu hiển thị cả ngày tháng và giờ
)

CREATE TABLE hous(
    STT int PRIMARY KEY AUTO_INCREMENT NOT NULL,
    TEMP DECIMAL(4, 2),
    HUMI DECIMAL(4, 2),
    LIGHT DECIMAL(4, 2),
    RAIN DECIMAL(4, 2),
    TIME TIMESTAMP -- kiểu dữ liệu hiển thị cả ngày tháng và giờ
)


-- rename column structure : ALTER TABLE house1 RENAME COLUMN old_column_name TO new_column_name
-- modify datatype : ALTER TABLE table_name MODIFY COLUMN column_name1 datatype,
--                                          MODIFY COLUMN column_name2 datatype;